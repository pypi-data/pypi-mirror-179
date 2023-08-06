from unittest import mock

from boto3 import client, session
from mock import patch
from moto import mock_cloudtrail, mock_s3
from moto.core import DEFAULT_ACCOUNT_ID

from providers.aws.lib.audit_info.audit_info import AWS_Audit_Info
from providers.aws.services.awslambda.awslambda_service import Function

AWS_REGION = "us-east-1"


# Mock generate_regional_clients()
def mock_generate_regional_clients(service, audit_info):
    regional_client = audit_info.audit_session.client(service, region_name=AWS_REGION)
    regional_client.region = AWS_REGION
    return {AWS_REGION: regional_client}


# Patch every AWS call using Boto3 and generate_regional_clients to have 1 client
@patch(
    "providers.aws.services.accessanalyzer.accessanalyzer_service.generate_regional_clients",
    new=mock_generate_regional_clients,
)
class Test_awslambda_function_invoke_api_operations_cloudtrail_logging_enabled:
    # Mocked Audit Info
    def set_mocked_audit_info(self):
        audit_info = AWS_Audit_Info(
            original_session=None,
            audit_session=session.Session(
                profile_name=None,
                botocore_session=None,
            ),
            audited_account=None,
            audited_user_id=None,
            audited_partition="aws",
            audited_identity_arn=None,
            profile=None,
            profile_region=None,
            credentials=None,
            assumed_role_info=None,
            audited_regions=None,
            organizations_metadata=None,
        )
        return audit_info

    @mock_cloudtrail
    def test_no_functions(self):
        lambda_client = mock.MagicMock
        lambda_client.functions = {}

        from providers.aws.services.cloudtrail.cloudtrail_service import Cloudtrail

        with mock.patch(
            "providers.aws.services.awslambda.awslambda_service.Lambda",
            new=lambda_client,
        ), mock.patch(
            "providers.aws.lib.audit_info.audit_info.current_audit_info",
            self.set_mocked_audit_info(),
        ), mock.patch(
            "providers.aws.services.awslambda.awslambda_function_invoke_api_operations_cloudtrail_logging_enabled.awslambda_function_invoke_api_operations_cloudtrail_logging_enabled.cloudtrail_client",
            new=Cloudtrail(self.set_mocked_audit_info()),
        ):
            # Test Check
            from providers.aws.services.awslambda.awslambda_function_invoke_api_operations_cloudtrail_logging_enabled.awslambda_function_invoke_api_operations_cloudtrail_logging_enabled import (
                awslambda_function_invoke_api_operations_cloudtrail_logging_enabled,
            )

            check = (
                awslambda_function_invoke_api_operations_cloudtrail_logging_enabled()
            )
            result = check.execute()

            assert len(result) == 0

    @mock_cloudtrail
    @mock_s3
    def test_lambda_not_recorded_by_cloudtrail(self):
        # Lambda Client
        lambda_client = mock.MagicMock
        function_name = "test-lambda"
        function_runtime = "python3.9"
        function_arn = (
            f"arn:aws:lambda:{AWS_REGION}:{DEFAULT_ACCOUNT_ID}:function/{function_name}"
        )
        lambda_client.functions = {
            function_name: Function(
                name=function_name,
                arn=function_arn,
                region=AWS_REGION,
                runtime=function_runtime,
            )
        }

        # CloudTrail Client
        cloudtrail_client = client("cloudtrail", region_name=AWS_REGION)
        s3_client = client("s3", region_name=AWS_REGION)
        trail_name = "test-trail"
        bucket_name = "test-bucket"
        s3_client.create_bucket(Bucket=bucket_name)
        cloudtrail_client.create_trail(
            Name=trail_name, S3BucketName=bucket_name, IsMultiRegionTrail=False
        )

        from providers.aws.services.cloudtrail.cloudtrail_service import Cloudtrail

        with mock.patch(
            "providers.aws.services.awslambda.awslambda_service.Lambda",
            new=lambda_client,
        ), mock.patch(
            "providers.aws.lib.audit_info.audit_info.current_audit_info",
            self.set_mocked_audit_info(),
        ), mock.patch(
            "providers.aws.services.awslambda.awslambda_function_invoke_api_operations_cloudtrail_logging_enabled.awslambda_function_invoke_api_operations_cloudtrail_logging_enabled.cloudtrail_client",
            new=Cloudtrail(self.set_mocked_audit_info()),
        ):

            # Test Check
            from providers.aws.services.awslambda.awslambda_function_invoke_api_operations_cloudtrail_logging_enabled.awslambda_function_invoke_api_operations_cloudtrail_logging_enabled import (
                awslambda_function_invoke_api_operations_cloudtrail_logging_enabled,
            )

            check = (
                awslambda_function_invoke_api_operations_cloudtrail_logging_enabled()
            )
            result = check.execute()

            assert len(result) == 1
            assert result[0].region == AWS_REGION
            assert result[0].resource_id == function_name
            assert result[0].resource_arn == function_arn
            assert result[0].status == "FAIL"
            assert (
                result[0].status_extended
                == f"Lambda function {function_name} is not recorded by CloudTrail"
            )

    @mock_cloudtrail
    @mock_s3
    def test_lambda_recorded_by_cloudtrail(self):
        # Lambda Client
        lambda_client = mock.MagicMock
        function_name = "test-lambda"
        function_runtime = "python3.9"
        function_arn = (
            f"arn:aws:lambda:{AWS_REGION}:{DEFAULT_ACCOUNT_ID}:function/{function_name}"
        )
        lambda_client.functions = {
            function_name: Function(
                name=function_name,
                arn=function_arn,
                region=AWS_REGION,
                runtime=function_runtime,
            )
        }

        # CloudTrail Client
        cloudtrail_client = client("cloudtrail", region_name=AWS_REGION)
        s3_client = client("s3", region_name=AWS_REGION)
        trail_name = "test-trail"
        bucket_name = "test-bucket"
        s3_client.create_bucket(Bucket=bucket_name)
        cloudtrail_client.create_trail(
            Name=trail_name, S3BucketName=bucket_name, IsMultiRegionTrail=False
        )
        _ = cloudtrail_client.put_event_selectors(
            TrailName=trail_name,
            EventSelectors=[
                {
                    "ReadWriteType": "All",
                    "IncludeManagementEvents": True,
                    "DataResources": [
                        {"Type": "AWS::Lambda::Function", "Values": [function_arn]}
                    ],
                }
            ],
        )

        from providers.aws.services.cloudtrail.cloudtrail_service import Cloudtrail

        with mock.patch(
            "providers.aws.services.awslambda.awslambda_service.Lambda",
            new=lambda_client,
        ), mock.patch(
            "providers.aws.lib.audit_info.audit_info.current_audit_info",
            self.set_mocked_audit_info(),
        ), mock.patch(
            "providers.aws.services.awslambda.awslambda_function_invoke_api_operations_cloudtrail_logging_enabled.awslambda_function_invoke_api_operations_cloudtrail_logging_enabled.cloudtrail_client",
            new=Cloudtrail(self.set_mocked_audit_info()),
        ):

            # Test Check
            from providers.aws.services.awslambda.awslambda_function_invoke_api_operations_cloudtrail_logging_enabled.awslambda_function_invoke_api_operations_cloudtrail_logging_enabled import (
                awslambda_function_invoke_api_operations_cloudtrail_logging_enabled,
            )

            check = (
                awslambda_function_invoke_api_operations_cloudtrail_logging_enabled()
            )
            result = check.execute()

            assert len(result) == 1
            assert result[0].region == AWS_REGION
            assert result[0].resource_id == function_name
            assert result[0].resource_arn == function_arn
            assert result[0].status == "PASS"
            assert (
                result[0].status_extended
                == f"Lambda function {function_name} is recorded by CloudTrail {trail_name}"
            )
