from unittest import mock

from boto3 import client
from moto import mock_logs

AWS_REGION = "us-east-1"


class Test_cloudwatch_log_group_retention_policy_specific_days_enabled:
    def test_cloudwatch_no_log_groups(self):
        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.cloudwatch.cloudwatch_service import Logs

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "providers.aws.services.cloudwatch.cloudwatch_log_group_retention_policy_specific_days_enabled.cloudwatch_log_group_retention_policy_specific_days_enabled.logs_client",
            new=Logs(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.cloudwatch.cloudwatch_log_group_retention_policy_specific_days_enabled.cloudwatch_log_group_retention_policy_specific_days_enabled import (
                cloudwatch_log_group_retention_policy_specific_days_enabled,
            )

            check = cloudwatch_log_group_retention_policy_specific_days_enabled()
            result = check.execute()

            assert len(result) == 0

    @mock_logs
    def test_cloudwatch_log_group_without_retention_days(self):
        # Generate Logs Client
        logs_client = client("logs", region_name=AWS_REGION)
        # Request Logs group
        logs_client.create_log_group(
            logGroupName="test",
        )
        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.cloudwatch.cloudwatch_service import Logs

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "providers.aws.services.cloudwatch.cloudwatch_log_group_retention_policy_specific_days_enabled.cloudwatch_log_group_retention_policy_specific_days_enabled.logs_client",
            new=Logs(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.cloudwatch.cloudwatch_log_group_retention_policy_specific_days_enabled.cloudwatch_log_group_retention_policy_specific_days_enabled import (
                cloudwatch_log_group_retention_policy_specific_days_enabled,
            )

            check = cloudwatch_log_group_retention_policy_specific_days_enabled()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert (
                result[0].status_extended
                == "Log Group test has less than 365 days retention period (0 days)."
            )
            assert result[0].resource_id == "test"

    @mock_logs
    def test_cloudwatch_log_group_with_compliant_retention_days(self):
        # Generate Logs Client
        logs_client = client("logs", region_name=AWS_REGION)
        # Request Logs group
        logs_client.create_log_group(
            logGroupName="test",
        )
        logs_client.put_retention_policy(logGroupName="test", retentionInDays=400)
        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.cloudwatch.cloudwatch_service import Logs

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "providers.aws.services.cloudwatch.cloudwatch_log_group_retention_policy_specific_days_enabled.cloudwatch_log_group_retention_policy_specific_days_enabled.logs_client",
            new=Logs(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.cloudwatch.cloudwatch_log_group_retention_policy_specific_days_enabled.cloudwatch_log_group_retention_policy_specific_days_enabled import (
                cloudwatch_log_group_retention_policy_specific_days_enabled,
            )

            check = cloudwatch_log_group_retention_policy_specific_days_enabled()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "PASS"
            assert (
                result[0].status_extended
                == "Log Group test comply with 365 days retention period since it has 400 days."
            )
            assert result[0].resource_id == "test"

    @mock_logs
    def test_cloudwatch_log_group_with_no_compliant_retention_days(self):
        # Generate Logs Client
        logs_client = client("logs", region_name=AWS_REGION)
        # Request Logs group
        logs_client.create_log_group(
            logGroupName="test",
        )
        logs_client.put_retention_policy(logGroupName="test", retentionInDays=7)
        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.cloudwatch.cloudwatch_service import Logs

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "providers.aws.services.cloudwatch.cloudwatch_log_group_retention_policy_specific_days_enabled.cloudwatch_log_group_retention_policy_specific_days_enabled.logs_client",
            new=Logs(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.cloudwatch.cloudwatch_log_group_retention_policy_specific_days_enabled.cloudwatch_log_group_retention_policy_specific_days_enabled import (
                cloudwatch_log_group_retention_policy_specific_days_enabled,
            )

            check = cloudwatch_log_group_retention_policy_specific_days_enabled()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert (
                result[0].status_extended
                == "Log Group test has less than 365 days retention period (7 days)."
            )
            assert result[0].resource_id == "test"
