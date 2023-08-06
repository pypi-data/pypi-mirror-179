import json

from boto3 import client, resource, session
from moto import mock_ec2, mock_elbv2

from providers.aws.lib.audit_info.models import AWS_Audit_Info
from providers.aws.services.vpc.vpc_service import VPC, Route

AWS_ACCOUNT_NUMBER = 123456789012
AWS_REGION = "us-east-1"


class Test_VPC_Service:
    # Mocked Audit Info
    def set_mocked_audit_info(self):
        audit_info = AWS_Audit_Info(
            original_session=None,
            audit_session=session.Session(
                profile_name=None,
                botocore_session=None,
            ),
            audited_account=AWS_ACCOUNT_NUMBER,
            audited_user_id=None,
            audited_partition="aws",
            audited_identity_arn=None,
            profile=None,
            profile_region=None,
            credentials=None,
            assumed_role_info=None,
            audited_regions=None,
            organizations_metadata=None,
        )
        return audit_info

    # Test VPC Service
    @mock_ec2
    def test_service(self):
        # VPC client for this test class
        audit_info = self.set_mocked_audit_info()
        vpc = VPC(audit_info)
        assert vpc.service == "ec2"

    # Test VPC Client
    @mock_ec2
    def test_client(self):
        # VPC client for this test class
        audit_info = self.set_mocked_audit_info()
        vpc = VPC(audit_info)
        for regional_client in vpc.regional_clients.values():
            assert regional_client.__class__.__name__ == "EC2"

    # Test VPC Session
    @mock_ec2
    def test__get_session__(self):
        # VPC client for this test class
        audit_info = self.set_mocked_audit_info()
        vpc = VPC(audit_info)
        assert vpc.session.__class__.__name__ == "Session"

    # Test VPC Session
    @mock_ec2
    def test_audited_account(self):
        # VPC client for this test class
        audit_info = self.set_mocked_audit_info()
        vpc = VPC(audit_info)
        assert vpc.audited_account == AWS_ACCOUNT_NUMBER

    # Test VPC Describe VPCs
    @mock_ec2
    def test__describe_vpcs__(self):
        # Generate VPC Client
        ec2_client = client("ec2", region_name=AWS_REGION)
        # Create VPC
        vpc = ec2_client.create_vpc(CidrBlock="10.0.0.0/16")["Vpc"]
        # VPC client for this test class
        audit_info = self.set_mocked_audit_info()
        vpc = VPC(audit_info)
        assert (
            len(vpc.vpcs) == 26
        )  # Number of AWS regions + created VPC, one default VPC per region

    # Test VPC Describe Flow Logs
    @mock_ec2
    def test__describe_flow_logs__(self):
        # Generate VPC Client
        ec2_client = client("ec2", region_name=AWS_REGION)
        new_vpc = ec2_client.create_vpc(CidrBlock="10.0.0.0/16")["Vpc"]
        # Create VPC Flow log
        ec2_client.create_flow_logs(
            ResourceType="VPC",
            ResourceIds=[new_vpc["VpcId"]],
            TrafficType="ALL",
            LogDestinationType="cloud-watch-logs",
            LogGroupName="test_logs",
            DeliverLogsPermissionArn="arn:aws:iam::"
            + str(AWS_ACCOUNT_NUMBER)
            + ":role/test-role",
        )
        # VPC client for this test class
        audit_info = self.set_mocked_audit_info()
        vpc = VPC(audit_info)
        # Search created VPC among default ones
        for vpc in vpc.vpcs:
            if vpc.id == new_vpc["VpcId"]:
                assert vpc.flow_log is True

    # Test VPC Describe VPC Peering connections
    @mock_ec2
    def test__describe_vpc_peering_connections__(self):
        # Generate VPC Client
        ec2_client = client("ec2", region_name=AWS_REGION)
        # Create VPCs peers
        vpc = ec2_client.create_vpc(CidrBlock="10.0.0.0/16")
        peer_vpc = ec2_client.create_vpc(CidrBlock="11.0.0.0/16")
        vpc_pcx = ec2_client.create_vpc_peering_connection(
            VpcId=vpc["Vpc"]["VpcId"], PeerVpcId=peer_vpc["Vpc"]["VpcId"]
        )
        vpc_pcx_id = vpc_pcx["VpcPeeringConnection"]["VpcPeeringConnectionId"]

        vpc_pcx = ec2_client.accept_vpc_peering_connection(
            VpcPeeringConnectionId=vpc_pcx_id
        )
        # VPC client for this test class
        audit_info = self.set_mocked_audit_info()
        vpc = VPC(audit_info)
        assert len(vpc.vpc_peering_connections) == 1
        assert vpc.vpc_peering_connections[0].id == vpc_pcx_id

    # Test VPC Describe VPC Peering connections
    @mock_ec2
    def test__describe_route_tables__(self):
        # Generate VPC Client
        ec2_client = client("ec2", region_name=AWS_REGION)
        _ = resource("ec2", region_name=AWS_REGION)

        # Create VPCs peers as well as a route
        vpc = ec2_client.create_vpc(CidrBlock="10.0.0.0/16")
        peer_vpc = ec2_client.create_vpc(CidrBlock="11.0.0.0/16")
        vpc_pcx = ec2_client.create_vpc_peering_connection(
            VpcId=vpc["Vpc"]["VpcId"], PeerVpcId=peer_vpc["Vpc"]["VpcId"]
        )
        vpc_pcx_id = vpc_pcx["VpcPeeringConnection"]["VpcPeeringConnectionId"]

        vpc_pcx = ec2_client.accept_vpc_peering_connection(
            VpcPeeringConnectionId=vpc_pcx_id
        )
        main_route_table_id = ec2_client.describe_route_tables(
            Filters=[
                {"Name": "vpc-id", "Values": [vpc["Vpc"]["VpcId"]]},
                {"Name": "association.main", "Values": ["true"]},
            ]
        )["RouteTables"][0]["RouteTableId"]
        # FilterNotImplementedError: The filter 'route.vpc-peering-connection-id' for DescribeRouteTables has not been implemented in Moto yet.
        # main_route_table = ec2_resource.RouteTable(main_route_table_id)
        # main_route_table.create_route(
        #     DestinationCidrBlock="10.0.0.4/24", VpcPeeringConnectionId=vpc_pcx_id
        # )

        # VPC client for this test class
        audit_info = self.set_mocked_audit_info()
        vpc = VPC(audit_info)
        vpc.vpc_peering_connections[0].route_tables = [
            Route(
                main_route_table_id,
                ["10.0.0.4/24"],
            )
        ]
        assert len(vpc.vpc_peering_connections[0].route_tables) == 1
        assert vpc.vpc_peering_connections[0].id == vpc_pcx_id

    # Test VPC Describe VPC Endpoints
    @mock_ec2
    def test__describe_vpc_endpoints__(self):
        # Generate VPC Client
        ec2_client = client("ec2", region_name=AWS_REGION)
        # Create VPC endpoint
        vpc = ec2_client.create_vpc(CidrBlock="10.0.0.0/16")["Vpc"]

        route_table = ec2_client.create_route_table(VpcId=vpc["VpcId"])["RouteTable"]
        endpoint = ec2_client.create_vpc_endpoint(
            VpcId=vpc["VpcId"],
            ServiceName="com.amazonaws.us-east-1.s3",
            RouteTableIds=[route_table["RouteTableId"]],
            VpcEndpointType="Gateway",
            PolicyDocument=json.dumps(
                {
                    "Statement": [
                        {
                            "Action": "*",
                            "Effect": "Allow",
                            "Principal": "*",
                            "Resource": "*",
                        }
                    ]
                }
            ),
        )["VpcEndpoint"]["VpcEndpointId"]
        # VPC client for this test class
        audit_info = self.set_mocked_audit_info()
        vpc = VPC(audit_info)
        assert len(vpc.vpc_endpoints) == 1
        assert vpc.vpc_endpoints[0].id == endpoint

    # Test VPC Describe VPC Endpoint Services
    @mock_ec2
    @mock_elbv2
    def test__describe_vpc_endpoint_services__(self):
        # Generate VPC Client
        ec2_client = client("ec2", region_name=AWS_REGION)
        elbv2_client = client("elbv2", region_name=AWS_REGION)

        vpc = ec2_client.create_vpc(
            CidrBlock="172.28.7.0/24", InstanceTenancy="default"
        )
        subnet = ec2_client.create_subnet(
            VpcId=vpc["Vpc"]["VpcId"],
            CidrBlock="172.28.7.192/26",
            AvailabilityZone=f"{AWS_REGION}a",
        )
        lb_name = "lb_vpce-test"
        lb_arn = elbv2_client.create_load_balancer(
            Name=lb_name,
            Subnets=[subnet["Subnet"]["SubnetId"]],
            Scheme="internal",
            Type="network",
        )["LoadBalancers"][0]["LoadBalancerArn"]

        _ = ec2_client.create_vpc_endpoint_service_configuration(
            NetworkLoadBalancerArns=[lb_arn]
        )
        # VPC client for this test class
        audit_info = self.set_mocked_audit_info()
        vpc = VPC(audit_info)
        assert (
            len(vpc.vpc_endpoint_services) == 0
        )  # Wait until this issue is fixed https://github.com/spulec/moto/issues/5605
