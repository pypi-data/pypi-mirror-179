from re import search
from unittest import mock

from boto3 import client
from moto import mock_rds

AWS_REGION = "us-east-1"


class Test_rds_instance_backup_enabled:
    @mock_rds
    def test_rds_no_instances(self):
        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.rds.rds_service import RDS

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "providers.aws.services.rds.rds_instance_backup_enabled.rds_instance_backup_enabled.rds_client",
            new=RDS(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.rds.rds_instance_backup_enabled.rds_instance_backup_enabled import (
                rds_instance_backup_enabled,
            )

            check = rds_instance_backup_enabled()
            result = check.execute()

            assert len(result) == 0

    @mock_rds
    def test_rds_instance_no_backup(self):
        conn = client("rds", region_name=AWS_REGION)
        conn.create_db_instance(
            DBInstanceIdentifier="db-master-1",
            AllocatedStorage=10,
            Engine="postgres",
            DBName="staging-postgres",
            DBInstanceClass="db.m1.small",
        )
        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.rds.rds_service import RDS

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "providers.aws.services.rds.rds_instance_backup_enabled.rds_instance_backup_enabled.rds_client",
            new=RDS(current_audit_info),
        ) as service_client:
            # Test Check
            from providers.aws.services.rds.rds_instance_backup_enabled.rds_instance_backup_enabled import (
                rds_instance_backup_enabled,
            )

            service_client.db_instances[0].backup_retention_period = 0

            check = rds_instance_backup_enabled()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert search(
                "has not backup enabled",
                result[0].status_extended,
            )
            assert result[0].resource_id == "db-master-1"

    @mock_rds
    def test_rds_instance_with_backup(self):
        conn = client("rds", region_name=AWS_REGION)
        conn.create_db_instance(
            DBInstanceIdentifier="db-master-1",
            AllocatedStorage=10,
            Engine="postgres",
            DBName="staging-postgres",
            DBInstanceClass="db.m1.small",
            BackupRetentionPeriod=10,
        )
        from providers.aws.lib.audit_info.audit_info import current_audit_info
        from providers.aws.services.rds.rds_service import RDS

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "providers.aws.services.rds.rds_instance_backup_enabled.rds_instance_backup_enabled.rds_client",
            new=RDS(current_audit_info),
        ):
            # Test Check
            from providers.aws.services.rds.rds_instance_backup_enabled.rds_instance_backup_enabled import (
                rds_instance_backup_enabled,
            )

            check = rds_instance_backup_enabled()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "PASS"
            assert search(
                "has backup enabled",
                result[0].status_extended,
            )
            assert result[0].resource_id == "db-master-1"
