from unittest import mock

from boto3 import client
from moto import mock_iam


class Test_iam_password_policy_minimum_length_14:
    @mock_iam
    def test_iam_password_policy_minimum_length_equal_14(self):
        iam_client = client("iam")
        # update password policy
        iam_client.update_account_password_policy(MinimumPasswordLength=14)

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.iam.iam_service import IAM

        with mock.patch(
            "providers.aws.services.iam.iam_password_policy_minimum_length_14.iam_password_policy_minimum_length_14.iam_client",
            new=IAM(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.iam.iam_password_policy_minimum_length_14.iam_password_policy_minimum_length_14 import (
                iam_password_policy_minimum_length_14,
            )

            check = iam_password_policy_minimum_length_14()
            result = check.execute()
            assert result[0].status == "PASS"

    @mock_iam
    def test_iam_password_policy_minimum_length_greater_14(self):
        iam_client = client("iam")
        # update password policy
        iam_client.update_account_password_policy(MinimumPasswordLength=20)

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.iam.iam_service import IAM

        with mock.patch(
            "providers.aws.services.iam.iam_password_policy_minimum_length_14.iam_password_policy_minimum_length_14.iam_client",
            new=IAM(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.iam.iam_password_policy_minimum_length_14.iam_password_policy_minimum_length_14 import (
                iam_password_policy_minimum_length_14,
            )

            check = iam_password_policy_minimum_length_14()
            result = check.execute()
            assert result[0].status == "PASS"

    @mock_iam
    def test_iam_password_policy_minimum_length_less_14(self):
        iam_client = client("iam")
        # update password policy
        iam_client.update_account_password_policy(MinimumPasswordLength=10)

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.iam.iam_service import IAM

        with mock.patch(
            "providers.aws.services.iam.iam_password_policy_minimum_length_14.iam_password_policy_minimum_length_14.iam_client",
            new=IAM(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.iam.iam_password_policy_minimum_length_14.iam_password_policy_minimum_length_14 import (
                iam_password_policy_minimum_length_14,
            )

            check = iam_password_policy_minimum_length_14()
            result = check.execute()
            assert result[0].status == "FAIL"
