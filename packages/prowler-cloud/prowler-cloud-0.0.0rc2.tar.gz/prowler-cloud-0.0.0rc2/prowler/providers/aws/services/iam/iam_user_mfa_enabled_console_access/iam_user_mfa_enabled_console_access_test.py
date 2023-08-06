from unittest import mock

from boto3 import client
from moto import mock_iam


class Test_iam_user_mfa_enabled_console_access_test:
    @mock_iam
    def test_user_not_password_console_enabled(self):
        iam_client = client("iam")
        user = "test-user"
        arn = iam_client.create_user(UserName=user)["User"]["Arn"]

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.iam.iam_service import IAM

        with mock.patch(
            "providers.aws.services.iam.iam_user_mfa_enabled_console_access.iam_user_mfa_enabled_console_access.iam_client",
            new=IAM(current_audit_info),
        ) as service_client:
            from providers.aws.services.iam.iam_user_mfa_enabled_console_access.iam_user_mfa_enabled_console_access import (
                iam_user_mfa_enabled_console_access,
            )

            service_client.credential_report[0]["password_enabled"] = "not_supported"

            check = iam_user_mfa_enabled_console_access()
            result = check.execute()

            assert result[0].status == "PASS"
            assert (
                result[0].status_extended
                == f"User {user} has not Console Password enabled."
            )
            assert result[0].resource_id == user
            assert result[0].resource_arn == arn

    @mock_iam
    def test_user_password_console_and_mfa_enabled(self):
        iam_client = client("iam")
        user = "test-user"
        arn = iam_client.create_user(UserName=user)["User"]["Arn"]

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.iam.iam_service import IAM

        with mock.patch(
            "providers.aws.services.iam.iam_user_mfa_enabled_console_access.iam_user_mfa_enabled_console_access.iam_client",
            new=IAM(current_audit_info),
        ) as service_client:
            from providers.aws.services.iam.iam_user_mfa_enabled_console_access.iam_user_mfa_enabled_console_access import (
                iam_user_mfa_enabled_console_access,
            )

            service_client.credential_report[0]["password_enabled"] = "true"
            service_client.credential_report[0]["mfa_active"] = "true"

            check = iam_user_mfa_enabled_console_access()
            result = check.execute()

            assert result[0].status == "PASS"
            assert (
                result[0].status_extended
                == f"User {user} has Console Password enabled and MFA enabled."
            )
            assert result[0].resource_id == user
            assert result[0].resource_arn == arn

    @mock_iam
    def test_user_password_console_enabled_and_mfa_not_enabled(self):
        iam_client = client("iam")
        user = "test-user"
        arn = iam_client.create_user(UserName=user)["User"]["Arn"]

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.iam.iam_service import IAM

        with mock.patch(
            "providers.aws.services.iam.iam_user_mfa_enabled_console_access.iam_user_mfa_enabled_console_access.iam_client",
            new=IAM(current_audit_info),
        ) as service_client:
            from providers.aws.services.iam.iam_user_mfa_enabled_console_access.iam_user_mfa_enabled_console_access import (
                iam_user_mfa_enabled_console_access,
            )

            service_client.credential_report[0]["password_enabled"] = "true"
            service_client.credential_report[0]["mfa_active"] = "false"

            check = iam_user_mfa_enabled_console_access()
            result = check.execute()

            assert result[0].status == "FAIL"
            assert (
                result[0].status_extended
                == f"User {user} has Console Password enabled but MFA disabled."
            )
            assert result[0].resource_id == user
            assert result[0].resource_arn == arn
