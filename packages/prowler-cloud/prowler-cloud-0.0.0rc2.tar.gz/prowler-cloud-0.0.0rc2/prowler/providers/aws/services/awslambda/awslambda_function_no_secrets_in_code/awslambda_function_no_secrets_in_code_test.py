import zipfile
from unittest import mock

from moto.core import DEFAULT_ACCOUNT_ID

from providers.aws.services.awslambda.awslambda_service import Function, LambdaCode
from providers.aws.services.awslambda.awslambda_service_test import create_zip_file

AWS_REGION = "us-east-1"


class Test_awslambda_function_no_secrets_in_code:
    def test_no_functions(self):
        lambda_client = mock.MagicMock
        lambda_client.functions = {}

        with mock.patch(
            "providers.aws.services.awslambda.awslambda_service.Lambda",
            new=lambda_client,
        ):
            # Test Check
            from providers.aws.services.awslambda.awslambda_function_no_secrets_in_code.awslambda_function_no_secrets_in_code import (
                awslambda_function_no_secrets_in_code,
            )

            check = awslambda_function_no_secrets_in_code()
            result = check.execute()

            assert len(result) == 0

    def test_function_code_with_secrets(self):
        lambda_client = mock.MagicMock
        function_name = "test-lambda"
        function_runtime = "nodejs4.3"
        function_arn = (
            f"arn:aws:lambda:{AWS_REGION}:{DEFAULT_ACCOUNT_ID}:function/{function_name}"
        )
        code_with_secrets = """
        def lambda_handler(event, context):
                db_password = "test-password"
                print("custom log event")
                return event
        """
        lambda_client.functions = {
            "function_name": Function(
                name=function_name,
                arn=function_arn,
                region=AWS_REGION,
                runtime=function_runtime,
                code=LambdaCode(
                    location="",
                    code_zip=zipfile.ZipFile(create_zip_file(code_with_secrets)),
                ),
            )
        }

        with mock.patch(
            "providers.aws.services.awslambda.awslambda_service.Lambda",
            new=lambda_client,
        ):
            # Test Check
            from providers.aws.services.awslambda.awslambda_function_no_secrets_in_code.awslambda_function_no_secrets_in_code import (
                awslambda_function_no_secrets_in_code,
            )

            check = awslambda_function_no_secrets_in_code()
            result = check.execute()

            assert len(result) == 1
            assert result[0].region == AWS_REGION
            assert result[0].resource_id == function_name
            assert result[0].resource_arn == function_arn
            assert result[0].status == "FAIL"
            assert (
                result[0].status_extended
                == f"Potential secret found in Lambda function {function_name} code"
            )

    def test_function_code_without_secrets(self):
        lambda_client = mock.MagicMock
        function_name = "test-lambda"
        function_runtime = "nodejs4.3"
        function_arn = (
            f"arn:aws:lambda:{AWS_REGION}:{DEFAULT_ACCOUNT_ID}:function/{function_name}"
        )
        code_with_secrets = """
        def lambda_handler(event, context):
                print("custom log event")
                return event
        """
        lambda_client.functions = {
            "function_name": Function(
                name=function_name,
                arn=function_arn,
                region=AWS_REGION,
                runtime=function_runtime,
                code=LambdaCode(
                    location="",
                    code_zip=zipfile.ZipFile(create_zip_file(code_with_secrets)),
                ),
            )
        }

        with mock.patch(
            "providers.aws.services.awslambda.awslambda_service.Lambda",
            new=lambda_client,
        ):
            # Test Check
            from providers.aws.services.awslambda.awslambda_function_no_secrets_in_code.awslambda_function_no_secrets_in_code import (
                awslambda_function_no_secrets_in_code,
            )

            check = awslambda_function_no_secrets_in_code()
            result = check.execute()

            assert len(result) == 1
            assert result[0].region == AWS_REGION
            assert result[0].resource_id == function_name
            assert result[0].resource_arn == function_arn
            assert result[0].status == "PASS"
            assert (
                result[0].status_extended
                == f"No secrets found in Lambda function {function_name} code"
            )
