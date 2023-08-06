from re import search
from unittest import mock

from boto3 import client, resource
from moto import mock_ec2, mock_elbv2

AWS_REGION = "eu-west-1"
AWS_ACCOUNT_NUMBER = "123456789012"


class Test_elbv2_request_smugling:
    @mock_elbv2
    def test_elb_no_balancers(self):

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.elbv2.elbv2_service import ELBv2

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "providers.aws.services.elbv2.elbv2_request_smugling.elbv2_request_smugling.elbv2_client",
            new=ELBv2(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.elbv2.elbv2_request_smugling.elbv2_request_smugling import (
                elbv2_request_smugling,
            )

            check = elbv2_request_smugling()
            result = check.execute()

            assert len(result) == 0

    @mock_ec2
    @mock_elbv2
    def test_elbv2_without_dropping(self):
        conn = client("elbv2", region_name=AWS_REGION)
        ec2 = resource("ec2", region_name=AWS_REGION)

        security_group = ec2.create_security_group(
            GroupName="a-security-group", Description="First One"
        )
        vpc = ec2.create_vpc(CidrBlock="172.28.7.0/24", InstanceTenancy="default")
        subnet1 = ec2.create_subnet(
            VpcId=vpc.id, CidrBlock="172.28.7.192/26", AvailabilityZone=f"{AWS_REGION}a"
        )
        subnet2 = ec2.create_subnet(
            VpcId=vpc.id, CidrBlock="172.28.7.0/26", AvailabilityZone=f"{AWS_REGION}b"
        )

        lb = conn.create_load_balancer(
            Name="my-lb",
            Subnets=[subnet1.id, subnet2.id],
            SecurityGroups=[security_group.id],
            Scheme="internal",
            Type="application",
        )["LoadBalancers"][0]

        conn.modify_load_balancer_attributes(
            LoadBalancerArn=lb["LoadBalancerArn"],
            Attributes=[
                {
                    "Key": "routing.http.drop_invalid_header_fields.enabled",
                    "Value": "false",
                },
            ],
        )

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.elbv2.elbv2_service import ELBv2

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "providers.aws.services.elbv2.elbv2_request_smugling.elbv2_request_smugling.elbv2_client",
            new=ELBv2(current_audit_info),
        ):
            from providers.aws.services.elbv2.elbv2_request_smugling.elbv2_request_smugling import (
                elbv2_request_smugling,
            )

            check = elbv2_request_smugling()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert search(
                "is not dropping invalid header fields",
                result[0].status_extended,
            )
            assert result[0].resource_id == "my-lb"
            assert result[0].resource_arn == lb["LoadBalancerArn"]

    @mock_ec2
    @mock_elbv2
    def test_elbv2_with_dropping(self):
        conn = client("elbv2", region_name=AWS_REGION)
        ec2 = resource("ec2", region_name=AWS_REGION)

        security_group = ec2.create_security_group(
            GroupName="a-security-group", Description="First One"
        )
        vpc = ec2.create_vpc(CidrBlock="172.28.7.0/24", InstanceTenancy="default")
        subnet1 = ec2.create_subnet(
            VpcId=vpc.id, CidrBlock="172.28.7.192/26", AvailabilityZone=f"{AWS_REGION}a"
        )
        subnet2 = ec2.create_subnet(
            VpcId=vpc.id, CidrBlock="172.28.7.0/26", AvailabilityZone=f"{AWS_REGION}b"
        )

        lb = conn.create_load_balancer(
            Name="my-lb",
            Subnets=[subnet1.id, subnet2.id],
            SecurityGroups=[security_group.id],
            Scheme="internal",
        )["LoadBalancers"][0]

        conn.modify_load_balancer_attributes(
            LoadBalancerArn=lb["LoadBalancerArn"],
            Attributes=[
                {
                    "Key": "routing.http.drop_invalid_header_fields.enabled",
                    "Value": "true",
                },
            ],
        )

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.elbv2.elbv2_service import ELBv2

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "providers.aws.services.elbv2.elbv2_request_smugling.elbv2_request_smugling.elbv2_client",
            new=ELBv2(current_audit_info),
        ):
            from providers.aws.services.elbv2.elbv2_request_smugling.elbv2_request_smugling import (
                elbv2_request_smugling,
            )

            check = elbv2_request_smugling()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "PASS"
            assert search(
                "is dropping invalid header fields",
                result[0].status_extended,
            )
            assert result[0].resource_id == "my-lb"
            assert result[0].resource_arn == lb["LoadBalancerArn"]
