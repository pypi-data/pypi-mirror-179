from json import dumps
from re import search
from unittest import mock

from boto3 import client
from moto import mock_iam


class Test_iam_administrator_access_with_mfa_test:
    @mock_iam
    def test_group_with_no_policies(self):
        iam = client("iam")
        group_name = "test-group"

        arn = iam.create_group(GroupName=group_name)["Group"]["Arn"]

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.iam.iam_service import IAM

        with mock.patch(
            "providers.aws.services.iam.iam_administrator_access_with_mfa.iam_administrator_access_with_mfa.iam_client",
            new=IAM(current_audit_info),
        ):
            from providers.aws.services.iam.iam_administrator_access_with_mfa.iam_administrator_access_with_mfa import (
                iam_administrator_access_with_mfa,
            )

            check = iam_administrator_access_with_mfa()
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "PASS"
            assert result[0].resource_id == group_name
            assert result[0].resource_arn == arn
            assert search(
                f"Group {group_name} has no policies.", result[0].status_extended
            )

    @mock_iam
    def test_group_non_administrative_policy(self):
        iam = client("iam")
        group_name = "test-group"
        policy_name = "policy1"
        policy_document = {
            "Version": "2012-10-17",
            "Statement": [
                {"Effect": "Allow", "Action": "logs:CreateLogGroup", "Resource": "*"},
            ],
        }
        policy_arn = iam.create_policy(
            PolicyName=policy_name, PolicyDocument=dumps(policy_document)
        )["Policy"]["Arn"]
        arn = iam.create_group(GroupName=group_name)["Group"]["Arn"]
        iam.attach_group_policy(GroupName=group_name, PolicyArn=policy_arn)

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.iam.iam_service import IAM

        with mock.patch(
            "providers.aws.services.iam.iam_administrator_access_with_mfa.iam_administrator_access_with_mfa.iam_client",
            new=IAM(current_audit_info),
        ):
            from providers.aws.services.iam.iam_administrator_access_with_mfa.iam_administrator_access_with_mfa import (
                iam_administrator_access_with_mfa,
            )

            check = iam_administrator_access_with_mfa()
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "PASS"
            assert result[0].resource_id == group_name
            assert result[0].resource_arn == arn
            assert search(
                f"Group {group_name} provides non-administrative access.",
                result[0].status_extended,
            )

    @mock_iam
    def test_admin_policy_no_users(self):
        iam = client("iam")
        group_name = "test-group"

        arn = iam.create_group(GroupName=group_name)["Group"]["Arn"]
        iam.attach_group_policy(
            GroupName=group_name,
            PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess",
        )

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.iam.iam_service import IAM

        with mock.patch(
            "providers.aws.services.iam.iam_administrator_access_with_mfa.iam_administrator_access_with_mfa.iam_client",
            new=IAM(current_audit_info),
        ):
            from providers.aws.services.iam.iam_administrator_access_with_mfa.iam_administrator_access_with_mfa import (
                iam_administrator_access_with_mfa,
            )

            check = iam_administrator_access_with_mfa()
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "PASS"
            assert result[0].resource_id == group_name
            assert result[0].resource_arn == arn
            assert search(
                f"Group {group_name} provides administrative access but does not have users.",
                result[0].status_extended,
            )

    @mock_iam
    def test_admin_policy_with_user_without_mfa(self):
        iam = client("iam")
        group_name = "test-group"
        user_name = "user-test"
        iam.create_user(UserName=user_name)
        arn = iam.create_group(GroupName=group_name)["Group"]["Arn"]
        iam.attach_group_policy(
            GroupName=group_name,
            PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess",
        )
        iam.add_user_to_group(GroupName=group_name, UserName=user_name)

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.iam.iam_service import IAM

        with mock.patch(
            "providers.aws.services.iam.iam_administrator_access_with_mfa.iam_administrator_access_with_mfa.iam_client",
            new=IAM(current_audit_info),
        ):
            from providers.aws.services.iam.iam_administrator_access_with_mfa.iam_administrator_access_with_mfa import (
                iam_administrator_access_with_mfa,
            )

            check = iam_administrator_access_with_mfa()
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert result[0].resource_id == group_name
            assert result[0].resource_arn == arn
            assert search(
                f"Group {group_name} provides administrator access to User {user_name} with MFA disabled.",
                result[0].status_extended,
            )

    @mock_iam
    def test_various_policies_with_users_with_and_without_mfa(self):
        iam = client("iam")
        group_name = "test-group"
        user_name_no_mfa = "user-no-mfa"
        user_name_mfa = "user-mfa"
        policy_name = "policy1"
        policy_document = {
            "Version": "2012-10-17",
            "Statement": [
                {"Effect": "Allow", "Action": "logs:CreateLogGroup", "Resource": "*"},
            ],
        }
        mfa_device_name = "mfa-test"
        mfa_serial_number = iam.create_virtual_mfa_device(
            VirtualMFADeviceName=mfa_device_name
        )["VirtualMFADevice"]["SerialNumber"]
        iam.create_user(UserName=user_name_no_mfa)
        iam.create_user(UserName=user_name_mfa)
        iam.enable_mfa_device(
            UserName=user_name_mfa,
            SerialNumber=mfa_serial_number,
            AuthenticationCode1="123456",
            AuthenticationCode2="123466",
        )
        policy_arn = iam.create_policy(
            PolicyName=policy_name, PolicyDocument=dumps(policy_document)
        )["Policy"]["Arn"]
        arn_group = iam.create_group(GroupName=group_name)["Group"]["Arn"]
        iam.attach_group_policy(GroupName=group_name, PolicyArn=policy_arn)
        iam.attach_group_policy(
            GroupName=group_name,
            PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess",
        )
        iam.add_user_to_group(GroupName=group_name, UserName=user_name_no_mfa)
        iam.add_user_to_group(GroupName=group_name, UserName=user_name_mfa)

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.iam.iam_service import IAM

        with mock.patch(
            "providers.aws.services.iam.iam_administrator_access_with_mfa.iam_administrator_access_with_mfa.iam_client",
            new=IAM(current_audit_info),
        ):
            from providers.aws.services.iam.iam_administrator_access_with_mfa.iam_administrator_access_with_mfa import (
                iam_administrator_access_with_mfa,
            )

            check = iam_administrator_access_with_mfa()
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert result[0].resource_id == group_name
            assert result[0].resource_arn == arn_group
            assert search(
                f"Group {group_name} provides administrator access to User {user_name_no_mfa} with MFA disabled.",
                result[0].status_extended,
            )
