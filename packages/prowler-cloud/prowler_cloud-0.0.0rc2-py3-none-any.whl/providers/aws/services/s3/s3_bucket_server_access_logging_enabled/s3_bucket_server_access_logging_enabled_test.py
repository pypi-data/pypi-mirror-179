from re import search
from unittest import mock

from boto3 import client
from moto import mock_s3

ACCOUNT_ID = "123456789012"


class Test_s3_bucket_server_access_logging_enabled:
    @mock_s3
    def test_bucket_no_logging(self):
        s3_client_us_east_1 = client("s3", region_name="us-east-1")
        bucket_name_us = "bucket_test_us"
        s3_client_us_east_1.create_bucket(Bucket=bucket_name_us)

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.s3.s3_service import S3

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "providers.aws.services.s3.s3_bucket_server_access_logging_enabled.s3_bucket_server_access_logging_enabled.s3_client",
            new=S3(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.s3.s3_bucket_server_access_logging_enabled.s3_bucket_server_access_logging_enabled import (
                s3_bucket_server_access_logging_enabled,
            )

            check = s3_bucket_server_access_logging_enabled()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert search(
                "server access logging disabled",
                result[0].status_extended,
            )
            assert result[0].resource_id == bucket_name_us

    @mock_s3
    def test_bucket_with_logging(self):
        s3_client_us_east_1 = client("s3", region_name="us-east-1")
        bucket_name_us = "bucket_test_us"
        s3_client_us_east_1.create_bucket(Bucket=bucket_name_us)
        bucket_owner = s3_client_us_east_1.get_bucket_acl(Bucket=bucket_name_us)[
            "Owner"
        ]
        s3_client_us_east_1.put_bucket_acl(
            Bucket=bucket_name_us,
            AccessControlPolicy={
                "Grants": [
                    {
                        "Grantee": {
                            "URI": "http://acs.amazonaws.com/groups/s3/LogDelivery",
                            "Type": "Group",
                        },
                        "Permission": "WRITE",
                    },
                    {
                        "Grantee": {
                            "URI": "http://acs.amazonaws.com/groups/s3/LogDelivery",
                            "Type": "Group",
                        },
                        "Permission": "READ_ACP",
                    },
                    {
                        "Grantee": {"Type": "CanonicalUser", "ID": bucket_owner["ID"]},
                        "Permission": "FULL_CONTROL",
                    },
                ],
                "Owner": bucket_owner,
            },
        )

        s3_client_us_east_1.put_bucket_logging(
            Bucket=bucket_name_us,
            BucketLoggingStatus={
                "LoggingEnabled": {
                    "TargetBucket": bucket_name_us,
                    "TargetPrefix": "{}/".format(bucket_name_us),
                    "TargetGrants": [
                        {
                            "Grantee": {
                                "ID": "SOMEIDSTRINGHERE9238748923734823917498237489237409123840983274",
                                "Type": "CanonicalUser",
                            },
                            "Permission": "READ",
                        },
                        {
                            "Grantee": {
                                "ID": "SOMEIDSTRINGHERE9238748923734823917498237489237409123840983274",
                                "Type": "CanonicalUser",
                            },
                            "Permission": "WRITE",
                        },
                    ],
                }
            },
        )
        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.s3.s3_service import S3

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "providers.aws.services.s3.s3_bucket_server_access_logging_enabled.s3_bucket_server_access_logging_enabled.s3_client",
            new=S3(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.s3.s3_bucket_server_access_logging_enabled.s3_bucket_server_access_logging_enabled import (
                s3_bucket_server_access_logging_enabled,
            )

            check = s3_bucket_server_access_logging_enabled()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "PASS"
            assert search(
                "server access logging enabled",
                result[0].status_extended,
            )
            assert result[0].resource_id == bucket_name_us
