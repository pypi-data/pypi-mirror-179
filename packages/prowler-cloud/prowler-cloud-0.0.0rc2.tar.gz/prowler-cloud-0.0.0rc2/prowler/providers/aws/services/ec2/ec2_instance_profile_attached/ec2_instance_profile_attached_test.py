from re import search
from unittest import mock

from boto3 import client, resource
from moto import mock_ec2, mock_iam

AWS_REGION = "us-east-1"
EXAMPLE_AMI_ID = "ami-12c6146b"


class Test_ec2_instance_profile_attached:
    @mock_ec2
    def test_ec2_no_instances(self):

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.ec2.ec2_service import EC2

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "providers.aws.services.ec2.ec2_instance_profile_attached.ec2_instance_profile_attached.ec2_client",
            new=EC2(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.ec2.ec2_instance_profile_attached.ec2_instance_profile_attached import (
                ec2_instance_profile_attached,
            )

            check = ec2_instance_profile_attached()
            result = check.execute()

            assert len(result) == 0

    @mock_iam
    @mock_ec2
    def test_one_compliant_ec2(self):
        iam = client("iam", "us-west-1")
        profile_name = "fake_profile"
        _ = iam.create_instance_profile(
            InstanceProfileName=profile_name,
        )
        ec2 = resource("ec2", region_name=AWS_REGION)
        vpc = ec2.create_vpc(CidrBlock="10.0.0.0/16")
        subnet = ec2.create_subnet(VpcId=vpc.id, CidrBlock="10.0.0.0/18")
        instance = ec2.create_instances(
            ImageId=EXAMPLE_AMI_ID,
            MinCount=1,
            MaxCount=1,
            IamInstanceProfile={"Name": profile_name},
            NetworkInterfaces=[
                {
                    "DeviceIndex": 0,
                    "SubnetId": subnet.id,
                    "AssociatePublicIpAddress": False,
                }
            ],
        )[0]

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.ec2.ec2_service import EC2

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "providers.aws.services.ec2.ec2_instance_profile_attached.ec2_instance_profile_attached.ec2_client",
            new=EC2(current_audit_info),
        ):
            from providers.aws.services.ec2.ec2_instance_profile_attached.ec2_instance_profile_attached import (
                ec2_instance_profile_attached,
            )

            check = ec2_instance_profile_attached()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "PASS"
            assert search(
                "associated with Instance Profile Role",
                result[0].status_extended,
            )
            assert result[0].resource_id == instance.id

    @mock_ec2
    def test_one_non_compliant_ec2(self):
        ec2 = resource("ec2", region_name=AWS_REGION)
        vpc = ec2.create_vpc(CidrBlock="10.0.0.0/16")
        subnet = ec2.create_subnet(VpcId=vpc.id, CidrBlock="10.0.0.0/18")
        instance = ec2.create_instances(
            ImageId=EXAMPLE_AMI_ID,
            MinCount=1,
            MaxCount=1,
            NetworkInterfaces=[
                {
                    "DeviceIndex": 0,
                    "SubnetId": subnet.id,
                    "AssociatePublicIpAddress": True,
                }
            ],
        )[0]

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.ec2.ec2_service import EC2

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "providers.aws.services.ec2.ec2_instance_profile_attached.ec2_instance_profile_attached.ec2_client",
            new=EC2(current_audit_info),
        ):
            from providers.aws.services.ec2.ec2_instance_profile_attached.ec2_instance_profile_attached import (
                ec2_instance_profile_attached,
            )

            check = ec2_instance_profile_attached()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert search(
                "not associated with an Instance Profile", result[0].status_extended
            )
            assert result[0].resource_id == instance.id
