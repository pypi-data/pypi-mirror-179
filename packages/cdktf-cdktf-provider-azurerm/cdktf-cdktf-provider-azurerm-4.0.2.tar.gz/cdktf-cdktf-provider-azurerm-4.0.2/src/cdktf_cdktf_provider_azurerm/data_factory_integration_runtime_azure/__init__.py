'''
# `azurerm_data_factory_integration_runtime_azure`

Refer to the Terraform Registory for docs: [`azurerm_data_factory_integration_runtime_azure`](https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure).
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


class DataFactoryIntegrationRuntimeAzure(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryIntegrationRuntimeAzure.DataFactoryIntegrationRuntimeAzure",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure azurerm_data_factory_integration_runtime_azure}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        data_factory_id: builtins.str,
        location: builtins.str,
        name: builtins.str,
        cleanup_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        compute_type: typing.Optional[builtins.str] = None,
        core_count: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DataFactoryIntegrationRuntimeAzureTimeouts", typing.Dict[str, typing.Any]]] = None,
        time_to_live_min: typing.Optional[jsii.Number] = None,
        virtual_network_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure azurerm_data_factory_integration_runtime_azure} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param data_factory_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#data_factory_id DataFactoryIntegrationRuntimeAzure#data_factory_id}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#location DataFactoryIntegrationRuntimeAzure#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#name DataFactoryIntegrationRuntimeAzure#name}.
        :param cleanup_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#cleanup_enabled DataFactoryIntegrationRuntimeAzure#cleanup_enabled}.
        :param compute_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#compute_type DataFactoryIntegrationRuntimeAzure#compute_type}.
        :param core_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#core_count DataFactoryIntegrationRuntimeAzure#core_count}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#description DataFactoryIntegrationRuntimeAzure#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#id DataFactoryIntegrationRuntimeAzure#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#timeouts DataFactoryIntegrationRuntimeAzure#timeouts}
        :param time_to_live_min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#time_to_live_min DataFactoryIntegrationRuntimeAzure#time_to_live_min}.
        :param virtual_network_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#virtual_network_enabled DataFactoryIntegrationRuntimeAzure#virtual_network_enabled}.
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
                data_factory_id: builtins.str,
                location: builtins.str,
                name: builtins.str,
                cleanup_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                compute_type: typing.Optional[builtins.str] = None,
                core_count: typing.Optional[jsii.Number] = None,
                description: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                timeouts: typing.Optional[typing.Union[DataFactoryIntegrationRuntimeAzureTimeouts, typing.Dict[str, typing.Any]]] = None,
                time_to_live_min: typing.Optional[jsii.Number] = None,
                virtual_network_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
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
        config = DataFactoryIntegrationRuntimeAzureConfig(
            data_factory_id=data_factory_id,
            location=location,
            name=name,
            cleanup_enabled=cleanup_enabled,
            compute_type=compute_type,
            core_count=core_count,
            description=description,
            id=id,
            timeouts=timeouts,
            time_to_live_min=time_to_live_min,
            virtual_network_enabled=virtual_network_enabled,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#create DataFactoryIntegrationRuntimeAzure#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#delete DataFactoryIntegrationRuntimeAzure#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#read DataFactoryIntegrationRuntimeAzure#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#update DataFactoryIntegrationRuntimeAzure#update}.
        '''
        value = DataFactoryIntegrationRuntimeAzureTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCleanupEnabled")
    def reset_cleanup_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCleanupEnabled", []))

    @jsii.member(jsii_name="resetComputeType")
    def reset_compute_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComputeType", []))

    @jsii.member(jsii_name="resetCoreCount")
    def reset_core_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCoreCount", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTimeToLiveMin")
    def reset_time_to_live_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeToLiveMin", []))

    @jsii.member(jsii_name="resetVirtualNetworkEnabled")
    def reset_virtual_network_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualNetworkEnabled", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DataFactoryIntegrationRuntimeAzureTimeoutsOutputReference":
        return typing.cast("DataFactoryIntegrationRuntimeAzureTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="cleanupEnabledInput")
    def cleanup_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "cleanupEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="computeTypeInput")
    def compute_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "computeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="coreCountInput")
    def core_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "coreCountInput"))

    @builtins.property
    @jsii.member(jsii_name="dataFactoryIdInput")
    def data_factory_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataFactoryIdInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DataFactoryIntegrationRuntimeAzureTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DataFactoryIntegrationRuntimeAzureTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeToLiveMinInput")
    def time_to_live_min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeToLiveMinInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkEnabledInput")
    def virtual_network_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "virtualNetworkEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="cleanupEnabled")
    def cleanup_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "cleanupEnabled"))

    @cleanup_enabled.setter
    def cleanup_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cleanupEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="computeType")
    def compute_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "computeType"))

    @compute_type.setter
    def compute_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computeType", value)

    @builtins.property
    @jsii.member(jsii_name="coreCount")
    def core_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "coreCount"))

    @core_count.setter
    def core_count(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coreCount", value)

    @builtins.property
    @jsii.member(jsii_name="dataFactoryId")
    def data_factory_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataFactoryId"))

    @data_factory_id.setter
    def data_factory_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataFactoryId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

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
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

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
    @jsii.member(jsii_name="timeToLiveMin")
    def time_to_live_min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeToLiveMin"))

    @time_to_live_min.setter
    def time_to_live_min(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeToLiveMin", value)

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkEnabled")
    def virtual_network_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "virtualNetworkEnabled"))

    @virtual_network_enabled.setter
    def virtual_network_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNetworkEnabled", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryIntegrationRuntimeAzure.DataFactoryIntegrationRuntimeAzureConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "data_factory_id": "dataFactoryId",
        "location": "location",
        "name": "name",
        "cleanup_enabled": "cleanupEnabled",
        "compute_type": "computeType",
        "core_count": "coreCount",
        "description": "description",
        "id": "id",
        "timeouts": "timeouts",
        "time_to_live_min": "timeToLiveMin",
        "virtual_network_enabled": "virtualNetworkEnabled",
    },
)
class DataFactoryIntegrationRuntimeAzureConfig(cdktf.TerraformMetaArguments):
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
        data_factory_id: builtins.str,
        location: builtins.str,
        name: builtins.str,
        cleanup_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        compute_type: typing.Optional[builtins.str] = None,
        core_count: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DataFactoryIntegrationRuntimeAzureTimeouts", typing.Dict[str, typing.Any]]] = None,
        time_to_live_min: typing.Optional[jsii.Number] = None,
        virtual_network_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param data_factory_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#data_factory_id DataFactoryIntegrationRuntimeAzure#data_factory_id}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#location DataFactoryIntegrationRuntimeAzure#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#name DataFactoryIntegrationRuntimeAzure#name}.
        :param cleanup_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#cleanup_enabled DataFactoryIntegrationRuntimeAzure#cleanup_enabled}.
        :param compute_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#compute_type DataFactoryIntegrationRuntimeAzure#compute_type}.
        :param core_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#core_count DataFactoryIntegrationRuntimeAzure#core_count}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#description DataFactoryIntegrationRuntimeAzure#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#id DataFactoryIntegrationRuntimeAzure#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#timeouts DataFactoryIntegrationRuntimeAzure#timeouts}
        :param time_to_live_min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#time_to_live_min DataFactoryIntegrationRuntimeAzure#time_to_live_min}.
        :param virtual_network_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#virtual_network_enabled DataFactoryIntegrationRuntimeAzure#virtual_network_enabled}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = DataFactoryIntegrationRuntimeAzureTimeouts(**timeouts)
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
                data_factory_id: builtins.str,
                location: builtins.str,
                name: builtins.str,
                cleanup_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                compute_type: typing.Optional[builtins.str] = None,
                core_count: typing.Optional[jsii.Number] = None,
                description: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                timeouts: typing.Optional[typing.Union[DataFactoryIntegrationRuntimeAzureTimeouts, typing.Dict[str, typing.Any]]] = None,
                time_to_live_min: typing.Optional[jsii.Number] = None,
                virtual_network_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
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
            check_type(argname="argument data_factory_id", value=data_factory_id, expected_type=type_hints["data_factory_id"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument cleanup_enabled", value=cleanup_enabled, expected_type=type_hints["cleanup_enabled"])
            check_type(argname="argument compute_type", value=compute_type, expected_type=type_hints["compute_type"])
            check_type(argname="argument core_count", value=core_count, expected_type=type_hints["core_count"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument time_to_live_min", value=time_to_live_min, expected_type=type_hints["time_to_live_min"])
            check_type(argname="argument virtual_network_enabled", value=virtual_network_enabled, expected_type=type_hints["virtual_network_enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "data_factory_id": data_factory_id,
            "location": location,
            "name": name,
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
        if cleanup_enabled is not None:
            self._values["cleanup_enabled"] = cleanup_enabled
        if compute_type is not None:
            self._values["compute_type"] = compute_type
        if core_count is not None:
            self._values["core_count"] = core_count
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if time_to_live_min is not None:
            self._values["time_to_live_min"] = time_to_live_min
        if virtual_network_enabled is not None:
            self._values["virtual_network_enabled"] = virtual_network_enabled

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
    def data_factory_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#data_factory_id DataFactoryIntegrationRuntimeAzure#data_factory_id}.'''
        result = self._values.get("data_factory_id")
        assert result is not None, "Required property 'data_factory_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#location DataFactoryIntegrationRuntimeAzure#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#name DataFactoryIntegrationRuntimeAzure#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cleanup_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#cleanup_enabled DataFactoryIntegrationRuntimeAzure#cleanup_enabled}.'''
        result = self._values.get("cleanup_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def compute_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#compute_type DataFactoryIntegrationRuntimeAzure#compute_type}.'''
        result = self._values.get("compute_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def core_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#core_count DataFactoryIntegrationRuntimeAzure#core_count}.'''
        result = self._values.get("core_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#description DataFactoryIntegrationRuntimeAzure#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#id DataFactoryIntegrationRuntimeAzure#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DataFactoryIntegrationRuntimeAzureTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#timeouts DataFactoryIntegrationRuntimeAzure#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DataFactoryIntegrationRuntimeAzureTimeouts"], result)

    @builtins.property
    def time_to_live_min(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#time_to_live_min DataFactoryIntegrationRuntimeAzure#time_to_live_min}.'''
        result = self._values.get("time_to_live_min")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def virtual_network_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#virtual_network_enabled DataFactoryIntegrationRuntimeAzure#virtual_network_enabled}.'''
        result = self._values.get("virtual_network_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryIntegrationRuntimeAzureConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryIntegrationRuntimeAzure.DataFactoryIntegrationRuntimeAzureTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class DataFactoryIntegrationRuntimeAzureTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#create DataFactoryIntegrationRuntimeAzure#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#delete DataFactoryIntegrationRuntimeAzure#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#read DataFactoryIntegrationRuntimeAzure#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#update DataFactoryIntegrationRuntimeAzure#update}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#create DataFactoryIntegrationRuntimeAzure#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#delete DataFactoryIntegrationRuntimeAzure#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#read DataFactoryIntegrationRuntimeAzure#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_integration_runtime_azure#update DataFactoryIntegrationRuntimeAzure#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryIntegrationRuntimeAzureTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataFactoryIntegrationRuntimeAzureTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryIntegrationRuntimeAzure.DataFactoryIntegrationRuntimeAzureTimeoutsOutputReference",
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
    ) -> typing.Optional[typing.Union[DataFactoryIntegrationRuntimeAzureTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataFactoryIntegrationRuntimeAzureTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataFactoryIntegrationRuntimeAzureTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[DataFactoryIntegrationRuntimeAzureTimeouts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataFactoryIntegrationRuntimeAzure",
    "DataFactoryIntegrationRuntimeAzureConfig",
    "DataFactoryIntegrationRuntimeAzureTimeouts",
    "DataFactoryIntegrationRuntimeAzureTimeoutsOutputReference",
]

publication.publish()
