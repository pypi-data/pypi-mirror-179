from json import dumps
from re import search
from unittest import mock

from boto3 import client
from moto import mock_iam


class Test_iam_policy_attached_only_to_group_or_roles:
    @mock_iam
    def test_iam_user_attached_policy(self):
        result = []
        iam_client = client("iam")
        user = "test_attached_policy"
        policy_name = "policy1"
        policy_document = {
            "Version": "2012-10-17",
            "Statement": [
                {"Effect": "Allow", "Action": "logs:CreateLogGroup", "Resource": "*"},
            ],
        }
        iam_client.create_user(UserName=user)
        policyArn = iam_client.create_policy(
            PolicyName=policy_name, PolicyDocument=dumps(policy_document)
        )["Policy"]["Arn"]
        iam_client.attach_user_policy(UserName=user, PolicyArn=policyArn)

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.iam.iam_service import IAM

        with mock.patch(
            "providers.aws.services.iam.iam_policy_attached_only_to_group_or_roles.iam_policy_attached_only_to_group_or_roles.iam_client",
            new=IAM(current_audit_info),
        ):
            from providers.aws.services.iam.iam_policy_attached_only_to_group_or_roles.iam_policy_attached_only_to_group_or_roles import (
                iam_policy_attached_only_to_group_or_roles,
            )

            check = iam_policy_attached_only_to_group_or_roles()
            result = check.execute()
            assert result[0].status == "FAIL"

    @mock_iam
    def test_iam_user_attached_and_inline_policy(self):
        result = []
        iam_client = client("iam")
        user = "test_inline_policy"
        policyName = "policy1"
        policyDocument = {
            "Version": "2012-10-17",
            "Statement": [
                {"Effect": "Allow", "Action": "logs:CreateLogGroup", "Resource": "*"},
            ],
        }
        iam_client.create_user(UserName=user)
        iam_client.put_user_policy(
            UserName=user, PolicyName=policyName, PolicyDocument=dumps(policyDocument)
        )
        policyArn = iam_client.create_policy(
            PolicyName=policyName, PolicyDocument=dumps(policyDocument)
        )["Policy"]["Arn"]
        iam_client.attach_user_policy(UserName=user, PolicyArn=policyArn)

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.iam.iam_service import IAM

        with mock.patch(
            "providers.aws.services.iam.iam_policy_attached_only_to_group_or_roles.iam_policy_attached_only_to_group_or_roles.iam_client",
            new=IAM(current_audit_info),
        ):
            from providers.aws.services.iam.iam_policy_attached_only_to_group_or_roles.iam_policy_attached_only_to_group_or_roles import (
                iam_policy_attached_only_to_group_or_roles,
            )

            check = iam_policy_attached_only_to_group_or_roles()
            result = check.execute()
            assert len(result) == 2
            assert result[0].status == "FAIL"
            assert result[1].status == "FAIL"
            assert search(
                f"User {user} has attached the following policy",
                result[0].status_extended,
            )
            assert search(
                f"User {user} has the following inline policy",
                result[1].status_extended,
            )

    @mock_iam
    def test_iam_user_inline_policy(self):
        result = []
        iam_client = client("iam")
        user = "test_attached_inline_policy"
        policyName = "policy1"
        policyDocument = {
            "Version": "2012-10-17",
            "Statement": [
                {"Effect": "Allow", "Action": "logs:CreateLogGroup", "Resource": "*"},
            ],
        }
        iam_client.create_user(UserName=user)
        iam_client.put_user_policy(
            UserName=user, PolicyName=policyName, PolicyDocument=dumps(policyDocument)
        )

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.iam.iam_service import IAM

        with mock.patch(
            "providers.aws.services.iam.iam_policy_attached_only_to_group_or_roles.iam_policy_attached_only_to_group_or_roles.iam_client",
            new=IAM(current_audit_info),
        ):
            from providers.aws.services.iam.iam_policy_attached_only_to_group_or_roles.iam_policy_attached_only_to_group_or_roles import (
                iam_policy_attached_only_to_group_or_roles,
            )

            check = iam_policy_attached_only_to_group_or_roles()
            result = check.execute()
            assert result[0].status == "FAIL"

    @mock_iam
    def test_iam_user_no_policies(self):
        result = []
        iam_client = client("iam")
        user = "test_no_policies"
        iam_client.create_user(UserName=user)

        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.iam.iam_service import IAM

        with mock.patch(
            "providers.aws.services.iam.iam_policy_attached_only_to_group_or_roles.iam_policy_attached_only_to_group_or_roles.iam_client",
            new=IAM(current_audit_info),
        ):
            from providers.aws.services.iam.iam_policy_attached_only_to_group_or_roles.iam_policy_attached_only_to_group_or_roles import (
                iam_policy_attached_only_to_group_or_roles,
            )

            check = iam_policy_attached_only_to_group_or_roles()
            result = check.execute()
            assert result[0].status == "PASS"
