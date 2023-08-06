from re import search
from unittest import mock

from providers.aws.services.efs.efs_service import FileSystem

# Mock Test Region
AWS_REGION = "eu-west-1"
AWS_ACCOUNT_NUMBER = "123456789012"

file_system_id = "fs-c7a0456e"

backup_valid_policy_status = "ENABLED"


class Test_efs_encryption_at_rest_enabled:
    def test_efs_encryption_enabled(self):
        efs_client = mock.MagicMock
        efs_client.filesystems = [
            FileSystem(
                id=file_system_id,
                region=AWS_REGION,
                policy=None,
                backup_policy=backup_valid_policy_status,
                encrypted=True,
            )
        ]
        with mock.patch(
            "providers.aws.services.efs.efs_service.EFS",
            efs_client,
        ):
            from providers.aws.services.efs.efs_encryption_at_rest_enabled.efs_encryption_at_rest_enabled import (
                efs_encryption_at_rest_enabled,
            )

            check = efs_encryption_at_rest_enabled()
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "PASS"
            assert search("has encryption at rest enabled", result[0].status_extended)
            assert result[0].resource_id == file_system_id
            assert result[0].resource_arn == ""

    def test_efs_encryption_disabled(self):
        efs_client = mock.MagicMock
        efs_client.filesystems = [
            FileSystem(
                id=file_system_id,
                region=AWS_REGION,
                policy=None,
                backup_policy=backup_valid_policy_status,
                encrypted=False,
            )
        ]
        with mock.patch(
            "providers.aws.services.efs.efs_service.EFS",
            efs_client,
        ):
            from providers.aws.services.efs.efs_encryption_at_rest_enabled.efs_encryption_at_rest_enabled import (
                efs_encryption_at_rest_enabled,
            )

            check = efs_encryption_at_rest_enabled()
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert search(
                "does not have encryption at rest enabled", result[0].status_extended
            )
            assert result[0].resource_id == file_system_id
            assert result[0].resource_arn == ""
