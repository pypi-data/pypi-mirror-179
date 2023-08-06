'''
# `azurerm_stream_analytics_stream_input_eventhub_v2`

Refer to the Terraform Registory for docs: [`azurerm_stream_analytics_stream_input_eventhub_v2`](https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2).
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


class StreamAnalyticsStreamInputEventhubV2(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.streamAnalyticsStreamInputEventhubV2.StreamAnalyticsStreamInputEventhubV2",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2 azurerm_stream_analytics_stream_input_eventhub_v2}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        eventhub_name: builtins.str,
        name: builtins.str,
        serialization: typing.Union["StreamAnalyticsStreamInputEventhubV2Serialization", typing.Dict[str, typing.Any]],
        servicebus_namespace: builtins.str,
        stream_analytics_job_id: builtins.str,
        authentication_mode: typing.Optional[builtins.str] = None,
        eventhub_consumer_group_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        partition_key: typing.Optional[builtins.str] = None,
        shared_access_policy_key: typing.Optional[builtins.str] = None,
        shared_access_policy_name: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["StreamAnalyticsStreamInputEventhubV2Timeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2 azurerm_stream_analytics_stream_input_eventhub_v2} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param eventhub_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#eventhub_name StreamAnalyticsStreamInputEventhubV2#eventhub_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#name StreamAnalyticsStreamInputEventhubV2#name}.
        :param serialization: serialization block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#serialization StreamAnalyticsStreamInputEventhubV2#serialization}
        :param servicebus_namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#servicebus_namespace StreamAnalyticsStreamInputEventhubV2#servicebus_namespace}.
        :param stream_analytics_job_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#stream_analytics_job_id StreamAnalyticsStreamInputEventhubV2#stream_analytics_job_id}.
        :param authentication_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#authentication_mode StreamAnalyticsStreamInputEventhubV2#authentication_mode}.
        :param eventhub_consumer_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#eventhub_consumer_group_name StreamAnalyticsStreamInputEventhubV2#eventhub_consumer_group_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#id StreamAnalyticsStreamInputEventhubV2#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param partition_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#partition_key StreamAnalyticsStreamInputEventhubV2#partition_key}.
        :param shared_access_policy_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#shared_access_policy_key StreamAnalyticsStreamInputEventhubV2#shared_access_policy_key}.
        :param shared_access_policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#shared_access_policy_name StreamAnalyticsStreamInputEventhubV2#shared_access_policy_name}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#timeouts StreamAnalyticsStreamInputEventhubV2#timeouts}
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
                eventhub_name: builtins.str,
                name: builtins.str,
                serialization: typing.Union[StreamAnalyticsStreamInputEventhubV2Serialization, typing.Dict[str, typing.Any]],
                servicebus_namespace: builtins.str,
                stream_analytics_job_id: builtins.str,
                authentication_mode: typing.Optional[builtins.str] = None,
                eventhub_consumer_group_name: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                partition_key: typing.Optional[builtins.str] = None,
                shared_access_policy_key: typing.Optional[builtins.str] = None,
                shared_access_policy_name: typing.Optional[builtins.str] = None,
                timeouts: typing.Optional[typing.Union[StreamAnalyticsStreamInputEventhubV2Timeouts, typing.Dict[str, typing.Any]]] = None,
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
        config = StreamAnalyticsStreamInputEventhubV2Config(
            eventhub_name=eventhub_name,
            name=name,
            serialization=serialization,
            servicebus_namespace=servicebus_namespace,
            stream_analytics_job_id=stream_analytics_job_id,
            authentication_mode=authentication_mode,
            eventhub_consumer_group_name=eventhub_consumer_group_name,
            id=id,
            partition_key=partition_key,
            shared_access_policy_key=shared_access_policy_key,
            shared_access_policy_name=shared_access_policy_name,
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

    @jsii.member(jsii_name="putSerialization")
    def put_serialization(
        self,
        *,
        type: builtins.str,
        encoding: typing.Optional[builtins.str] = None,
        field_delimiter: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#type StreamAnalyticsStreamInputEventhubV2#type}.
        :param encoding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#encoding StreamAnalyticsStreamInputEventhubV2#encoding}.
        :param field_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#field_delimiter StreamAnalyticsStreamInputEventhubV2#field_delimiter}.
        '''
        value = StreamAnalyticsStreamInputEventhubV2Serialization(
            type=type, encoding=encoding, field_delimiter=field_delimiter
        )

        return typing.cast(None, jsii.invoke(self, "putSerialization", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#create StreamAnalyticsStreamInputEventhubV2#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#delete StreamAnalyticsStreamInputEventhubV2#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#read StreamAnalyticsStreamInputEventhubV2#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#update StreamAnalyticsStreamInputEventhubV2#update}.
        '''
        value = StreamAnalyticsStreamInputEventhubV2Timeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAuthenticationMode")
    def reset_authentication_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticationMode", []))

    @jsii.member(jsii_name="resetEventhubConsumerGroupName")
    def reset_eventhub_consumer_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventhubConsumerGroupName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPartitionKey")
    def reset_partition_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartitionKey", []))

    @jsii.member(jsii_name="resetSharedAccessPolicyKey")
    def reset_shared_access_policy_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSharedAccessPolicyKey", []))

    @jsii.member(jsii_name="resetSharedAccessPolicyName")
    def reset_shared_access_policy_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSharedAccessPolicyName", []))

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
    @jsii.member(jsii_name="serialization")
    def serialization(
        self,
    ) -> "StreamAnalyticsStreamInputEventhubV2SerializationOutputReference":
        return typing.cast("StreamAnalyticsStreamInputEventhubV2SerializationOutputReference", jsii.get(self, "serialization"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "StreamAnalyticsStreamInputEventhubV2TimeoutsOutputReference":
        return typing.cast("StreamAnalyticsStreamInputEventhubV2TimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="authenticationModeInput")
    def authentication_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authenticationModeInput"))

    @builtins.property
    @jsii.member(jsii_name="eventhubConsumerGroupNameInput")
    def eventhub_consumer_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventhubConsumerGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="eventhubNameInput")
    def eventhub_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventhubNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionKeyInput")
    def partition_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "partitionKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="serializationInput")
    def serialization_input(
        self,
    ) -> typing.Optional["StreamAnalyticsStreamInputEventhubV2Serialization"]:
        return typing.cast(typing.Optional["StreamAnalyticsStreamInputEventhubV2Serialization"], jsii.get(self, "serializationInput"))

    @builtins.property
    @jsii.member(jsii_name="servicebusNamespaceInput")
    def servicebus_namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "servicebusNamespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="sharedAccessPolicyKeyInput")
    def shared_access_policy_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sharedAccessPolicyKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="sharedAccessPolicyNameInput")
    def shared_access_policy_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sharedAccessPolicyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="streamAnalyticsJobIdInput")
    def stream_analytics_job_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamAnalyticsJobIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["StreamAnalyticsStreamInputEventhubV2Timeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["StreamAnalyticsStreamInputEventhubV2Timeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationMode")
    def authentication_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authenticationMode"))

    @authentication_mode.setter
    def authentication_mode(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationMode", value)

    @builtins.property
    @jsii.member(jsii_name="eventhubConsumerGroupName")
    def eventhub_consumer_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventhubConsumerGroupName"))

    @eventhub_consumer_group_name.setter
    def eventhub_consumer_group_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventhubConsumerGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="eventhubName")
    def eventhub_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventhubName"))

    @eventhub_name.setter
    def eventhub_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventhubName", value)

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
    @jsii.member(jsii_name="partitionKey")
    def partition_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "partitionKey"))

    @partition_key.setter
    def partition_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partitionKey", value)

    @builtins.property
    @jsii.member(jsii_name="servicebusNamespace")
    def servicebus_namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servicebusNamespace"))

    @servicebus_namespace.setter
    def servicebus_namespace(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servicebusNamespace", value)

    @builtins.property
    @jsii.member(jsii_name="sharedAccessPolicyKey")
    def shared_access_policy_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sharedAccessPolicyKey"))

    @shared_access_policy_key.setter
    def shared_access_policy_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sharedAccessPolicyKey", value)

    @builtins.property
    @jsii.member(jsii_name="sharedAccessPolicyName")
    def shared_access_policy_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sharedAccessPolicyName"))

    @shared_access_policy_name.setter
    def shared_access_policy_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sharedAccessPolicyName", value)

    @builtins.property
    @jsii.member(jsii_name="streamAnalyticsJobId")
    def stream_analytics_job_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamAnalyticsJobId"))

    @stream_analytics_job_id.setter
    def stream_analytics_job_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamAnalyticsJobId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.streamAnalyticsStreamInputEventhubV2.StreamAnalyticsStreamInputEventhubV2Config",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "eventhub_name": "eventhubName",
        "name": "name",
        "serialization": "serialization",
        "servicebus_namespace": "servicebusNamespace",
        "stream_analytics_job_id": "streamAnalyticsJobId",
        "authentication_mode": "authenticationMode",
        "eventhub_consumer_group_name": "eventhubConsumerGroupName",
        "id": "id",
        "partition_key": "partitionKey",
        "shared_access_policy_key": "sharedAccessPolicyKey",
        "shared_access_policy_name": "sharedAccessPolicyName",
        "timeouts": "timeouts",
    },
)
class StreamAnalyticsStreamInputEventhubV2Config(cdktf.TerraformMetaArguments):
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
        eventhub_name: builtins.str,
        name: builtins.str,
        serialization: typing.Union["StreamAnalyticsStreamInputEventhubV2Serialization", typing.Dict[str, typing.Any]],
        servicebus_namespace: builtins.str,
        stream_analytics_job_id: builtins.str,
        authentication_mode: typing.Optional[builtins.str] = None,
        eventhub_consumer_group_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        partition_key: typing.Optional[builtins.str] = None,
        shared_access_policy_key: typing.Optional[builtins.str] = None,
        shared_access_policy_name: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["StreamAnalyticsStreamInputEventhubV2Timeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param eventhub_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#eventhub_name StreamAnalyticsStreamInputEventhubV2#eventhub_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#name StreamAnalyticsStreamInputEventhubV2#name}.
        :param serialization: serialization block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#serialization StreamAnalyticsStreamInputEventhubV2#serialization}
        :param servicebus_namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#servicebus_namespace StreamAnalyticsStreamInputEventhubV2#servicebus_namespace}.
        :param stream_analytics_job_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#stream_analytics_job_id StreamAnalyticsStreamInputEventhubV2#stream_analytics_job_id}.
        :param authentication_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#authentication_mode StreamAnalyticsStreamInputEventhubV2#authentication_mode}.
        :param eventhub_consumer_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#eventhub_consumer_group_name StreamAnalyticsStreamInputEventhubV2#eventhub_consumer_group_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#id StreamAnalyticsStreamInputEventhubV2#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param partition_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#partition_key StreamAnalyticsStreamInputEventhubV2#partition_key}.
        :param shared_access_policy_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#shared_access_policy_key StreamAnalyticsStreamInputEventhubV2#shared_access_policy_key}.
        :param shared_access_policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#shared_access_policy_name StreamAnalyticsStreamInputEventhubV2#shared_access_policy_name}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#timeouts StreamAnalyticsStreamInputEventhubV2#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(serialization, dict):
            serialization = StreamAnalyticsStreamInputEventhubV2Serialization(**serialization)
        if isinstance(timeouts, dict):
            timeouts = StreamAnalyticsStreamInputEventhubV2Timeouts(**timeouts)
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
                eventhub_name: builtins.str,
                name: builtins.str,
                serialization: typing.Union[StreamAnalyticsStreamInputEventhubV2Serialization, typing.Dict[str, typing.Any]],
                servicebus_namespace: builtins.str,
                stream_analytics_job_id: builtins.str,
                authentication_mode: typing.Optional[builtins.str] = None,
                eventhub_consumer_group_name: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                partition_key: typing.Optional[builtins.str] = None,
                shared_access_policy_key: typing.Optional[builtins.str] = None,
                shared_access_policy_name: typing.Optional[builtins.str] = None,
                timeouts: typing.Optional[typing.Union[StreamAnalyticsStreamInputEventhubV2Timeouts, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument eventhub_name", value=eventhub_name, expected_type=type_hints["eventhub_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument serialization", value=serialization, expected_type=type_hints["serialization"])
            check_type(argname="argument servicebus_namespace", value=servicebus_namespace, expected_type=type_hints["servicebus_namespace"])
            check_type(argname="argument stream_analytics_job_id", value=stream_analytics_job_id, expected_type=type_hints["stream_analytics_job_id"])
            check_type(argname="argument authentication_mode", value=authentication_mode, expected_type=type_hints["authentication_mode"])
            check_type(argname="argument eventhub_consumer_group_name", value=eventhub_consumer_group_name, expected_type=type_hints["eventhub_consumer_group_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument partition_key", value=partition_key, expected_type=type_hints["partition_key"])
            check_type(argname="argument shared_access_policy_key", value=shared_access_policy_key, expected_type=type_hints["shared_access_policy_key"])
            check_type(argname="argument shared_access_policy_name", value=shared_access_policy_name, expected_type=type_hints["shared_access_policy_name"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "eventhub_name": eventhub_name,
            "name": name,
            "serialization": serialization,
            "servicebus_namespace": servicebus_namespace,
            "stream_analytics_job_id": stream_analytics_job_id,
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
        if authentication_mode is not None:
            self._values["authentication_mode"] = authentication_mode
        if eventhub_consumer_group_name is not None:
            self._values["eventhub_consumer_group_name"] = eventhub_consumer_group_name
        if id is not None:
            self._values["id"] = id
        if partition_key is not None:
            self._values["partition_key"] = partition_key
        if shared_access_policy_key is not None:
            self._values["shared_access_policy_key"] = shared_access_policy_key
        if shared_access_policy_name is not None:
            self._values["shared_access_policy_name"] = shared_access_policy_name
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
    def eventhub_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#eventhub_name StreamAnalyticsStreamInputEventhubV2#eventhub_name}.'''
        result = self._values.get("eventhub_name")
        assert result is not None, "Required property 'eventhub_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#name StreamAnalyticsStreamInputEventhubV2#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def serialization(self) -> "StreamAnalyticsStreamInputEventhubV2Serialization":
        '''serialization block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#serialization StreamAnalyticsStreamInputEventhubV2#serialization}
        '''
        result = self._values.get("serialization")
        assert result is not None, "Required property 'serialization' is missing"
        return typing.cast("StreamAnalyticsStreamInputEventhubV2Serialization", result)

    @builtins.property
    def servicebus_namespace(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#servicebus_namespace StreamAnalyticsStreamInputEventhubV2#servicebus_namespace}.'''
        result = self._values.get("servicebus_namespace")
        assert result is not None, "Required property 'servicebus_namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stream_analytics_job_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#stream_analytics_job_id StreamAnalyticsStreamInputEventhubV2#stream_analytics_job_id}.'''
        result = self._values.get("stream_analytics_job_id")
        assert result is not None, "Required property 'stream_analytics_job_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authentication_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#authentication_mode StreamAnalyticsStreamInputEventhubV2#authentication_mode}.'''
        result = self._values.get("authentication_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def eventhub_consumer_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#eventhub_consumer_group_name StreamAnalyticsStreamInputEventhubV2#eventhub_consumer_group_name}.'''
        result = self._values.get("eventhub_consumer_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#id StreamAnalyticsStreamInputEventhubV2#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#partition_key StreamAnalyticsStreamInputEventhubV2#partition_key}.'''
        result = self._values.get("partition_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def shared_access_policy_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#shared_access_policy_key StreamAnalyticsStreamInputEventhubV2#shared_access_policy_key}.'''
        result = self._values.get("shared_access_policy_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def shared_access_policy_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#shared_access_policy_name StreamAnalyticsStreamInputEventhubV2#shared_access_policy_name}.'''
        result = self._values.get("shared_access_policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["StreamAnalyticsStreamInputEventhubV2Timeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#timeouts StreamAnalyticsStreamInputEventhubV2#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["StreamAnalyticsStreamInputEventhubV2Timeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StreamAnalyticsStreamInputEventhubV2Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.streamAnalyticsStreamInputEventhubV2.StreamAnalyticsStreamInputEventhubV2Serialization",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "encoding": "encoding",
        "field_delimiter": "fieldDelimiter",
    },
)
class StreamAnalyticsStreamInputEventhubV2Serialization:
    def __init__(
        self,
        *,
        type: builtins.str,
        encoding: typing.Optional[builtins.str] = None,
        field_delimiter: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#type StreamAnalyticsStreamInputEventhubV2#type}.
        :param encoding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#encoding StreamAnalyticsStreamInputEventhubV2#encoding}.
        :param field_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#field_delimiter StreamAnalyticsStreamInputEventhubV2#field_delimiter}.
        '''
        if __debug__:
            def stub(
                *,
                type: builtins.str,
                encoding: typing.Optional[builtins.str] = None,
                field_delimiter: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument encoding", value=encoding, expected_type=type_hints["encoding"])
            check_type(argname="argument field_delimiter", value=field_delimiter, expected_type=type_hints["field_delimiter"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if encoding is not None:
            self._values["encoding"] = encoding
        if field_delimiter is not None:
            self._values["field_delimiter"] = field_delimiter

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#type StreamAnalyticsStreamInputEventhubV2#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def encoding(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#encoding StreamAnalyticsStreamInputEventhubV2#encoding}.'''
        result = self._values.get("encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def field_delimiter(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#field_delimiter StreamAnalyticsStreamInputEventhubV2#field_delimiter}.'''
        result = self._values.get("field_delimiter")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StreamAnalyticsStreamInputEventhubV2Serialization(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StreamAnalyticsStreamInputEventhubV2SerializationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.streamAnalyticsStreamInputEventhubV2.StreamAnalyticsStreamInputEventhubV2SerializationOutputReference",
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

    @jsii.member(jsii_name="resetEncoding")
    def reset_encoding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncoding", []))

    @jsii.member(jsii_name="resetFieldDelimiter")
    def reset_field_delimiter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFieldDelimiter", []))

    @builtins.property
    @jsii.member(jsii_name="encodingInput")
    def encoding_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encodingInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldDelimiterInput")
    def field_delimiter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldDelimiterInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="encoding")
    def encoding(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encoding"))

    @encoding.setter
    def encoding(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encoding", value)

    @builtins.property
    @jsii.member(jsii_name="fieldDelimiter")
    def field_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fieldDelimiter"))

    @field_delimiter.setter
    def field_delimiter(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fieldDelimiter", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StreamAnalyticsStreamInputEventhubV2Serialization]:
        return typing.cast(typing.Optional[StreamAnalyticsStreamInputEventhubV2Serialization], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StreamAnalyticsStreamInputEventhubV2Serialization],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[StreamAnalyticsStreamInputEventhubV2Serialization],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.streamAnalyticsStreamInputEventhubV2.StreamAnalyticsStreamInputEventhubV2Timeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class StreamAnalyticsStreamInputEventhubV2Timeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#create StreamAnalyticsStreamInputEventhubV2#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#delete StreamAnalyticsStreamInputEventhubV2#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#read StreamAnalyticsStreamInputEventhubV2#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#update StreamAnalyticsStreamInputEventhubV2#update}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#create StreamAnalyticsStreamInputEventhubV2#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#delete StreamAnalyticsStreamInputEventhubV2#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#read StreamAnalyticsStreamInputEventhubV2#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_stream_input_eventhub_v2#update StreamAnalyticsStreamInputEventhubV2#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StreamAnalyticsStreamInputEventhubV2Timeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StreamAnalyticsStreamInputEventhubV2TimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.streamAnalyticsStreamInputEventhubV2.StreamAnalyticsStreamInputEventhubV2TimeoutsOutputReference",
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
    ) -> typing.Optional[typing.Union[StreamAnalyticsStreamInputEventhubV2Timeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[StreamAnalyticsStreamInputEventhubV2Timeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[StreamAnalyticsStreamInputEventhubV2Timeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[StreamAnalyticsStreamInputEventhubV2Timeouts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "StreamAnalyticsStreamInputEventhubV2",
    "StreamAnalyticsStreamInputEventhubV2Config",
    "StreamAnalyticsStreamInputEventhubV2Serialization",
    "StreamAnalyticsStreamInputEventhubV2SerializationOutputReference",
    "StreamAnalyticsStreamInputEventhubV2Timeouts",
    "StreamAnalyticsStreamInputEventhubV2TimeoutsOutputReference",
]

publication.publish()
