from unittest import mock

from providers.aws.services.macie.macie_service import Session


class Test_macie_is_enabled:
    def test_macie_disabled(self):
        macie_client = mock.MagicMock
        macie_client.sessions = [
            Session(
                "DISABLED",
                "eu-west-1",
            )
        ]
        with mock.patch(
            "providers.aws.services.macie.macie_service.Macie",
            new=macie_client,
        ):
            # Test Check
            from providers.aws.services.macie.macie_is_enabled.macie_is_enabled import (
                macie_is_enabled,
            )

            check = macie_is_enabled()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert result[0].status_extended == "Macie is not enabled."
            assert result[0].resource_id == "Macie"

    def test_macie_enabled(self):
        macie_client = mock.MagicMock
        macie_client.sessions = [
            Session(
                "ENABLED",
                "eu-west-1",
            )
        ]
        with mock.patch(
            "providers.aws.services.macie.macie_service.Macie",
            new=macie_client,
        ):
            # Test Check
            from providers.aws.services.macie.macie_is_enabled.macie_is_enabled import (
                macie_is_enabled,
            )

            check = macie_is_enabled()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "PASS"
            assert result[0].status_extended == "Macie is enabled."
            assert result[0].resource_id == "Macie"

    def test_macie_suspended(self):
        macie_client = mock.MagicMock
        macie_client.sessions = [
            Session(
                "PAUSED",
                "eu-west-1",
            )
        ]
        with mock.patch(
            "providers.aws.services.macie.macie_service.Macie",
            new=macie_client,
        ):
            # Test Check
            from providers.aws.services.macie.macie_is_enabled.macie_is_enabled import (
                macie_is_enabled,
            )

            check = macie_is_enabled()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert (
                result[0].status_extended == "Macie is currently in a SUSPENDED state."
            )
            assert result[0].resource_id == "Macie"
