'''
# `azurerm_machine_learning_compute_cluster`

Refer to the Terraform Registory for docs: [`azurerm_machine_learning_compute_cluster`](https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster).
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


class MachineLearningComputeCluster(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.machineLearningComputeCluster.MachineLearningComputeCluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster azurerm_machine_learning_compute_cluster}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        machine_learning_workspace_id: builtins.str,
        name: builtins.str,
        scale_settings: typing.Union["MachineLearningComputeClusterScaleSettings", typing.Dict[str, typing.Any]],
        vm_priority: builtins.str,
        vm_size: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["MachineLearningComputeClusterIdentity", typing.Dict[str, typing.Any]]] = None,
        local_auth_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ssh: typing.Optional[typing.Union["MachineLearningComputeClusterSsh", typing.Dict[str, typing.Any]]] = None,
        ssh_public_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        subnet_resource_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["MachineLearningComputeClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster azurerm_machine_learning_compute_cluster} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#location MachineLearningComputeCluster#location}.
        :param machine_learning_workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#machine_learning_workspace_id MachineLearningComputeCluster#machine_learning_workspace_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#name MachineLearningComputeCluster#name}.
        :param scale_settings: scale_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#scale_settings MachineLearningComputeCluster#scale_settings}
        :param vm_priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#vm_priority MachineLearningComputeCluster#vm_priority}.
        :param vm_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#vm_size MachineLearningComputeCluster#vm_size}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#description MachineLearningComputeCluster#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#id MachineLearningComputeCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#identity MachineLearningComputeCluster#identity}
        :param local_auth_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#local_auth_enabled MachineLearningComputeCluster#local_auth_enabled}.
        :param ssh: ssh block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#ssh MachineLearningComputeCluster#ssh}
        :param ssh_public_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#ssh_public_access_enabled MachineLearningComputeCluster#ssh_public_access_enabled}.
        :param subnet_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#subnet_resource_id MachineLearningComputeCluster#subnet_resource_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#tags MachineLearningComputeCluster#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#timeouts MachineLearningComputeCluster#timeouts}
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
                location: builtins.str,
                machine_learning_workspace_id: builtins.str,
                name: builtins.str,
                scale_settings: typing.Union[MachineLearningComputeClusterScaleSettings, typing.Dict[str, typing.Any]],
                vm_priority: builtins.str,
                vm_size: builtins.str,
                description: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                identity: typing.Optional[typing.Union[MachineLearningComputeClusterIdentity, typing.Dict[str, typing.Any]]] = None,
                local_auth_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                ssh: typing.Optional[typing.Union[MachineLearningComputeClusterSsh, typing.Dict[str, typing.Any]]] = None,
                ssh_public_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                subnet_resource_id: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[MachineLearningComputeClusterTimeouts, typing.Dict[str, typing.Any]]] = None,
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
        config = MachineLearningComputeClusterConfig(
            location=location,
            machine_learning_workspace_id=machine_learning_workspace_id,
            name=name,
            scale_settings=scale_settings,
            vm_priority=vm_priority,
            vm_size=vm_size,
            description=description,
            id=id,
            identity=identity,
            local_auth_enabled=local_auth_enabled,
            ssh=ssh,
            ssh_public_access_enabled=ssh_public_access_enabled,
            subnet_resource_id=subnet_resource_id,
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

    @jsii.member(jsii_name="putIdentity")
    def put_identity(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#type MachineLearningComputeCluster#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#identity_ids MachineLearningComputeCluster#identity_ids}.
        '''
        value = MachineLearningComputeClusterIdentity(
            type=type, identity_ids=identity_ids
        )

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="putScaleSettings")
    def put_scale_settings(
        self,
        *,
        max_node_count: jsii.Number,
        min_node_count: jsii.Number,
        scale_down_nodes_after_idle_duration: builtins.str,
    ) -> None:
        '''
        :param max_node_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#max_node_count MachineLearningComputeCluster#max_node_count}.
        :param min_node_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#min_node_count MachineLearningComputeCluster#min_node_count}.
        :param scale_down_nodes_after_idle_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#scale_down_nodes_after_idle_duration MachineLearningComputeCluster#scale_down_nodes_after_idle_duration}.
        '''
        value = MachineLearningComputeClusterScaleSettings(
            max_node_count=max_node_count,
            min_node_count=min_node_count,
            scale_down_nodes_after_idle_duration=scale_down_nodes_after_idle_duration,
        )

        return typing.cast(None, jsii.invoke(self, "putScaleSettings", [value]))

    @jsii.member(jsii_name="putSsh")
    def put_ssh(
        self,
        *,
        admin_username: builtins.str,
        admin_password: typing.Optional[builtins.str] = None,
        key_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param admin_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#admin_username MachineLearningComputeCluster#admin_username}.
        :param admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#admin_password MachineLearningComputeCluster#admin_password}.
        :param key_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#key_value MachineLearningComputeCluster#key_value}.
        '''
        value = MachineLearningComputeClusterSsh(
            admin_username=admin_username,
            admin_password=admin_password,
            key_value=key_value,
        )

        return typing.cast(None, jsii.invoke(self, "putSsh", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#create MachineLearningComputeCluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#delete MachineLearningComputeCluster#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#read MachineLearningComputeCluster#read}.
        '''
        value = MachineLearningComputeClusterTimeouts(
            create=create, delete=delete, read=read
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetLocalAuthEnabled")
    def reset_local_auth_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalAuthEnabled", []))

    @jsii.member(jsii_name="resetSsh")
    def reset_ssh(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSsh", []))

    @jsii.member(jsii_name="resetSshPublicAccessEnabled")
    def reset_ssh_public_access_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSshPublicAccessEnabled", []))

    @jsii.member(jsii_name="resetSubnetResourceId")
    def reset_subnet_resource_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetResourceId", []))

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
    @jsii.member(jsii_name="identity")
    def identity(self) -> "MachineLearningComputeClusterIdentityOutputReference":
        return typing.cast("MachineLearningComputeClusterIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="scaleSettings")
    def scale_settings(
        self,
    ) -> "MachineLearningComputeClusterScaleSettingsOutputReference":
        return typing.cast("MachineLearningComputeClusterScaleSettingsOutputReference", jsii.get(self, "scaleSettings"))

    @builtins.property
    @jsii.member(jsii_name="ssh")
    def ssh(self) -> "MachineLearningComputeClusterSshOutputReference":
        return typing.cast("MachineLearningComputeClusterSshOutputReference", jsii.get(self, "ssh"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MachineLearningComputeClusterTimeoutsOutputReference":
        return typing.cast("MachineLearningComputeClusterTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(
        self,
    ) -> typing.Optional["MachineLearningComputeClusterIdentity"]:
        return typing.cast(typing.Optional["MachineLearningComputeClusterIdentity"], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="localAuthEnabledInput")
    def local_auth_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "localAuthEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="machineLearningWorkspaceIdInput")
    def machine_learning_workspace_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "machineLearningWorkspaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleSettingsInput")
    def scale_settings_input(
        self,
    ) -> typing.Optional["MachineLearningComputeClusterScaleSettings"]:
        return typing.cast(typing.Optional["MachineLearningComputeClusterScaleSettings"], jsii.get(self, "scaleSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="sshInput")
    def ssh_input(self) -> typing.Optional["MachineLearningComputeClusterSsh"]:
        return typing.cast(typing.Optional["MachineLearningComputeClusterSsh"], jsii.get(self, "sshInput"))

    @builtins.property
    @jsii.member(jsii_name="sshPublicAccessEnabledInput")
    def ssh_public_access_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "sshPublicAccessEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetResourceIdInput")
    def subnet_resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetResourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MachineLearningComputeClusterTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MachineLearningComputeClusterTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="vmPriorityInput")
    def vm_priority_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vmPriorityInput"))

    @builtins.property
    @jsii.member(jsii_name="vmSizeInput")
    def vm_size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vmSizeInput"))

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
    @jsii.member(jsii_name="localAuthEnabled")
    def local_auth_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "localAuthEnabled"))

    @local_auth_enabled.setter
    def local_auth_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localAuthEnabled", value)

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
    @jsii.member(jsii_name="machineLearningWorkspaceId")
    def machine_learning_workspace_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "machineLearningWorkspaceId"))

    @machine_learning_workspace_id.setter
    def machine_learning_workspace_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "machineLearningWorkspaceId", value)

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
    @jsii.member(jsii_name="sshPublicAccessEnabled")
    def ssh_public_access_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "sshPublicAccessEnabled"))

    @ssh_public_access_enabled.setter
    def ssh_public_access_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshPublicAccessEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="subnetResourceId")
    def subnet_resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetResourceId"))

    @subnet_resource_id.setter
    def subnet_resource_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetResourceId", value)

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
    @jsii.member(jsii_name="vmPriority")
    def vm_priority(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vmPriority"))

    @vm_priority.setter
    def vm_priority(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vmPriority", value)

    @builtins.property
    @jsii.member(jsii_name="vmSize")
    def vm_size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vmSize"))

    @vm_size.setter
    def vm_size(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vmSize", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.machineLearningComputeCluster.MachineLearningComputeClusterConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "location": "location",
        "machine_learning_workspace_id": "machineLearningWorkspaceId",
        "name": "name",
        "scale_settings": "scaleSettings",
        "vm_priority": "vmPriority",
        "vm_size": "vmSize",
        "description": "description",
        "id": "id",
        "identity": "identity",
        "local_auth_enabled": "localAuthEnabled",
        "ssh": "ssh",
        "ssh_public_access_enabled": "sshPublicAccessEnabled",
        "subnet_resource_id": "subnetResourceId",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class MachineLearningComputeClusterConfig(cdktf.TerraformMetaArguments):
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
        location: builtins.str,
        machine_learning_workspace_id: builtins.str,
        name: builtins.str,
        scale_settings: typing.Union["MachineLearningComputeClusterScaleSettings", typing.Dict[str, typing.Any]],
        vm_priority: builtins.str,
        vm_size: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["MachineLearningComputeClusterIdentity", typing.Dict[str, typing.Any]]] = None,
        local_auth_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ssh: typing.Optional[typing.Union["MachineLearningComputeClusterSsh", typing.Dict[str, typing.Any]]] = None,
        ssh_public_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        subnet_resource_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["MachineLearningComputeClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#location MachineLearningComputeCluster#location}.
        :param machine_learning_workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#machine_learning_workspace_id MachineLearningComputeCluster#machine_learning_workspace_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#name MachineLearningComputeCluster#name}.
        :param scale_settings: scale_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#scale_settings MachineLearningComputeCluster#scale_settings}
        :param vm_priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#vm_priority MachineLearningComputeCluster#vm_priority}.
        :param vm_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#vm_size MachineLearningComputeCluster#vm_size}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#description MachineLearningComputeCluster#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#id MachineLearningComputeCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#identity MachineLearningComputeCluster#identity}
        :param local_auth_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#local_auth_enabled MachineLearningComputeCluster#local_auth_enabled}.
        :param ssh: ssh block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#ssh MachineLearningComputeCluster#ssh}
        :param ssh_public_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#ssh_public_access_enabled MachineLearningComputeCluster#ssh_public_access_enabled}.
        :param subnet_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#subnet_resource_id MachineLearningComputeCluster#subnet_resource_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#tags MachineLearningComputeCluster#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#timeouts MachineLearningComputeCluster#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(scale_settings, dict):
            scale_settings = MachineLearningComputeClusterScaleSettings(**scale_settings)
        if isinstance(identity, dict):
            identity = MachineLearningComputeClusterIdentity(**identity)
        if isinstance(ssh, dict):
            ssh = MachineLearningComputeClusterSsh(**ssh)
        if isinstance(timeouts, dict):
            timeouts = MachineLearningComputeClusterTimeouts(**timeouts)
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
                location: builtins.str,
                machine_learning_workspace_id: builtins.str,
                name: builtins.str,
                scale_settings: typing.Union[MachineLearningComputeClusterScaleSettings, typing.Dict[str, typing.Any]],
                vm_priority: builtins.str,
                vm_size: builtins.str,
                description: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                identity: typing.Optional[typing.Union[MachineLearningComputeClusterIdentity, typing.Dict[str, typing.Any]]] = None,
                local_auth_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                ssh: typing.Optional[typing.Union[MachineLearningComputeClusterSsh, typing.Dict[str, typing.Any]]] = None,
                ssh_public_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                subnet_resource_id: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[MachineLearningComputeClusterTimeouts, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument machine_learning_workspace_id", value=machine_learning_workspace_id, expected_type=type_hints["machine_learning_workspace_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument scale_settings", value=scale_settings, expected_type=type_hints["scale_settings"])
            check_type(argname="argument vm_priority", value=vm_priority, expected_type=type_hints["vm_priority"])
            check_type(argname="argument vm_size", value=vm_size, expected_type=type_hints["vm_size"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument local_auth_enabled", value=local_auth_enabled, expected_type=type_hints["local_auth_enabled"])
            check_type(argname="argument ssh", value=ssh, expected_type=type_hints["ssh"])
            check_type(argname="argument ssh_public_access_enabled", value=ssh_public_access_enabled, expected_type=type_hints["ssh_public_access_enabled"])
            check_type(argname="argument subnet_resource_id", value=subnet_resource_id, expected_type=type_hints["subnet_resource_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
            "machine_learning_workspace_id": machine_learning_workspace_id,
            "name": name,
            "scale_settings": scale_settings,
            "vm_priority": vm_priority,
            "vm_size": vm_size,
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
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if identity is not None:
            self._values["identity"] = identity
        if local_auth_enabled is not None:
            self._values["local_auth_enabled"] = local_auth_enabled
        if ssh is not None:
            self._values["ssh"] = ssh
        if ssh_public_access_enabled is not None:
            self._values["ssh_public_access_enabled"] = ssh_public_access_enabled
        if subnet_resource_id is not None:
            self._values["subnet_resource_id"] = subnet_resource_id
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
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#location MachineLearningComputeCluster#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def machine_learning_workspace_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#machine_learning_workspace_id MachineLearningComputeCluster#machine_learning_workspace_id}.'''
        result = self._values.get("machine_learning_workspace_id")
        assert result is not None, "Required property 'machine_learning_workspace_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#name MachineLearningComputeCluster#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scale_settings(self) -> "MachineLearningComputeClusterScaleSettings":
        '''scale_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#scale_settings MachineLearningComputeCluster#scale_settings}
        '''
        result = self._values.get("scale_settings")
        assert result is not None, "Required property 'scale_settings' is missing"
        return typing.cast("MachineLearningComputeClusterScaleSettings", result)

    @builtins.property
    def vm_priority(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#vm_priority MachineLearningComputeCluster#vm_priority}.'''
        result = self._values.get("vm_priority")
        assert result is not None, "Required property 'vm_priority' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vm_size(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#vm_size MachineLearningComputeCluster#vm_size}.'''
        result = self._values.get("vm_size")
        assert result is not None, "Required property 'vm_size' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#description MachineLearningComputeCluster#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#id MachineLearningComputeCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["MachineLearningComputeClusterIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#identity MachineLearningComputeCluster#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["MachineLearningComputeClusterIdentity"], result)

    @builtins.property
    def local_auth_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#local_auth_enabled MachineLearningComputeCluster#local_auth_enabled}.'''
        result = self._values.get("local_auth_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ssh(self) -> typing.Optional["MachineLearningComputeClusterSsh"]:
        '''ssh block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#ssh MachineLearningComputeCluster#ssh}
        '''
        result = self._values.get("ssh")
        return typing.cast(typing.Optional["MachineLearningComputeClusterSsh"], result)

    @builtins.property
    def ssh_public_access_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#ssh_public_access_enabled MachineLearningComputeCluster#ssh_public_access_enabled}.'''
        result = self._values.get("ssh_public_access_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def subnet_resource_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#subnet_resource_id MachineLearningComputeCluster#subnet_resource_id}.'''
        result = self._values.get("subnet_resource_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#tags MachineLearningComputeCluster#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MachineLearningComputeClusterTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#timeouts MachineLearningComputeCluster#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MachineLearningComputeClusterTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MachineLearningComputeClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.machineLearningComputeCluster.MachineLearningComputeClusterIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "identity_ids": "identityIds"},
)
class MachineLearningComputeClusterIdentity:
    def __init__(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#type MachineLearningComputeCluster#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#identity_ids MachineLearningComputeCluster#identity_ids}.
        '''
        if __debug__:
            def stub(
                *,
                type: builtins.str,
                identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument identity_ids", value=identity_ids, expected_type=type_hints["identity_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if identity_ids is not None:
            self._values["identity_ids"] = identity_ids

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#type MachineLearningComputeCluster#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#identity_ids MachineLearningComputeCluster#identity_ids}.'''
        result = self._values.get("identity_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MachineLearningComputeClusterIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MachineLearningComputeClusterIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.machineLearningComputeCluster.MachineLearningComputeClusterIdentityOutputReference",
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

    @jsii.member(jsii_name="resetIdentityIds")
    def reset_identity_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityIds", []))

    @builtins.property
    @jsii.member(jsii_name="principalId")
    def principal_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principalId"))

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @builtins.property
    @jsii.member(jsii_name="identityIdsInput")
    def identity_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "identityIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="identityIds")
    def identity_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "identityIds"))

    @identity_ids.setter
    def identity_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityIds", value)

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
    def internal_value(self) -> typing.Optional[MachineLearningComputeClusterIdentity]:
        return typing.cast(typing.Optional[MachineLearningComputeClusterIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MachineLearningComputeClusterIdentity],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MachineLearningComputeClusterIdentity],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.machineLearningComputeCluster.MachineLearningComputeClusterScaleSettings",
    jsii_struct_bases=[],
    name_mapping={
        "max_node_count": "maxNodeCount",
        "min_node_count": "minNodeCount",
        "scale_down_nodes_after_idle_duration": "scaleDownNodesAfterIdleDuration",
    },
)
class MachineLearningComputeClusterScaleSettings:
    def __init__(
        self,
        *,
        max_node_count: jsii.Number,
        min_node_count: jsii.Number,
        scale_down_nodes_after_idle_duration: builtins.str,
    ) -> None:
        '''
        :param max_node_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#max_node_count MachineLearningComputeCluster#max_node_count}.
        :param min_node_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#min_node_count MachineLearningComputeCluster#min_node_count}.
        :param scale_down_nodes_after_idle_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#scale_down_nodes_after_idle_duration MachineLearningComputeCluster#scale_down_nodes_after_idle_duration}.
        '''
        if __debug__:
            def stub(
                *,
                max_node_count: jsii.Number,
                min_node_count: jsii.Number,
                scale_down_nodes_after_idle_duration: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument max_node_count", value=max_node_count, expected_type=type_hints["max_node_count"])
            check_type(argname="argument min_node_count", value=min_node_count, expected_type=type_hints["min_node_count"])
            check_type(argname="argument scale_down_nodes_after_idle_duration", value=scale_down_nodes_after_idle_duration, expected_type=type_hints["scale_down_nodes_after_idle_duration"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_node_count": max_node_count,
            "min_node_count": min_node_count,
            "scale_down_nodes_after_idle_duration": scale_down_nodes_after_idle_duration,
        }

    @builtins.property
    def max_node_count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#max_node_count MachineLearningComputeCluster#max_node_count}.'''
        result = self._values.get("max_node_count")
        assert result is not None, "Required property 'max_node_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_node_count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#min_node_count MachineLearningComputeCluster#min_node_count}.'''
        result = self._values.get("min_node_count")
        assert result is not None, "Required property 'min_node_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def scale_down_nodes_after_idle_duration(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#scale_down_nodes_after_idle_duration MachineLearningComputeCluster#scale_down_nodes_after_idle_duration}.'''
        result = self._values.get("scale_down_nodes_after_idle_duration")
        assert result is not None, "Required property 'scale_down_nodes_after_idle_duration' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MachineLearningComputeClusterScaleSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MachineLearningComputeClusterScaleSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.machineLearningComputeCluster.MachineLearningComputeClusterScaleSettingsOutputReference",
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
    @jsii.member(jsii_name="maxNodeCountInput")
    def max_node_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxNodeCountInput"))

    @builtins.property
    @jsii.member(jsii_name="minNodeCountInput")
    def min_node_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minNodeCountInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleDownNodesAfterIdleDurationInput")
    def scale_down_nodes_after_idle_duration_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scaleDownNodesAfterIdleDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="maxNodeCount")
    def max_node_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxNodeCount"))

    @max_node_count.setter
    def max_node_count(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxNodeCount", value)

    @builtins.property
    @jsii.member(jsii_name="minNodeCount")
    def min_node_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minNodeCount"))

    @min_node_count.setter
    def min_node_count(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minNodeCount", value)

    @builtins.property
    @jsii.member(jsii_name="scaleDownNodesAfterIdleDuration")
    def scale_down_nodes_after_idle_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scaleDownNodesAfterIdleDuration"))

    @scale_down_nodes_after_idle_duration.setter
    def scale_down_nodes_after_idle_duration(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleDownNodesAfterIdleDuration", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MachineLearningComputeClusterScaleSettings]:
        return typing.cast(typing.Optional[MachineLearningComputeClusterScaleSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MachineLearningComputeClusterScaleSettings],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MachineLearningComputeClusterScaleSettings],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.machineLearningComputeCluster.MachineLearningComputeClusterSsh",
    jsii_struct_bases=[],
    name_mapping={
        "admin_username": "adminUsername",
        "admin_password": "adminPassword",
        "key_value": "keyValue",
    },
)
class MachineLearningComputeClusterSsh:
    def __init__(
        self,
        *,
        admin_username: builtins.str,
        admin_password: typing.Optional[builtins.str] = None,
        key_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param admin_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#admin_username MachineLearningComputeCluster#admin_username}.
        :param admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#admin_password MachineLearningComputeCluster#admin_password}.
        :param key_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#key_value MachineLearningComputeCluster#key_value}.
        '''
        if __debug__:
            def stub(
                *,
                admin_username: builtins.str,
                admin_password: typing.Optional[builtins.str] = None,
                key_value: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument admin_username", value=admin_username, expected_type=type_hints["admin_username"])
            check_type(argname="argument admin_password", value=admin_password, expected_type=type_hints["admin_password"])
            check_type(argname="argument key_value", value=key_value, expected_type=type_hints["key_value"])
        self._values: typing.Dict[str, typing.Any] = {
            "admin_username": admin_username,
        }
        if admin_password is not None:
            self._values["admin_password"] = admin_password
        if key_value is not None:
            self._values["key_value"] = key_value

    @builtins.property
    def admin_username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#admin_username MachineLearningComputeCluster#admin_username}.'''
        result = self._values.get("admin_username")
        assert result is not None, "Required property 'admin_username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def admin_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#admin_password MachineLearningComputeCluster#admin_password}.'''
        result = self._values.get("admin_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#key_value MachineLearningComputeCluster#key_value}.'''
        result = self._values.get("key_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MachineLearningComputeClusterSsh(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MachineLearningComputeClusterSshOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.machineLearningComputeCluster.MachineLearningComputeClusterSshOutputReference",
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

    @jsii.member(jsii_name="resetAdminPassword")
    def reset_admin_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminPassword", []))

    @jsii.member(jsii_name="resetKeyValue")
    def reset_key_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyValue", []))

    @builtins.property
    @jsii.member(jsii_name="adminPasswordInput")
    def admin_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="adminUsernameInput")
    def admin_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="keyValueInput")
    def key_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyValueInput"))

    @builtins.property
    @jsii.member(jsii_name="adminPassword")
    def admin_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminPassword"))

    @admin_password.setter
    def admin_password(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminPassword", value)

    @builtins.property
    @jsii.member(jsii_name="adminUsername")
    def admin_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminUsername"))

    @admin_username.setter
    def admin_username(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminUsername", value)

    @builtins.property
    @jsii.member(jsii_name="keyValue")
    def key_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyValue"))

    @key_value.setter
    def key_value(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MachineLearningComputeClusterSsh]:
        return typing.cast(typing.Optional[MachineLearningComputeClusterSsh], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MachineLearningComputeClusterSsh],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[MachineLearningComputeClusterSsh]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.machineLearningComputeCluster.MachineLearningComputeClusterTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "read": "read"},
)
class MachineLearningComputeClusterTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#create MachineLearningComputeCluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#delete MachineLearningComputeCluster#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#read MachineLearningComputeCluster#read}.
        '''
        if __debug__:
            def stub(
                *,
                create: typing.Optional[builtins.str] = None,
                delete: typing.Optional[builtins.str] = None,
                read: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#create MachineLearningComputeCluster#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#delete MachineLearningComputeCluster#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_compute_cluster#read MachineLearningComputeCluster#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MachineLearningComputeClusterTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MachineLearningComputeClusterTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.machineLearningComputeCluster.MachineLearningComputeClusterTimeoutsOutputReference",
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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MachineLearningComputeClusterTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MachineLearningComputeClusterTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MachineLearningComputeClusterTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[MachineLearningComputeClusterTimeouts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MachineLearningComputeCluster",
    "MachineLearningComputeClusterConfig",
    "MachineLearningComputeClusterIdentity",
    "MachineLearningComputeClusterIdentityOutputReference",
    "MachineLearningComputeClusterScaleSettings",
    "MachineLearningComputeClusterScaleSettingsOutputReference",
    "MachineLearningComputeClusterSsh",
    "MachineLearningComputeClusterSshOutputReference",
    "MachineLearningComputeClusterTimeouts",
    "MachineLearningComputeClusterTimeoutsOutputReference",
]

publication.publish()
