from boto3 import client, resource, session
from moto import mock_ec2, mock_elb

from providers.aws.lib.audit_info.models import AWS_Audit_Info
from providers.aws.services.elb.elb_service import ELB

AWS_ACCOUNT_NUMBER = 123456789012
AWS_REGION = "us-east-1"


class Test_ELB_Service:
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

    # Test ELB Service
    @mock_elb
    def test_service(self):
        # ELB client for this test class
        audit_info = self.set_mocked_audit_info()
        elb = ELB(audit_info)
        assert elb.service == "elb"

    # Test ELB Client
    @mock_elb
    def test_client(self):
        # ELB client for this test class
        audit_info = self.set_mocked_audit_info()
        elb = ELB(audit_info)
        for regional_client in elb.regional_clients.values():
            assert regional_client.__class__.__name__ == "ElasticLoadBalancing"

    # Test ELB Session
    @mock_elb
    def test__get_session__(self):
        # ELB client for this test class
        audit_info = self.set_mocked_audit_info()
        elb = ELB(audit_info)
        assert elb.session.__class__.__name__ == "Session"

    # Test ELB Describe Load Balancers
    @mock_ec2
    @mock_elb
    def test__describe_load_balancers__(self):
        elb = client("elb", region_name=AWS_REGION)
        ec2 = resource("ec2", region_name=AWS_REGION)

        security_group = ec2.create_security_group(
            GroupName="sg01", Description="Test security group sg01"
        )

        elb.create_load_balancer(
            LoadBalancerName="my-lb",
            Listeners=[
                {"Protocol": "tcp", "LoadBalancerPort": 80, "InstancePort": 8080},
                {"Protocol": "http", "LoadBalancerPort": 81, "InstancePort": 9000},
            ],
            AvailabilityZones=[f"{AWS_REGION}a"],
            Scheme="internal",
            SecurityGroups=[security_group.id],
        )
        # ELB client for this test class
        audit_info = self.set_mocked_audit_info()
        elb = ELB(audit_info)
        assert len(elb.loadbalancers) == 1
        assert elb.loadbalancers[0].name == "my-lb"
        assert elb.loadbalancers[0].region == AWS_REGION
        assert elb.loadbalancers[0].scheme == "internal"
        assert (
            elb.loadbalancers[0].arn
            == f"arn:aws:elasticloadbalancing:{AWS_REGION}:{AWS_ACCOUNT_NUMBER}:loadbalancer/my-lb"
        )

    # Test ELB Describe Load Balancers Attributes
    @mock_ec2
    @mock_elb
    def test__describe_load_balancer_attributes__(self):
        elb = client("elb", region_name=AWS_REGION)
        ec2 = resource("ec2", region_name=AWS_REGION)

        security_group = ec2.create_security_group(
            GroupName="sg01", Description="Test security group sg01"
        )

        elb.create_load_balancer(
            LoadBalancerName="my-lb",
            Listeners=[
                {"Protocol": "tcp", "LoadBalancerPort": 80, "InstancePort": 8080},
                {"Protocol": "http", "LoadBalancerPort": 81, "InstancePort": 9000},
            ],
            AvailabilityZones=[f"{AWS_REGION}a"],
            Scheme="internal",
            SecurityGroups=[security_group.id],
        )

        elb.modify_load_balancer_attributes(
            LoadBalancerName="my-lb",
            LoadBalancerAttributes={
                "AccessLog": {
                    "Enabled": True,
                    "S3BucketName": "mb",
                    "EmitInterval": 42,
                    "S3BucketPrefix": "s3bf",
                }
            },
        )
        # ELB client for this test class
        audit_info = self.set_mocked_audit_info()
        elb = ELB(audit_info)
        assert elb.loadbalancers[0].name == "my-lb"
        assert elb.loadbalancers[0].region == AWS_REGION
        assert elb.loadbalancers[0].scheme == "internal"
        assert elb.loadbalancers[0].access_logs
        assert (
            elb.loadbalancers[0].arn
            == f"arn:aws:elasticloadbalancing:{AWS_REGION}:{AWS_ACCOUNT_NUMBER}:loadbalancer/my-lb"
        )
