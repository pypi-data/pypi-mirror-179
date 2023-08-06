from re import search
from unittest import mock
from uuid import uuid4

from providers.aws.services.guardduty.guardduty_service import Detector

AWS_REGION = "eu-west-1"
AWS_ACCOUNT_NUMBER = "123456789012"

detector_id = str(uuid4())


class Test_guardduty_no_high_severity_findings:
    def test_no_detectors(self):
        guardduty_client = mock.MagicMock
        guardduty_client.detectors = []
        with mock.patch(
            "providers.aws.services.guardduty.guardduty_service.GuardDuty",
            guardduty_client,
        ):
            from providers.aws.services.guardduty.guardduty_no_high_severity_findings.guardduty_no_high_severity_findings import (
                guardduty_no_high_severity_findings,
            )

            check = guardduty_no_high_severity_findings()
            result = check.execute()
            assert len(result) == 0

    def test_no_high_findings(self):
        guardduty_client = mock.MagicMock
        guardduty_client.detectors = []
        guardduty_client.detectors.append(
            Detector(
                id=detector_id,
                region=AWS_REGION,
            )
        )
        with mock.patch(
            "providers.aws.services.guardduty.guardduty_service.GuardDuty",
            guardduty_client,
        ):
            from providers.aws.services.guardduty.guardduty_no_high_severity_findings.guardduty_no_high_severity_findings import (
                guardduty_no_high_severity_findings,
            )

            check = guardduty_no_high_severity_findings()
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "PASS"
            assert search(
                "does not have high severity findings.", result[0].status_extended
            )
            assert result[0].resource_id == detector_id
            assert result[0].resource_arn == ""

    def test_high_findings(self):
        guardduty_client = mock.MagicMock
        guardduty_client.detectors = []
        guardduty_client.detectors.append(
            Detector(
                id=detector_id, region=AWS_REGION, status=False, findings=[str(uuid4())]
            )
        )
        with mock.patch(
            "providers.aws.services.guardduty.guardduty_service.GuardDuty",
            guardduty_client,
        ):
            from providers.aws.services.guardduty.guardduty_no_high_severity_findings.guardduty_no_high_severity_findings import (
                guardduty_no_high_severity_findings,
            )

            check = guardduty_no_high_severity_findings()
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert search("has 1 high severity findings", result[0].status_extended)
            assert result[0].resource_id == detector_id
            assert result[0].resource_arn == ""
