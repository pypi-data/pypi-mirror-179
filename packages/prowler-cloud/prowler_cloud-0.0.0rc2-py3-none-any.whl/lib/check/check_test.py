import os
from unittest import mock

from lib.check.check import (
    bulk_load_compliance_frameworks,
    exclude_checks_to_run,
    exclude_services_to_run,
    parse_checks_from_compliance_framework,
    parse_checks_from_file,
)
from lib.check.models import load_check_metadata


class Test_Check:
    def test_load_check_metadata(self):
        test_cases = [
            {
                "input": {
                    "metadata_path": f"{os.path.dirname(os.path.realpath(__file__))}/fixtures/metadata.json",
                },
                "expected": {
                    "CheckID": "iam_disable_30_days_credentials",
                    "CheckTitle": "Ensure credentials unused for 30 days or greater are disabled",
                    "ServiceName": "iam",
                    "Severity": "low",
                },
            }
        ]
        for test in test_cases:
            metadata_path = test["input"]["metadata_path"]
            check_metadata = load_check_metadata(metadata_path)
            assert check_metadata.CheckID == test["expected"]["CheckID"]
            assert check_metadata.CheckTitle == test["expected"]["CheckTitle"]
            assert check_metadata.ServiceName == test["expected"]["ServiceName"]
            assert check_metadata.Severity == test["expected"]["Severity"]

    def test_parse_checks_from_file(self):
        test_cases = [
            {
                "input": {
                    "path": f"{os.path.dirname(os.path.realpath(__file__))}/fixtures/checklistA.json",
                    "provider": "aws",
                },
                "expected": {"check11", "check12", "check7777"},
            }
        ]
        for test in test_cases:
            check_file = test["input"]["path"]
            provider = test["input"]["provider"]
            assert parse_checks_from_file(check_file, provider) == test["expected"]

    def test_exclude_checks_to_run(self):
        test_cases = [
            {
                "input": {
                    "check_list": {"check12", "check11", "extra72", "check13"},
                    "excluded_checks": {"check12", "check13"},
                },
                "expected": {"check11", "extra72"},
            },
            {
                "input": {
                    "check_list": {"check112", "check11", "extra72", "check13"},
                    "excluded_checks": {"check12", "check13", "check14"},
                },
                "expected": {"check112", "check11", "extra72"},
            },
        ]
        for test in test_cases:
            check_list = test["input"]["check_list"]
            excluded_checks = test["input"]["excluded_checks"]
            assert (
                exclude_checks_to_run(check_list, excluded_checks) == test["expected"]
            )

    def test_exclude_services_to_run(self):
        test_cases = [
            {
                "input": {
                    "checks_to_run": {
                        "iam_disable_30_days_credentials",
                        "iam_disable_90_days_credentials",
                    },
                    "excluded_services": {"ec2"},
                    "provider": "aws",
                },
                "expected": {
                    "iam_disable_30_days_credentials",
                    "iam_disable_90_days_credentials",
                },
            },
            {
                "input": {
                    "checks_to_run": {
                        "iam_disable_30_days_credentials",
                        "iam_disable_90_days_credentials",
                    },
                    "excluded_services": {"iam"},
                    "provider": "aws",
                },
                "expected": set(),
            },
        ]
        for test in test_cases:
            excluded_services = test["input"]["excluded_services"]
            checks_to_run = test["input"]["checks_to_run"]
            provider = test["input"]["provider"]
            assert (
                exclude_services_to_run(checks_to_run, excluded_services, provider)
                == test["expected"]
            )

    def test_parse_checks_from_compliance_framework_two(self):
        test_case = {
            "input": {"compliance_frameworks": ["cis_v1.4_aws", "ens_v3_aws"]},
            "expected": {
                "vpc_flow_logs_enabled",
                "ec2_ebs_snapshot_encryption",
                "iam_user_mfa_enabled_console_access",
                "cloudtrail_multi_region_enabled",
                "ec2_elbv2_insecure_ssl_ciphers",
                "guardduty_is_enabled",
                "s3_bucket_default_encryption",
                "cloudfront_distributions_https_enabled",
                "iam_avoid_root_usage",
                "s3_bucket_secure_transport_policy",
            },
        }
        with mock.patch(
            "lib.check.check.compliance_specification_dir",
            new=f"{os.path.dirname(os.path.realpath(__file__))}/fixtures",
        ):
            provider = "aws"
            bulk_compliance_frameworks = bulk_load_compliance_frameworks(provider)
            compliance_frameworks = test_case["input"]["compliance_frameworks"]
            assert (
                parse_checks_from_compliance_framework(
                    compliance_frameworks, bulk_compliance_frameworks
                )
                == test_case["expected"]
            )

    def test_parse_checks_from_compliance_framework_one(self):
        test_case = {
            "input": {"compliance_frameworks": ["cis_v1.4_aws"]},
            "expected": {
                "iam_user_mfa_enabled_console_access",
                "s3_bucket_default_encryption",
                "iam_avoid_root_usage",
            },
        }
        with mock.patch(
            "lib.check.check.compliance_specification_dir",
            new=f"{os.path.dirname(os.path.realpath(__file__))}/fixtures",
        ):
            provider = "aws"
            bulk_compliance_frameworks = bulk_load_compliance_frameworks(provider)
            compliance_frameworks = test_case["input"]["compliance_frameworks"]
            assert (
                parse_checks_from_compliance_framework(
                    compliance_frameworks, bulk_compliance_frameworks
                )
                == test_case["expected"]
            )

    def test_parse_checks_from_compliance_framework_no_compliance(self):
        test_case = {
            "input": {"compliance_frameworks": []},
            "expected": set(),
        }
        with mock.patch(
            "lib.check.check.compliance_specification_dir",
            new=f"{os.path.dirname(os.path.realpath(__file__))}/fixtures",
        ):
            provider = "aws"
            bulk_compliance_frameworks = bulk_load_compliance_frameworks(provider)
            compliance_frameworks = test_case["input"]["compliance_frameworks"]
            assert (
                parse_checks_from_compliance_framework(
                    compliance_frameworks, bulk_compliance_frameworks
                )
                == test_case["expected"]
            )
