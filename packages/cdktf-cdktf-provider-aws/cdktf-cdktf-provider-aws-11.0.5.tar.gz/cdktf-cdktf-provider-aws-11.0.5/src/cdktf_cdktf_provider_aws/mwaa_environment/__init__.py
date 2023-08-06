'''
# `aws_mwaa_environment`

Refer to the Terraform Registory for docs: [`aws_mwaa_environment`](https://www.terraform.io/docs/providers/aws/r/mwaa_environment).
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


class MwaaEnvironment(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mwaaEnvironment.MwaaEnvironment",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment aws_mwaa_environment}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        dag_s3_path: builtins.str,
        execution_role_arn: builtins.str,
        name: builtins.str,
        network_configuration: typing.Union["MwaaEnvironmentNetworkConfiguration", typing.Dict[str, typing.Any]],
        source_bucket_arn: builtins.str,
        airflow_configuration_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        airflow_version: typing.Optional[builtins.str] = None,
        environment_class: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kms_key: typing.Optional[builtins.str] = None,
        logging_configuration: typing.Optional[typing.Union["MwaaEnvironmentLoggingConfiguration", typing.Dict[str, typing.Any]]] = None,
        max_workers: typing.Optional[jsii.Number] = None,
        min_workers: typing.Optional[jsii.Number] = None,
        plugins_s3_object_version: typing.Optional[builtins.str] = None,
        plugins_s3_path: typing.Optional[builtins.str] = None,
        requirements_s3_object_version: typing.Optional[builtins.str] = None,
        requirements_s3_path: typing.Optional[builtins.str] = None,
        schedulers: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["MwaaEnvironmentTimeouts", typing.Dict[str, typing.Any]]] = None,
        webserver_access_mode: typing.Optional[builtins.str] = None,
        weekly_maintenance_window_start: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment aws_mwaa_environment} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param dag_s3_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#dag_s3_path MwaaEnvironment#dag_s3_path}.
        :param execution_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#execution_role_arn MwaaEnvironment#execution_role_arn}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#name MwaaEnvironment#name}.
        :param network_configuration: network_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#network_configuration MwaaEnvironment#network_configuration}
        :param source_bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#source_bucket_arn MwaaEnvironment#source_bucket_arn}.
        :param airflow_configuration_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#airflow_configuration_options MwaaEnvironment#airflow_configuration_options}.
        :param airflow_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#airflow_version MwaaEnvironment#airflow_version}.
        :param environment_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#environment_class MwaaEnvironment#environment_class}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#id MwaaEnvironment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#kms_key MwaaEnvironment#kms_key}.
        :param logging_configuration: logging_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#logging_configuration MwaaEnvironment#logging_configuration}
        :param max_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#max_workers MwaaEnvironment#max_workers}.
        :param min_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#min_workers MwaaEnvironment#min_workers}.
        :param plugins_s3_object_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#plugins_s3_object_version MwaaEnvironment#plugins_s3_object_version}.
        :param plugins_s3_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#plugins_s3_path MwaaEnvironment#plugins_s3_path}.
        :param requirements_s3_object_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#requirements_s3_object_version MwaaEnvironment#requirements_s3_object_version}.
        :param requirements_s3_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#requirements_s3_path MwaaEnvironment#requirements_s3_path}.
        :param schedulers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#schedulers MwaaEnvironment#schedulers}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#tags MwaaEnvironment#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#tags_all MwaaEnvironment#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#timeouts MwaaEnvironment#timeouts}
        :param webserver_access_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#webserver_access_mode MwaaEnvironment#webserver_access_mode}.
        :param weekly_maintenance_window_start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#weekly_maintenance_window_start MwaaEnvironment#weekly_maintenance_window_start}.
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
                dag_s3_path: builtins.str,
                execution_role_arn: builtins.str,
                name: builtins.str,
                network_configuration: typing.Union[MwaaEnvironmentNetworkConfiguration, typing.Dict[str, typing.Any]],
                source_bucket_arn: builtins.str,
                airflow_configuration_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                airflow_version: typing.Optional[builtins.str] = None,
                environment_class: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                kms_key: typing.Optional[builtins.str] = None,
                logging_configuration: typing.Optional[typing.Union[MwaaEnvironmentLoggingConfiguration, typing.Dict[str, typing.Any]]] = None,
                max_workers: typing.Optional[jsii.Number] = None,
                min_workers: typing.Optional[jsii.Number] = None,
                plugins_s3_object_version: typing.Optional[builtins.str] = None,
                plugins_s3_path: typing.Optional[builtins.str] = None,
                requirements_s3_object_version: typing.Optional[builtins.str] = None,
                requirements_s3_path: typing.Optional[builtins.str] = None,
                schedulers: typing.Optional[jsii.Number] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[MwaaEnvironmentTimeouts, typing.Dict[str, typing.Any]]] = None,
                webserver_access_mode: typing.Optional[builtins.str] = None,
                weekly_maintenance_window_start: typing.Optional[builtins.str] = None,
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
        config = MwaaEnvironmentConfig(
            dag_s3_path=dag_s3_path,
            execution_role_arn=execution_role_arn,
            name=name,
            network_configuration=network_configuration,
            source_bucket_arn=source_bucket_arn,
            airflow_configuration_options=airflow_configuration_options,
            airflow_version=airflow_version,
            environment_class=environment_class,
            id=id,
            kms_key=kms_key,
            logging_configuration=logging_configuration,
            max_workers=max_workers,
            min_workers=min_workers,
            plugins_s3_object_version=plugins_s3_object_version,
            plugins_s3_path=plugins_s3_path,
            requirements_s3_object_version=requirements_s3_object_version,
            requirements_s3_path=requirements_s3_path,
            schedulers=schedulers,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            webserver_access_mode=webserver_access_mode,
            weekly_maintenance_window_start=weekly_maintenance_window_start,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putLoggingConfiguration")
    def put_logging_configuration(
        self,
        *,
        dag_processing_logs: typing.Optional[typing.Union["MwaaEnvironmentLoggingConfigurationDagProcessingLogs", typing.Dict[str, typing.Any]]] = None,
        scheduler_logs: typing.Optional[typing.Union["MwaaEnvironmentLoggingConfigurationSchedulerLogs", typing.Dict[str, typing.Any]]] = None,
        task_logs: typing.Optional[typing.Union["MwaaEnvironmentLoggingConfigurationTaskLogs", typing.Dict[str, typing.Any]]] = None,
        webserver_logs: typing.Optional[typing.Union["MwaaEnvironmentLoggingConfigurationWebserverLogs", typing.Dict[str, typing.Any]]] = None,
        worker_logs: typing.Optional[typing.Union["MwaaEnvironmentLoggingConfigurationWorkerLogs", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param dag_processing_logs: dag_processing_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#dag_processing_logs MwaaEnvironment#dag_processing_logs}
        :param scheduler_logs: scheduler_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#scheduler_logs MwaaEnvironment#scheduler_logs}
        :param task_logs: task_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#task_logs MwaaEnvironment#task_logs}
        :param webserver_logs: webserver_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#webserver_logs MwaaEnvironment#webserver_logs}
        :param worker_logs: worker_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#worker_logs MwaaEnvironment#worker_logs}
        '''
        value = MwaaEnvironmentLoggingConfiguration(
            dag_processing_logs=dag_processing_logs,
            scheduler_logs=scheduler_logs,
            task_logs=task_logs,
            webserver_logs=webserver_logs,
            worker_logs=worker_logs,
        )

        return typing.cast(None, jsii.invoke(self, "putLoggingConfiguration", [value]))

    @jsii.member(jsii_name="putNetworkConfiguration")
    def put_network_configuration(
        self,
        *,
        security_group_ids: typing.Sequence[builtins.str],
        subnet_ids: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#security_group_ids MwaaEnvironment#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#subnet_ids MwaaEnvironment#subnet_ids}.
        '''
        value = MwaaEnvironmentNetworkConfiguration(
            security_group_ids=security_group_ids, subnet_ids=subnet_ids
        )

        return typing.cast(None, jsii.invoke(self, "putNetworkConfiguration", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#create MwaaEnvironment#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#delete MwaaEnvironment#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#update MwaaEnvironment#update}.
        '''
        value = MwaaEnvironmentTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAirflowConfigurationOptions")
    def reset_airflow_configuration_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAirflowConfigurationOptions", []))

    @jsii.member(jsii_name="resetAirflowVersion")
    def reset_airflow_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAirflowVersion", []))

    @jsii.member(jsii_name="resetEnvironmentClass")
    def reset_environment_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironmentClass", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKmsKey")
    def reset_kms_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKey", []))

    @jsii.member(jsii_name="resetLoggingConfiguration")
    def reset_logging_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoggingConfiguration", []))

    @jsii.member(jsii_name="resetMaxWorkers")
    def reset_max_workers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxWorkers", []))

    @jsii.member(jsii_name="resetMinWorkers")
    def reset_min_workers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinWorkers", []))

    @jsii.member(jsii_name="resetPluginsS3ObjectVersion")
    def reset_plugins_s3_object_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPluginsS3ObjectVersion", []))

    @jsii.member(jsii_name="resetPluginsS3Path")
    def reset_plugins_s3_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPluginsS3Path", []))

    @jsii.member(jsii_name="resetRequirementsS3ObjectVersion")
    def reset_requirements_s3_object_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequirementsS3ObjectVersion", []))

    @jsii.member(jsii_name="resetRequirementsS3Path")
    def reset_requirements_s3_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequirementsS3Path", []))

    @jsii.member(jsii_name="resetSchedulers")
    def reset_schedulers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedulers", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetWebserverAccessMode")
    def reset_webserver_access_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebserverAccessMode", []))

    @jsii.member(jsii_name="resetWeeklyMaintenanceWindowStart")
    def reset_weekly_maintenance_window_start(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeeklyMaintenanceWindowStart", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAt"))

    @builtins.property
    @jsii.member(jsii_name="lastUpdated")
    def last_updated(self) -> "MwaaEnvironmentLastUpdatedList":
        return typing.cast("MwaaEnvironmentLastUpdatedList", jsii.get(self, "lastUpdated"))

    @builtins.property
    @jsii.member(jsii_name="loggingConfiguration")
    def logging_configuration(
        self,
    ) -> "MwaaEnvironmentLoggingConfigurationOutputReference":
        return typing.cast("MwaaEnvironmentLoggingConfigurationOutputReference", jsii.get(self, "loggingConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(
        self,
    ) -> "MwaaEnvironmentNetworkConfigurationOutputReference":
        return typing.cast("MwaaEnvironmentNetworkConfigurationOutputReference", jsii.get(self, "networkConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="serviceRoleArn")
    def service_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceRoleArn"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MwaaEnvironmentTimeoutsOutputReference":
        return typing.cast("MwaaEnvironmentTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="webserverUrl")
    def webserver_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webserverUrl"))

    @builtins.property
    @jsii.member(jsii_name="airflowConfigurationOptionsInput")
    def airflow_configuration_options_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "airflowConfigurationOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="airflowVersionInput")
    def airflow_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "airflowVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="dagS3PathInput")
    def dag_s3_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dagS3PathInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentClassInput")
    def environment_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentClassInput"))

    @builtins.property
    @jsii.member(jsii_name="executionRoleArnInput")
    def execution_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyInput")
    def kms_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingConfigurationInput")
    def logging_configuration_input(
        self,
    ) -> typing.Optional["MwaaEnvironmentLoggingConfiguration"]:
        return typing.cast(typing.Optional["MwaaEnvironmentLoggingConfiguration"], jsii.get(self, "loggingConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="maxWorkersInput")
    def max_workers_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxWorkersInput"))

    @builtins.property
    @jsii.member(jsii_name="minWorkersInput")
    def min_workers_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minWorkersInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkConfigurationInput")
    def network_configuration_input(
        self,
    ) -> typing.Optional["MwaaEnvironmentNetworkConfiguration"]:
        return typing.cast(typing.Optional["MwaaEnvironmentNetworkConfiguration"], jsii.get(self, "networkConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="pluginsS3ObjectVersionInput")
    def plugins_s3_object_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginsS3ObjectVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="pluginsS3PathInput")
    def plugins_s3_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginsS3PathInput"))

    @builtins.property
    @jsii.member(jsii_name="requirementsS3ObjectVersionInput")
    def requirements_s3_object_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requirementsS3ObjectVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="requirementsS3PathInput")
    def requirements_s3_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requirementsS3PathInput"))

    @builtins.property
    @jsii.member(jsii_name="schedulersInput")
    def schedulers_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "schedulersInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceBucketArnInput")
    def source_bucket_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceBucketArnInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MwaaEnvironmentTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MwaaEnvironmentTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="webserverAccessModeInput")
    def webserver_access_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "webserverAccessModeInput"))

    @builtins.property
    @jsii.member(jsii_name="weeklyMaintenanceWindowStartInput")
    def weekly_maintenance_window_start_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "weeklyMaintenanceWindowStartInput"))

    @builtins.property
    @jsii.member(jsii_name="airflowConfigurationOptions")
    def airflow_configuration_options(
        self,
    ) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "airflowConfigurationOptions"))

    @airflow_configuration_options.setter
    def airflow_configuration_options(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "airflowConfigurationOptions", value)

    @builtins.property
    @jsii.member(jsii_name="airflowVersion")
    def airflow_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "airflowVersion"))

    @airflow_version.setter
    def airflow_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "airflowVersion", value)

    @builtins.property
    @jsii.member(jsii_name="dagS3Path")
    def dag_s3_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dagS3Path"))

    @dag_s3_path.setter
    def dag_s3_path(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dagS3Path", value)

    @builtins.property
    @jsii.member(jsii_name="environmentClass")
    def environment_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "environmentClass"))

    @environment_class.setter
    def environment_class(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentClass", value)

    @builtins.property
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleArn", value)

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
    @jsii.member(jsii_name="kmsKey")
    def kms_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKey"))

    @kms_key.setter
    def kms_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKey", value)

    @builtins.property
    @jsii.member(jsii_name="maxWorkers")
    def max_workers(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxWorkers"))

    @max_workers.setter
    def max_workers(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="minWorkers")
    def min_workers(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minWorkers"))

    @min_workers.setter
    def min_workers(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minWorkers", value)

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
    @jsii.member(jsii_name="pluginsS3ObjectVersion")
    def plugins_s3_object_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pluginsS3ObjectVersion"))

    @plugins_s3_object_version.setter
    def plugins_s3_object_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginsS3ObjectVersion", value)

    @builtins.property
    @jsii.member(jsii_name="pluginsS3Path")
    def plugins_s3_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pluginsS3Path"))

    @plugins_s3_path.setter
    def plugins_s3_path(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginsS3Path", value)

    @builtins.property
    @jsii.member(jsii_name="requirementsS3ObjectVersion")
    def requirements_s3_object_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "requirementsS3ObjectVersion"))

    @requirements_s3_object_version.setter
    def requirements_s3_object_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requirementsS3ObjectVersion", value)

    @builtins.property
    @jsii.member(jsii_name="requirementsS3Path")
    def requirements_s3_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "requirementsS3Path"))

    @requirements_s3_path.setter
    def requirements_s3_path(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requirementsS3Path", value)

    @builtins.property
    @jsii.member(jsii_name="schedulers")
    def schedulers(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "schedulers"))

    @schedulers.setter
    def schedulers(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedulers", value)

    @builtins.property
    @jsii.member(jsii_name="sourceBucketArn")
    def source_bucket_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceBucketArn"))

    @source_bucket_arn.setter
    def source_bucket_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceBucketArn", value)

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
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="webserverAccessMode")
    def webserver_access_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webserverAccessMode"))

    @webserver_access_mode.setter
    def webserver_access_mode(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "webserverAccessMode", value)

    @builtins.property
    @jsii.member(jsii_name="weeklyMaintenanceWindowStart")
    def weekly_maintenance_window_start(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "weeklyMaintenanceWindowStart"))

    @weekly_maintenance_window_start.setter
    def weekly_maintenance_window_start(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weeklyMaintenanceWindowStart", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mwaaEnvironment.MwaaEnvironmentConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "dag_s3_path": "dagS3Path",
        "execution_role_arn": "executionRoleArn",
        "name": "name",
        "network_configuration": "networkConfiguration",
        "source_bucket_arn": "sourceBucketArn",
        "airflow_configuration_options": "airflowConfigurationOptions",
        "airflow_version": "airflowVersion",
        "environment_class": "environmentClass",
        "id": "id",
        "kms_key": "kmsKey",
        "logging_configuration": "loggingConfiguration",
        "max_workers": "maxWorkers",
        "min_workers": "minWorkers",
        "plugins_s3_object_version": "pluginsS3ObjectVersion",
        "plugins_s3_path": "pluginsS3Path",
        "requirements_s3_object_version": "requirementsS3ObjectVersion",
        "requirements_s3_path": "requirementsS3Path",
        "schedulers": "schedulers",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
        "webserver_access_mode": "webserverAccessMode",
        "weekly_maintenance_window_start": "weeklyMaintenanceWindowStart",
    },
)
class MwaaEnvironmentConfig(cdktf.TerraformMetaArguments):
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
        dag_s3_path: builtins.str,
        execution_role_arn: builtins.str,
        name: builtins.str,
        network_configuration: typing.Union["MwaaEnvironmentNetworkConfiguration", typing.Dict[str, typing.Any]],
        source_bucket_arn: builtins.str,
        airflow_configuration_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        airflow_version: typing.Optional[builtins.str] = None,
        environment_class: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kms_key: typing.Optional[builtins.str] = None,
        logging_configuration: typing.Optional[typing.Union["MwaaEnvironmentLoggingConfiguration", typing.Dict[str, typing.Any]]] = None,
        max_workers: typing.Optional[jsii.Number] = None,
        min_workers: typing.Optional[jsii.Number] = None,
        plugins_s3_object_version: typing.Optional[builtins.str] = None,
        plugins_s3_path: typing.Optional[builtins.str] = None,
        requirements_s3_object_version: typing.Optional[builtins.str] = None,
        requirements_s3_path: typing.Optional[builtins.str] = None,
        schedulers: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["MwaaEnvironmentTimeouts", typing.Dict[str, typing.Any]]] = None,
        webserver_access_mode: typing.Optional[builtins.str] = None,
        weekly_maintenance_window_start: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param dag_s3_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#dag_s3_path MwaaEnvironment#dag_s3_path}.
        :param execution_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#execution_role_arn MwaaEnvironment#execution_role_arn}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#name MwaaEnvironment#name}.
        :param network_configuration: network_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#network_configuration MwaaEnvironment#network_configuration}
        :param source_bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#source_bucket_arn MwaaEnvironment#source_bucket_arn}.
        :param airflow_configuration_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#airflow_configuration_options MwaaEnvironment#airflow_configuration_options}.
        :param airflow_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#airflow_version MwaaEnvironment#airflow_version}.
        :param environment_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#environment_class MwaaEnvironment#environment_class}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#id MwaaEnvironment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#kms_key MwaaEnvironment#kms_key}.
        :param logging_configuration: logging_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#logging_configuration MwaaEnvironment#logging_configuration}
        :param max_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#max_workers MwaaEnvironment#max_workers}.
        :param min_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#min_workers MwaaEnvironment#min_workers}.
        :param plugins_s3_object_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#plugins_s3_object_version MwaaEnvironment#plugins_s3_object_version}.
        :param plugins_s3_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#plugins_s3_path MwaaEnvironment#plugins_s3_path}.
        :param requirements_s3_object_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#requirements_s3_object_version MwaaEnvironment#requirements_s3_object_version}.
        :param requirements_s3_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#requirements_s3_path MwaaEnvironment#requirements_s3_path}.
        :param schedulers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#schedulers MwaaEnvironment#schedulers}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#tags MwaaEnvironment#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#tags_all MwaaEnvironment#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#timeouts MwaaEnvironment#timeouts}
        :param webserver_access_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#webserver_access_mode MwaaEnvironment#webserver_access_mode}.
        :param weekly_maintenance_window_start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#weekly_maintenance_window_start MwaaEnvironment#weekly_maintenance_window_start}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(network_configuration, dict):
            network_configuration = MwaaEnvironmentNetworkConfiguration(**network_configuration)
        if isinstance(logging_configuration, dict):
            logging_configuration = MwaaEnvironmentLoggingConfiguration(**logging_configuration)
        if isinstance(timeouts, dict):
            timeouts = MwaaEnvironmentTimeouts(**timeouts)
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
                dag_s3_path: builtins.str,
                execution_role_arn: builtins.str,
                name: builtins.str,
                network_configuration: typing.Union[MwaaEnvironmentNetworkConfiguration, typing.Dict[str, typing.Any]],
                source_bucket_arn: builtins.str,
                airflow_configuration_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                airflow_version: typing.Optional[builtins.str] = None,
                environment_class: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                kms_key: typing.Optional[builtins.str] = None,
                logging_configuration: typing.Optional[typing.Union[MwaaEnvironmentLoggingConfiguration, typing.Dict[str, typing.Any]]] = None,
                max_workers: typing.Optional[jsii.Number] = None,
                min_workers: typing.Optional[jsii.Number] = None,
                plugins_s3_object_version: typing.Optional[builtins.str] = None,
                plugins_s3_path: typing.Optional[builtins.str] = None,
                requirements_s3_object_version: typing.Optional[builtins.str] = None,
                requirements_s3_path: typing.Optional[builtins.str] = None,
                schedulers: typing.Optional[jsii.Number] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[MwaaEnvironmentTimeouts, typing.Dict[str, typing.Any]]] = None,
                webserver_access_mode: typing.Optional[builtins.str] = None,
                weekly_maintenance_window_start: typing.Optional[builtins.str] = None,
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
            check_type(argname="argument dag_s3_path", value=dag_s3_path, expected_type=type_hints["dag_s3_path"])
            check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
            check_type(argname="argument source_bucket_arn", value=source_bucket_arn, expected_type=type_hints["source_bucket_arn"])
            check_type(argname="argument airflow_configuration_options", value=airflow_configuration_options, expected_type=type_hints["airflow_configuration_options"])
            check_type(argname="argument airflow_version", value=airflow_version, expected_type=type_hints["airflow_version"])
            check_type(argname="argument environment_class", value=environment_class, expected_type=type_hints["environment_class"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            check_type(argname="argument logging_configuration", value=logging_configuration, expected_type=type_hints["logging_configuration"])
            check_type(argname="argument max_workers", value=max_workers, expected_type=type_hints["max_workers"])
            check_type(argname="argument min_workers", value=min_workers, expected_type=type_hints["min_workers"])
            check_type(argname="argument plugins_s3_object_version", value=plugins_s3_object_version, expected_type=type_hints["plugins_s3_object_version"])
            check_type(argname="argument plugins_s3_path", value=plugins_s3_path, expected_type=type_hints["plugins_s3_path"])
            check_type(argname="argument requirements_s3_object_version", value=requirements_s3_object_version, expected_type=type_hints["requirements_s3_object_version"])
            check_type(argname="argument requirements_s3_path", value=requirements_s3_path, expected_type=type_hints["requirements_s3_path"])
            check_type(argname="argument schedulers", value=schedulers, expected_type=type_hints["schedulers"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument webserver_access_mode", value=webserver_access_mode, expected_type=type_hints["webserver_access_mode"])
            check_type(argname="argument weekly_maintenance_window_start", value=weekly_maintenance_window_start, expected_type=type_hints["weekly_maintenance_window_start"])
        self._values: typing.Dict[str, typing.Any] = {
            "dag_s3_path": dag_s3_path,
            "execution_role_arn": execution_role_arn,
            "name": name,
            "network_configuration": network_configuration,
            "source_bucket_arn": source_bucket_arn,
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
        if airflow_configuration_options is not None:
            self._values["airflow_configuration_options"] = airflow_configuration_options
        if airflow_version is not None:
            self._values["airflow_version"] = airflow_version
        if environment_class is not None:
            self._values["environment_class"] = environment_class
        if id is not None:
            self._values["id"] = id
        if kms_key is not None:
            self._values["kms_key"] = kms_key
        if logging_configuration is not None:
            self._values["logging_configuration"] = logging_configuration
        if max_workers is not None:
            self._values["max_workers"] = max_workers
        if min_workers is not None:
            self._values["min_workers"] = min_workers
        if plugins_s3_object_version is not None:
            self._values["plugins_s3_object_version"] = plugins_s3_object_version
        if plugins_s3_path is not None:
            self._values["plugins_s3_path"] = plugins_s3_path
        if requirements_s3_object_version is not None:
            self._values["requirements_s3_object_version"] = requirements_s3_object_version
        if requirements_s3_path is not None:
            self._values["requirements_s3_path"] = requirements_s3_path
        if schedulers is not None:
            self._values["schedulers"] = schedulers
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if webserver_access_mode is not None:
            self._values["webserver_access_mode"] = webserver_access_mode
        if weekly_maintenance_window_start is not None:
            self._values["weekly_maintenance_window_start"] = weekly_maintenance_window_start

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
    def dag_s3_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#dag_s3_path MwaaEnvironment#dag_s3_path}.'''
        result = self._values.get("dag_s3_path")
        assert result is not None, "Required property 'dag_s3_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def execution_role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#execution_role_arn MwaaEnvironment#execution_role_arn}.'''
        result = self._values.get("execution_role_arn")
        assert result is not None, "Required property 'execution_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#name MwaaEnvironment#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_configuration(self) -> "MwaaEnvironmentNetworkConfiguration":
        '''network_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#network_configuration MwaaEnvironment#network_configuration}
        '''
        result = self._values.get("network_configuration")
        assert result is not None, "Required property 'network_configuration' is missing"
        return typing.cast("MwaaEnvironmentNetworkConfiguration", result)

    @builtins.property
    def source_bucket_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#source_bucket_arn MwaaEnvironment#source_bucket_arn}.'''
        result = self._values.get("source_bucket_arn")
        assert result is not None, "Required property 'source_bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def airflow_configuration_options(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#airflow_configuration_options MwaaEnvironment#airflow_configuration_options}.'''
        result = self._values.get("airflow_configuration_options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def airflow_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#airflow_version MwaaEnvironment#airflow_version}.'''
        result = self._values.get("airflow_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_class(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#environment_class MwaaEnvironment#environment_class}.'''
        result = self._values.get("environment_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#id MwaaEnvironment#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#kms_key MwaaEnvironment#kms_key}.'''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_configuration(
        self,
    ) -> typing.Optional["MwaaEnvironmentLoggingConfiguration"]:
        '''logging_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#logging_configuration MwaaEnvironment#logging_configuration}
        '''
        result = self._values.get("logging_configuration")
        return typing.cast(typing.Optional["MwaaEnvironmentLoggingConfiguration"], result)

    @builtins.property
    def max_workers(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#max_workers MwaaEnvironment#max_workers}.'''
        result = self._values.get("max_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_workers(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#min_workers MwaaEnvironment#min_workers}.'''
        result = self._values.get("min_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def plugins_s3_object_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#plugins_s3_object_version MwaaEnvironment#plugins_s3_object_version}.'''
        result = self._values.get("plugins_s3_object_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plugins_s3_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#plugins_s3_path MwaaEnvironment#plugins_s3_path}.'''
        result = self._values.get("plugins_s3_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def requirements_s3_object_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#requirements_s3_object_version MwaaEnvironment#requirements_s3_object_version}.'''
        result = self._values.get("requirements_s3_object_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def requirements_s3_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#requirements_s3_path MwaaEnvironment#requirements_s3_path}.'''
        result = self._values.get("requirements_s3_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedulers(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#schedulers MwaaEnvironment#schedulers}.'''
        result = self._values.get("schedulers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#tags MwaaEnvironment#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#tags_all MwaaEnvironment#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MwaaEnvironmentTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#timeouts MwaaEnvironment#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MwaaEnvironmentTimeouts"], result)

    @builtins.property
    def webserver_access_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#webserver_access_mode MwaaEnvironment#webserver_access_mode}.'''
        result = self._values.get("webserver_access_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def weekly_maintenance_window_start(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#weekly_maintenance_window_start MwaaEnvironment#weekly_maintenance_window_start}.'''
        result = self._values.get("weekly_maintenance_window_start")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwaaEnvironmentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mwaaEnvironment.MwaaEnvironmentLastUpdated",
    jsii_struct_bases=[],
    name_mapping={},
)
class MwaaEnvironmentLastUpdated:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwaaEnvironmentLastUpdated(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mwaaEnvironment.MwaaEnvironmentLastUpdatedError",
    jsii_struct_bases=[],
    name_mapping={},
)
class MwaaEnvironmentLastUpdatedError:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwaaEnvironmentLastUpdatedError(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MwaaEnvironmentLastUpdatedErrorList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mwaaEnvironment.MwaaEnvironmentLastUpdatedErrorList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                wraps_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MwaaEnvironmentLastUpdatedErrorOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MwaaEnvironmentLastUpdatedErrorOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            def stub(value: cdktf.IInterpolatingParent) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            def stub(value: builtins.bool) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class MwaaEnvironmentLastUpdatedErrorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mwaaEnvironment.MwaaEnvironmentLastUpdatedErrorOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                complex_object_index: jsii.Number,
                complex_object_is_from_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="errorCode")
    def error_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorCode"))

    @builtins.property
    @jsii.member(jsii_name="errorMessage")
    def error_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorMessage"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MwaaEnvironmentLastUpdatedError]:
        return typing.cast(typing.Optional[MwaaEnvironmentLastUpdatedError], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MwaaEnvironmentLastUpdatedError],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[MwaaEnvironmentLastUpdatedError]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MwaaEnvironmentLastUpdatedList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mwaaEnvironment.MwaaEnvironmentLastUpdatedList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                wraps_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "MwaaEnvironmentLastUpdatedOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MwaaEnvironmentLastUpdatedOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            def stub(value: cdktf.IInterpolatingParent) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            def stub(value: builtins.bool) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class MwaaEnvironmentLastUpdatedOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mwaaEnvironment.MwaaEnvironmentLastUpdatedOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                complex_object_index: jsii.Number,
                complex_object_is_from_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAt"))

    @builtins.property
    @jsii.member(jsii_name="error")
    def error(self) -> MwaaEnvironmentLastUpdatedErrorList:
        return typing.cast(MwaaEnvironmentLastUpdatedErrorList, jsii.get(self, "error"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MwaaEnvironmentLastUpdated]:
        return typing.cast(typing.Optional[MwaaEnvironmentLastUpdated], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MwaaEnvironmentLastUpdated],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[MwaaEnvironmentLastUpdated]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mwaaEnvironment.MwaaEnvironmentLoggingConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "dag_processing_logs": "dagProcessingLogs",
        "scheduler_logs": "schedulerLogs",
        "task_logs": "taskLogs",
        "webserver_logs": "webserverLogs",
        "worker_logs": "workerLogs",
    },
)
class MwaaEnvironmentLoggingConfiguration:
    def __init__(
        self,
        *,
        dag_processing_logs: typing.Optional[typing.Union["MwaaEnvironmentLoggingConfigurationDagProcessingLogs", typing.Dict[str, typing.Any]]] = None,
        scheduler_logs: typing.Optional[typing.Union["MwaaEnvironmentLoggingConfigurationSchedulerLogs", typing.Dict[str, typing.Any]]] = None,
        task_logs: typing.Optional[typing.Union["MwaaEnvironmentLoggingConfigurationTaskLogs", typing.Dict[str, typing.Any]]] = None,
        webserver_logs: typing.Optional[typing.Union["MwaaEnvironmentLoggingConfigurationWebserverLogs", typing.Dict[str, typing.Any]]] = None,
        worker_logs: typing.Optional[typing.Union["MwaaEnvironmentLoggingConfigurationWorkerLogs", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param dag_processing_logs: dag_processing_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#dag_processing_logs MwaaEnvironment#dag_processing_logs}
        :param scheduler_logs: scheduler_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#scheduler_logs MwaaEnvironment#scheduler_logs}
        :param task_logs: task_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#task_logs MwaaEnvironment#task_logs}
        :param webserver_logs: webserver_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#webserver_logs MwaaEnvironment#webserver_logs}
        :param worker_logs: worker_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#worker_logs MwaaEnvironment#worker_logs}
        '''
        if isinstance(dag_processing_logs, dict):
            dag_processing_logs = MwaaEnvironmentLoggingConfigurationDagProcessingLogs(**dag_processing_logs)
        if isinstance(scheduler_logs, dict):
            scheduler_logs = MwaaEnvironmentLoggingConfigurationSchedulerLogs(**scheduler_logs)
        if isinstance(task_logs, dict):
            task_logs = MwaaEnvironmentLoggingConfigurationTaskLogs(**task_logs)
        if isinstance(webserver_logs, dict):
            webserver_logs = MwaaEnvironmentLoggingConfigurationWebserverLogs(**webserver_logs)
        if isinstance(worker_logs, dict):
            worker_logs = MwaaEnvironmentLoggingConfigurationWorkerLogs(**worker_logs)
        if __debug__:
            def stub(
                *,
                dag_processing_logs: typing.Optional[typing.Union[MwaaEnvironmentLoggingConfigurationDagProcessingLogs, typing.Dict[str, typing.Any]]] = None,
                scheduler_logs: typing.Optional[typing.Union[MwaaEnvironmentLoggingConfigurationSchedulerLogs, typing.Dict[str, typing.Any]]] = None,
                task_logs: typing.Optional[typing.Union[MwaaEnvironmentLoggingConfigurationTaskLogs, typing.Dict[str, typing.Any]]] = None,
                webserver_logs: typing.Optional[typing.Union[MwaaEnvironmentLoggingConfigurationWebserverLogs, typing.Dict[str, typing.Any]]] = None,
                worker_logs: typing.Optional[typing.Union[MwaaEnvironmentLoggingConfigurationWorkerLogs, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument dag_processing_logs", value=dag_processing_logs, expected_type=type_hints["dag_processing_logs"])
            check_type(argname="argument scheduler_logs", value=scheduler_logs, expected_type=type_hints["scheduler_logs"])
            check_type(argname="argument task_logs", value=task_logs, expected_type=type_hints["task_logs"])
            check_type(argname="argument webserver_logs", value=webserver_logs, expected_type=type_hints["webserver_logs"])
            check_type(argname="argument worker_logs", value=worker_logs, expected_type=type_hints["worker_logs"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dag_processing_logs is not None:
            self._values["dag_processing_logs"] = dag_processing_logs
        if scheduler_logs is not None:
            self._values["scheduler_logs"] = scheduler_logs
        if task_logs is not None:
            self._values["task_logs"] = task_logs
        if webserver_logs is not None:
            self._values["webserver_logs"] = webserver_logs
        if worker_logs is not None:
            self._values["worker_logs"] = worker_logs

    @builtins.property
    def dag_processing_logs(
        self,
    ) -> typing.Optional["MwaaEnvironmentLoggingConfigurationDagProcessingLogs"]:
        '''dag_processing_logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#dag_processing_logs MwaaEnvironment#dag_processing_logs}
        '''
        result = self._values.get("dag_processing_logs")
        return typing.cast(typing.Optional["MwaaEnvironmentLoggingConfigurationDagProcessingLogs"], result)

    @builtins.property
    def scheduler_logs(
        self,
    ) -> typing.Optional["MwaaEnvironmentLoggingConfigurationSchedulerLogs"]:
        '''scheduler_logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#scheduler_logs MwaaEnvironment#scheduler_logs}
        '''
        result = self._values.get("scheduler_logs")
        return typing.cast(typing.Optional["MwaaEnvironmentLoggingConfigurationSchedulerLogs"], result)

    @builtins.property
    def task_logs(
        self,
    ) -> typing.Optional["MwaaEnvironmentLoggingConfigurationTaskLogs"]:
        '''task_logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#task_logs MwaaEnvironment#task_logs}
        '''
        result = self._values.get("task_logs")
        return typing.cast(typing.Optional["MwaaEnvironmentLoggingConfigurationTaskLogs"], result)

    @builtins.property
    def webserver_logs(
        self,
    ) -> typing.Optional["MwaaEnvironmentLoggingConfigurationWebserverLogs"]:
        '''webserver_logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#webserver_logs MwaaEnvironment#webserver_logs}
        '''
        result = self._values.get("webserver_logs")
        return typing.cast(typing.Optional["MwaaEnvironmentLoggingConfigurationWebserverLogs"], result)

    @builtins.property
    def worker_logs(
        self,
    ) -> typing.Optional["MwaaEnvironmentLoggingConfigurationWorkerLogs"]:
        '''worker_logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#worker_logs MwaaEnvironment#worker_logs}
        '''
        result = self._values.get("worker_logs")
        return typing.cast(typing.Optional["MwaaEnvironmentLoggingConfigurationWorkerLogs"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwaaEnvironmentLoggingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mwaaEnvironment.MwaaEnvironmentLoggingConfigurationDagProcessingLogs",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "log_level": "logLevel"},
)
class MwaaEnvironmentLoggingConfigurationDagProcessingLogs:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#enabled MwaaEnvironment#enabled}.
        :param log_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#log_level MwaaEnvironment#log_level}.
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                log_level: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if log_level is not None:
            self._values["log_level"] = log_level

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#enabled MwaaEnvironment#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def log_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#log_level MwaaEnvironment#log_level}.'''
        result = self._values.get("log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwaaEnvironmentLoggingConfigurationDagProcessingLogs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MwaaEnvironmentLoggingConfigurationDagProcessingLogsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mwaaEnvironment.MwaaEnvironmentLoggingConfigurationDagProcessingLogsOutputReference",
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

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetLogLevel")
    def reset_log_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogLevel", []))

    @builtins.property
    @jsii.member(jsii_name="cloudWatchLogGroupArn")
    def cloud_watch_log_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudWatchLogGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logLevelInput")
    def log_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logLevelInput"))

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
    @jsii.member(jsii_name="logLevel")
    def log_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logLevel"))

    @log_level.setter
    def log_level(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logLevel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MwaaEnvironmentLoggingConfigurationDagProcessingLogs]:
        return typing.cast(typing.Optional[MwaaEnvironmentLoggingConfigurationDagProcessingLogs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MwaaEnvironmentLoggingConfigurationDagProcessingLogs],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MwaaEnvironmentLoggingConfigurationDagProcessingLogs],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MwaaEnvironmentLoggingConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mwaaEnvironment.MwaaEnvironmentLoggingConfigurationOutputReference",
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

    @jsii.member(jsii_name="putDagProcessingLogs")
    def put_dag_processing_logs(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#enabled MwaaEnvironment#enabled}.
        :param log_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#log_level MwaaEnvironment#log_level}.
        '''
        value = MwaaEnvironmentLoggingConfigurationDagProcessingLogs(
            enabled=enabled, log_level=log_level
        )

        return typing.cast(None, jsii.invoke(self, "putDagProcessingLogs", [value]))

    @jsii.member(jsii_name="putSchedulerLogs")
    def put_scheduler_logs(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#enabled MwaaEnvironment#enabled}.
        :param log_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#log_level MwaaEnvironment#log_level}.
        '''
        value = MwaaEnvironmentLoggingConfigurationSchedulerLogs(
            enabled=enabled, log_level=log_level
        )

        return typing.cast(None, jsii.invoke(self, "putSchedulerLogs", [value]))

    @jsii.member(jsii_name="putTaskLogs")
    def put_task_logs(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#enabled MwaaEnvironment#enabled}.
        :param log_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#log_level MwaaEnvironment#log_level}.
        '''
        value = MwaaEnvironmentLoggingConfigurationTaskLogs(
            enabled=enabled, log_level=log_level
        )

        return typing.cast(None, jsii.invoke(self, "putTaskLogs", [value]))

    @jsii.member(jsii_name="putWebserverLogs")
    def put_webserver_logs(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#enabled MwaaEnvironment#enabled}.
        :param log_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#log_level MwaaEnvironment#log_level}.
        '''
        value = MwaaEnvironmentLoggingConfigurationWebserverLogs(
            enabled=enabled, log_level=log_level
        )

        return typing.cast(None, jsii.invoke(self, "putWebserverLogs", [value]))

    @jsii.member(jsii_name="putWorkerLogs")
    def put_worker_logs(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#enabled MwaaEnvironment#enabled}.
        :param log_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#log_level MwaaEnvironment#log_level}.
        '''
        value = MwaaEnvironmentLoggingConfigurationWorkerLogs(
            enabled=enabled, log_level=log_level
        )

        return typing.cast(None, jsii.invoke(self, "putWorkerLogs", [value]))

    @jsii.member(jsii_name="resetDagProcessingLogs")
    def reset_dag_processing_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDagProcessingLogs", []))

    @jsii.member(jsii_name="resetSchedulerLogs")
    def reset_scheduler_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedulerLogs", []))

    @jsii.member(jsii_name="resetTaskLogs")
    def reset_task_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaskLogs", []))

    @jsii.member(jsii_name="resetWebserverLogs")
    def reset_webserver_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebserverLogs", []))

    @jsii.member(jsii_name="resetWorkerLogs")
    def reset_worker_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkerLogs", []))

    @builtins.property
    @jsii.member(jsii_name="dagProcessingLogs")
    def dag_processing_logs(
        self,
    ) -> MwaaEnvironmentLoggingConfigurationDagProcessingLogsOutputReference:
        return typing.cast(MwaaEnvironmentLoggingConfigurationDagProcessingLogsOutputReference, jsii.get(self, "dagProcessingLogs"))

    @builtins.property
    @jsii.member(jsii_name="schedulerLogs")
    def scheduler_logs(
        self,
    ) -> "MwaaEnvironmentLoggingConfigurationSchedulerLogsOutputReference":
        return typing.cast("MwaaEnvironmentLoggingConfigurationSchedulerLogsOutputReference", jsii.get(self, "schedulerLogs"))

    @builtins.property
    @jsii.member(jsii_name="taskLogs")
    def task_logs(self) -> "MwaaEnvironmentLoggingConfigurationTaskLogsOutputReference":
        return typing.cast("MwaaEnvironmentLoggingConfigurationTaskLogsOutputReference", jsii.get(self, "taskLogs"))

    @builtins.property
    @jsii.member(jsii_name="webserverLogs")
    def webserver_logs(
        self,
    ) -> "MwaaEnvironmentLoggingConfigurationWebserverLogsOutputReference":
        return typing.cast("MwaaEnvironmentLoggingConfigurationWebserverLogsOutputReference", jsii.get(self, "webserverLogs"))

    @builtins.property
    @jsii.member(jsii_name="workerLogs")
    def worker_logs(
        self,
    ) -> "MwaaEnvironmentLoggingConfigurationWorkerLogsOutputReference":
        return typing.cast("MwaaEnvironmentLoggingConfigurationWorkerLogsOutputReference", jsii.get(self, "workerLogs"))

    @builtins.property
    @jsii.member(jsii_name="dagProcessingLogsInput")
    def dag_processing_logs_input(
        self,
    ) -> typing.Optional[MwaaEnvironmentLoggingConfigurationDagProcessingLogs]:
        return typing.cast(typing.Optional[MwaaEnvironmentLoggingConfigurationDagProcessingLogs], jsii.get(self, "dagProcessingLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="schedulerLogsInput")
    def scheduler_logs_input(
        self,
    ) -> typing.Optional["MwaaEnvironmentLoggingConfigurationSchedulerLogs"]:
        return typing.cast(typing.Optional["MwaaEnvironmentLoggingConfigurationSchedulerLogs"], jsii.get(self, "schedulerLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="taskLogsInput")
    def task_logs_input(
        self,
    ) -> typing.Optional["MwaaEnvironmentLoggingConfigurationTaskLogs"]:
        return typing.cast(typing.Optional["MwaaEnvironmentLoggingConfigurationTaskLogs"], jsii.get(self, "taskLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="webserverLogsInput")
    def webserver_logs_input(
        self,
    ) -> typing.Optional["MwaaEnvironmentLoggingConfigurationWebserverLogs"]:
        return typing.cast(typing.Optional["MwaaEnvironmentLoggingConfigurationWebserverLogs"], jsii.get(self, "webserverLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="workerLogsInput")
    def worker_logs_input(
        self,
    ) -> typing.Optional["MwaaEnvironmentLoggingConfigurationWorkerLogs"]:
        return typing.cast(typing.Optional["MwaaEnvironmentLoggingConfigurationWorkerLogs"], jsii.get(self, "workerLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MwaaEnvironmentLoggingConfiguration]:
        return typing.cast(typing.Optional[MwaaEnvironmentLoggingConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MwaaEnvironmentLoggingConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MwaaEnvironmentLoggingConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mwaaEnvironment.MwaaEnvironmentLoggingConfigurationSchedulerLogs",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "log_level": "logLevel"},
)
class MwaaEnvironmentLoggingConfigurationSchedulerLogs:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#enabled MwaaEnvironment#enabled}.
        :param log_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#log_level MwaaEnvironment#log_level}.
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                log_level: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if log_level is not None:
            self._values["log_level"] = log_level

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#enabled MwaaEnvironment#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def log_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#log_level MwaaEnvironment#log_level}.'''
        result = self._values.get("log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwaaEnvironmentLoggingConfigurationSchedulerLogs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MwaaEnvironmentLoggingConfigurationSchedulerLogsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mwaaEnvironment.MwaaEnvironmentLoggingConfigurationSchedulerLogsOutputReference",
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

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetLogLevel")
    def reset_log_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogLevel", []))

    @builtins.property
    @jsii.member(jsii_name="cloudWatchLogGroupArn")
    def cloud_watch_log_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudWatchLogGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logLevelInput")
    def log_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logLevelInput"))

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
    @jsii.member(jsii_name="logLevel")
    def log_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logLevel"))

    @log_level.setter
    def log_level(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logLevel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MwaaEnvironmentLoggingConfigurationSchedulerLogs]:
        return typing.cast(typing.Optional[MwaaEnvironmentLoggingConfigurationSchedulerLogs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MwaaEnvironmentLoggingConfigurationSchedulerLogs],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MwaaEnvironmentLoggingConfigurationSchedulerLogs],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mwaaEnvironment.MwaaEnvironmentLoggingConfigurationTaskLogs",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "log_level": "logLevel"},
)
class MwaaEnvironmentLoggingConfigurationTaskLogs:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#enabled MwaaEnvironment#enabled}.
        :param log_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#log_level MwaaEnvironment#log_level}.
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                log_level: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if log_level is not None:
            self._values["log_level"] = log_level

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#enabled MwaaEnvironment#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def log_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#log_level MwaaEnvironment#log_level}.'''
        result = self._values.get("log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwaaEnvironmentLoggingConfigurationTaskLogs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MwaaEnvironmentLoggingConfigurationTaskLogsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mwaaEnvironment.MwaaEnvironmentLoggingConfigurationTaskLogsOutputReference",
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

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetLogLevel")
    def reset_log_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogLevel", []))

    @builtins.property
    @jsii.member(jsii_name="cloudWatchLogGroupArn")
    def cloud_watch_log_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudWatchLogGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logLevelInput")
    def log_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logLevelInput"))

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
    @jsii.member(jsii_name="logLevel")
    def log_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logLevel"))

    @log_level.setter
    def log_level(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logLevel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MwaaEnvironmentLoggingConfigurationTaskLogs]:
        return typing.cast(typing.Optional[MwaaEnvironmentLoggingConfigurationTaskLogs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MwaaEnvironmentLoggingConfigurationTaskLogs],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MwaaEnvironmentLoggingConfigurationTaskLogs],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mwaaEnvironment.MwaaEnvironmentLoggingConfigurationWebserverLogs",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "log_level": "logLevel"},
)
class MwaaEnvironmentLoggingConfigurationWebserverLogs:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#enabled MwaaEnvironment#enabled}.
        :param log_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#log_level MwaaEnvironment#log_level}.
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                log_level: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if log_level is not None:
            self._values["log_level"] = log_level

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#enabled MwaaEnvironment#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def log_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#log_level MwaaEnvironment#log_level}.'''
        result = self._values.get("log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwaaEnvironmentLoggingConfigurationWebserverLogs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MwaaEnvironmentLoggingConfigurationWebserverLogsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mwaaEnvironment.MwaaEnvironmentLoggingConfigurationWebserverLogsOutputReference",
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

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetLogLevel")
    def reset_log_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogLevel", []))

    @builtins.property
    @jsii.member(jsii_name="cloudWatchLogGroupArn")
    def cloud_watch_log_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudWatchLogGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logLevelInput")
    def log_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logLevelInput"))

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
    @jsii.member(jsii_name="logLevel")
    def log_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logLevel"))

    @log_level.setter
    def log_level(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logLevel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MwaaEnvironmentLoggingConfigurationWebserverLogs]:
        return typing.cast(typing.Optional[MwaaEnvironmentLoggingConfigurationWebserverLogs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MwaaEnvironmentLoggingConfigurationWebserverLogs],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MwaaEnvironmentLoggingConfigurationWebserverLogs],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mwaaEnvironment.MwaaEnvironmentLoggingConfigurationWorkerLogs",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "log_level": "logLevel"},
)
class MwaaEnvironmentLoggingConfigurationWorkerLogs:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#enabled MwaaEnvironment#enabled}.
        :param log_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#log_level MwaaEnvironment#log_level}.
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                log_level: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if log_level is not None:
            self._values["log_level"] = log_level

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#enabled MwaaEnvironment#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def log_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#log_level MwaaEnvironment#log_level}.'''
        result = self._values.get("log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwaaEnvironmentLoggingConfigurationWorkerLogs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MwaaEnvironmentLoggingConfigurationWorkerLogsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mwaaEnvironment.MwaaEnvironmentLoggingConfigurationWorkerLogsOutputReference",
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

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetLogLevel")
    def reset_log_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogLevel", []))

    @builtins.property
    @jsii.member(jsii_name="cloudWatchLogGroupArn")
    def cloud_watch_log_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudWatchLogGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logLevelInput")
    def log_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logLevelInput"))

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
    @jsii.member(jsii_name="logLevel")
    def log_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logLevel"))

    @log_level.setter
    def log_level(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logLevel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MwaaEnvironmentLoggingConfigurationWorkerLogs]:
        return typing.cast(typing.Optional[MwaaEnvironmentLoggingConfigurationWorkerLogs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MwaaEnvironmentLoggingConfigurationWorkerLogs],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MwaaEnvironmentLoggingConfigurationWorkerLogs],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mwaaEnvironment.MwaaEnvironmentNetworkConfiguration",
    jsii_struct_bases=[],
    name_mapping={"security_group_ids": "securityGroupIds", "subnet_ids": "subnetIds"},
)
class MwaaEnvironmentNetworkConfiguration:
    def __init__(
        self,
        *,
        security_group_ids: typing.Sequence[builtins.str],
        subnet_ids: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#security_group_ids MwaaEnvironment#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#subnet_ids MwaaEnvironment#subnet_ids}.
        '''
        if __debug__:
            def stub(
                *,
                security_group_ids: typing.Sequence[builtins.str],
                subnet_ids: typing.Sequence[builtins.str],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "security_group_ids": security_group_ids,
            "subnet_ids": subnet_ids,
        }

    @builtins.property
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#security_group_ids MwaaEnvironment#security_group_ids}.'''
        result = self._values.get("security_group_ids")
        assert result is not None, "Required property 'security_group_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#subnet_ids MwaaEnvironment#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwaaEnvironmentNetworkConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MwaaEnvironmentNetworkConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mwaaEnvironment.MwaaEnvironmentNetworkConfigurationOutputReference",
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
    @jsii.member(jsii_name="securityGroupIdsInput")
    def security_group_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdsInput")
    def subnet_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MwaaEnvironmentNetworkConfiguration]:
        return typing.cast(typing.Optional[MwaaEnvironmentNetworkConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MwaaEnvironmentNetworkConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MwaaEnvironmentNetworkConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mwaaEnvironment.MwaaEnvironmentTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class MwaaEnvironmentTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#create MwaaEnvironment#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#delete MwaaEnvironment#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#update MwaaEnvironment#update}.
        '''
        if __debug__:
            def stub(
                *,
                create: typing.Optional[builtins.str] = None,
                delete: typing.Optional[builtins.str] = None,
                update: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#create MwaaEnvironment#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#delete MwaaEnvironment#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mwaa_environment#update MwaaEnvironment#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwaaEnvironmentTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MwaaEnvironmentTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mwaaEnvironment.MwaaEnvironmentTimeoutsOutputReference",
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
    ) -> typing.Optional[typing.Union[MwaaEnvironmentTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MwaaEnvironmentTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MwaaEnvironmentTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[MwaaEnvironmentTimeouts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MwaaEnvironment",
    "MwaaEnvironmentConfig",
    "MwaaEnvironmentLastUpdated",
    "MwaaEnvironmentLastUpdatedError",
    "MwaaEnvironmentLastUpdatedErrorList",
    "MwaaEnvironmentLastUpdatedErrorOutputReference",
    "MwaaEnvironmentLastUpdatedList",
    "MwaaEnvironmentLastUpdatedOutputReference",
    "MwaaEnvironmentLoggingConfiguration",
    "MwaaEnvironmentLoggingConfigurationDagProcessingLogs",
    "MwaaEnvironmentLoggingConfigurationDagProcessingLogsOutputReference",
    "MwaaEnvironmentLoggingConfigurationOutputReference",
    "MwaaEnvironmentLoggingConfigurationSchedulerLogs",
    "MwaaEnvironmentLoggingConfigurationSchedulerLogsOutputReference",
    "MwaaEnvironmentLoggingConfigurationTaskLogs",
    "MwaaEnvironmentLoggingConfigurationTaskLogsOutputReference",
    "MwaaEnvironmentLoggingConfigurationWebserverLogs",
    "MwaaEnvironmentLoggingConfigurationWebserverLogsOutputReference",
    "MwaaEnvironmentLoggingConfigurationWorkerLogs",
    "MwaaEnvironmentLoggingConfigurationWorkerLogsOutputReference",
    "MwaaEnvironmentNetworkConfiguration",
    "MwaaEnvironmentNetworkConfigurationOutputReference",
    "MwaaEnvironmentTimeouts",
    "MwaaEnvironmentTimeoutsOutputReference",
]

publication.publish()
