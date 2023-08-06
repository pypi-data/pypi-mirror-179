import json
from unittest import mock

from boto3 import client
from moto import mock_kms

AWS_REGION = "us-east-1"


class Test_kms_key_not_publicly_accessible:
    @mock_kms
    def test_no_kms_keys(self):
        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.kms.kms_service import KMS

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "providers.aws.services.kms.kms_key_not_publicly_accessible.kms_key_not_publicly_accessible.kms_client",
            new=KMS(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.kms.kms_key_not_publicly_accessible.kms_key_not_publicly_accessible import (
                kms_key_not_publicly_accessible,
            )

            check = kms_key_not_publicly_accessible()
            result = check.execute()

            assert len(result) == 0

    @mock_kms
    def test_kms_key_not_publicly_accessible(self):
        # Generate KMS Client
        kms_client = client("kms", region_name=AWS_REGION)
        # Creaty KMS key without policy
        key = kms_client.create_key()["KeyMetadata"]
        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.kms.kms_service import KMS

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "providers.aws.services.kms.kms_key_not_publicly_accessible.kms_key_not_publicly_accessible.kms_client",
            new=KMS(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.kms.kms_key_not_publicly_accessible.kms_key_not_publicly_accessible import (
                kms_key_not_publicly_accessible,
            )

            check = kms_key_not_publicly_accessible()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "PASS"
            assert (
                result[0].status_extended
                == f"KMS key {key['KeyId']} is not exposed to Public."
            )
            assert result[0].resource_id == key["KeyId"]
            assert result[0].resource_arn == key["Arn"]

    @mock_kms
    def test_kms_key_public_accessible(self):
        # Generate KMS Client
        kms_client = client("kms", region_name=AWS_REGION)
        # Creaty KMS key with public policy
        key = kms_client.create_key(
            Policy=json.dumps(
                {
                    "Version": "2012-10-17",
                    "Id": "key-default-1",
                    "Statement": [
                        {
                            "Sid": "Enable IAM User Permissions",
                            "Effect": "Allow",
                            "Principal": "*",
                            "Action": "kms:*",
                            "Resource": "*",
                        }
                    ],
                }
            )
        )["KeyMetadata"]
        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.kms.kms_service import KMS

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "providers.aws.services.kms.kms_key_not_publicly_accessible.kms_key_not_publicly_accessible.kms_client",
            new=KMS(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.kms.kms_key_not_publicly_accessible.kms_key_not_publicly_accessible import (
                kms_key_not_publicly_accessible,
            )

            check = kms_key_not_publicly_accessible()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert (
                result[0].status_extended
                == f"KMS key {key['KeyId']} may be publicly accessible!"
            )
            assert result[0].resource_id == key["KeyId"]
            assert result[0].resource_arn == key["Arn"]
