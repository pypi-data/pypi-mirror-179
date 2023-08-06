from re import search
from unittest import mock

from boto3 import client, resource
from moto import mock_ec2

AWS_REGION = "us-east-1"
EXAMPLE_AMI_ID = "ami-12c6146b"


class Test_ec2_elastic_ip_unassgined:
    @mock_ec2
    def test_no_eips(self):

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.ec2.ec2_service import EC2

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "providers.aws.services.ec2.ec2_elastic_ip_unassgined.ec2_elastic_ip_unassgined.ec2_client",
            new=EC2(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.ec2.ec2_elastic_ip_unassgined.ec2_elastic_ip_unassgined import (
                ec2_elastic_ip_unassgined,
            )

            check = ec2_elastic_ip_unassgined()
            result = check.execute()

            assert len(result) == 0

    @mock_ec2
    def test_eip_unassociated(self):
        # Create EC2 Mocked Resources
        ec2_client = client("ec2", region_name=AWS_REGION)
        ec2_client.allocate_address(Domain="vpc", Address="127.38.43.222")

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.ec2.ec2_service import EC2

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "providers.aws.services.ec2.ec2_elastic_ip_unassgined.ec2_elastic_ip_unassgined.ec2_client",
            new=EC2(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.ec2.ec2_elastic_ip_unassgined.ec2_elastic_ip_unassgined import (
                ec2_elastic_ip_unassgined,
            )

            check = ec2_elastic_ip_unassgined()
            results = check.execute()

            assert len(results) == 1
            assert results[0].status == "FAIL"
            assert search(
                "is not associated",
                results[0].status_extended,
            )

    @mock_ec2
    def test_eip_associated(self):
        # Create EC2 Mocked Resources
        ec2_client = client("ec2", region_name=AWS_REGION)
        ec2_resource = resource("ec2", region_name=AWS_REGION)

        reservation = ec2_client.run_instances(
            ImageId=EXAMPLE_AMI_ID, MinCount=1, MaxCount=1
        )
        instance = ec2_resource.Instance(reservation["Instances"][0]["InstanceId"])

        eip = ec2_client.allocate_address(Domain="vpc")

        eip = ec2_resource.VpcAddress(eip["AllocationId"])

        ec2_client.associate_address(
            InstanceId=instance.id, AllocationId=eip.allocation_id
        )

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.ec2.ec2_service import EC2

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "providers.aws.services.ec2.ec2_elastic_ip_unassgined.ec2_elastic_ip_unassgined.ec2_client",
            new=EC2(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.ec2.ec2_elastic_ip_unassgined.ec2_elastic_ip_unassgined import (
                ec2_elastic_ip_unassgined,
            )

            check = ec2_elastic_ip_unassgined()
            results = check.execute()

            assert len(results) == 1
            assert results[0].status == "PASS"
            assert search(
                "is associated",
                results[0].status_extended,
            )
