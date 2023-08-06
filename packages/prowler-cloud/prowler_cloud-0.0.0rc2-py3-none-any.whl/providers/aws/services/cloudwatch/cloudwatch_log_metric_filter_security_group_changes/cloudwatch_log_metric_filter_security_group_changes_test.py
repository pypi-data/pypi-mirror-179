from unittest import mock

from boto3 import client
from moto import mock_cloudtrail, mock_cloudwatch, mock_logs, mock_s3
from moto.core import DEFAULT_ACCOUNT_ID

AWS_REGION = "us-east-1"


class Test_cloudwatch_log_metric_filter_unauthorized_api_calls:
    @mock_logs
    @mock_cloudtrail
    @mock_cloudwatch
    def test_cloudwatch_no_log_groups(self):
        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.cloudwatch.cloudwatch_service import (
            CloudWatch,
            Logs,
        )

        current_audit_info.audited_partition = "aws"
        from providers.aws.services.cloudtrail.cloudtrail_client import Cloudtrail

        with mock.patch(
            "providers.aws.services.cloudwatch.cloudwatch_log_metric_filter_security_group_changes.cloudwatch_log_metric_filter_security_group_changes.logs_client",
            new=Logs(current_audit_info),
        ), mock.patch(
            "providers.aws.services.cloudwatch.cloudwatch_log_metric_filter_security_group_changes.cloudwatch_log_metric_filter_security_group_changes.cloudwatch_client",
            new=CloudWatch(current_audit_info),
        ), mock.patch(
            "providers.aws.services.cloudwatch.cloudwatch_log_metric_filter_security_group_changes.cloudwatch_log_metric_filter_security_group_changes.cloudtrail_client",
            new=Cloudtrail(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.cloudwatch.cloudwatch_log_metric_filter_security_group_changes.cloudwatch_log_metric_filter_security_group_changes import (
                cloudwatch_log_metric_filter_security_group_changes,
            )

            check = cloudwatch_log_metric_filter_security_group_changes()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert (
                result[0].status_extended
                == "No CloudWatch log groups found with metric filters or alarms associated."
            )
            assert result[0].resource_id == ""

    @mock_logs
    @mock_cloudtrail
    @mock_cloudwatch
    @mock_s3
    def test_cloudwatch_trail_no_log_group(self):
        cloudtrail_client = client("cloudtrail", region_name=AWS_REGION)
        s3_client = client("s3", region_name=AWS_REGION)
        s3_client.create_bucket(Bucket="test")
        cloudtrail_client.create_trail(Name="test_trail", S3BucketName="test")

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.cloudwatch.cloudwatch_service import (
            CloudWatch,
            Logs,
        )

        current_audit_info.audited_partition = "aws"
        from providers.aws.services.cloudtrail.cloudtrail_client import Cloudtrail

        with mock.patch(
            "providers.aws.services.cloudwatch.cloudwatch_log_metric_filter_security_group_changes.cloudwatch_log_metric_filter_security_group_changes.logs_client",
            new=Logs(current_audit_info),
        ), mock.patch(
            "providers.aws.services.cloudwatch.cloudwatch_log_metric_filter_security_group_changes.cloudwatch_log_metric_filter_security_group_changes.cloudwatch_client",
            new=CloudWatch(current_audit_info),
        ), mock.patch(
            "providers.aws.services.cloudwatch.cloudwatch_log_metric_filter_security_group_changes.cloudwatch_log_metric_filter_security_group_changes.cloudtrail_client",
            new=Cloudtrail(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.cloudwatch.cloudwatch_log_metric_filter_security_group_changes.cloudwatch_log_metric_filter_security_group_changes import (
                cloudwatch_log_metric_filter_security_group_changes,
            )

            check = cloudwatch_log_metric_filter_security_group_changes()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert (
                result[0].status_extended
                == "No CloudWatch log groups found with metric filters or alarms associated."
            )
            assert result[0].resource_id == ""

    @mock_logs
    @mock_cloudtrail
    @mock_cloudwatch
    @mock_s3
    def test_cloudwatch_trail_with_log_group(self):
        cloudtrail_client = client("cloudtrail", region_name=AWS_REGION)
        logs_client = client("logs", region_name=AWS_REGION)
        s3_client = client("s3", region_name=AWS_REGION)
        s3_client.create_bucket(Bucket="test")
        logs_client.create_log_group(logGroupName="/log-group/test")
        cloudtrail_client.create_trail(
            Name="test_trail",
            S3BucketName="test",
            CloudWatchLogsLogGroupArn=f"arn:aws:logs:{AWS_REGION}:{DEFAULT_ACCOUNT_ID}:log-group:/log-group/test:*",
        )

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.cloudwatch.cloudwatch_service import (
            CloudWatch,
            Logs,
        )

        current_audit_info.audited_partition = "aws"
        from providers.aws.services.cloudtrail.cloudtrail_client import Cloudtrail

        with mock.patch(
            "providers.aws.services.cloudwatch.cloudwatch_log_metric_filter_security_group_changes.cloudwatch_log_metric_filter_security_group_changes.logs_client",
            new=Logs(current_audit_info),
        ), mock.patch(
            "providers.aws.services.cloudwatch.cloudwatch_log_metric_filter_security_group_changes.cloudwatch_log_metric_filter_security_group_changes.cloudwatch_client",
            new=CloudWatch(current_audit_info),
        ), mock.patch(
            "providers.aws.services.cloudwatch.cloudwatch_log_metric_filter_security_group_changes.cloudwatch_log_metric_filter_security_group_changes.cloudtrail_client",
            new=Cloudtrail(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.cloudwatch.cloudwatch_log_metric_filter_security_group_changes.cloudwatch_log_metric_filter_security_group_changes import (
                cloudwatch_log_metric_filter_security_group_changes,
            )

            check = cloudwatch_log_metric_filter_security_group_changes()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert (
                result[0].status_extended
                == "No CloudWatch log groups found with metric filters or alarms associated."
            )
            assert result[0].resource_id == ""

    @mock_logs
    @mock_cloudtrail
    @mock_cloudwatch
    @mock_s3
    def test_cloudwatch_trail_with_log_group_with_metric(self):
        cloudtrail_client = client("cloudtrail", region_name=AWS_REGION)
        logs_client = client("logs", region_name=AWS_REGION)
        s3_client = client("s3", region_name=AWS_REGION)
        s3_client.create_bucket(Bucket="test")
        logs_client.create_log_group(logGroupName="/log-group/test")
        cloudtrail_client.create_trail(
            Name="test_trail",
            S3BucketName="test",
            CloudWatchLogsLogGroupArn=f"arn:aws:logs:{AWS_REGION}:{DEFAULT_ACCOUNT_ID}:log-group:/log-group/test:*",
        )
        logs_client.put_metric_filter(
            logGroupName="/log-group/test",
            filterName="test-filter",
            filterPattern="{($.eventName = AuthorizeSecurityGroupIngress) || ($.eventName = AuthorizeSecurityGroupEgress) || ($.eventName = RevokeSecurityGroupIngress) || ($.eventName = RevokeSecurityGroupEgress) || ($.eventName = CreateSecurityGroup) || ($.eventName = DeleteSecurityGroup) }",
            metricTransformations=[
                {
                    "metricName": "my-metric",
                    "metricNamespace": "my-namespace",
                    "metricValue": "$.value",
                }
            ],
        )

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.cloudwatch.cloudwatch_service import (
            CloudWatch,
            Logs,
        )

        current_audit_info.audited_partition = "aws"
        from providers.aws.services.cloudtrail.cloudtrail_client import Cloudtrail

        with mock.patch(
            "providers.aws.services.cloudwatch.cloudwatch_log_metric_filter_security_group_changes.cloudwatch_log_metric_filter_security_group_changes.logs_client",
            new=Logs(current_audit_info),
        ), mock.patch(
            "providers.aws.services.cloudwatch.cloudwatch_log_metric_filter_security_group_changes.cloudwatch_log_metric_filter_security_group_changes.cloudwatch_client",
            new=CloudWatch(current_audit_info),
        ), mock.patch(
            "providers.aws.services.cloudwatch.cloudwatch_log_metric_filter_security_group_changes.cloudwatch_log_metric_filter_security_group_changes.cloudtrail_client",
            new=Cloudtrail(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.cloudwatch.cloudwatch_log_metric_filter_security_group_changes.cloudwatch_log_metric_filter_security_group_changes import (
                cloudwatch_log_metric_filter_security_group_changes,
            )

            check = cloudwatch_log_metric_filter_security_group_changes()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert (
                result[0].status_extended
                == "CloudWatch log group /log-group/test found with metric filter test-filter but no alarms associated."
            )
            assert result[0].resource_id == "/log-group/test"

    @mock_logs
    @mock_cloudtrail
    @mock_cloudwatch
    @mock_s3
    def test_cloudwatch_trail_with_log_group_with_metric_and_alarm(self):
        cloudtrail_client = client("cloudtrail", region_name=AWS_REGION)
        cloudwatch_client = client("cloudwatch", region_name=AWS_REGION)
        logs_client = client("logs", region_name=AWS_REGION)
        s3_client = client("s3", region_name=AWS_REGION)
        s3_client.create_bucket(Bucket="test")
        logs_client.create_log_group(logGroupName="/log-group/test")
        cloudtrail_client.create_trail(
            Name="test_trail",
            S3BucketName="test",
            CloudWatchLogsLogGroupArn=f"arn:aws:logs:{AWS_REGION}:{DEFAULT_ACCOUNT_ID}:log-group:/log-group/test:*",
        )
        logs_client.put_metric_filter(
            logGroupName="/log-group/test",
            filterName="test-filter",
            filterPattern="{($.eventName = AuthorizeSecurityGroupIngress) || ($.eventName = AuthorizeSecurityGroupEgress) || ($.eventName = RevokeSecurityGroupIngress) || ($.eventName = RevokeSecurityGroupEgress) || ($.eventName = CreateSecurityGroup) || ($.eventName = DeleteSecurityGroup) }",
            metricTransformations=[
                {
                    "metricName": "my-metric",
                    "metricNamespace": "my-namespace",
                    "metricValue": "$.value",
                }
            ],
        )
        cloudwatch_client.put_metric_alarm(
            AlarmName="test-alarm",
            MetricName="my-metric",
            Namespace="my-namespace",
            Period=10,
            EvaluationPeriods=5,
            Statistic="Average",
            Threshold=2,
            ComparisonOperator="GreaterThanThreshold",
            ActionsEnabled=True,
        )

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.cloudwatch.cloudwatch_service import (
            CloudWatch,
            Logs,
        )

        current_audit_info.audited_partition = "aws"
        from providers.aws.services.cloudtrail.cloudtrail_client import Cloudtrail

        with mock.patch(
            "providers.aws.services.cloudwatch.cloudwatch_log_metric_filter_security_group_changes.cloudwatch_log_metric_filter_security_group_changes.logs_client",
            new=Logs(current_audit_info),
        ), mock.patch(
            "providers.aws.services.cloudwatch.cloudwatch_log_metric_filter_security_group_changes.cloudwatch_log_metric_filter_security_group_changes.cloudwatch_client",
            new=CloudWatch(current_audit_info),
        ), mock.patch(
            "providers.aws.services.cloudwatch.cloudwatch_log_metric_filter_security_group_changes.cloudwatch_log_metric_filter_security_group_changes.cloudtrail_client",
            new=Cloudtrail(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.cloudwatch.cloudwatch_log_metric_filter_security_group_changes.cloudwatch_log_metric_filter_security_group_changes import (
                cloudwatch_log_metric_filter_security_group_changes,
            )

            check = cloudwatch_log_metric_filter_security_group_changes()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "PASS"
            assert (
                result[0].status_extended
                == "CloudWatch log group /log-group/test found with metric filter test-filter and alarms set."
            )
            assert result[0].resource_id == "/log-group/test"
