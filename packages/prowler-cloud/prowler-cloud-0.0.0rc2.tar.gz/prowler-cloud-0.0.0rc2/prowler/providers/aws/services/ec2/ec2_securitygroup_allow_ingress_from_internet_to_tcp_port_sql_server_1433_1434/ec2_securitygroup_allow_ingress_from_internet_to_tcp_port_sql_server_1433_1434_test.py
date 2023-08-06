from re import search
from unittest import mock

from boto3 import client
from moto import mock_ec2

AWS_REGION = "us-east-1"


class ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_sql_server_1433_1434:
    @mock_ec2
    def test_ec2_default_sgs(self):
        # Create EC2 Mocked Resources
        ec2_client = client("ec2", region_name=AWS_REGION)
        ec2_client.create_vpc(CidrBlock="10.0.0.0/16")

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.ec2.ec2_service import EC2

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "providers.aws.services.ec2.ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_sql_server_1433_1434.ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_sql_server_1433_1434.ec2_client",
            new=EC2(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.ec2.ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_sql_server_1433_1434.ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_sql_server_1433_1434 import (
                ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_sql_server_1433_1434,
            )

            check = (
                ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_sql_server_1433_1434()
            )
            result = check.execute()

            # One default sg per region
            assert len(result) == 26
            # All are compliant by default
            assert result[0].status == "PASS"

    @mock_ec2
    def test_ec2_non_compliant_default_sg(self):
        # Create EC2 Mocked Resources
        ec2_client = client("ec2", region_name=AWS_REGION)
        ec2_client.create_vpc(CidrBlock="10.0.0.0/16")
        default_sg_id = ec2_client.describe_security_groups(GroupNames=["default"])[
            "SecurityGroups"
        ][0]["GroupId"]
        ec2_client.authorize_security_group_ingress(
            GroupId=default_sg_id,
            IpPermissions=[
                {
                    "IpProtocol": "tcp",
                    "FromPort": 1433,
                    "ToPort": 1434,
                    "IpRanges": [{"CidrIp": "0.0.0.0/0"}],
                }
            ],
        )

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.ec2.ec2_service import EC2

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "providers.aws.services.ec2.ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_sql_server_1433_1434.ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_sql_server_1433_1434.ec2_client",
            new=EC2(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.ec2.ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_sql_server_1433_1434.ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_sql_server_1433_1434 import (
                ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_sql_server_1433_1434,
            )

            check = (
                ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_sql_server_1433_1434()
            )
            result = check.execute()

            # One default sg per region
            assert len(result) == 26
            # Search changed sg
            for sg in result:
                if sg.resource_id == default_sg_id:
                    assert sg.status == "FAIL"
                    assert search(
                        "has Microsoft SQL Server ports 1433 and 1434 open to the Internet",
                        sg.status_extended,
                    )

    @mock_ec2
    def test_ec2_compliant_default_sg(self):
        # Create EC2 Mocked Resources
        ec2_client = client("ec2", region_name=AWS_REGION)
        ec2_client.create_vpc(CidrBlock="10.0.0.0/16")
        default_sg_id = ec2_client.describe_security_groups(GroupNames=["default"])[
            "SecurityGroups"
        ][0]["GroupId"]
        ec2_client.authorize_security_group_ingress(
            GroupId=default_sg_id,
            IpPermissions=[
                {
                    "IpProtocol": "tcp",
                    "FromPort": 1433,
                    "ToPort": 1434,
                    "IpRanges": [{"CidrIp": "123.123.123.123/32"}],
                }
            ],
        )

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.ec2.ec2_service import EC2

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "providers.aws.services.ec2.ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_sql_server_1433_1434.ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_sql_server_1433_1434.ec2_client",
            new=EC2(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.ec2.ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_sql_server_1433_1434.ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_sql_server_1433_1434 import (
                ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_sql_server_1433_1434,
            )

            check = (
                ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_sql_server_1433_1434()
            )
            result = check.execute()

            # One default sg per region
            assert len(result) == 26
            # Search changed sg
            for sg in result:
                if sg.resource_id == default_sg_id:
                    assert sg.status == "PASS"
                    assert search(
                        "has not Microsoft SQL Server ports 1433 and 1434 open to the Internet",
                        sg.status_extended,
                    )
