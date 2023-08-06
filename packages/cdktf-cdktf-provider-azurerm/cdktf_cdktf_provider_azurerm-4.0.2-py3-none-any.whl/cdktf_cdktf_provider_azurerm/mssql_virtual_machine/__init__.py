'''
# `azurerm_mssql_virtual_machine`

Refer to the Terraform Registory for docs: [`azurerm_mssql_virtual_machine`](https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf
import constructs


class MssqlVirtualMachine(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlVirtualMachine.MssqlVirtualMachine",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine azurerm_mssql_virtual_machine}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        sql_license_type: builtins.str,
        virtual_machine_id: builtins.str,
        assessment: typing.Optional[typing.Union["MssqlVirtualMachineAssessment", typing.Dict[str, typing.Any]]] = None,
        auto_backup: typing.Optional[typing.Union["MssqlVirtualMachineAutoBackup", typing.Dict[str, typing.Any]]] = None,
        auto_patching: typing.Optional[typing.Union["MssqlVirtualMachineAutoPatching", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        key_vault_credential: typing.Optional[typing.Union["MssqlVirtualMachineKeyVaultCredential", typing.Dict[str, typing.Any]]] = None,
        r_services_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sql_connectivity_port: typing.Optional[jsii.Number] = None,
        sql_connectivity_type: typing.Optional[builtins.str] = None,
        sql_connectivity_update_password: typing.Optional[builtins.str] = None,
        sql_connectivity_update_username: typing.Optional[builtins.str] = None,
        sql_instance: typing.Optional[typing.Union["MssqlVirtualMachineSqlInstance", typing.Dict[str, typing.Any]]] = None,
        storage_configuration: typing.Optional[typing.Union["MssqlVirtualMachineStorageConfiguration", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["MssqlVirtualMachineTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine azurerm_mssql_virtual_machine} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param sql_license_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#sql_license_type MssqlVirtualMachine#sql_license_type}.
        :param virtual_machine_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#virtual_machine_id MssqlVirtualMachine#virtual_machine_id}.
        :param assessment: assessment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#assessment MssqlVirtualMachine#assessment}
        :param auto_backup: auto_backup block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#auto_backup MssqlVirtualMachine#auto_backup}
        :param auto_patching: auto_patching block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#auto_patching MssqlVirtualMachine#auto_patching}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#id MssqlVirtualMachine#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param key_vault_credential: key_vault_credential block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#key_vault_credential MssqlVirtualMachine#key_vault_credential}
        :param r_services_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#r_services_enabled MssqlVirtualMachine#r_services_enabled}.
        :param sql_connectivity_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#sql_connectivity_port MssqlVirtualMachine#sql_connectivity_port}.
        :param sql_connectivity_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#sql_connectivity_type MssqlVirtualMachine#sql_connectivity_type}.
        :param sql_connectivity_update_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#sql_connectivity_update_password MssqlVirtualMachine#sql_connectivity_update_password}.
        :param sql_connectivity_update_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#sql_connectivity_update_username MssqlVirtualMachine#sql_connectivity_update_username}.
        :param sql_instance: sql_instance block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#sql_instance MssqlVirtualMachine#sql_instance}
        :param storage_configuration: storage_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#storage_configuration MssqlVirtualMachine#storage_configuration}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#tags MssqlVirtualMachine#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#timeouts MssqlVirtualMachine#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id_: builtins.str,
                *,
                sql_license_type: builtins.str,
                virtual_machine_id: builtins.str,
                assessment: typing.Optional[typing.Union[MssqlVirtualMachineAssessment, typing.Dict[str, typing.Any]]] = None,
                auto_backup: typing.Optional[typing.Union[MssqlVirtualMachineAutoBackup, typing.Dict[str, typing.Any]]] = None,
                auto_patching: typing.Optional[typing.Union[MssqlVirtualMachineAutoPatching, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                key_vault_credential: typing.Optional[typing.Union[MssqlVirtualMachineKeyVaultCredential, typing.Dict[str, typing.Any]]] = None,
                r_services_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                sql_connectivity_port: typing.Optional[jsii.Number] = None,
                sql_connectivity_type: typing.Optional[builtins.str] = None,
                sql_connectivity_update_password: typing.Optional[builtins.str] = None,
                sql_connectivity_update_username: typing.Optional[builtins.str] = None,
                sql_instance: typing.Optional[typing.Union[MssqlVirtualMachineSqlInstance, typing.Dict[str, typing.Any]]] = None,
                storage_configuration: typing.Optional[typing.Union[MssqlVirtualMachineStorageConfiguration, typing.Dict[str, typing.Any]]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[MssqlVirtualMachineTimeouts, typing.Dict[str, typing.Any]]] = None,
                connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
                count: typing.Optional[jsii.Number] = None,
                depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
                for_each: typing.Optional[cdktf.ITerraformIterator] = None,
                lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
                provider: typing.Optional[cdktf.TerraformProvider] = None,
                provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MssqlVirtualMachineConfig(
            sql_license_type=sql_license_type,
            virtual_machine_id=virtual_machine_id,
            assessment=assessment,
            auto_backup=auto_backup,
            auto_patching=auto_patching,
            id=id,
            key_vault_credential=key_vault_credential,
            r_services_enabled=r_services_enabled,
            sql_connectivity_port=sql_connectivity_port,
            sql_connectivity_type=sql_connectivity_type,
            sql_connectivity_update_password=sql_connectivity_update_password,
            sql_connectivity_update_username=sql_connectivity_update_username,
            sql_instance=sql_instance,
            storage_configuration=storage_configuration,
            tags=tags,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAssessment")
    def put_assessment(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        run_immediately: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        schedule: typing.Optional[typing.Union["MssqlVirtualMachineAssessmentSchedule", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#enabled MssqlVirtualMachine#enabled}.
        :param run_immediately: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#run_immediately MssqlVirtualMachine#run_immediately}.
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#schedule MssqlVirtualMachine#schedule}
        '''
        value = MssqlVirtualMachineAssessment(
            enabled=enabled, run_immediately=run_immediately, schedule=schedule
        )

        return typing.cast(None, jsii.invoke(self, "putAssessment", [value]))

    @jsii.member(jsii_name="putAutoBackup")
    def put_auto_backup(
        self,
        *,
        retention_period_in_days: jsii.Number,
        storage_account_access_key: builtins.str,
        storage_blob_endpoint: builtins.str,
        encryption_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        encryption_password: typing.Optional[builtins.str] = None,
        manual_schedule: typing.Optional[typing.Union["MssqlVirtualMachineAutoBackupManualSchedule", typing.Dict[str, typing.Any]]] = None,
        system_databases_backup_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param retention_period_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#retention_period_in_days MssqlVirtualMachine#retention_period_in_days}.
        :param storage_account_access_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#storage_account_access_key MssqlVirtualMachine#storage_account_access_key}.
        :param storage_blob_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#storage_blob_endpoint MssqlVirtualMachine#storage_blob_endpoint}.
        :param encryption_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#encryption_enabled MssqlVirtualMachine#encryption_enabled}.
        :param encryption_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#encryption_password MssqlVirtualMachine#encryption_password}.
        :param manual_schedule: manual_schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#manual_schedule MssqlVirtualMachine#manual_schedule}
        :param system_databases_backup_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#system_databases_backup_enabled MssqlVirtualMachine#system_databases_backup_enabled}.
        '''
        value = MssqlVirtualMachineAutoBackup(
            retention_period_in_days=retention_period_in_days,
            storage_account_access_key=storage_account_access_key,
            storage_blob_endpoint=storage_blob_endpoint,
            encryption_enabled=encryption_enabled,
            encryption_password=encryption_password,
            manual_schedule=manual_schedule,
            system_databases_backup_enabled=system_databases_backup_enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putAutoBackup", [value]))

    @jsii.member(jsii_name="putAutoPatching")
    def put_auto_patching(
        self,
        *,
        day_of_week: builtins.str,
        maintenance_window_duration_in_minutes: jsii.Number,
        maintenance_window_starting_hour: jsii.Number,
    ) -> None:
        '''
        :param day_of_week: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#day_of_week MssqlVirtualMachine#day_of_week}.
        :param maintenance_window_duration_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#maintenance_window_duration_in_minutes MssqlVirtualMachine#maintenance_window_duration_in_minutes}.
        :param maintenance_window_starting_hour: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#maintenance_window_starting_hour MssqlVirtualMachine#maintenance_window_starting_hour}.
        '''
        value = MssqlVirtualMachineAutoPatching(
            day_of_week=day_of_week,
            maintenance_window_duration_in_minutes=maintenance_window_duration_in_minutes,
            maintenance_window_starting_hour=maintenance_window_starting_hour,
        )

        return typing.cast(None, jsii.invoke(self, "putAutoPatching", [value]))

    @jsii.member(jsii_name="putKeyVaultCredential")
    def put_key_vault_credential(
        self,
        *,
        key_vault_url: builtins.str,
        name: builtins.str,
        service_principal_name: builtins.str,
        service_principal_secret: builtins.str,
    ) -> None:
        '''
        :param key_vault_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#key_vault_url MssqlVirtualMachine#key_vault_url}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#name MssqlVirtualMachine#name}.
        :param service_principal_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#service_principal_name MssqlVirtualMachine#service_principal_name}.
        :param service_principal_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#service_principal_secret MssqlVirtualMachine#service_principal_secret}.
        '''
        value = MssqlVirtualMachineKeyVaultCredential(
            key_vault_url=key_vault_url,
            name=name,
            service_principal_name=service_principal_name,
            service_principal_secret=service_principal_secret,
        )

        return typing.cast(None, jsii.invoke(self, "putKeyVaultCredential", [value]))

    @jsii.member(jsii_name="putSqlInstance")
    def put_sql_instance(
        self,
        *,
        adhoc_workloads_optimization_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        collation: typing.Optional[builtins.str] = None,
        instant_file_initialization_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        lock_pages_in_memory_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_dop: typing.Optional[jsii.Number] = None,
        max_server_memory_mb: typing.Optional[jsii.Number] = None,
        min_server_memory_mb: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param adhoc_workloads_optimization_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#adhoc_workloads_optimization_enabled MssqlVirtualMachine#adhoc_workloads_optimization_enabled}.
        :param collation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#collation MssqlVirtualMachine#collation}.
        :param instant_file_initialization_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#instant_file_initialization_enabled MssqlVirtualMachine#instant_file_initialization_enabled}.
        :param lock_pages_in_memory_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#lock_pages_in_memory_enabled MssqlVirtualMachine#lock_pages_in_memory_enabled}.
        :param max_dop: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#max_dop MssqlVirtualMachine#max_dop}.
        :param max_server_memory_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#max_server_memory_mb MssqlVirtualMachine#max_server_memory_mb}.
        :param min_server_memory_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#min_server_memory_mb MssqlVirtualMachine#min_server_memory_mb}.
        '''
        value = MssqlVirtualMachineSqlInstance(
            adhoc_workloads_optimization_enabled=adhoc_workloads_optimization_enabled,
            collation=collation,
            instant_file_initialization_enabled=instant_file_initialization_enabled,
            lock_pages_in_memory_enabled=lock_pages_in_memory_enabled,
            max_dop=max_dop,
            max_server_memory_mb=max_server_memory_mb,
            min_server_memory_mb=min_server_memory_mb,
        )

        return typing.cast(None, jsii.invoke(self, "putSqlInstance", [value]))

    @jsii.member(jsii_name="putStorageConfiguration")
    def put_storage_configuration(
        self,
        *,
        disk_type: builtins.str,
        storage_workload_type: builtins.str,
        data_settings: typing.Optional[typing.Union["MssqlVirtualMachineStorageConfigurationDataSettings", typing.Dict[str, typing.Any]]] = None,
        log_settings: typing.Optional[typing.Union["MssqlVirtualMachineStorageConfigurationLogSettings", typing.Dict[str, typing.Any]]] = None,
        system_db_on_data_disk_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        temp_db_settings: typing.Optional[typing.Union["MssqlVirtualMachineStorageConfigurationTempDbSettings", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param disk_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#disk_type MssqlVirtualMachine#disk_type}.
        :param storage_workload_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#storage_workload_type MssqlVirtualMachine#storage_workload_type}.
        :param data_settings: data_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#data_settings MssqlVirtualMachine#data_settings}
        :param log_settings: log_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#log_settings MssqlVirtualMachine#log_settings}
        :param system_db_on_data_disk_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#system_db_on_data_disk_enabled MssqlVirtualMachine#system_db_on_data_disk_enabled}.
        :param temp_db_settings: temp_db_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#temp_db_settings MssqlVirtualMachine#temp_db_settings}
        '''
        value = MssqlVirtualMachineStorageConfiguration(
            disk_type=disk_type,
            storage_workload_type=storage_workload_type,
            data_settings=data_settings,
            log_settings=log_settings,
            system_db_on_data_disk_enabled=system_db_on_data_disk_enabled,
            temp_db_settings=temp_db_settings,
        )

        return typing.cast(None, jsii.invoke(self, "putStorageConfiguration", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#create MssqlVirtualMachine#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#delete MssqlVirtualMachine#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#read MssqlVirtualMachine#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#update MssqlVirtualMachine#update}.
        '''
        value = MssqlVirtualMachineTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAssessment")
    def reset_assessment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssessment", []))

    @jsii.member(jsii_name="resetAutoBackup")
    def reset_auto_backup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoBackup", []))

    @jsii.member(jsii_name="resetAutoPatching")
    def reset_auto_patching(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoPatching", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKeyVaultCredential")
    def reset_key_vault_credential(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyVaultCredential", []))

    @jsii.member(jsii_name="resetRServicesEnabled")
    def reset_r_services_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRServicesEnabled", []))

    @jsii.member(jsii_name="resetSqlConnectivityPort")
    def reset_sql_connectivity_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqlConnectivityPort", []))

    @jsii.member(jsii_name="resetSqlConnectivityType")
    def reset_sql_connectivity_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqlConnectivityType", []))

    @jsii.member(jsii_name="resetSqlConnectivityUpdatePassword")
    def reset_sql_connectivity_update_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqlConnectivityUpdatePassword", []))

    @jsii.member(jsii_name="resetSqlConnectivityUpdateUsername")
    def reset_sql_connectivity_update_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqlConnectivityUpdateUsername", []))

    @jsii.member(jsii_name="resetSqlInstance")
    def reset_sql_instance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqlInstance", []))

    @jsii.member(jsii_name="resetStorageConfiguration")
    def reset_storage_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageConfiguration", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="assessment")
    def assessment(self) -> "MssqlVirtualMachineAssessmentOutputReference":
        return typing.cast("MssqlVirtualMachineAssessmentOutputReference", jsii.get(self, "assessment"))

    @builtins.property
    @jsii.member(jsii_name="autoBackup")
    def auto_backup(self) -> "MssqlVirtualMachineAutoBackupOutputReference":
        return typing.cast("MssqlVirtualMachineAutoBackupOutputReference", jsii.get(self, "autoBackup"))

    @builtins.property
    @jsii.member(jsii_name="autoPatching")
    def auto_patching(self) -> "MssqlVirtualMachineAutoPatchingOutputReference":
        return typing.cast("MssqlVirtualMachineAutoPatchingOutputReference", jsii.get(self, "autoPatching"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultCredential")
    def key_vault_credential(
        self,
    ) -> "MssqlVirtualMachineKeyVaultCredentialOutputReference":
        return typing.cast("MssqlVirtualMachineKeyVaultCredentialOutputReference", jsii.get(self, "keyVaultCredential"))

    @builtins.property
    @jsii.member(jsii_name="sqlInstance")
    def sql_instance(self) -> "MssqlVirtualMachineSqlInstanceOutputReference":
        return typing.cast("MssqlVirtualMachineSqlInstanceOutputReference", jsii.get(self, "sqlInstance"))

    @builtins.property
    @jsii.member(jsii_name="storageConfiguration")
    def storage_configuration(
        self,
    ) -> "MssqlVirtualMachineStorageConfigurationOutputReference":
        return typing.cast("MssqlVirtualMachineStorageConfigurationOutputReference", jsii.get(self, "storageConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MssqlVirtualMachineTimeoutsOutputReference":
        return typing.cast("MssqlVirtualMachineTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="assessmentInput")
    def assessment_input(self) -> typing.Optional["MssqlVirtualMachineAssessment"]:
        return typing.cast(typing.Optional["MssqlVirtualMachineAssessment"], jsii.get(self, "assessmentInput"))

    @builtins.property
    @jsii.member(jsii_name="autoBackupInput")
    def auto_backup_input(self) -> typing.Optional["MssqlVirtualMachineAutoBackup"]:
        return typing.cast(typing.Optional["MssqlVirtualMachineAutoBackup"], jsii.get(self, "autoBackupInput"))

    @builtins.property
    @jsii.member(jsii_name="autoPatchingInput")
    def auto_patching_input(self) -> typing.Optional["MssqlVirtualMachineAutoPatching"]:
        return typing.cast(typing.Optional["MssqlVirtualMachineAutoPatching"], jsii.get(self, "autoPatchingInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultCredentialInput")
    def key_vault_credential_input(
        self,
    ) -> typing.Optional["MssqlVirtualMachineKeyVaultCredential"]:
        return typing.cast(typing.Optional["MssqlVirtualMachineKeyVaultCredential"], jsii.get(self, "keyVaultCredentialInput"))

    @builtins.property
    @jsii.member(jsii_name="rServicesEnabledInput")
    def r_services_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "rServicesEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlConnectivityPortInput")
    def sql_connectivity_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sqlConnectivityPortInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlConnectivityTypeInput")
    def sql_connectivity_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sqlConnectivityTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlConnectivityUpdatePasswordInput")
    def sql_connectivity_update_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sqlConnectivityUpdatePasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlConnectivityUpdateUsernameInput")
    def sql_connectivity_update_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sqlConnectivityUpdateUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlInstanceInput")
    def sql_instance_input(self) -> typing.Optional["MssqlVirtualMachineSqlInstance"]:
        return typing.cast(typing.Optional["MssqlVirtualMachineSqlInstance"], jsii.get(self, "sqlInstanceInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlLicenseTypeInput")
    def sql_license_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sqlLicenseTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="storageConfigurationInput")
    def storage_configuration_input(
        self,
    ) -> typing.Optional["MssqlVirtualMachineStorageConfiguration"]:
        return typing.cast(typing.Optional["MssqlVirtualMachineStorageConfiguration"], jsii.get(self, "storageConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MssqlVirtualMachineTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MssqlVirtualMachineTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualMachineIdInput")
    def virtual_machine_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualMachineIdInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="rServicesEnabled")
    def r_services_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "rServicesEnabled"))

    @r_services_enabled.setter
    def r_services_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rServicesEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="sqlConnectivityPort")
    def sql_connectivity_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sqlConnectivityPort"))

    @sql_connectivity_port.setter
    def sql_connectivity_port(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sqlConnectivityPort", value)

    @builtins.property
    @jsii.member(jsii_name="sqlConnectivityType")
    def sql_connectivity_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sqlConnectivityType"))

    @sql_connectivity_type.setter
    def sql_connectivity_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sqlConnectivityType", value)

    @builtins.property
    @jsii.member(jsii_name="sqlConnectivityUpdatePassword")
    def sql_connectivity_update_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sqlConnectivityUpdatePassword"))

    @sql_connectivity_update_password.setter
    def sql_connectivity_update_password(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sqlConnectivityUpdatePassword", value)

    @builtins.property
    @jsii.member(jsii_name="sqlConnectivityUpdateUsername")
    def sql_connectivity_update_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sqlConnectivityUpdateUsername"))

    @sql_connectivity_update_username.setter
    def sql_connectivity_update_username(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sqlConnectivityUpdateUsername", value)

    @builtins.property
    @jsii.member(jsii_name="sqlLicenseType")
    def sql_license_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sqlLicenseType"))

    @sql_license_type.setter
    def sql_license_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sqlLicenseType", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="virtualMachineId")
    def virtual_machine_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualMachineId"))

    @virtual_machine_id.setter
    def virtual_machine_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualMachineId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlVirtualMachine.MssqlVirtualMachineAssessment",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "run_immediately": "runImmediately",
        "schedule": "schedule",
    },
)
class MssqlVirtualMachineAssessment:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        run_immediately: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        schedule: typing.Optional[typing.Union["MssqlVirtualMachineAssessmentSchedule", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#enabled MssqlVirtualMachine#enabled}.
        :param run_immediately: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#run_immediately MssqlVirtualMachine#run_immediately}.
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#schedule MssqlVirtualMachine#schedule}
        '''
        if isinstance(schedule, dict):
            schedule = MssqlVirtualMachineAssessmentSchedule(**schedule)
        if __debug__:
            def stub(
                *,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                run_immediately: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                schedule: typing.Optional[typing.Union[MssqlVirtualMachineAssessmentSchedule, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument run_immediately", value=run_immediately, expected_type=type_hints["run_immediately"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if run_immediately is not None:
            self._values["run_immediately"] = run_immediately
        if schedule is not None:
            self._values["schedule"] = schedule

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#enabled MssqlVirtualMachine#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def run_immediately(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#run_immediately MssqlVirtualMachine#run_immediately}.'''
        result = self._values.get("run_immediately")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def schedule(self) -> typing.Optional["MssqlVirtualMachineAssessmentSchedule"]:
        '''schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#schedule MssqlVirtualMachine#schedule}
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional["MssqlVirtualMachineAssessmentSchedule"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlVirtualMachineAssessment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MssqlVirtualMachineAssessmentOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlVirtualMachine.MssqlVirtualMachineAssessmentOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSchedule")
    def put_schedule(
        self,
        *,
        day_of_week: builtins.str,
        start_time: builtins.str,
        monthly_occurrence: typing.Optional[jsii.Number] = None,
        weekly_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param day_of_week: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#day_of_week MssqlVirtualMachine#day_of_week}.
        :param start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#start_time MssqlVirtualMachine#start_time}.
        :param monthly_occurrence: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#monthly_occurrence MssqlVirtualMachine#monthly_occurrence}.
        :param weekly_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#weekly_interval MssqlVirtualMachine#weekly_interval}.
        '''
        value = MssqlVirtualMachineAssessmentSchedule(
            day_of_week=day_of_week,
            start_time=start_time,
            monthly_occurrence=monthly_occurrence,
            weekly_interval=weekly_interval,
        )

        return typing.cast(None, jsii.invoke(self, "putSchedule", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetRunImmediately")
    def reset_run_immediately(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunImmediately", []))

    @jsii.member(jsii_name="resetSchedule")
    def reset_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedule", []))

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> "MssqlVirtualMachineAssessmentScheduleOutputReference":
        return typing.cast("MssqlVirtualMachineAssessmentScheduleOutputReference", jsii.get(self, "schedule"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="runImmediatelyInput")
    def run_immediately_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "runImmediatelyInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(
        self,
    ) -> typing.Optional["MssqlVirtualMachineAssessmentSchedule"]:
        return typing.cast(typing.Optional["MssqlVirtualMachineAssessmentSchedule"], jsii.get(self, "scheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="runImmediately")
    def run_immediately(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "runImmediately"))

    @run_immediately.setter
    def run_immediately(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runImmediately", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MssqlVirtualMachineAssessment]:
        return typing.cast(typing.Optional[MssqlVirtualMachineAssessment], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MssqlVirtualMachineAssessment],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[MssqlVirtualMachineAssessment]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlVirtualMachine.MssqlVirtualMachineAssessmentSchedule",
    jsii_struct_bases=[],
    name_mapping={
        "day_of_week": "dayOfWeek",
        "start_time": "startTime",
        "monthly_occurrence": "monthlyOccurrence",
        "weekly_interval": "weeklyInterval",
    },
)
class MssqlVirtualMachineAssessmentSchedule:
    def __init__(
        self,
        *,
        day_of_week: builtins.str,
        start_time: builtins.str,
        monthly_occurrence: typing.Optional[jsii.Number] = None,
        weekly_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param day_of_week: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#day_of_week MssqlVirtualMachine#day_of_week}.
        :param start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#start_time MssqlVirtualMachine#start_time}.
        :param monthly_occurrence: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#monthly_occurrence MssqlVirtualMachine#monthly_occurrence}.
        :param weekly_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#weekly_interval MssqlVirtualMachine#weekly_interval}.
        '''
        if __debug__:
            def stub(
                *,
                day_of_week: builtins.str,
                start_time: builtins.str,
                monthly_occurrence: typing.Optional[jsii.Number] = None,
                weekly_interval: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument day_of_week", value=day_of_week, expected_type=type_hints["day_of_week"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            check_type(argname="argument monthly_occurrence", value=monthly_occurrence, expected_type=type_hints["monthly_occurrence"])
            check_type(argname="argument weekly_interval", value=weekly_interval, expected_type=type_hints["weekly_interval"])
        self._values: typing.Dict[str, typing.Any] = {
            "day_of_week": day_of_week,
            "start_time": start_time,
        }
        if monthly_occurrence is not None:
            self._values["monthly_occurrence"] = monthly_occurrence
        if weekly_interval is not None:
            self._values["weekly_interval"] = weekly_interval

    @builtins.property
    def day_of_week(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#day_of_week MssqlVirtualMachine#day_of_week}.'''
        result = self._values.get("day_of_week")
        assert result is not None, "Required property 'day_of_week' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def start_time(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#start_time MssqlVirtualMachine#start_time}.'''
        result = self._values.get("start_time")
        assert result is not None, "Required property 'start_time' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def monthly_occurrence(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#monthly_occurrence MssqlVirtualMachine#monthly_occurrence}.'''
        result = self._values.get("monthly_occurrence")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def weekly_interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#weekly_interval MssqlVirtualMachine#weekly_interval}.'''
        result = self._values.get("weekly_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlVirtualMachineAssessmentSchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MssqlVirtualMachineAssessmentScheduleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlVirtualMachine.MssqlVirtualMachineAssessmentScheduleOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMonthlyOccurrence")
    def reset_monthly_occurrence(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonthlyOccurrence", []))

    @jsii.member(jsii_name="resetWeeklyInterval")
    def reset_weekly_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeeklyInterval", []))

    @builtins.property
    @jsii.member(jsii_name="dayOfWeekInput")
    def day_of_week_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dayOfWeekInput"))

    @builtins.property
    @jsii.member(jsii_name="monthlyOccurrenceInput")
    def monthly_occurrence_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "monthlyOccurrenceInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimeInput")
    def start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="weeklyIntervalInput")
    def weekly_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weeklyIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="dayOfWeek")
    def day_of_week(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dayOfWeek"))

    @day_of_week.setter
    def day_of_week(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dayOfWeek", value)

    @builtins.property
    @jsii.member(jsii_name="monthlyOccurrence")
    def monthly_occurrence(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "monthlyOccurrence"))

    @monthly_occurrence.setter
    def monthly_occurrence(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monthlyOccurrence", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="weeklyInterval")
    def weekly_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weeklyInterval"))

    @weekly_interval.setter
    def weekly_interval(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weeklyInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MssqlVirtualMachineAssessmentSchedule]:
        return typing.cast(typing.Optional[MssqlVirtualMachineAssessmentSchedule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MssqlVirtualMachineAssessmentSchedule],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MssqlVirtualMachineAssessmentSchedule],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlVirtualMachine.MssqlVirtualMachineAutoBackup",
    jsii_struct_bases=[],
    name_mapping={
        "retention_period_in_days": "retentionPeriodInDays",
        "storage_account_access_key": "storageAccountAccessKey",
        "storage_blob_endpoint": "storageBlobEndpoint",
        "encryption_enabled": "encryptionEnabled",
        "encryption_password": "encryptionPassword",
        "manual_schedule": "manualSchedule",
        "system_databases_backup_enabled": "systemDatabasesBackupEnabled",
    },
)
class MssqlVirtualMachineAutoBackup:
    def __init__(
        self,
        *,
        retention_period_in_days: jsii.Number,
        storage_account_access_key: builtins.str,
        storage_blob_endpoint: builtins.str,
        encryption_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        encryption_password: typing.Optional[builtins.str] = None,
        manual_schedule: typing.Optional[typing.Union["MssqlVirtualMachineAutoBackupManualSchedule", typing.Dict[str, typing.Any]]] = None,
        system_databases_backup_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param retention_period_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#retention_period_in_days MssqlVirtualMachine#retention_period_in_days}.
        :param storage_account_access_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#storage_account_access_key MssqlVirtualMachine#storage_account_access_key}.
        :param storage_blob_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#storage_blob_endpoint MssqlVirtualMachine#storage_blob_endpoint}.
        :param encryption_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#encryption_enabled MssqlVirtualMachine#encryption_enabled}.
        :param encryption_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#encryption_password MssqlVirtualMachine#encryption_password}.
        :param manual_schedule: manual_schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#manual_schedule MssqlVirtualMachine#manual_schedule}
        :param system_databases_backup_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#system_databases_backup_enabled MssqlVirtualMachine#system_databases_backup_enabled}.
        '''
        if isinstance(manual_schedule, dict):
            manual_schedule = MssqlVirtualMachineAutoBackupManualSchedule(**manual_schedule)
        if __debug__:
            def stub(
                *,
                retention_period_in_days: jsii.Number,
                storage_account_access_key: builtins.str,
                storage_blob_endpoint: builtins.str,
                encryption_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                encryption_password: typing.Optional[builtins.str] = None,
                manual_schedule: typing.Optional[typing.Union[MssqlVirtualMachineAutoBackupManualSchedule, typing.Dict[str, typing.Any]]] = None,
                system_databases_backup_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument retention_period_in_days", value=retention_period_in_days, expected_type=type_hints["retention_period_in_days"])
            check_type(argname="argument storage_account_access_key", value=storage_account_access_key, expected_type=type_hints["storage_account_access_key"])
            check_type(argname="argument storage_blob_endpoint", value=storage_blob_endpoint, expected_type=type_hints["storage_blob_endpoint"])
            check_type(argname="argument encryption_enabled", value=encryption_enabled, expected_type=type_hints["encryption_enabled"])
            check_type(argname="argument encryption_password", value=encryption_password, expected_type=type_hints["encryption_password"])
            check_type(argname="argument manual_schedule", value=manual_schedule, expected_type=type_hints["manual_schedule"])
            check_type(argname="argument system_databases_backup_enabled", value=system_databases_backup_enabled, expected_type=type_hints["system_databases_backup_enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "retention_period_in_days": retention_period_in_days,
            "storage_account_access_key": storage_account_access_key,
            "storage_blob_endpoint": storage_blob_endpoint,
        }
        if encryption_enabled is not None:
            self._values["encryption_enabled"] = encryption_enabled
        if encryption_password is not None:
            self._values["encryption_password"] = encryption_password
        if manual_schedule is not None:
            self._values["manual_schedule"] = manual_schedule
        if system_databases_backup_enabled is not None:
            self._values["system_databases_backup_enabled"] = system_databases_backup_enabled

    @builtins.property
    def retention_period_in_days(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#retention_period_in_days MssqlVirtualMachine#retention_period_in_days}.'''
        result = self._values.get("retention_period_in_days")
        assert result is not None, "Required property 'retention_period_in_days' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def storage_account_access_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#storage_account_access_key MssqlVirtualMachine#storage_account_access_key}.'''
        result = self._values.get("storage_account_access_key")
        assert result is not None, "Required property 'storage_account_access_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_blob_endpoint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#storage_blob_endpoint MssqlVirtualMachine#storage_blob_endpoint}.'''
        result = self._values.get("storage_blob_endpoint")
        assert result is not None, "Required property 'storage_blob_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#encryption_enabled MssqlVirtualMachine#encryption_enabled}.'''
        result = self._values.get("encryption_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def encryption_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#encryption_password MssqlVirtualMachine#encryption_password}.'''
        result = self._values.get("encryption_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def manual_schedule(
        self,
    ) -> typing.Optional["MssqlVirtualMachineAutoBackupManualSchedule"]:
        '''manual_schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#manual_schedule MssqlVirtualMachine#manual_schedule}
        '''
        result = self._values.get("manual_schedule")
        return typing.cast(typing.Optional["MssqlVirtualMachineAutoBackupManualSchedule"], result)

    @builtins.property
    def system_databases_backup_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#system_databases_backup_enabled MssqlVirtualMachine#system_databases_backup_enabled}.'''
        result = self._values.get("system_databases_backup_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlVirtualMachineAutoBackup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlVirtualMachine.MssqlVirtualMachineAutoBackupManualSchedule",
    jsii_struct_bases=[],
    name_mapping={
        "full_backup_frequency": "fullBackupFrequency",
        "full_backup_start_hour": "fullBackupStartHour",
        "full_backup_window_in_hours": "fullBackupWindowInHours",
        "log_backup_frequency_in_minutes": "logBackupFrequencyInMinutes",
    },
)
class MssqlVirtualMachineAutoBackupManualSchedule:
    def __init__(
        self,
        *,
        full_backup_frequency: builtins.str,
        full_backup_start_hour: jsii.Number,
        full_backup_window_in_hours: jsii.Number,
        log_backup_frequency_in_minutes: jsii.Number,
    ) -> None:
        '''
        :param full_backup_frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#full_backup_frequency MssqlVirtualMachine#full_backup_frequency}.
        :param full_backup_start_hour: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#full_backup_start_hour MssqlVirtualMachine#full_backup_start_hour}.
        :param full_backup_window_in_hours: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#full_backup_window_in_hours MssqlVirtualMachine#full_backup_window_in_hours}.
        :param log_backup_frequency_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#log_backup_frequency_in_minutes MssqlVirtualMachine#log_backup_frequency_in_minutes}.
        '''
        if __debug__:
            def stub(
                *,
                full_backup_frequency: builtins.str,
                full_backup_start_hour: jsii.Number,
                full_backup_window_in_hours: jsii.Number,
                log_backup_frequency_in_minutes: jsii.Number,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument full_backup_frequency", value=full_backup_frequency, expected_type=type_hints["full_backup_frequency"])
            check_type(argname="argument full_backup_start_hour", value=full_backup_start_hour, expected_type=type_hints["full_backup_start_hour"])
            check_type(argname="argument full_backup_window_in_hours", value=full_backup_window_in_hours, expected_type=type_hints["full_backup_window_in_hours"])
            check_type(argname="argument log_backup_frequency_in_minutes", value=log_backup_frequency_in_minutes, expected_type=type_hints["log_backup_frequency_in_minutes"])
        self._values: typing.Dict[str, typing.Any] = {
            "full_backup_frequency": full_backup_frequency,
            "full_backup_start_hour": full_backup_start_hour,
            "full_backup_window_in_hours": full_backup_window_in_hours,
            "log_backup_frequency_in_minutes": log_backup_frequency_in_minutes,
        }

    @builtins.property
    def full_backup_frequency(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#full_backup_frequency MssqlVirtualMachine#full_backup_frequency}.'''
        result = self._values.get("full_backup_frequency")
        assert result is not None, "Required property 'full_backup_frequency' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def full_backup_start_hour(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#full_backup_start_hour MssqlVirtualMachine#full_backup_start_hour}.'''
        result = self._values.get("full_backup_start_hour")
        assert result is not None, "Required property 'full_backup_start_hour' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def full_backup_window_in_hours(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#full_backup_window_in_hours MssqlVirtualMachine#full_backup_window_in_hours}.'''
        result = self._values.get("full_backup_window_in_hours")
        assert result is not None, "Required property 'full_backup_window_in_hours' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def log_backup_frequency_in_minutes(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#log_backup_frequency_in_minutes MssqlVirtualMachine#log_backup_frequency_in_minutes}.'''
        result = self._values.get("log_backup_frequency_in_minutes")
        assert result is not None, "Required property 'log_backup_frequency_in_minutes' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlVirtualMachineAutoBackupManualSchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MssqlVirtualMachineAutoBackupManualScheduleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlVirtualMachine.MssqlVirtualMachineAutoBackupManualScheduleOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="fullBackupFrequencyInput")
    def full_backup_frequency_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fullBackupFrequencyInput"))

    @builtins.property
    @jsii.member(jsii_name="fullBackupStartHourInput")
    def full_backup_start_hour_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fullBackupStartHourInput"))

    @builtins.property
    @jsii.member(jsii_name="fullBackupWindowInHoursInput")
    def full_backup_window_in_hours_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fullBackupWindowInHoursInput"))

    @builtins.property
    @jsii.member(jsii_name="logBackupFrequencyInMinutesInput")
    def log_backup_frequency_in_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "logBackupFrequencyInMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="fullBackupFrequency")
    def full_backup_frequency(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fullBackupFrequency"))

    @full_backup_frequency.setter
    def full_backup_frequency(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fullBackupFrequency", value)

    @builtins.property
    @jsii.member(jsii_name="fullBackupStartHour")
    def full_backup_start_hour(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fullBackupStartHour"))

    @full_backup_start_hour.setter
    def full_backup_start_hour(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fullBackupStartHour", value)

    @builtins.property
    @jsii.member(jsii_name="fullBackupWindowInHours")
    def full_backup_window_in_hours(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fullBackupWindowInHours"))

    @full_backup_window_in_hours.setter
    def full_backup_window_in_hours(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fullBackupWindowInHours", value)

    @builtins.property
    @jsii.member(jsii_name="logBackupFrequencyInMinutes")
    def log_backup_frequency_in_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "logBackupFrequencyInMinutes"))

    @log_backup_frequency_in_minutes.setter
    def log_backup_frequency_in_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logBackupFrequencyInMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MssqlVirtualMachineAutoBackupManualSchedule]:
        return typing.cast(typing.Optional[MssqlVirtualMachineAutoBackupManualSchedule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MssqlVirtualMachineAutoBackupManualSchedule],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MssqlVirtualMachineAutoBackupManualSchedule],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MssqlVirtualMachineAutoBackupOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlVirtualMachine.MssqlVirtualMachineAutoBackupOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putManualSchedule")
    def put_manual_schedule(
        self,
        *,
        full_backup_frequency: builtins.str,
        full_backup_start_hour: jsii.Number,
        full_backup_window_in_hours: jsii.Number,
        log_backup_frequency_in_minutes: jsii.Number,
    ) -> None:
        '''
        :param full_backup_frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#full_backup_frequency MssqlVirtualMachine#full_backup_frequency}.
        :param full_backup_start_hour: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#full_backup_start_hour MssqlVirtualMachine#full_backup_start_hour}.
        :param full_backup_window_in_hours: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#full_backup_window_in_hours MssqlVirtualMachine#full_backup_window_in_hours}.
        :param log_backup_frequency_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#log_backup_frequency_in_minutes MssqlVirtualMachine#log_backup_frequency_in_minutes}.
        '''
        value = MssqlVirtualMachineAutoBackupManualSchedule(
            full_backup_frequency=full_backup_frequency,
            full_backup_start_hour=full_backup_start_hour,
            full_backup_window_in_hours=full_backup_window_in_hours,
            log_backup_frequency_in_minutes=log_backup_frequency_in_minutes,
        )

        return typing.cast(None, jsii.invoke(self, "putManualSchedule", [value]))

    @jsii.member(jsii_name="resetEncryptionEnabled")
    def reset_encryption_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionEnabled", []))

    @jsii.member(jsii_name="resetEncryptionPassword")
    def reset_encryption_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionPassword", []))

    @jsii.member(jsii_name="resetManualSchedule")
    def reset_manual_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManualSchedule", []))

    @jsii.member(jsii_name="resetSystemDatabasesBackupEnabled")
    def reset_system_databases_backup_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSystemDatabasesBackupEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="manualSchedule")
    def manual_schedule(
        self,
    ) -> MssqlVirtualMachineAutoBackupManualScheduleOutputReference:
        return typing.cast(MssqlVirtualMachineAutoBackupManualScheduleOutputReference, jsii.get(self, "manualSchedule"))

    @builtins.property
    @jsii.member(jsii_name="encryptionEnabledInput")
    def encryption_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "encryptionEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionPasswordInput")
    def encryption_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="manualScheduleInput")
    def manual_schedule_input(
        self,
    ) -> typing.Optional[MssqlVirtualMachineAutoBackupManualSchedule]:
        return typing.cast(typing.Optional[MssqlVirtualMachineAutoBackupManualSchedule], jsii.get(self, "manualScheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionPeriodInDaysInput")
    def retention_period_in_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionPeriodInDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountAccessKeyInput")
    def storage_account_access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountAccessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="storageBlobEndpointInput")
    def storage_blob_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageBlobEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="systemDatabasesBackupEnabledInput")
    def system_databases_backup_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "systemDatabasesBackupEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionEnabled")
    def encryption_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "encryptionEnabled"))

    @encryption_enabled.setter
    def encryption_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionPassword")
    def encryption_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionPassword"))

    @encryption_password.setter
    def encryption_password(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionPassword", value)

    @builtins.property
    @jsii.member(jsii_name="retentionPeriodInDays")
    def retention_period_in_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionPeriodInDays"))

    @retention_period_in_days.setter
    def retention_period_in_days(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionPeriodInDays", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountAccessKey")
    def storage_account_access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountAccessKey"))

    @storage_account_access_key.setter
    def storage_account_access_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountAccessKey", value)

    @builtins.property
    @jsii.member(jsii_name="storageBlobEndpoint")
    def storage_blob_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageBlobEndpoint"))

    @storage_blob_endpoint.setter
    def storage_blob_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageBlobEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="systemDatabasesBackupEnabled")
    def system_databases_backup_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "systemDatabasesBackupEnabled"))

    @system_databases_backup_enabled.setter
    def system_databases_backup_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "systemDatabasesBackupEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MssqlVirtualMachineAutoBackup]:
        return typing.cast(typing.Optional[MssqlVirtualMachineAutoBackup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MssqlVirtualMachineAutoBackup],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[MssqlVirtualMachineAutoBackup]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlVirtualMachine.MssqlVirtualMachineAutoPatching",
    jsii_struct_bases=[],
    name_mapping={
        "day_of_week": "dayOfWeek",
        "maintenance_window_duration_in_minutes": "maintenanceWindowDurationInMinutes",
        "maintenance_window_starting_hour": "maintenanceWindowStartingHour",
    },
)
class MssqlVirtualMachineAutoPatching:
    def __init__(
        self,
        *,
        day_of_week: builtins.str,
        maintenance_window_duration_in_minutes: jsii.Number,
        maintenance_window_starting_hour: jsii.Number,
    ) -> None:
        '''
        :param day_of_week: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#day_of_week MssqlVirtualMachine#day_of_week}.
        :param maintenance_window_duration_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#maintenance_window_duration_in_minutes MssqlVirtualMachine#maintenance_window_duration_in_minutes}.
        :param maintenance_window_starting_hour: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#maintenance_window_starting_hour MssqlVirtualMachine#maintenance_window_starting_hour}.
        '''
        if __debug__:
            def stub(
                *,
                day_of_week: builtins.str,
                maintenance_window_duration_in_minutes: jsii.Number,
                maintenance_window_starting_hour: jsii.Number,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument day_of_week", value=day_of_week, expected_type=type_hints["day_of_week"])
            check_type(argname="argument maintenance_window_duration_in_minutes", value=maintenance_window_duration_in_minutes, expected_type=type_hints["maintenance_window_duration_in_minutes"])
            check_type(argname="argument maintenance_window_starting_hour", value=maintenance_window_starting_hour, expected_type=type_hints["maintenance_window_starting_hour"])
        self._values: typing.Dict[str, typing.Any] = {
            "day_of_week": day_of_week,
            "maintenance_window_duration_in_minutes": maintenance_window_duration_in_minutes,
            "maintenance_window_starting_hour": maintenance_window_starting_hour,
        }

    @builtins.property
    def day_of_week(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#day_of_week MssqlVirtualMachine#day_of_week}.'''
        result = self._values.get("day_of_week")
        assert result is not None, "Required property 'day_of_week' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def maintenance_window_duration_in_minutes(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#maintenance_window_duration_in_minutes MssqlVirtualMachine#maintenance_window_duration_in_minutes}.'''
        result = self._values.get("maintenance_window_duration_in_minutes")
        assert result is not None, "Required property 'maintenance_window_duration_in_minutes' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def maintenance_window_starting_hour(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#maintenance_window_starting_hour MssqlVirtualMachine#maintenance_window_starting_hour}.'''
        result = self._values.get("maintenance_window_starting_hour")
        assert result is not None, "Required property 'maintenance_window_starting_hour' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlVirtualMachineAutoPatching(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MssqlVirtualMachineAutoPatchingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlVirtualMachine.MssqlVirtualMachineAutoPatchingOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="dayOfWeekInput")
    def day_of_week_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dayOfWeekInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowDurationInMinutesInput")
    def maintenance_window_duration_in_minutes_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maintenanceWindowDurationInMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowStartingHourInput")
    def maintenance_window_starting_hour_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maintenanceWindowStartingHourInput"))

    @builtins.property
    @jsii.member(jsii_name="dayOfWeek")
    def day_of_week(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dayOfWeek"))

    @day_of_week.setter
    def day_of_week(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dayOfWeek", value)

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowDurationInMinutes")
    def maintenance_window_duration_in_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maintenanceWindowDurationInMinutes"))

    @maintenance_window_duration_in_minutes.setter
    def maintenance_window_duration_in_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maintenanceWindowDurationInMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowStartingHour")
    def maintenance_window_starting_hour(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maintenanceWindowStartingHour"))

    @maintenance_window_starting_hour.setter
    def maintenance_window_starting_hour(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maintenanceWindowStartingHour", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MssqlVirtualMachineAutoPatching]:
        return typing.cast(typing.Optional[MssqlVirtualMachineAutoPatching], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MssqlVirtualMachineAutoPatching],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[MssqlVirtualMachineAutoPatching]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlVirtualMachine.MssqlVirtualMachineConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "sql_license_type": "sqlLicenseType",
        "virtual_machine_id": "virtualMachineId",
        "assessment": "assessment",
        "auto_backup": "autoBackup",
        "auto_patching": "autoPatching",
        "id": "id",
        "key_vault_credential": "keyVaultCredential",
        "r_services_enabled": "rServicesEnabled",
        "sql_connectivity_port": "sqlConnectivityPort",
        "sql_connectivity_type": "sqlConnectivityType",
        "sql_connectivity_update_password": "sqlConnectivityUpdatePassword",
        "sql_connectivity_update_username": "sqlConnectivityUpdateUsername",
        "sql_instance": "sqlInstance",
        "storage_configuration": "storageConfiguration",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class MssqlVirtualMachineConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        sql_license_type: builtins.str,
        virtual_machine_id: builtins.str,
        assessment: typing.Optional[typing.Union[MssqlVirtualMachineAssessment, typing.Dict[str, typing.Any]]] = None,
        auto_backup: typing.Optional[typing.Union[MssqlVirtualMachineAutoBackup, typing.Dict[str, typing.Any]]] = None,
        auto_patching: typing.Optional[typing.Union[MssqlVirtualMachineAutoPatching, typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        key_vault_credential: typing.Optional[typing.Union["MssqlVirtualMachineKeyVaultCredential", typing.Dict[str, typing.Any]]] = None,
        r_services_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sql_connectivity_port: typing.Optional[jsii.Number] = None,
        sql_connectivity_type: typing.Optional[builtins.str] = None,
        sql_connectivity_update_password: typing.Optional[builtins.str] = None,
        sql_connectivity_update_username: typing.Optional[builtins.str] = None,
        sql_instance: typing.Optional[typing.Union["MssqlVirtualMachineSqlInstance", typing.Dict[str, typing.Any]]] = None,
        storage_configuration: typing.Optional[typing.Union["MssqlVirtualMachineStorageConfiguration", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["MssqlVirtualMachineTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param sql_license_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#sql_license_type MssqlVirtualMachine#sql_license_type}.
        :param virtual_machine_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#virtual_machine_id MssqlVirtualMachine#virtual_machine_id}.
        :param assessment: assessment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#assessment MssqlVirtualMachine#assessment}
        :param auto_backup: auto_backup block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#auto_backup MssqlVirtualMachine#auto_backup}
        :param auto_patching: auto_patching block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#auto_patching MssqlVirtualMachine#auto_patching}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#id MssqlVirtualMachine#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param key_vault_credential: key_vault_credential block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#key_vault_credential MssqlVirtualMachine#key_vault_credential}
        :param r_services_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#r_services_enabled MssqlVirtualMachine#r_services_enabled}.
        :param sql_connectivity_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#sql_connectivity_port MssqlVirtualMachine#sql_connectivity_port}.
        :param sql_connectivity_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#sql_connectivity_type MssqlVirtualMachine#sql_connectivity_type}.
        :param sql_connectivity_update_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#sql_connectivity_update_password MssqlVirtualMachine#sql_connectivity_update_password}.
        :param sql_connectivity_update_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#sql_connectivity_update_username MssqlVirtualMachine#sql_connectivity_update_username}.
        :param sql_instance: sql_instance block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#sql_instance MssqlVirtualMachine#sql_instance}
        :param storage_configuration: storage_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#storage_configuration MssqlVirtualMachine#storage_configuration}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#tags MssqlVirtualMachine#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#timeouts MssqlVirtualMachine#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(assessment, dict):
            assessment = MssqlVirtualMachineAssessment(**assessment)
        if isinstance(auto_backup, dict):
            auto_backup = MssqlVirtualMachineAutoBackup(**auto_backup)
        if isinstance(auto_patching, dict):
            auto_patching = MssqlVirtualMachineAutoPatching(**auto_patching)
        if isinstance(key_vault_credential, dict):
            key_vault_credential = MssqlVirtualMachineKeyVaultCredential(**key_vault_credential)
        if isinstance(sql_instance, dict):
            sql_instance = MssqlVirtualMachineSqlInstance(**sql_instance)
        if isinstance(storage_configuration, dict):
            storage_configuration = MssqlVirtualMachineStorageConfiguration(**storage_configuration)
        if isinstance(timeouts, dict):
            timeouts = MssqlVirtualMachineTimeouts(**timeouts)
        if __debug__:
            def stub(
                *,
                connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
                count: typing.Optional[jsii.Number] = None,
                depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
                for_each: typing.Optional[cdktf.ITerraformIterator] = None,
                lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
                provider: typing.Optional[cdktf.TerraformProvider] = None,
                provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
                sql_license_type: builtins.str,
                virtual_machine_id: builtins.str,
                assessment: typing.Optional[typing.Union[MssqlVirtualMachineAssessment, typing.Dict[str, typing.Any]]] = None,
                auto_backup: typing.Optional[typing.Union[MssqlVirtualMachineAutoBackup, typing.Dict[str, typing.Any]]] = None,
                auto_patching: typing.Optional[typing.Union[MssqlVirtualMachineAutoPatching, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                key_vault_credential: typing.Optional[typing.Union[MssqlVirtualMachineKeyVaultCredential, typing.Dict[str, typing.Any]]] = None,
                r_services_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                sql_connectivity_port: typing.Optional[jsii.Number] = None,
                sql_connectivity_type: typing.Optional[builtins.str] = None,
                sql_connectivity_update_password: typing.Optional[builtins.str] = None,
                sql_connectivity_update_username: typing.Optional[builtins.str] = None,
                sql_instance: typing.Optional[typing.Union[MssqlVirtualMachineSqlInstance, typing.Dict[str, typing.Any]]] = None,
                storage_configuration: typing.Optional[typing.Union[MssqlVirtualMachineStorageConfiguration, typing.Dict[str, typing.Any]]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[MssqlVirtualMachineTimeouts, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument sql_license_type", value=sql_license_type, expected_type=type_hints["sql_license_type"])
            check_type(argname="argument virtual_machine_id", value=virtual_machine_id, expected_type=type_hints["virtual_machine_id"])
            check_type(argname="argument assessment", value=assessment, expected_type=type_hints["assessment"])
            check_type(argname="argument auto_backup", value=auto_backup, expected_type=type_hints["auto_backup"])
            check_type(argname="argument auto_patching", value=auto_patching, expected_type=type_hints["auto_patching"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument key_vault_credential", value=key_vault_credential, expected_type=type_hints["key_vault_credential"])
            check_type(argname="argument r_services_enabled", value=r_services_enabled, expected_type=type_hints["r_services_enabled"])
            check_type(argname="argument sql_connectivity_port", value=sql_connectivity_port, expected_type=type_hints["sql_connectivity_port"])
            check_type(argname="argument sql_connectivity_type", value=sql_connectivity_type, expected_type=type_hints["sql_connectivity_type"])
            check_type(argname="argument sql_connectivity_update_password", value=sql_connectivity_update_password, expected_type=type_hints["sql_connectivity_update_password"])
            check_type(argname="argument sql_connectivity_update_username", value=sql_connectivity_update_username, expected_type=type_hints["sql_connectivity_update_username"])
            check_type(argname="argument sql_instance", value=sql_instance, expected_type=type_hints["sql_instance"])
            check_type(argname="argument storage_configuration", value=storage_configuration, expected_type=type_hints["storage_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "sql_license_type": sql_license_type,
            "virtual_machine_id": virtual_machine_id,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if assessment is not None:
            self._values["assessment"] = assessment
        if auto_backup is not None:
            self._values["auto_backup"] = auto_backup
        if auto_patching is not None:
            self._values["auto_patching"] = auto_patching
        if id is not None:
            self._values["id"] = id
        if key_vault_credential is not None:
            self._values["key_vault_credential"] = key_vault_credential
        if r_services_enabled is not None:
            self._values["r_services_enabled"] = r_services_enabled
        if sql_connectivity_port is not None:
            self._values["sql_connectivity_port"] = sql_connectivity_port
        if sql_connectivity_type is not None:
            self._values["sql_connectivity_type"] = sql_connectivity_type
        if sql_connectivity_update_password is not None:
            self._values["sql_connectivity_update_password"] = sql_connectivity_update_password
        if sql_connectivity_update_username is not None:
            self._values["sql_connectivity_update_username"] = sql_connectivity_update_username
        if sql_instance is not None:
            self._values["sql_instance"] = sql_instance
        if storage_configuration is not None:
            self._values["storage_configuration"] = storage_configuration
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def sql_license_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#sql_license_type MssqlVirtualMachine#sql_license_type}.'''
        result = self._values.get("sql_license_type")
        assert result is not None, "Required property 'sql_license_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def virtual_machine_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#virtual_machine_id MssqlVirtualMachine#virtual_machine_id}.'''
        result = self._values.get("virtual_machine_id")
        assert result is not None, "Required property 'virtual_machine_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assessment(self) -> typing.Optional[MssqlVirtualMachineAssessment]:
        '''assessment block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#assessment MssqlVirtualMachine#assessment}
        '''
        result = self._values.get("assessment")
        return typing.cast(typing.Optional[MssqlVirtualMachineAssessment], result)

    @builtins.property
    def auto_backup(self) -> typing.Optional[MssqlVirtualMachineAutoBackup]:
        '''auto_backup block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#auto_backup MssqlVirtualMachine#auto_backup}
        '''
        result = self._values.get("auto_backup")
        return typing.cast(typing.Optional[MssqlVirtualMachineAutoBackup], result)

    @builtins.property
    def auto_patching(self) -> typing.Optional[MssqlVirtualMachineAutoPatching]:
        '''auto_patching block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#auto_patching MssqlVirtualMachine#auto_patching}
        '''
        result = self._values.get("auto_patching")
        return typing.cast(typing.Optional[MssqlVirtualMachineAutoPatching], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#id MssqlVirtualMachine#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_vault_credential(
        self,
    ) -> typing.Optional["MssqlVirtualMachineKeyVaultCredential"]:
        '''key_vault_credential block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#key_vault_credential MssqlVirtualMachine#key_vault_credential}
        '''
        result = self._values.get("key_vault_credential")
        return typing.cast(typing.Optional["MssqlVirtualMachineKeyVaultCredential"], result)

    @builtins.property
    def r_services_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#r_services_enabled MssqlVirtualMachine#r_services_enabled}.'''
        result = self._values.get("r_services_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def sql_connectivity_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#sql_connectivity_port MssqlVirtualMachine#sql_connectivity_port}.'''
        result = self._values.get("sql_connectivity_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sql_connectivity_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#sql_connectivity_type MssqlVirtualMachine#sql_connectivity_type}.'''
        result = self._values.get("sql_connectivity_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sql_connectivity_update_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#sql_connectivity_update_password MssqlVirtualMachine#sql_connectivity_update_password}.'''
        result = self._values.get("sql_connectivity_update_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sql_connectivity_update_username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#sql_connectivity_update_username MssqlVirtualMachine#sql_connectivity_update_username}.'''
        result = self._values.get("sql_connectivity_update_username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sql_instance(self) -> typing.Optional["MssqlVirtualMachineSqlInstance"]:
        '''sql_instance block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#sql_instance MssqlVirtualMachine#sql_instance}
        '''
        result = self._values.get("sql_instance")
        return typing.cast(typing.Optional["MssqlVirtualMachineSqlInstance"], result)

    @builtins.property
    def storage_configuration(
        self,
    ) -> typing.Optional["MssqlVirtualMachineStorageConfiguration"]:
        '''storage_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#storage_configuration MssqlVirtualMachine#storage_configuration}
        '''
        result = self._values.get("storage_configuration")
        return typing.cast(typing.Optional["MssqlVirtualMachineStorageConfiguration"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#tags MssqlVirtualMachine#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MssqlVirtualMachineTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#timeouts MssqlVirtualMachine#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MssqlVirtualMachineTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlVirtualMachineConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlVirtualMachine.MssqlVirtualMachineKeyVaultCredential",
    jsii_struct_bases=[],
    name_mapping={
        "key_vault_url": "keyVaultUrl",
        "name": "name",
        "service_principal_name": "servicePrincipalName",
        "service_principal_secret": "servicePrincipalSecret",
    },
)
class MssqlVirtualMachineKeyVaultCredential:
    def __init__(
        self,
        *,
        key_vault_url: builtins.str,
        name: builtins.str,
        service_principal_name: builtins.str,
        service_principal_secret: builtins.str,
    ) -> None:
        '''
        :param key_vault_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#key_vault_url MssqlVirtualMachine#key_vault_url}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#name MssqlVirtualMachine#name}.
        :param service_principal_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#service_principal_name MssqlVirtualMachine#service_principal_name}.
        :param service_principal_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#service_principal_secret MssqlVirtualMachine#service_principal_secret}.
        '''
        if __debug__:
            def stub(
                *,
                key_vault_url: builtins.str,
                name: builtins.str,
                service_principal_name: builtins.str,
                service_principal_secret: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key_vault_url", value=key_vault_url, expected_type=type_hints["key_vault_url"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument service_principal_name", value=service_principal_name, expected_type=type_hints["service_principal_name"])
            check_type(argname="argument service_principal_secret", value=service_principal_secret, expected_type=type_hints["service_principal_secret"])
        self._values: typing.Dict[str, typing.Any] = {
            "key_vault_url": key_vault_url,
            "name": name,
            "service_principal_name": service_principal_name,
            "service_principal_secret": service_principal_secret,
        }

    @builtins.property
    def key_vault_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#key_vault_url MssqlVirtualMachine#key_vault_url}.'''
        result = self._values.get("key_vault_url")
        assert result is not None, "Required property 'key_vault_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#name MssqlVirtualMachine#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_principal_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#service_principal_name MssqlVirtualMachine#service_principal_name}.'''
        result = self._values.get("service_principal_name")
        assert result is not None, "Required property 'service_principal_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_principal_secret(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#service_principal_secret MssqlVirtualMachine#service_principal_secret}.'''
        result = self._values.get("service_principal_secret")
        assert result is not None, "Required property 'service_principal_secret' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlVirtualMachineKeyVaultCredential(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MssqlVirtualMachineKeyVaultCredentialOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlVirtualMachine.MssqlVirtualMachineKeyVaultCredentialOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="keyVaultUrlInput")
    def key_vault_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="servicePrincipalNameInput")
    def service_principal_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "servicePrincipalNameInput"))

    @builtins.property
    @jsii.member(jsii_name="servicePrincipalSecretInput")
    def service_principal_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "servicePrincipalSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultUrl")
    def key_vault_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultUrl"))

    @key_vault_url.setter
    def key_vault_url(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultUrl", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="servicePrincipalName")
    def service_principal_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servicePrincipalName"))

    @service_principal_name.setter
    def service_principal_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servicePrincipalName", value)

    @builtins.property
    @jsii.member(jsii_name="servicePrincipalSecret")
    def service_principal_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servicePrincipalSecret"))

    @service_principal_secret.setter
    def service_principal_secret(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servicePrincipalSecret", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MssqlVirtualMachineKeyVaultCredential]:
        return typing.cast(typing.Optional[MssqlVirtualMachineKeyVaultCredential], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MssqlVirtualMachineKeyVaultCredential],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MssqlVirtualMachineKeyVaultCredential],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlVirtualMachine.MssqlVirtualMachineSqlInstance",
    jsii_struct_bases=[],
    name_mapping={
        "adhoc_workloads_optimization_enabled": "adhocWorkloadsOptimizationEnabled",
        "collation": "collation",
        "instant_file_initialization_enabled": "instantFileInitializationEnabled",
        "lock_pages_in_memory_enabled": "lockPagesInMemoryEnabled",
        "max_dop": "maxDop",
        "max_server_memory_mb": "maxServerMemoryMb",
        "min_server_memory_mb": "minServerMemoryMb",
    },
)
class MssqlVirtualMachineSqlInstance:
    def __init__(
        self,
        *,
        adhoc_workloads_optimization_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        collation: typing.Optional[builtins.str] = None,
        instant_file_initialization_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        lock_pages_in_memory_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_dop: typing.Optional[jsii.Number] = None,
        max_server_memory_mb: typing.Optional[jsii.Number] = None,
        min_server_memory_mb: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param adhoc_workloads_optimization_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#adhoc_workloads_optimization_enabled MssqlVirtualMachine#adhoc_workloads_optimization_enabled}.
        :param collation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#collation MssqlVirtualMachine#collation}.
        :param instant_file_initialization_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#instant_file_initialization_enabled MssqlVirtualMachine#instant_file_initialization_enabled}.
        :param lock_pages_in_memory_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#lock_pages_in_memory_enabled MssqlVirtualMachine#lock_pages_in_memory_enabled}.
        :param max_dop: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#max_dop MssqlVirtualMachine#max_dop}.
        :param max_server_memory_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#max_server_memory_mb MssqlVirtualMachine#max_server_memory_mb}.
        :param min_server_memory_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#min_server_memory_mb MssqlVirtualMachine#min_server_memory_mb}.
        '''
        if __debug__:
            def stub(
                *,
                adhoc_workloads_optimization_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                collation: typing.Optional[builtins.str] = None,
                instant_file_initialization_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                lock_pages_in_memory_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                max_dop: typing.Optional[jsii.Number] = None,
                max_server_memory_mb: typing.Optional[jsii.Number] = None,
                min_server_memory_mb: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument adhoc_workloads_optimization_enabled", value=adhoc_workloads_optimization_enabled, expected_type=type_hints["adhoc_workloads_optimization_enabled"])
            check_type(argname="argument collation", value=collation, expected_type=type_hints["collation"])
            check_type(argname="argument instant_file_initialization_enabled", value=instant_file_initialization_enabled, expected_type=type_hints["instant_file_initialization_enabled"])
            check_type(argname="argument lock_pages_in_memory_enabled", value=lock_pages_in_memory_enabled, expected_type=type_hints["lock_pages_in_memory_enabled"])
            check_type(argname="argument max_dop", value=max_dop, expected_type=type_hints["max_dop"])
            check_type(argname="argument max_server_memory_mb", value=max_server_memory_mb, expected_type=type_hints["max_server_memory_mb"])
            check_type(argname="argument min_server_memory_mb", value=min_server_memory_mb, expected_type=type_hints["min_server_memory_mb"])
        self._values: typing.Dict[str, typing.Any] = {}
        if adhoc_workloads_optimization_enabled is not None:
            self._values["adhoc_workloads_optimization_enabled"] = adhoc_workloads_optimization_enabled
        if collation is not None:
            self._values["collation"] = collation
        if instant_file_initialization_enabled is not None:
            self._values["instant_file_initialization_enabled"] = instant_file_initialization_enabled
        if lock_pages_in_memory_enabled is not None:
            self._values["lock_pages_in_memory_enabled"] = lock_pages_in_memory_enabled
        if max_dop is not None:
            self._values["max_dop"] = max_dop
        if max_server_memory_mb is not None:
            self._values["max_server_memory_mb"] = max_server_memory_mb
        if min_server_memory_mb is not None:
            self._values["min_server_memory_mb"] = min_server_memory_mb

    @builtins.property
    def adhoc_workloads_optimization_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#adhoc_workloads_optimization_enabled MssqlVirtualMachine#adhoc_workloads_optimization_enabled}.'''
        result = self._values.get("adhoc_workloads_optimization_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def collation(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#collation MssqlVirtualMachine#collation}.'''
        result = self._values.get("collation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instant_file_initialization_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#instant_file_initialization_enabled MssqlVirtualMachine#instant_file_initialization_enabled}.'''
        result = self._values.get("instant_file_initialization_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def lock_pages_in_memory_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#lock_pages_in_memory_enabled MssqlVirtualMachine#lock_pages_in_memory_enabled}.'''
        result = self._values.get("lock_pages_in_memory_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def max_dop(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#max_dop MssqlVirtualMachine#max_dop}.'''
        result = self._values.get("max_dop")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_server_memory_mb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#max_server_memory_mb MssqlVirtualMachine#max_server_memory_mb}.'''
        result = self._values.get("max_server_memory_mb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_server_memory_mb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#min_server_memory_mb MssqlVirtualMachine#min_server_memory_mb}.'''
        result = self._values.get("min_server_memory_mb")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlVirtualMachineSqlInstance(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MssqlVirtualMachineSqlInstanceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlVirtualMachine.MssqlVirtualMachineSqlInstanceOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAdhocWorkloadsOptimizationEnabled")
    def reset_adhoc_workloads_optimization_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdhocWorkloadsOptimizationEnabled", []))

    @jsii.member(jsii_name="resetCollation")
    def reset_collation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCollation", []))

    @jsii.member(jsii_name="resetInstantFileInitializationEnabled")
    def reset_instant_file_initialization_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstantFileInitializationEnabled", []))

    @jsii.member(jsii_name="resetLockPagesInMemoryEnabled")
    def reset_lock_pages_in_memory_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLockPagesInMemoryEnabled", []))

    @jsii.member(jsii_name="resetMaxDop")
    def reset_max_dop(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxDop", []))

    @jsii.member(jsii_name="resetMaxServerMemoryMb")
    def reset_max_server_memory_mb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxServerMemoryMb", []))

    @jsii.member(jsii_name="resetMinServerMemoryMb")
    def reset_min_server_memory_mb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinServerMemoryMb", []))

    @builtins.property
    @jsii.member(jsii_name="adhocWorkloadsOptimizationEnabledInput")
    def adhoc_workloads_optimization_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "adhocWorkloadsOptimizationEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="collationInput")
    def collation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "collationInput"))

    @builtins.property
    @jsii.member(jsii_name="instantFileInitializationEnabledInput")
    def instant_file_initialization_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "instantFileInitializationEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="lockPagesInMemoryEnabledInput")
    def lock_pages_in_memory_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "lockPagesInMemoryEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="maxDopInput")
    def max_dop_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxDopInput"))

    @builtins.property
    @jsii.member(jsii_name="maxServerMemoryMbInput")
    def max_server_memory_mb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxServerMemoryMbInput"))

    @builtins.property
    @jsii.member(jsii_name="minServerMemoryMbInput")
    def min_server_memory_mb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minServerMemoryMbInput"))

    @builtins.property
    @jsii.member(jsii_name="adhocWorkloadsOptimizationEnabled")
    def adhoc_workloads_optimization_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "adhocWorkloadsOptimizationEnabled"))

    @adhoc_workloads_optimization_enabled.setter
    def adhoc_workloads_optimization_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adhocWorkloadsOptimizationEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="collation")
    def collation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "collation"))

    @collation.setter
    def collation(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "collation", value)

    @builtins.property
    @jsii.member(jsii_name="instantFileInitializationEnabled")
    def instant_file_initialization_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "instantFileInitializationEnabled"))

    @instant_file_initialization_enabled.setter
    def instant_file_initialization_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instantFileInitializationEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="lockPagesInMemoryEnabled")
    def lock_pages_in_memory_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "lockPagesInMemoryEnabled"))

    @lock_pages_in_memory_enabled.setter
    def lock_pages_in_memory_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lockPagesInMemoryEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="maxDop")
    def max_dop(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxDop"))

    @max_dop.setter
    def max_dop(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxDop", value)

    @builtins.property
    @jsii.member(jsii_name="maxServerMemoryMb")
    def max_server_memory_mb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxServerMemoryMb"))

    @max_server_memory_mb.setter
    def max_server_memory_mb(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxServerMemoryMb", value)

    @builtins.property
    @jsii.member(jsii_name="minServerMemoryMb")
    def min_server_memory_mb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minServerMemoryMb"))

    @min_server_memory_mb.setter
    def min_server_memory_mb(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minServerMemoryMb", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MssqlVirtualMachineSqlInstance]:
        return typing.cast(typing.Optional[MssqlVirtualMachineSqlInstance], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MssqlVirtualMachineSqlInstance],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[MssqlVirtualMachineSqlInstance]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlVirtualMachine.MssqlVirtualMachineStorageConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "disk_type": "diskType",
        "storage_workload_type": "storageWorkloadType",
        "data_settings": "dataSettings",
        "log_settings": "logSettings",
        "system_db_on_data_disk_enabled": "systemDbOnDataDiskEnabled",
        "temp_db_settings": "tempDbSettings",
    },
)
class MssqlVirtualMachineStorageConfiguration:
    def __init__(
        self,
        *,
        disk_type: builtins.str,
        storage_workload_type: builtins.str,
        data_settings: typing.Optional[typing.Union["MssqlVirtualMachineStorageConfigurationDataSettings", typing.Dict[str, typing.Any]]] = None,
        log_settings: typing.Optional[typing.Union["MssqlVirtualMachineStorageConfigurationLogSettings", typing.Dict[str, typing.Any]]] = None,
        system_db_on_data_disk_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        temp_db_settings: typing.Optional[typing.Union["MssqlVirtualMachineStorageConfigurationTempDbSettings", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param disk_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#disk_type MssqlVirtualMachine#disk_type}.
        :param storage_workload_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#storage_workload_type MssqlVirtualMachine#storage_workload_type}.
        :param data_settings: data_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#data_settings MssqlVirtualMachine#data_settings}
        :param log_settings: log_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#log_settings MssqlVirtualMachine#log_settings}
        :param system_db_on_data_disk_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#system_db_on_data_disk_enabled MssqlVirtualMachine#system_db_on_data_disk_enabled}.
        :param temp_db_settings: temp_db_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#temp_db_settings MssqlVirtualMachine#temp_db_settings}
        '''
        if isinstance(data_settings, dict):
            data_settings = MssqlVirtualMachineStorageConfigurationDataSettings(**data_settings)
        if isinstance(log_settings, dict):
            log_settings = MssqlVirtualMachineStorageConfigurationLogSettings(**log_settings)
        if isinstance(temp_db_settings, dict):
            temp_db_settings = MssqlVirtualMachineStorageConfigurationTempDbSettings(**temp_db_settings)
        if __debug__:
            def stub(
                *,
                disk_type: builtins.str,
                storage_workload_type: builtins.str,
                data_settings: typing.Optional[typing.Union[MssqlVirtualMachineStorageConfigurationDataSettings, typing.Dict[str, typing.Any]]] = None,
                log_settings: typing.Optional[typing.Union[MssqlVirtualMachineStorageConfigurationLogSettings, typing.Dict[str, typing.Any]]] = None,
                system_db_on_data_disk_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                temp_db_settings: typing.Optional[typing.Union[MssqlVirtualMachineStorageConfigurationTempDbSettings, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument disk_type", value=disk_type, expected_type=type_hints["disk_type"])
            check_type(argname="argument storage_workload_type", value=storage_workload_type, expected_type=type_hints["storage_workload_type"])
            check_type(argname="argument data_settings", value=data_settings, expected_type=type_hints["data_settings"])
            check_type(argname="argument log_settings", value=log_settings, expected_type=type_hints["log_settings"])
            check_type(argname="argument system_db_on_data_disk_enabled", value=system_db_on_data_disk_enabled, expected_type=type_hints["system_db_on_data_disk_enabled"])
            check_type(argname="argument temp_db_settings", value=temp_db_settings, expected_type=type_hints["temp_db_settings"])
        self._values: typing.Dict[str, typing.Any] = {
            "disk_type": disk_type,
            "storage_workload_type": storage_workload_type,
        }
        if data_settings is not None:
            self._values["data_settings"] = data_settings
        if log_settings is not None:
            self._values["log_settings"] = log_settings
        if system_db_on_data_disk_enabled is not None:
            self._values["system_db_on_data_disk_enabled"] = system_db_on_data_disk_enabled
        if temp_db_settings is not None:
            self._values["temp_db_settings"] = temp_db_settings

    @builtins.property
    def disk_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#disk_type MssqlVirtualMachine#disk_type}.'''
        result = self._values.get("disk_type")
        assert result is not None, "Required property 'disk_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_workload_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#storage_workload_type MssqlVirtualMachine#storage_workload_type}.'''
        result = self._values.get("storage_workload_type")
        assert result is not None, "Required property 'storage_workload_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_settings(
        self,
    ) -> typing.Optional["MssqlVirtualMachineStorageConfigurationDataSettings"]:
        '''data_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#data_settings MssqlVirtualMachine#data_settings}
        '''
        result = self._values.get("data_settings")
        return typing.cast(typing.Optional["MssqlVirtualMachineStorageConfigurationDataSettings"], result)

    @builtins.property
    def log_settings(
        self,
    ) -> typing.Optional["MssqlVirtualMachineStorageConfigurationLogSettings"]:
        '''log_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#log_settings MssqlVirtualMachine#log_settings}
        '''
        result = self._values.get("log_settings")
        return typing.cast(typing.Optional["MssqlVirtualMachineStorageConfigurationLogSettings"], result)

    @builtins.property
    def system_db_on_data_disk_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#system_db_on_data_disk_enabled MssqlVirtualMachine#system_db_on_data_disk_enabled}.'''
        result = self._values.get("system_db_on_data_disk_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def temp_db_settings(
        self,
    ) -> typing.Optional["MssqlVirtualMachineStorageConfigurationTempDbSettings"]:
        '''temp_db_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#temp_db_settings MssqlVirtualMachine#temp_db_settings}
        '''
        result = self._values.get("temp_db_settings")
        return typing.cast(typing.Optional["MssqlVirtualMachineStorageConfigurationTempDbSettings"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlVirtualMachineStorageConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlVirtualMachine.MssqlVirtualMachineStorageConfigurationDataSettings",
    jsii_struct_bases=[],
    name_mapping={"default_file_path": "defaultFilePath", "luns": "luns"},
)
class MssqlVirtualMachineStorageConfigurationDataSettings:
    def __init__(
        self,
        *,
        default_file_path: builtins.str,
        luns: typing.Sequence[jsii.Number],
    ) -> None:
        '''
        :param default_file_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#default_file_path MssqlVirtualMachine#default_file_path}.
        :param luns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#luns MssqlVirtualMachine#luns}.
        '''
        if __debug__:
            def stub(
                *,
                default_file_path: builtins.str,
                luns: typing.Sequence[jsii.Number],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument default_file_path", value=default_file_path, expected_type=type_hints["default_file_path"])
            check_type(argname="argument luns", value=luns, expected_type=type_hints["luns"])
        self._values: typing.Dict[str, typing.Any] = {
            "default_file_path": default_file_path,
            "luns": luns,
        }

    @builtins.property
    def default_file_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#default_file_path MssqlVirtualMachine#default_file_path}.'''
        result = self._values.get("default_file_path")
        assert result is not None, "Required property 'default_file_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def luns(self) -> typing.List[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#luns MssqlVirtualMachine#luns}.'''
        result = self._values.get("luns")
        assert result is not None, "Required property 'luns' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlVirtualMachineStorageConfigurationDataSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MssqlVirtualMachineStorageConfigurationDataSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlVirtualMachine.MssqlVirtualMachineStorageConfigurationDataSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="defaultFilePathInput")
    def default_file_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultFilePathInput"))

    @builtins.property
    @jsii.member(jsii_name="lunsInput")
    def luns_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "lunsInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultFilePath")
    def default_file_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultFilePath"))

    @default_file_path.setter
    def default_file_path(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultFilePath", value)

    @builtins.property
    @jsii.member(jsii_name="luns")
    def luns(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "luns"))

    @luns.setter
    def luns(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            def stub(value: typing.List[jsii.Number]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "luns", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MssqlVirtualMachineStorageConfigurationDataSettings]:
        return typing.cast(typing.Optional[MssqlVirtualMachineStorageConfigurationDataSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MssqlVirtualMachineStorageConfigurationDataSettings],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MssqlVirtualMachineStorageConfigurationDataSettings],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlVirtualMachine.MssqlVirtualMachineStorageConfigurationLogSettings",
    jsii_struct_bases=[],
    name_mapping={"default_file_path": "defaultFilePath", "luns": "luns"},
)
class MssqlVirtualMachineStorageConfigurationLogSettings:
    def __init__(
        self,
        *,
        default_file_path: builtins.str,
        luns: typing.Sequence[jsii.Number],
    ) -> None:
        '''
        :param default_file_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#default_file_path MssqlVirtualMachine#default_file_path}.
        :param luns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#luns MssqlVirtualMachine#luns}.
        '''
        if __debug__:
            def stub(
                *,
                default_file_path: builtins.str,
                luns: typing.Sequence[jsii.Number],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument default_file_path", value=default_file_path, expected_type=type_hints["default_file_path"])
            check_type(argname="argument luns", value=luns, expected_type=type_hints["luns"])
        self._values: typing.Dict[str, typing.Any] = {
            "default_file_path": default_file_path,
            "luns": luns,
        }

    @builtins.property
    def default_file_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#default_file_path MssqlVirtualMachine#default_file_path}.'''
        result = self._values.get("default_file_path")
        assert result is not None, "Required property 'default_file_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def luns(self) -> typing.List[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#luns MssqlVirtualMachine#luns}.'''
        result = self._values.get("luns")
        assert result is not None, "Required property 'luns' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlVirtualMachineStorageConfigurationLogSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MssqlVirtualMachineStorageConfigurationLogSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlVirtualMachine.MssqlVirtualMachineStorageConfigurationLogSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="defaultFilePathInput")
    def default_file_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultFilePathInput"))

    @builtins.property
    @jsii.member(jsii_name="lunsInput")
    def luns_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "lunsInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultFilePath")
    def default_file_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultFilePath"))

    @default_file_path.setter
    def default_file_path(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultFilePath", value)

    @builtins.property
    @jsii.member(jsii_name="luns")
    def luns(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "luns"))

    @luns.setter
    def luns(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            def stub(value: typing.List[jsii.Number]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "luns", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MssqlVirtualMachineStorageConfigurationLogSettings]:
        return typing.cast(typing.Optional[MssqlVirtualMachineStorageConfigurationLogSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MssqlVirtualMachineStorageConfigurationLogSettings],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MssqlVirtualMachineStorageConfigurationLogSettings],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MssqlVirtualMachineStorageConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlVirtualMachine.MssqlVirtualMachineStorageConfigurationOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDataSettings")
    def put_data_settings(
        self,
        *,
        default_file_path: builtins.str,
        luns: typing.Sequence[jsii.Number],
    ) -> None:
        '''
        :param default_file_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#default_file_path MssqlVirtualMachine#default_file_path}.
        :param luns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#luns MssqlVirtualMachine#luns}.
        '''
        value = MssqlVirtualMachineStorageConfigurationDataSettings(
            default_file_path=default_file_path, luns=luns
        )

        return typing.cast(None, jsii.invoke(self, "putDataSettings", [value]))

    @jsii.member(jsii_name="putLogSettings")
    def put_log_settings(
        self,
        *,
        default_file_path: builtins.str,
        luns: typing.Sequence[jsii.Number],
    ) -> None:
        '''
        :param default_file_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#default_file_path MssqlVirtualMachine#default_file_path}.
        :param luns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#luns MssqlVirtualMachine#luns}.
        '''
        value = MssqlVirtualMachineStorageConfigurationLogSettings(
            default_file_path=default_file_path, luns=luns
        )

        return typing.cast(None, jsii.invoke(self, "putLogSettings", [value]))

    @jsii.member(jsii_name="putTempDbSettings")
    def put_temp_db_settings(
        self,
        *,
        default_file_path: builtins.str,
        luns: typing.Sequence[jsii.Number],
        data_file_count: typing.Optional[jsii.Number] = None,
        data_file_growth_in_mb: typing.Optional[jsii.Number] = None,
        data_file_size_mb: typing.Optional[jsii.Number] = None,
        log_file_growth_mb: typing.Optional[jsii.Number] = None,
        log_file_size_mb: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param default_file_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#default_file_path MssqlVirtualMachine#default_file_path}.
        :param luns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#luns MssqlVirtualMachine#luns}.
        :param data_file_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#data_file_count MssqlVirtualMachine#data_file_count}.
        :param data_file_growth_in_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#data_file_growth_in_mb MssqlVirtualMachine#data_file_growth_in_mb}.
        :param data_file_size_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#data_file_size_mb MssqlVirtualMachine#data_file_size_mb}.
        :param log_file_growth_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#log_file_growth_mb MssqlVirtualMachine#log_file_growth_mb}.
        :param log_file_size_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#log_file_size_mb MssqlVirtualMachine#log_file_size_mb}.
        '''
        value = MssqlVirtualMachineStorageConfigurationTempDbSettings(
            default_file_path=default_file_path,
            luns=luns,
            data_file_count=data_file_count,
            data_file_growth_in_mb=data_file_growth_in_mb,
            data_file_size_mb=data_file_size_mb,
            log_file_growth_mb=log_file_growth_mb,
            log_file_size_mb=log_file_size_mb,
        )

        return typing.cast(None, jsii.invoke(self, "putTempDbSettings", [value]))

    @jsii.member(jsii_name="resetDataSettings")
    def reset_data_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataSettings", []))

    @jsii.member(jsii_name="resetLogSettings")
    def reset_log_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogSettings", []))

    @jsii.member(jsii_name="resetSystemDbOnDataDiskEnabled")
    def reset_system_db_on_data_disk_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSystemDbOnDataDiskEnabled", []))

    @jsii.member(jsii_name="resetTempDbSettings")
    def reset_temp_db_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTempDbSettings", []))

    @builtins.property
    @jsii.member(jsii_name="dataSettings")
    def data_settings(
        self,
    ) -> MssqlVirtualMachineStorageConfigurationDataSettingsOutputReference:
        return typing.cast(MssqlVirtualMachineStorageConfigurationDataSettingsOutputReference, jsii.get(self, "dataSettings"))

    @builtins.property
    @jsii.member(jsii_name="logSettings")
    def log_settings(
        self,
    ) -> MssqlVirtualMachineStorageConfigurationLogSettingsOutputReference:
        return typing.cast(MssqlVirtualMachineStorageConfigurationLogSettingsOutputReference, jsii.get(self, "logSettings"))

    @builtins.property
    @jsii.member(jsii_name="tempDbSettings")
    def temp_db_settings(
        self,
    ) -> "MssqlVirtualMachineStorageConfigurationTempDbSettingsOutputReference":
        return typing.cast("MssqlVirtualMachineStorageConfigurationTempDbSettingsOutputReference", jsii.get(self, "tempDbSettings"))

    @builtins.property
    @jsii.member(jsii_name="dataSettingsInput")
    def data_settings_input(
        self,
    ) -> typing.Optional[MssqlVirtualMachineStorageConfigurationDataSettings]:
        return typing.cast(typing.Optional[MssqlVirtualMachineStorageConfigurationDataSettings], jsii.get(self, "dataSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="diskTypeInput")
    def disk_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="logSettingsInput")
    def log_settings_input(
        self,
    ) -> typing.Optional[MssqlVirtualMachineStorageConfigurationLogSettings]:
        return typing.cast(typing.Optional[MssqlVirtualMachineStorageConfigurationLogSettings], jsii.get(self, "logSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="storageWorkloadTypeInput")
    def storage_workload_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageWorkloadTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="systemDbOnDataDiskEnabledInput")
    def system_db_on_data_disk_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "systemDbOnDataDiskEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="tempDbSettingsInput")
    def temp_db_settings_input(
        self,
    ) -> typing.Optional["MssqlVirtualMachineStorageConfigurationTempDbSettings"]:
        return typing.cast(typing.Optional["MssqlVirtualMachineStorageConfigurationTempDbSettings"], jsii.get(self, "tempDbSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="diskType")
    def disk_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskType"))

    @disk_type.setter
    def disk_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskType", value)

    @builtins.property
    @jsii.member(jsii_name="storageWorkloadType")
    def storage_workload_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageWorkloadType"))

    @storage_workload_type.setter
    def storage_workload_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageWorkloadType", value)

    @builtins.property
    @jsii.member(jsii_name="systemDbOnDataDiskEnabled")
    def system_db_on_data_disk_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "systemDbOnDataDiskEnabled"))

    @system_db_on_data_disk_enabled.setter
    def system_db_on_data_disk_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "systemDbOnDataDiskEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MssqlVirtualMachineStorageConfiguration]:
        return typing.cast(typing.Optional[MssqlVirtualMachineStorageConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MssqlVirtualMachineStorageConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MssqlVirtualMachineStorageConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlVirtualMachine.MssqlVirtualMachineStorageConfigurationTempDbSettings",
    jsii_struct_bases=[],
    name_mapping={
        "default_file_path": "defaultFilePath",
        "luns": "luns",
        "data_file_count": "dataFileCount",
        "data_file_growth_in_mb": "dataFileGrowthInMb",
        "data_file_size_mb": "dataFileSizeMb",
        "log_file_growth_mb": "logFileGrowthMb",
        "log_file_size_mb": "logFileSizeMb",
    },
)
class MssqlVirtualMachineStorageConfigurationTempDbSettings:
    def __init__(
        self,
        *,
        default_file_path: builtins.str,
        luns: typing.Sequence[jsii.Number],
        data_file_count: typing.Optional[jsii.Number] = None,
        data_file_growth_in_mb: typing.Optional[jsii.Number] = None,
        data_file_size_mb: typing.Optional[jsii.Number] = None,
        log_file_growth_mb: typing.Optional[jsii.Number] = None,
        log_file_size_mb: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param default_file_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#default_file_path MssqlVirtualMachine#default_file_path}.
        :param luns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#luns MssqlVirtualMachine#luns}.
        :param data_file_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#data_file_count MssqlVirtualMachine#data_file_count}.
        :param data_file_growth_in_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#data_file_growth_in_mb MssqlVirtualMachine#data_file_growth_in_mb}.
        :param data_file_size_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#data_file_size_mb MssqlVirtualMachine#data_file_size_mb}.
        :param log_file_growth_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#log_file_growth_mb MssqlVirtualMachine#log_file_growth_mb}.
        :param log_file_size_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#log_file_size_mb MssqlVirtualMachine#log_file_size_mb}.
        '''
        if __debug__:
            def stub(
                *,
                default_file_path: builtins.str,
                luns: typing.Sequence[jsii.Number],
                data_file_count: typing.Optional[jsii.Number] = None,
                data_file_growth_in_mb: typing.Optional[jsii.Number] = None,
                data_file_size_mb: typing.Optional[jsii.Number] = None,
                log_file_growth_mb: typing.Optional[jsii.Number] = None,
                log_file_size_mb: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument default_file_path", value=default_file_path, expected_type=type_hints["default_file_path"])
            check_type(argname="argument luns", value=luns, expected_type=type_hints["luns"])
            check_type(argname="argument data_file_count", value=data_file_count, expected_type=type_hints["data_file_count"])
            check_type(argname="argument data_file_growth_in_mb", value=data_file_growth_in_mb, expected_type=type_hints["data_file_growth_in_mb"])
            check_type(argname="argument data_file_size_mb", value=data_file_size_mb, expected_type=type_hints["data_file_size_mb"])
            check_type(argname="argument log_file_growth_mb", value=log_file_growth_mb, expected_type=type_hints["log_file_growth_mb"])
            check_type(argname="argument log_file_size_mb", value=log_file_size_mb, expected_type=type_hints["log_file_size_mb"])
        self._values: typing.Dict[str, typing.Any] = {
            "default_file_path": default_file_path,
            "luns": luns,
        }
        if data_file_count is not None:
            self._values["data_file_count"] = data_file_count
        if data_file_growth_in_mb is not None:
            self._values["data_file_growth_in_mb"] = data_file_growth_in_mb
        if data_file_size_mb is not None:
            self._values["data_file_size_mb"] = data_file_size_mb
        if log_file_growth_mb is not None:
            self._values["log_file_growth_mb"] = log_file_growth_mb
        if log_file_size_mb is not None:
            self._values["log_file_size_mb"] = log_file_size_mb

    @builtins.property
    def default_file_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#default_file_path MssqlVirtualMachine#default_file_path}.'''
        result = self._values.get("default_file_path")
        assert result is not None, "Required property 'default_file_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def luns(self) -> typing.List[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#luns MssqlVirtualMachine#luns}.'''
        result = self._values.get("luns")
        assert result is not None, "Required property 'luns' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    @builtins.property
    def data_file_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#data_file_count MssqlVirtualMachine#data_file_count}.'''
        result = self._values.get("data_file_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def data_file_growth_in_mb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#data_file_growth_in_mb MssqlVirtualMachine#data_file_growth_in_mb}.'''
        result = self._values.get("data_file_growth_in_mb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def data_file_size_mb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#data_file_size_mb MssqlVirtualMachine#data_file_size_mb}.'''
        result = self._values.get("data_file_size_mb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def log_file_growth_mb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#log_file_growth_mb MssqlVirtualMachine#log_file_growth_mb}.'''
        result = self._values.get("log_file_growth_mb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def log_file_size_mb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#log_file_size_mb MssqlVirtualMachine#log_file_size_mb}.'''
        result = self._values.get("log_file_size_mb")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlVirtualMachineStorageConfigurationTempDbSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MssqlVirtualMachineStorageConfigurationTempDbSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlVirtualMachine.MssqlVirtualMachineStorageConfigurationTempDbSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDataFileCount")
    def reset_data_file_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataFileCount", []))

    @jsii.member(jsii_name="resetDataFileGrowthInMb")
    def reset_data_file_growth_in_mb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataFileGrowthInMb", []))

    @jsii.member(jsii_name="resetDataFileSizeMb")
    def reset_data_file_size_mb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataFileSizeMb", []))

    @jsii.member(jsii_name="resetLogFileGrowthMb")
    def reset_log_file_growth_mb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogFileGrowthMb", []))

    @jsii.member(jsii_name="resetLogFileSizeMb")
    def reset_log_file_size_mb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogFileSizeMb", []))

    @builtins.property
    @jsii.member(jsii_name="dataFileCountInput")
    def data_file_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dataFileCountInput"))

    @builtins.property
    @jsii.member(jsii_name="dataFileGrowthInMbInput")
    def data_file_growth_in_mb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dataFileGrowthInMbInput"))

    @builtins.property
    @jsii.member(jsii_name="dataFileSizeMbInput")
    def data_file_size_mb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dataFileSizeMbInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultFilePathInput")
    def default_file_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultFilePathInput"))

    @builtins.property
    @jsii.member(jsii_name="logFileGrowthMbInput")
    def log_file_growth_mb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "logFileGrowthMbInput"))

    @builtins.property
    @jsii.member(jsii_name="logFileSizeMbInput")
    def log_file_size_mb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "logFileSizeMbInput"))

    @builtins.property
    @jsii.member(jsii_name="lunsInput")
    def luns_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "lunsInput"))

    @builtins.property
    @jsii.member(jsii_name="dataFileCount")
    def data_file_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dataFileCount"))

    @data_file_count.setter
    def data_file_count(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataFileCount", value)

    @builtins.property
    @jsii.member(jsii_name="dataFileGrowthInMb")
    def data_file_growth_in_mb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dataFileGrowthInMb"))

    @data_file_growth_in_mb.setter
    def data_file_growth_in_mb(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataFileGrowthInMb", value)

    @builtins.property
    @jsii.member(jsii_name="dataFileSizeMb")
    def data_file_size_mb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dataFileSizeMb"))

    @data_file_size_mb.setter
    def data_file_size_mb(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataFileSizeMb", value)

    @builtins.property
    @jsii.member(jsii_name="defaultFilePath")
    def default_file_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultFilePath"))

    @default_file_path.setter
    def default_file_path(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultFilePath", value)

    @builtins.property
    @jsii.member(jsii_name="logFileGrowthMb")
    def log_file_growth_mb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "logFileGrowthMb"))

    @log_file_growth_mb.setter
    def log_file_growth_mb(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logFileGrowthMb", value)

    @builtins.property
    @jsii.member(jsii_name="logFileSizeMb")
    def log_file_size_mb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "logFileSizeMb"))

    @log_file_size_mb.setter
    def log_file_size_mb(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logFileSizeMb", value)

    @builtins.property
    @jsii.member(jsii_name="luns")
    def luns(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "luns"))

    @luns.setter
    def luns(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            def stub(value: typing.List[jsii.Number]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "luns", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MssqlVirtualMachineStorageConfigurationTempDbSettings]:
        return typing.cast(typing.Optional[MssqlVirtualMachineStorageConfigurationTempDbSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MssqlVirtualMachineStorageConfigurationTempDbSettings],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MssqlVirtualMachineStorageConfigurationTempDbSettings],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlVirtualMachine.MssqlVirtualMachineTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class MssqlVirtualMachineTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#create MssqlVirtualMachine#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#delete MssqlVirtualMachine#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#read MssqlVirtualMachine#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#update MssqlVirtualMachine#update}.
        '''
        if __debug__:
            def stub(
                *,
                create: typing.Optional[builtins.str] = None,
                delete: typing.Optional[builtins.str] = None,
                read: typing.Optional[builtins.str] = None,
                update: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#create MssqlVirtualMachine#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#delete MssqlVirtualMachine#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#read MssqlVirtualMachine#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_virtual_machine#update MssqlVirtualMachine#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlVirtualMachineTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MssqlVirtualMachineTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlVirtualMachine.MssqlVirtualMachineTimeoutsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MssqlVirtualMachineTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MssqlVirtualMachineTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MssqlVirtualMachineTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[MssqlVirtualMachineTimeouts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MssqlVirtualMachine",
    "MssqlVirtualMachineAssessment",
    "MssqlVirtualMachineAssessmentOutputReference",
    "MssqlVirtualMachineAssessmentSchedule",
    "MssqlVirtualMachineAssessmentScheduleOutputReference",
    "MssqlVirtualMachineAutoBackup",
    "MssqlVirtualMachineAutoBackupManualSchedule",
    "MssqlVirtualMachineAutoBackupManualScheduleOutputReference",
    "MssqlVirtualMachineAutoBackupOutputReference",
    "MssqlVirtualMachineAutoPatching",
    "MssqlVirtualMachineAutoPatchingOutputReference",
    "MssqlVirtualMachineConfig",
    "MssqlVirtualMachineKeyVaultCredential",
    "MssqlVirtualMachineKeyVaultCredentialOutputReference",
    "MssqlVirtualMachineSqlInstance",
    "MssqlVirtualMachineSqlInstanceOutputReference",
    "MssqlVirtualMachineStorageConfiguration",
    "MssqlVirtualMachineStorageConfigurationDataSettings",
    "MssqlVirtualMachineStorageConfigurationDataSettingsOutputReference",
    "MssqlVirtualMachineStorageConfigurationLogSettings",
    "MssqlVirtualMachineStorageConfigurationLogSettingsOutputReference",
    "MssqlVirtualMachineStorageConfigurationOutputReference",
    "MssqlVirtualMachineStorageConfigurationTempDbSettings",
    "MssqlVirtualMachineStorageConfigurationTempDbSettingsOutputReference",
    "MssqlVirtualMachineTimeouts",
    "MssqlVirtualMachineTimeoutsOutputReference",
]

publication.publish()
