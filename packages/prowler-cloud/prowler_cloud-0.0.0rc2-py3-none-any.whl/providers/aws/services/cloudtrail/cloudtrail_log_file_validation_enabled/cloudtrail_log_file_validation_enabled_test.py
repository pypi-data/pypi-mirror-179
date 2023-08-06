from re import search
from unittest import mock

from boto3 import client
from moto import mock_cloudtrail, mock_s3


class Test_cloudtrail_log_file_validation_enabled:
    @mock_cloudtrail
    @mock_s3
    def test_no_logging_validation(self):
        cloudtrail_client_us_east_1 = client("cloudtrail", region_name="us-east-1")
        s3_client_us_east_1 = client("s3", region_name="us-east-1")
        trail_name_us = "trail_test_us"
        bucket_name_us = "bucket_test_us"
        s3_client_us_east_1.create_bucket(Bucket=bucket_name_us)
        trail_us = cloudtrail_client_us_east_1.create_trail(
            Name=trail_name_us, S3BucketName=bucket_name_us, IsMultiRegionTrail=False
        )
        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.cloudtrail.cloudtrail_service import Cloudtrail

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "providers.aws.services.cloudtrail.cloudtrail_log_file_validation_enabled.cloudtrail_log_file_validation_enabled.cloudtrail_client",
            new=Cloudtrail(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.cloudtrail.cloudtrail_log_file_validation_enabled.cloudtrail_log_file_validation_enabled import (
                cloudtrail_log_file_validation_enabled,
            )

            check = cloudtrail_log_file_validation_enabled()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert search("log file validation disabled", result[0].status_extended)
            assert result[0].resource_id == trail_name_us
            assert result[0].resource_arn == trail_us["TrailARN"]

    @mock_cloudtrail
    @mock_s3
    def test_various_trails_with_and_without_logging_validation(self):
        cloudtrail_client_us_east_1 = client("cloudtrail", region_name="us-east-1")
        s3_client_us_east_1 = client("s3", region_name="us-east-1")
        cloudtrail_client_eu_west_1 = client("cloudtrail", region_name="eu-west-1")
        s3_client_eu_west_1 = client("s3", region_name="eu-west-1")
        trail_name_us = "trail_test_us"
        bucket_name_us = "bucket_test_us"
        trail_name_eu = "trail_test_eu"
        bucket_name_eu = "bucket_test_eu"
        s3_client_us_east_1.create_bucket(Bucket=bucket_name_us)
        s3_client_eu_west_1.create_bucket(
            Bucket=bucket_name_eu,
            CreateBucketConfiguration={"LocationConstraint": "eu-west-1"},
        )
        trail_us = cloudtrail_client_us_east_1.create_trail(
            Name=trail_name_us,
            S3BucketName=bucket_name_us,
            IsMultiRegionTrail=False,
            EnableLogFileValidation=True,
        )
        trail_eu = cloudtrail_client_eu_west_1.create_trail(
            Name=trail_name_eu, S3BucketName=bucket_name_eu, IsMultiRegionTrail=False
        )

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.cloudtrail.cloudtrail_service import Cloudtrail

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "providers.aws.services.cloudtrail.cloudtrail_log_file_validation_enabled.cloudtrail_log_file_validation_enabled.cloudtrail_client",
            new=Cloudtrail(current_audit_info),
        ) as service_client:
            # Test Check
            from providers.aws.services.cloudtrail.cloudtrail_log_file_validation_enabled.cloudtrail_log_file_validation_enabled import (
                cloudtrail_log_file_validation_enabled,
            )

            regions = []
            for region in service_client.regional_clients.keys():
                regions.append(region)

            check = cloudtrail_log_file_validation_enabled()
            result = check.execute()
            assert len(result) == 2
            for report in result:
                if report.resource_id == trail_name_us:
                    assert report.status == "PASS"
                    assert search("log file validation enabled", report.status_extended)
                    assert report.resource_id == trail_name_us
                    assert report.resource_arn == trail_us["TrailARN"]
                elif report.resource_id == trail_name_eu:
                    assert report.status == "FAIL"
                    assert search(
                        "log file validation disabled", report.status_extended
                    )
                    assert report.resource_id == trail_name_eu
                    assert report.resource_arn == trail_eu["TrailARN"]
