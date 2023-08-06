'''
# `aws_timestreamwrite_table`

Refer to the Terraform Registory for docs: [`aws_timestreamwrite_table`](https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table).
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


class TimestreamwriteTable(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.timestreamwriteTable.TimestreamwriteTable",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table aws_timestreamwrite_table}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        database_name: builtins.str,
        table_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        magnetic_store_write_properties: typing.Optional[typing.Union["TimestreamwriteTableMagneticStoreWriteProperties", typing.Dict[str, typing.Any]]] = None,
        retention_properties: typing.Optional[typing.Union["TimestreamwriteTableRetentionProperties", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table aws_timestreamwrite_table} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#database_name TimestreamwriteTable#database_name}.
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#table_name TimestreamwriteTable#table_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#id TimestreamwriteTable#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param magnetic_store_write_properties: magnetic_store_write_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#magnetic_store_write_properties TimestreamwriteTable#magnetic_store_write_properties}
        :param retention_properties: retention_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#retention_properties TimestreamwriteTable#retention_properties}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#tags TimestreamwriteTable#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#tags_all TimestreamwriteTable#tags_all}.
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
                database_name: builtins.str,
                table_name: builtins.str,
                id: typing.Optional[builtins.str] = None,
                magnetic_store_write_properties: typing.Optional[typing.Union[TimestreamwriteTableMagneticStoreWriteProperties, typing.Dict[str, typing.Any]]] = None,
                retention_properties: typing.Optional[typing.Union[TimestreamwriteTableRetentionProperties, typing.Dict[str, typing.Any]]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
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
        config = TimestreamwriteTableConfig(
            database_name=database_name,
            table_name=table_name,
            id=id,
            magnetic_store_write_properties=magnetic_store_write_properties,
            retention_properties=retention_properties,
            tags=tags,
            tags_all=tags_all,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putMagneticStoreWriteProperties")
    def put_magnetic_store_write_properties(
        self,
        *,
        enable_magnetic_store_writes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        magnetic_store_rejected_data_location: typing.Optional[typing.Union["TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param enable_magnetic_store_writes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#enable_magnetic_store_writes TimestreamwriteTable#enable_magnetic_store_writes}.
        :param magnetic_store_rejected_data_location: magnetic_store_rejected_data_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#magnetic_store_rejected_data_location TimestreamwriteTable#magnetic_store_rejected_data_location}
        '''
        value = TimestreamwriteTableMagneticStoreWriteProperties(
            enable_magnetic_store_writes=enable_magnetic_store_writes,
            magnetic_store_rejected_data_location=magnetic_store_rejected_data_location,
        )

        return typing.cast(None, jsii.invoke(self, "putMagneticStoreWriteProperties", [value]))

    @jsii.member(jsii_name="putRetentionProperties")
    def put_retention_properties(
        self,
        *,
        magnetic_store_retention_period_in_days: jsii.Number,
        memory_store_retention_period_in_hours: jsii.Number,
    ) -> None:
        '''
        :param magnetic_store_retention_period_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#magnetic_store_retention_period_in_days TimestreamwriteTable#magnetic_store_retention_period_in_days}.
        :param memory_store_retention_period_in_hours: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#memory_store_retention_period_in_hours TimestreamwriteTable#memory_store_retention_period_in_hours}.
        '''
        value = TimestreamwriteTableRetentionProperties(
            magnetic_store_retention_period_in_days=magnetic_store_retention_period_in_days,
            memory_store_retention_period_in_hours=memory_store_retention_period_in_hours,
        )

        return typing.cast(None, jsii.invoke(self, "putRetentionProperties", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMagneticStoreWriteProperties")
    def reset_magnetic_store_write_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMagneticStoreWriteProperties", []))

    @jsii.member(jsii_name="resetRetentionProperties")
    def reset_retention_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionProperties", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

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
    @jsii.member(jsii_name="magneticStoreWriteProperties")
    def magnetic_store_write_properties(
        self,
    ) -> "TimestreamwriteTableMagneticStoreWritePropertiesOutputReference":
        return typing.cast("TimestreamwriteTableMagneticStoreWritePropertiesOutputReference", jsii.get(self, "magneticStoreWriteProperties"))

    @builtins.property
    @jsii.member(jsii_name="retentionProperties")
    def retention_properties(
        self,
    ) -> "TimestreamwriteTableRetentionPropertiesOutputReference":
        return typing.cast("TimestreamwriteTableRetentionPropertiesOutputReference", jsii.get(self, "retentionProperties"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="magneticStoreWritePropertiesInput")
    def magnetic_store_write_properties_input(
        self,
    ) -> typing.Optional["TimestreamwriteTableMagneticStoreWriteProperties"]:
        return typing.cast(typing.Optional["TimestreamwriteTableMagneticStoreWriteProperties"], jsii.get(self, "magneticStoreWritePropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionPropertiesInput")
    def retention_properties_input(
        self,
    ) -> typing.Optional["TimestreamwriteTableRetentionProperties"]:
        return typing.cast(typing.Optional["TimestreamwriteTableRetentionProperties"], jsii.get(self, "retentionPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="tableNameInput")
    def table_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableNameInput"))

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
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

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
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableName"))

    @table_name.setter
    def table_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableName", value)

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


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.timestreamwriteTable.TimestreamwriteTableConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "database_name": "databaseName",
        "table_name": "tableName",
        "id": "id",
        "magnetic_store_write_properties": "magneticStoreWriteProperties",
        "retention_properties": "retentionProperties",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class TimestreamwriteTableConfig(cdktf.TerraformMetaArguments):
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
        database_name: builtins.str,
        table_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        magnetic_store_write_properties: typing.Optional[typing.Union["TimestreamwriteTableMagneticStoreWriteProperties", typing.Dict[str, typing.Any]]] = None,
        retention_properties: typing.Optional[typing.Union["TimestreamwriteTableRetentionProperties", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#database_name TimestreamwriteTable#database_name}.
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#table_name TimestreamwriteTable#table_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#id TimestreamwriteTable#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param magnetic_store_write_properties: magnetic_store_write_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#magnetic_store_write_properties TimestreamwriteTable#magnetic_store_write_properties}
        :param retention_properties: retention_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#retention_properties TimestreamwriteTable#retention_properties}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#tags TimestreamwriteTable#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#tags_all TimestreamwriteTable#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(magnetic_store_write_properties, dict):
            magnetic_store_write_properties = TimestreamwriteTableMagneticStoreWriteProperties(**magnetic_store_write_properties)
        if isinstance(retention_properties, dict):
            retention_properties = TimestreamwriteTableRetentionProperties(**retention_properties)
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
                database_name: builtins.str,
                table_name: builtins.str,
                id: typing.Optional[builtins.str] = None,
                magnetic_store_write_properties: typing.Optional[typing.Union[TimestreamwriteTableMagneticStoreWriteProperties, typing.Dict[str, typing.Any]]] = None,
                retention_properties: typing.Optional[typing.Union[TimestreamwriteTableRetentionProperties, typing.Dict[str, typing.Any]]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
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
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument magnetic_store_write_properties", value=magnetic_store_write_properties, expected_type=type_hints["magnetic_store_write_properties"])
            check_type(argname="argument retention_properties", value=retention_properties, expected_type=type_hints["retention_properties"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[str, typing.Any] = {
            "database_name": database_name,
            "table_name": table_name,
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
        if id is not None:
            self._values["id"] = id
        if magnetic_store_write_properties is not None:
            self._values["magnetic_store_write_properties"] = magnetic_store_write_properties
        if retention_properties is not None:
            self._values["retention_properties"] = retention_properties
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all

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
    def database_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#database_name TimestreamwriteTable#database_name}.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#table_name TimestreamwriteTable#table_name}.'''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#id TimestreamwriteTable#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def magnetic_store_write_properties(
        self,
    ) -> typing.Optional["TimestreamwriteTableMagneticStoreWriteProperties"]:
        '''magnetic_store_write_properties block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#magnetic_store_write_properties TimestreamwriteTable#magnetic_store_write_properties}
        '''
        result = self._values.get("magnetic_store_write_properties")
        return typing.cast(typing.Optional["TimestreamwriteTableMagneticStoreWriteProperties"], result)

    @builtins.property
    def retention_properties(
        self,
    ) -> typing.Optional["TimestreamwriteTableRetentionProperties"]:
        '''retention_properties block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#retention_properties TimestreamwriteTable#retention_properties}
        '''
        result = self._values.get("retention_properties")
        return typing.cast(typing.Optional["TimestreamwriteTableRetentionProperties"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#tags TimestreamwriteTable#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#tags_all TimestreamwriteTable#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TimestreamwriteTableConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.timestreamwriteTable.TimestreamwriteTableMagneticStoreWriteProperties",
    jsii_struct_bases=[],
    name_mapping={
        "enable_magnetic_store_writes": "enableMagneticStoreWrites",
        "magnetic_store_rejected_data_location": "magneticStoreRejectedDataLocation",
    },
)
class TimestreamwriteTableMagneticStoreWriteProperties:
    def __init__(
        self,
        *,
        enable_magnetic_store_writes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        magnetic_store_rejected_data_location: typing.Optional[typing.Union["TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param enable_magnetic_store_writes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#enable_magnetic_store_writes TimestreamwriteTable#enable_magnetic_store_writes}.
        :param magnetic_store_rejected_data_location: magnetic_store_rejected_data_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#magnetic_store_rejected_data_location TimestreamwriteTable#magnetic_store_rejected_data_location}
        '''
        if isinstance(magnetic_store_rejected_data_location, dict):
            magnetic_store_rejected_data_location = TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation(**magnetic_store_rejected_data_location)
        if __debug__:
            def stub(
                *,
                enable_magnetic_store_writes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                magnetic_store_rejected_data_location: typing.Optional[typing.Union[TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enable_magnetic_store_writes", value=enable_magnetic_store_writes, expected_type=type_hints["enable_magnetic_store_writes"])
            check_type(argname="argument magnetic_store_rejected_data_location", value=magnetic_store_rejected_data_location, expected_type=type_hints["magnetic_store_rejected_data_location"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enable_magnetic_store_writes is not None:
            self._values["enable_magnetic_store_writes"] = enable_magnetic_store_writes
        if magnetic_store_rejected_data_location is not None:
            self._values["magnetic_store_rejected_data_location"] = magnetic_store_rejected_data_location

    @builtins.property
    def enable_magnetic_store_writes(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#enable_magnetic_store_writes TimestreamwriteTable#enable_magnetic_store_writes}.'''
        result = self._values.get("enable_magnetic_store_writes")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def magnetic_store_rejected_data_location(
        self,
    ) -> typing.Optional["TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation"]:
        '''magnetic_store_rejected_data_location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#magnetic_store_rejected_data_location TimestreamwriteTable#magnetic_store_rejected_data_location}
        '''
        result = self._values.get("magnetic_store_rejected_data_location")
        return typing.cast(typing.Optional["TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TimestreamwriteTableMagneticStoreWriteProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.timestreamwriteTable.TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation",
    jsii_struct_bases=[],
    name_mapping={"s3_configuration": "s3Configuration"},
)
class TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation:
    def __init__(
        self,
        *,
        s3_configuration: typing.Optional[typing.Union["TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param s3_configuration: s3_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#s3_configuration TimestreamwriteTable#s3_configuration}
        '''
        if isinstance(s3_configuration, dict):
            s3_configuration = TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration(**s3_configuration)
        if __debug__:
            def stub(
                *,
                s3_configuration: typing.Optional[typing.Union[TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument s3_configuration", value=s3_configuration, expected_type=type_hints["s3_configuration"])
        self._values: typing.Dict[str, typing.Any] = {}
        if s3_configuration is not None:
            self._values["s3_configuration"] = s3_configuration

    @builtins.property
    def s3_configuration(
        self,
    ) -> typing.Optional["TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration"]:
        '''s3_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#s3_configuration TimestreamwriteTable#s3_configuration}
        '''
        result = self._values.get("s3_configuration")
        return typing.cast(typing.Optional["TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.timestreamwriteTable.TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationOutputReference",
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

    @jsii.member(jsii_name="putS3Configuration")
    def put_s3_configuration(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        encryption_option: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        object_key_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#bucket_name TimestreamwriteTable#bucket_name}.
        :param encryption_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#encryption_option TimestreamwriteTable#encryption_option}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#kms_key_id TimestreamwriteTable#kms_key_id}.
        :param object_key_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#object_key_prefix TimestreamwriteTable#object_key_prefix}.
        '''
        value = TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration(
            bucket_name=bucket_name,
            encryption_option=encryption_option,
            kms_key_id=kms_key_id,
            object_key_prefix=object_key_prefix,
        )

        return typing.cast(None, jsii.invoke(self, "putS3Configuration", [value]))

    @jsii.member(jsii_name="resetS3Configuration")
    def reset_s3_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3Configuration", []))

    @builtins.property
    @jsii.member(jsii_name="s3Configuration")
    def s3_configuration(
        self,
    ) -> "TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3ConfigurationOutputReference":
        return typing.cast("TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3ConfigurationOutputReference", jsii.get(self, "s3Configuration"))

    @builtins.property
    @jsii.member(jsii_name="s3ConfigurationInput")
    def s3_configuration_input(
        self,
    ) -> typing.Optional["TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration"]:
        return typing.cast(typing.Optional["TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration"], jsii.get(self, "s3ConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation]:
        return typing.cast(typing.Optional[TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.timestreamwriteTable.TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "encryption_option": "encryptionOption",
        "kms_key_id": "kmsKeyId",
        "object_key_prefix": "objectKeyPrefix",
    },
)
class TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration:
    def __init__(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        encryption_option: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        object_key_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#bucket_name TimestreamwriteTable#bucket_name}.
        :param encryption_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#encryption_option TimestreamwriteTable#encryption_option}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#kms_key_id TimestreamwriteTable#kms_key_id}.
        :param object_key_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#object_key_prefix TimestreamwriteTable#object_key_prefix}.
        '''
        if __debug__:
            def stub(
                *,
                bucket_name: typing.Optional[builtins.str] = None,
                encryption_option: typing.Optional[builtins.str] = None,
                kms_key_id: typing.Optional[builtins.str] = None,
                object_key_prefix: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument encryption_option", value=encryption_option, expected_type=type_hints["encryption_option"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument object_key_prefix", value=object_key_prefix, expected_type=type_hints["object_key_prefix"])
        self._values: typing.Dict[str, typing.Any] = {}
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if encryption_option is not None:
            self._values["encryption_option"] = encryption_option
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if object_key_prefix is not None:
            self._values["object_key_prefix"] = object_key_prefix

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#bucket_name TimestreamwriteTable#bucket_name}.'''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_option(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#encryption_option TimestreamwriteTable#encryption_option}.'''
        result = self._values.get("encryption_option")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#kms_key_id TimestreamwriteTable#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def object_key_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#object_key_prefix TimestreamwriteTable#object_key_prefix}.'''
        result = self._values.get("object_key_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3ConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.timestreamwriteTable.TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3ConfigurationOutputReference",
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

    @jsii.member(jsii_name="resetBucketName")
    def reset_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketName", []))

    @jsii.member(jsii_name="resetEncryptionOption")
    def reset_encryption_option(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionOption", []))

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @jsii.member(jsii_name="resetObjectKeyPrefix")
    def reset_object_key_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectKeyPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionOptionInput")
    def encryption_option_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="objectKeyPrefixInput")
    def object_key_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectKeyPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionOption")
    def encryption_option(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionOption"))

    @encryption_option.setter
    def encryption_option(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionOption", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="objectKeyPrefix")
    def object_key_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectKeyPrefix"))

    @object_key_prefix.setter
    def object_key_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectKeyPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration]:
        return typing.cast(typing.Optional[TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TimestreamwriteTableMagneticStoreWritePropertiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.timestreamwriteTable.TimestreamwriteTableMagneticStoreWritePropertiesOutputReference",
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

    @jsii.member(jsii_name="putMagneticStoreRejectedDataLocation")
    def put_magnetic_store_rejected_data_location(
        self,
        *,
        s3_configuration: typing.Optional[typing.Union[TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param s3_configuration: s3_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#s3_configuration TimestreamwriteTable#s3_configuration}
        '''
        value = TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation(
            s3_configuration=s3_configuration
        )

        return typing.cast(None, jsii.invoke(self, "putMagneticStoreRejectedDataLocation", [value]))

    @jsii.member(jsii_name="resetEnableMagneticStoreWrites")
    def reset_enable_magnetic_store_writes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableMagneticStoreWrites", []))

    @jsii.member(jsii_name="resetMagneticStoreRejectedDataLocation")
    def reset_magnetic_store_rejected_data_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMagneticStoreRejectedDataLocation", []))

    @builtins.property
    @jsii.member(jsii_name="magneticStoreRejectedDataLocation")
    def magnetic_store_rejected_data_location(
        self,
    ) -> TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationOutputReference:
        return typing.cast(TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationOutputReference, jsii.get(self, "magneticStoreRejectedDataLocation"))

    @builtins.property
    @jsii.member(jsii_name="enableMagneticStoreWritesInput")
    def enable_magnetic_store_writes_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableMagneticStoreWritesInput"))

    @builtins.property
    @jsii.member(jsii_name="magneticStoreRejectedDataLocationInput")
    def magnetic_store_rejected_data_location_input(
        self,
    ) -> typing.Optional[TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation]:
        return typing.cast(typing.Optional[TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation], jsii.get(self, "magneticStoreRejectedDataLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="enableMagneticStoreWrites")
    def enable_magnetic_store_writes(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableMagneticStoreWrites"))

    @enable_magnetic_store_writes.setter
    def enable_magnetic_store_writes(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableMagneticStoreWrites", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TimestreamwriteTableMagneticStoreWriteProperties]:
        return typing.cast(typing.Optional[TimestreamwriteTableMagneticStoreWriteProperties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TimestreamwriteTableMagneticStoreWriteProperties],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[TimestreamwriteTableMagneticStoreWriteProperties],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.timestreamwriteTable.TimestreamwriteTableRetentionProperties",
    jsii_struct_bases=[],
    name_mapping={
        "magnetic_store_retention_period_in_days": "magneticStoreRetentionPeriodInDays",
        "memory_store_retention_period_in_hours": "memoryStoreRetentionPeriodInHours",
    },
)
class TimestreamwriteTableRetentionProperties:
    def __init__(
        self,
        *,
        magnetic_store_retention_period_in_days: jsii.Number,
        memory_store_retention_period_in_hours: jsii.Number,
    ) -> None:
        '''
        :param magnetic_store_retention_period_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#magnetic_store_retention_period_in_days TimestreamwriteTable#magnetic_store_retention_period_in_days}.
        :param memory_store_retention_period_in_hours: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#memory_store_retention_period_in_hours TimestreamwriteTable#memory_store_retention_period_in_hours}.
        '''
        if __debug__:
            def stub(
                *,
                magnetic_store_retention_period_in_days: jsii.Number,
                memory_store_retention_period_in_hours: jsii.Number,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument magnetic_store_retention_period_in_days", value=magnetic_store_retention_period_in_days, expected_type=type_hints["magnetic_store_retention_period_in_days"])
            check_type(argname="argument memory_store_retention_period_in_hours", value=memory_store_retention_period_in_hours, expected_type=type_hints["memory_store_retention_period_in_hours"])
        self._values: typing.Dict[str, typing.Any] = {
            "magnetic_store_retention_period_in_days": magnetic_store_retention_period_in_days,
            "memory_store_retention_period_in_hours": memory_store_retention_period_in_hours,
        }

    @builtins.property
    def magnetic_store_retention_period_in_days(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#magnetic_store_retention_period_in_days TimestreamwriteTable#magnetic_store_retention_period_in_days}.'''
        result = self._values.get("magnetic_store_retention_period_in_days")
        assert result is not None, "Required property 'magnetic_store_retention_period_in_days' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def memory_store_retention_period_in_hours(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/timestreamwrite_table#memory_store_retention_period_in_hours TimestreamwriteTable#memory_store_retention_period_in_hours}.'''
        result = self._values.get("memory_store_retention_period_in_hours")
        assert result is not None, "Required property 'memory_store_retention_period_in_hours' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TimestreamwriteTableRetentionProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TimestreamwriteTableRetentionPropertiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.timestreamwriteTable.TimestreamwriteTableRetentionPropertiesOutputReference",
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
    @jsii.member(jsii_name="magneticStoreRetentionPeriodInDaysInput")
    def magnetic_store_retention_period_in_days_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "magneticStoreRetentionPeriodInDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryStoreRetentionPeriodInHoursInput")
    def memory_store_retention_period_in_hours_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memoryStoreRetentionPeriodInHoursInput"))

    @builtins.property
    @jsii.member(jsii_name="magneticStoreRetentionPeriodInDays")
    def magnetic_store_retention_period_in_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "magneticStoreRetentionPeriodInDays"))

    @magnetic_store_retention_period_in_days.setter
    def magnetic_store_retention_period_in_days(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "magneticStoreRetentionPeriodInDays", value)

    @builtins.property
    @jsii.member(jsii_name="memoryStoreRetentionPeriodInHours")
    def memory_store_retention_period_in_hours(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryStoreRetentionPeriodInHours"))

    @memory_store_retention_period_in_hours.setter
    def memory_store_retention_period_in_hours(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryStoreRetentionPeriodInHours", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TimestreamwriteTableRetentionProperties]:
        return typing.cast(typing.Optional[TimestreamwriteTableRetentionProperties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TimestreamwriteTableRetentionProperties],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[TimestreamwriteTableRetentionProperties],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "TimestreamwriteTable",
    "TimestreamwriteTableConfig",
    "TimestreamwriteTableMagneticStoreWriteProperties",
    "TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation",
    "TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationOutputReference",
    "TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration",
    "TimestreamwriteTableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3ConfigurationOutputReference",
    "TimestreamwriteTableMagneticStoreWritePropertiesOutputReference",
    "TimestreamwriteTableRetentionProperties",
    "TimestreamwriteTableRetentionPropertiesOutputReference",
]

publication.publish()
