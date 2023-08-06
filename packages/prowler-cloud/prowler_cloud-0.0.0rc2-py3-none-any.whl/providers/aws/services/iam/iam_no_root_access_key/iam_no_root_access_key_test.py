from re import search
from unittest import mock

from boto3 import client
from moto import mock_iam


class Test_iam_no_root_access_key_test:
    @mock_iam
    def test_iam_root_no_access_keys(self):
        iam_client = client("iam")
        user = "test"
        iam_client.create_user(UserName=user)["User"]["Arn"]

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.iam.iam_service import IAM

        with mock.patch(
            "providers.aws.services.iam.iam_no_root_access_key.iam_no_root_access_key.iam_client",
            new=IAM(current_audit_info),
        ) as service_client:
            from providers.aws.services.iam.iam_no_root_access_key.iam_no_root_access_key import (
                iam_no_root_access_key,
            )

            service_client.credential_report[0]["user"] = "<root_account>"
            service_client.credential_report[0][
                "arn"
            ] = "arn:aws:iam::123456789012:user/<root_account>"
            service_client.credential_report[0]["access_key_1_active"] = "false"
            service_client.credential_report[0]["access_key_2_active"] = "false"
            check = iam_no_root_access_key()
            result = check.execute()

            # raise Exception
            assert result[0].status == "PASS"
            assert search(
                "User <root_account> has not access keys.",
                result[0].status_extended,
            )
            assert result[0].resource_id == "<root_account>"
            assert (
                result[0].resource_arn
                == "arn:aws:iam::123456789012:user/<root_account>"
            )

    @mock_iam
    def test_iam_root_access_key_1(self):
        iam_client = client("iam")
        user = "test"
        iam_client.create_user(UserName=user)["User"]["Arn"]

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.iam.iam_service import IAM

        with mock.patch(
            "providers.aws.services.iam.iam_no_root_access_key.iam_no_root_access_key.iam_client",
            new=IAM(current_audit_info),
        ) as service_client:
            from providers.aws.services.iam.iam_no_root_access_key.iam_no_root_access_key import (
                iam_no_root_access_key,
            )

            service_client.credential_report[0]["user"] = "<root_account>"
            service_client.credential_report[0][
                "arn"
            ] = "arn:aws:iam::123456789012:user/<root_account>"
            service_client.credential_report[0]["access_key_1_active"] = "true"
            service_client.credential_report[0]["access_key_2_active"] = "false"
            check = iam_no_root_access_key()
            result = check.execute()

            # raise Exception
            assert result[0].status == "FAIL"
            assert search(
                "User <root_account> has one active access key.",
                result[0].status_extended,
            )
            assert result[0].resource_id == "<root_account>"
            assert (
                result[0].resource_arn
                == "arn:aws:iam::123456789012:user/<root_account>"
            )

    @mock_iam
    def test_iam_root_access_key_2(self):
        iam_client = client("iam")
        user = "test"
        iam_client.create_user(UserName=user)["User"]["Arn"]

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.iam.iam_service import IAM

        with mock.patch(
            "providers.aws.services.iam.iam_no_root_access_key.iam_no_root_access_key.iam_client",
            new=IAM(current_audit_info),
        ) as service_client:
            from providers.aws.services.iam.iam_no_root_access_key.iam_no_root_access_key import (
                iam_no_root_access_key,
            )

            service_client.credential_report[0]["user"] = "<root_account>"
            service_client.credential_report[0][
                "arn"
            ] = "arn:aws:iam::123456789012:user/<root_account>"
            service_client.credential_report[0]["access_key_1_active"] = "false"
            service_client.credential_report[0]["access_key_2_active"] = "true"
            check = iam_no_root_access_key()
            result = check.execute()

            # raise Exception
            assert result[0].status == "FAIL"
            assert search(
                "User <root_account> has one active access key.",
                result[0].status_extended,
            )
            assert result[0].resource_id == "<root_account>"
            assert (
                result[0].resource_arn
                == "arn:aws:iam::123456789012:user/<root_account>"
            )

    @mock_iam
    def test_iam_root_both_access_keys(self):
        iam_client = client("iam")
        user = "test"
        iam_client.create_user(UserName=user)["User"]["Arn"]

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.iam.iam_service import IAM

        with mock.patch(
            "providers.aws.services.iam.iam_no_root_access_key.iam_no_root_access_key.iam_client",
            new=IAM(current_audit_info),
        ) as service_client:
            from providers.aws.services.iam.iam_no_root_access_key.iam_no_root_access_key import (
                iam_no_root_access_key,
            )

            service_client.credential_report[0]["user"] = "<root_account>"
            service_client.credential_report[0][
                "arn"
            ] = "arn:aws:iam::123456789012:user/<root_account>"
            service_client.credential_report[0]["access_key_1_active"] = "true"
            service_client.credential_report[0]["access_key_2_active"] = "true"
            check = iam_no_root_access_key()
            result = check.execute()

            # raise Exception
            assert result[0].status == "FAIL"
            assert search(
                "User <root_account> has two active access key.",
                result[0].status_extended,
            )
            assert result[0].resource_id == "<root_account>"
            assert (
                result[0].resource_arn
                == "arn:aws:iam::123456789012:user/<root_account>"
            )
