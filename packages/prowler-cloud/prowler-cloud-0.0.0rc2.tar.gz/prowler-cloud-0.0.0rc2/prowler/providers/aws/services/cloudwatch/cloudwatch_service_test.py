from boto3 import session
from moto import mock_cloudwatch

from providers.aws.lib.audit_info.models import AWS_Audit_Info
from providers.aws.services.cloudwatch.cloudwatch_service import CloudWatch

AWS_ACCOUNT_NUMBER = 123456789012
AWS_REGION = "us-east-1"


class Test_CloudWatch_Service:
    # Mocked Audit Info
    def set_mocked_audit_info(self):
        audit_info = AWS_Audit_Info(
            original_session=None,
            audit_session=session.Session(
                profile_name=None,
                botocore_session=None,
            ),
            audited_account=AWS_ACCOUNT_NUMBER,
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

    # Test CloudWatch Service
    @mock_cloudwatch
    def test_service(self):
        # CloudWatch client for this test class
        audit_info = self.set_mocked_audit_info()
        cloudwatch = CloudWatch(audit_info)
        assert cloudwatch.service == "cloudwatch"

    # Test CloudWatch Client
    @mock_cloudwatch
    def test_client(self):
        # CloudWatch client for this test class
        audit_info = self.set_mocked_audit_info()
        cloudwatch = CloudWatch(audit_info)
        for client in cloudwatch.regional_clients.values():
            assert client.__class__.__name__ == "CloudWatch"

    # Test CloudWatch Session
    @mock_cloudwatch
    def test__get_session__(self):
        # CloudWatch client for this test class
        audit_info = self.set_mocked_audit_info()
        cloudwatch = CloudWatch(audit_info)
        assert cloudwatch.session.__class__.__name__ == "Session"

    # Test CloudWatch Session
    @mock_cloudwatch
    def test_audited_account(self):
        # CloudWatch client for this test class
        audit_info = self.set_mocked_audit_info()
        cloudwatch = CloudWatch(audit_info)
        assert cloudwatch.audited_account == AWS_ACCOUNT_NUMBER
