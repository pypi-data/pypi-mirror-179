from re import search
from unittest import mock

from boto3 import client
from moto import mock_s3


class Test_s3_bucket_secure_transport_policy:
    @mock_s3
    def test_bucket_no_policy(self):
        s3_client_us_east_1 = client("s3", region_name="us-east-1")
        bucket_name_us = "bucket_test_us"
        s3_client_us_east_1.create_bucket(Bucket=bucket_name_us)

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.s3.s3_service import S3

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "providers.aws.services.s3.s3_bucket_secure_transport_policy.s3_bucket_secure_transport_policy.s3_client",
            new=S3(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.s3.s3_bucket_secure_transport_policy.s3_bucket_secure_transport_policy import (
                s3_bucket_secure_transport_policy,
            )

            check = s3_bucket_secure_transport_policy()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert search(
                "does not have a bucket policy",
                result[0].status_extended,
            )
            assert result[0].resource_id == bucket_name_us
            assert result[0].region == "us-east-1"

    @mock_s3
    def test_bucket_comply_policy(self):
        s3_client_us_east_1 = client("s3", region_name="us-east-1")
        bucket_name_us = "bucket_test_us"
        s3_client_us_east_1.create_bucket(Bucket=bucket_name_us)

        ssl_policy = """
{
  "Version": "2012-10-17",
  "Id": "PutObjPolicy",
  "Statement": [
    {
      "Sid": "s3-bucket-ssl-requests-only",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::bucket_test_us/*",
      "Condition": {
        "Bool": {
          "aws:SecureTransport": "false"
        }
      }
    }
  ]
}
"""
        s3_client_us_east_1.put_bucket_policy(
            Bucket=bucket_name_us,
            Policy=ssl_policy,
        )
        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.s3.s3_service import S3

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "providers.aws.services.s3.s3_bucket_secure_transport_policy.s3_bucket_secure_transport_policy.s3_client",
            new=S3(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.s3.s3_bucket_secure_transport_policy.s3_bucket_secure_transport_policy import (
                s3_bucket_secure_transport_policy,
            )

            check = s3_bucket_secure_transport_policy()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "PASS"
            assert search(
                "bucket policy to deny requests over insecure transport",
                result[0].status_extended,
            )
            assert result[0].resource_id == bucket_name_us
            assert result[0].region == "us-east-1"

    @mock_s3
    def test_bucket_uncomply_policy(self):
        s3_client_us_east_1 = client("s3", region_name="us-east-1")
        bucket_name_us = "bucket_test_us"
        s3_client_us_east_1.create_bucket(Bucket=bucket_name_us)

        ssl_policy = """
{
  "Version": "2012-10-17",
  "Id": "PutObjPolicy",
  "Statement": [
    {
      "Sid": "s3-bucket-ssl-requests-only",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::bucket_test_us/*",
      "Condition": {
        "Bool": {
          "aws:SecureTransport": "false"
        }
      }
    }
  ]
}
"""
        s3_client_us_east_1.put_bucket_policy(
            Bucket=bucket_name_us,
            Policy=ssl_policy,
        )
        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.s3.s3_service import S3

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "providers.aws.services.s3.s3_bucket_secure_transport_policy.s3_bucket_secure_transport_policy.s3_client",
            new=S3(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.s3.s3_bucket_secure_transport_policy.s3_bucket_secure_transport_policy import (
                s3_bucket_secure_transport_policy,
            )

            check = s3_bucket_secure_transport_policy()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert search(
                "allows requests over insecure transport in the bucket policy",
                result[0].status_extended,
            )
            assert result[0].resource_id == bucket_name_us
            assert result[0].region == "us-east-1"
