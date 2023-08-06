'''
# `azurerm_api_management_backend`

Refer to the Terraform Registory for docs: [`azurerm_api_management_backend`](https://www.terraform.io/docs/providers/azurerm/r/api_management_backend).
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


class ApiManagementBackend(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementBackend.ApiManagementBackend",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend azurerm_api_management_backend}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        api_management_name: builtins.str,
        name: builtins.str,
        protocol: builtins.str,
        resource_group_name: builtins.str,
        url: builtins.str,
        credentials: typing.Optional[typing.Union["ApiManagementBackendCredentials", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        proxy: typing.Optional[typing.Union["ApiManagementBackendProxy", typing.Dict[str, typing.Any]]] = None,
        resource_id: typing.Optional[builtins.str] = None,
        service_fabric_cluster: typing.Optional[typing.Union["ApiManagementBackendServiceFabricCluster", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["ApiManagementBackendTimeouts", typing.Dict[str, typing.Any]]] = None,
        title: typing.Optional[builtins.str] = None,
        tls: typing.Optional[typing.Union["ApiManagementBackendTls", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend azurerm_api_management_backend} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param api_management_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#api_management_name ApiManagementBackend#api_management_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#name ApiManagementBackend#name}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#protocol ApiManagementBackend#protocol}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#resource_group_name ApiManagementBackend#resource_group_name}.
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#url ApiManagementBackend#url}.
        :param credentials: credentials block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#credentials ApiManagementBackend#credentials}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#description ApiManagementBackend#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#id ApiManagementBackend#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param proxy: proxy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#proxy ApiManagementBackend#proxy}
        :param resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#resource_id ApiManagementBackend#resource_id}.
        :param service_fabric_cluster: service_fabric_cluster block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#service_fabric_cluster ApiManagementBackend#service_fabric_cluster}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#timeouts ApiManagementBackend#timeouts}
        :param title: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#title ApiManagementBackend#title}.
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#tls ApiManagementBackend#tls}
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
                api_management_name: builtins.str,
                name: builtins.str,
                protocol: builtins.str,
                resource_group_name: builtins.str,
                url: builtins.str,
                credentials: typing.Optional[typing.Union[ApiManagementBackendCredentials, typing.Dict[str, typing.Any]]] = None,
                description: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                proxy: typing.Optional[typing.Union[ApiManagementBackendProxy, typing.Dict[str, typing.Any]]] = None,
                resource_id: typing.Optional[builtins.str] = None,
                service_fabric_cluster: typing.Optional[typing.Union[ApiManagementBackendServiceFabricCluster, typing.Dict[str, typing.Any]]] = None,
                timeouts: typing.Optional[typing.Union[ApiManagementBackendTimeouts, typing.Dict[str, typing.Any]]] = None,
                title: typing.Optional[builtins.str] = None,
                tls: typing.Optional[typing.Union[ApiManagementBackendTls, typing.Dict[str, typing.Any]]] = None,
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
        config = ApiManagementBackendConfig(
            api_management_name=api_management_name,
            name=name,
            protocol=protocol,
            resource_group_name=resource_group_name,
            url=url,
            credentials=credentials,
            description=description,
            id=id,
            proxy=proxy,
            resource_id=resource_id,
            service_fabric_cluster=service_fabric_cluster,
            timeouts=timeouts,
            title=title,
            tls=tls,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCredentials")
    def put_credentials(
        self,
        *,
        authorization: typing.Optional[typing.Union["ApiManagementBackendCredentialsAuthorization", typing.Dict[str, typing.Any]]] = None,
        certificate: typing.Optional[typing.Sequence[builtins.str]] = None,
        header: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        query: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param authorization: authorization block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#authorization ApiManagementBackend#authorization}
        :param certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#certificate ApiManagementBackend#certificate}.
        :param header: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#header ApiManagementBackend#header}.
        :param query: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#query ApiManagementBackend#query}.
        '''
        value = ApiManagementBackendCredentials(
            authorization=authorization,
            certificate=certificate,
            header=header,
            query=query,
        )

        return typing.cast(None, jsii.invoke(self, "putCredentials", [value]))

    @jsii.member(jsii_name="putProxy")
    def put_proxy(
        self,
        *,
        url: builtins.str,
        username: builtins.str,
        password: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#url ApiManagementBackend#url}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#username ApiManagementBackend#username}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#password ApiManagementBackend#password}.
        '''
        value = ApiManagementBackendProxy(
            url=url, username=username, password=password
        )

        return typing.cast(None, jsii.invoke(self, "putProxy", [value]))

    @jsii.member(jsii_name="putServiceFabricCluster")
    def put_service_fabric_cluster(
        self,
        *,
        management_endpoints: typing.Sequence[builtins.str],
        max_partition_resolution_retries: jsii.Number,
        client_certificate_id: typing.Optional[builtins.str] = None,
        client_certificate_thumbprint: typing.Optional[builtins.str] = None,
        server_certificate_thumbprints: typing.Optional[typing.Sequence[builtins.str]] = None,
        server_x509_name: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementBackendServiceFabricClusterServerX509Name", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param management_endpoints: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#management_endpoints ApiManagementBackend#management_endpoints}.
        :param max_partition_resolution_retries: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#max_partition_resolution_retries ApiManagementBackend#max_partition_resolution_retries}.
        :param client_certificate_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#client_certificate_id ApiManagementBackend#client_certificate_id}.
        :param client_certificate_thumbprint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#client_certificate_thumbprint ApiManagementBackend#client_certificate_thumbprint}.
        :param server_certificate_thumbprints: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#server_certificate_thumbprints ApiManagementBackend#server_certificate_thumbprints}.
        :param server_x509_name: server_x509_name block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#server_x509_name ApiManagementBackend#server_x509_name}
        '''
        value = ApiManagementBackendServiceFabricCluster(
            management_endpoints=management_endpoints,
            max_partition_resolution_retries=max_partition_resolution_retries,
            client_certificate_id=client_certificate_id,
            client_certificate_thumbprint=client_certificate_thumbprint,
            server_certificate_thumbprints=server_certificate_thumbprints,
            server_x509_name=server_x509_name,
        )

        return typing.cast(None, jsii.invoke(self, "putServiceFabricCluster", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#create ApiManagementBackend#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#delete ApiManagementBackend#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#read ApiManagementBackend#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#update ApiManagementBackend#update}.
        '''
        value = ApiManagementBackendTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putTls")
    def put_tls(
        self,
        *,
        validate_certificate_chain: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        validate_certificate_name: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param validate_certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#validate_certificate_chain ApiManagementBackend#validate_certificate_chain}.
        :param validate_certificate_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#validate_certificate_name ApiManagementBackend#validate_certificate_name}.
        '''
        value = ApiManagementBackendTls(
            validate_certificate_chain=validate_certificate_chain,
            validate_certificate_name=validate_certificate_name,
        )

        return typing.cast(None, jsii.invoke(self, "putTls", [value]))

    @jsii.member(jsii_name="resetCredentials")
    def reset_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCredentials", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProxy")
    def reset_proxy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProxy", []))

    @jsii.member(jsii_name="resetResourceId")
    def reset_resource_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceId", []))

    @jsii.member(jsii_name="resetServiceFabricCluster")
    def reset_service_fabric_cluster(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceFabricCluster", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTitle")
    def reset_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTitle", []))

    @jsii.member(jsii_name="resetTls")
    def reset_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTls", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="credentials")
    def credentials(self) -> "ApiManagementBackendCredentialsOutputReference":
        return typing.cast("ApiManagementBackendCredentialsOutputReference", jsii.get(self, "credentials"))

    @builtins.property
    @jsii.member(jsii_name="proxy")
    def proxy(self) -> "ApiManagementBackendProxyOutputReference":
        return typing.cast("ApiManagementBackendProxyOutputReference", jsii.get(self, "proxy"))

    @builtins.property
    @jsii.member(jsii_name="serviceFabricCluster")
    def service_fabric_cluster(
        self,
    ) -> "ApiManagementBackendServiceFabricClusterOutputReference":
        return typing.cast("ApiManagementBackendServiceFabricClusterOutputReference", jsii.get(self, "serviceFabricCluster"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ApiManagementBackendTimeoutsOutputReference":
        return typing.cast("ApiManagementBackendTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="tls")
    def tls(self) -> "ApiManagementBackendTlsOutputReference":
        return typing.cast("ApiManagementBackendTlsOutputReference", jsii.get(self, "tls"))

    @builtins.property
    @jsii.member(jsii_name="apiManagementNameInput")
    def api_management_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiManagementNameInput"))

    @builtins.property
    @jsii.member(jsii_name="credentialsInput")
    def credentials_input(self) -> typing.Optional["ApiManagementBackendCredentials"]:
        return typing.cast(typing.Optional["ApiManagementBackendCredentials"], jsii.get(self, "credentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="proxyInput")
    def proxy_input(self) -> typing.Optional["ApiManagementBackendProxy"]:
        return typing.cast(typing.Optional["ApiManagementBackendProxy"], jsii.get(self, "proxyInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceIdInput")
    def resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceFabricClusterInput")
    def service_fabric_cluster_input(
        self,
    ) -> typing.Optional["ApiManagementBackendServiceFabricCluster"]:
        return typing.cast(typing.Optional["ApiManagementBackendServiceFabricCluster"], jsii.get(self, "serviceFabricClusterInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ApiManagementBackendTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ApiManagementBackendTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsInput")
    def tls_input(self) -> typing.Optional["ApiManagementBackendTls"]:
        return typing.cast(typing.Optional["ApiManagementBackendTls"], jsii.get(self, "tlsInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="apiManagementName")
    def api_management_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiManagementName"))

    @api_management_name.setter
    def api_management_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiManagementName", value)

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
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceId"))

    @resource_id.setter
    def resource_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceId", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementBackend.ApiManagementBackendConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "api_management_name": "apiManagementName",
        "name": "name",
        "protocol": "protocol",
        "resource_group_name": "resourceGroupName",
        "url": "url",
        "credentials": "credentials",
        "description": "description",
        "id": "id",
        "proxy": "proxy",
        "resource_id": "resourceId",
        "service_fabric_cluster": "serviceFabricCluster",
        "timeouts": "timeouts",
        "title": "title",
        "tls": "tls",
    },
)
class ApiManagementBackendConfig(cdktf.TerraformMetaArguments):
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
        api_management_name: builtins.str,
        name: builtins.str,
        protocol: builtins.str,
        resource_group_name: builtins.str,
        url: builtins.str,
        credentials: typing.Optional[typing.Union["ApiManagementBackendCredentials", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        proxy: typing.Optional[typing.Union["ApiManagementBackendProxy", typing.Dict[str, typing.Any]]] = None,
        resource_id: typing.Optional[builtins.str] = None,
        service_fabric_cluster: typing.Optional[typing.Union["ApiManagementBackendServiceFabricCluster", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["ApiManagementBackendTimeouts", typing.Dict[str, typing.Any]]] = None,
        title: typing.Optional[builtins.str] = None,
        tls: typing.Optional[typing.Union["ApiManagementBackendTls", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param api_management_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#api_management_name ApiManagementBackend#api_management_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#name ApiManagementBackend#name}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#protocol ApiManagementBackend#protocol}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#resource_group_name ApiManagementBackend#resource_group_name}.
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#url ApiManagementBackend#url}.
        :param credentials: credentials block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#credentials ApiManagementBackend#credentials}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#description ApiManagementBackend#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#id ApiManagementBackend#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param proxy: proxy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#proxy ApiManagementBackend#proxy}
        :param resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#resource_id ApiManagementBackend#resource_id}.
        :param service_fabric_cluster: service_fabric_cluster block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#service_fabric_cluster ApiManagementBackend#service_fabric_cluster}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#timeouts ApiManagementBackend#timeouts}
        :param title: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#title ApiManagementBackend#title}.
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#tls ApiManagementBackend#tls}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(credentials, dict):
            credentials = ApiManagementBackendCredentials(**credentials)
        if isinstance(proxy, dict):
            proxy = ApiManagementBackendProxy(**proxy)
        if isinstance(service_fabric_cluster, dict):
            service_fabric_cluster = ApiManagementBackendServiceFabricCluster(**service_fabric_cluster)
        if isinstance(timeouts, dict):
            timeouts = ApiManagementBackendTimeouts(**timeouts)
        if isinstance(tls, dict):
            tls = ApiManagementBackendTls(**tls)
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
                api_management_name: builtins.str,
                name: builtins.str,
                protocol: builtins.str,
                resource_group_name: builtins.str,
                url: builtins.str,
                credentials: typing.Optional[typing.Union[ApiManagementBackendCredentials, typing.Dict[str, typing.Any]]] = None,
                description: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                proxy: typing.Optional[typing.Union[ApiManagementBackendProxy, typing.Dict[str, typing.Any]]] = None,
                resource_id: typing.Optional[builtins.str] = None,
                service_fabric_cluster: typing.Optional[typing.Union[ApiManagementBackendServiceFabricCluster, typing.Dict[str, typing.Any]]] = None,
                timeouts: typing.Optional[typing.Union[ApiManagementBackendTimeouts, typing.Dict[str, typing.Any]]] = None,
                title: typing.Optional[builtins.str] = None,
                tls: typing.Optional[typing.Union[ApiManagementBackendTls, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument api_management_name", value=api_management_name, expected_type=type_hints["api_management_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument proxy", value=proxy, expected_type=type_hints["proxy"])
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
            check_type(argname="argument service_fabric_cluster", value=service_fabric_cluster, expected_type=type_hints["service_fabric_cluster"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_management_name": api_management_name,
            "name": name,
            "protocol": protocol,
            "resource_group_name": resource_group_name,
            "url": url,
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
        if credentials is not None:
            self._values["credentials"] = credentials
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if proxy is not None:
            self._values["proxy"] = proxy
        if resource_id is not None:
            self._values["resource_id"] = resource_id
        if service_fabric_cluster is not None:
            self._values["service_fabric_cluster"] = service_fabric_cluster
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if title is not None:
            self._values["title"] = title
        if tls is not None:
            self._values["tls"] = tls

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
    def api_management_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#api_management_name ApiManagementBackend#api_management_name}.'''
        result = self._values.get("api_management_name")
        assert result is not None, "Required property 'api_management_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#name ApiManagementBackend#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#protocol ApiManagementBackend#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#resource_group_name ApiManagementBackend#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#url ApiManagementBackend#url}.'''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def credentials(self) -> typing.Optional["ApiManagementBackendCredentials"]:
        '''credentials block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#credentials ApiManagementBackend#credentials}
        '''
        result = self._values.get("credentials")
        return typing.cast(typing.Optional["ApiManagementBackendCredentials"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#description ApiManagementBackend#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#id ApiManagementBackend#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def proxy(self) -> typing.Optional["ApiManagementBackendProxy"]:
        '''proxy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#proxy ApiManagementBackend#proxy}
        '''
        result = self._values.get("proxy")
        return typing.cast(typing.Optional["ApiManagementBackendProxy"], result)

    @builtins.property
    def resource_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#resource_id ApiManagementBackend#resource_id}.'''
        result = self._values.get("resource_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_fabric_cluster(
        self,
    ) -> typing.Optional["ApiManagementBackendServiceFabricCluster"]:
        '''service_fabric_cluster block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#service_fabric_cluster ApiManagementBackend#service_fabric_cluster}
        '''
        result = self._values.get("service_fabric_cluster")
        return typing.cast(typing.Optional["ApiManagementBackendServiceFabricCluster"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ApiManagementBackendTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#timeouts ApiManagementBackend#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ApiManagementBackendTimeouts"], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#title ApiManagementBackend#title}.'''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls(self) -> typing.Optional["ApiManagementBackendTls"]:
        '''tls block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#tls ApiManagementBackend#tls}
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional["ApiManagementBackendTls"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementBackendConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementBackend.ApiManagementBackendCredentials",
    jsii_struct_bases=[],
    name_mapping={
        "authorization": "authorization",
        "certificate": "certificate",
        "header": "header",
        "query": "query",
    },
)
class ApiManagementBackendCredentials:
    def __init__(
        self,
        *,
        authorization: typing.Optional[typing.Union["ApiManagementBackendCredentialsAuthorization", typing.Dict[str, typing.Any]]] = None,
        certificate: typing.Optional[typing.Sequence[builtins.str]] = None,
        header: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        query: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param authorization: authorization block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#authorization ApiManagementBackend#authorization}
        :param certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#certificate ApiManagementBackend#certificate}.
        :param header: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#header ApiManagementBackend#header}.
        :param query: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#query ApiManagementBackend#query}.
        '''
        if isinstance(authorization, dict):
            authorization = ApiManagementBackendCredentialsAuthorization(**authorization)
        if __debug__:
            def stub(
                *,
                authorization: typing.Optional[typing.Union[ApiManagementBackendCredentialsAuthorization, typing.Dict[str, typing.Any]]] = None,
                certificate: typing.Optional[typing.Sequence[builtins.str]] = None,
                header: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                query: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument authorization", value=authorization, expected_type=type_hints["authorization"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument header", value=header, expected_type=type_hints["header"])
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
        self._values: typing.Dict[str, typing.Any] = {}
        if authorization is not None:
            self._values["authorization"] = authorization
        if certificate is not None:
            self._values["certificate"] = certificate
        if header is not None:
            self._values["header"] = header
        if query is not None:
            self._values["query"] = query

    @builtins.property
    def authorization(
        self,
    ) -> typing.Optional["ApiManagementBackendCredentialsAuthorization"]:
        '''authorization block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#authorization ApiManagementBackend#authorization}
        '''
        result = self._values.get("authorization")
        return typing.cast(typing.Optional["ApiManagementBackendCredentialsAuthorization"], result)

    @builtins.property
    def certificate(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#certificate ApiManagementBackend#certificate}.'''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def header(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#header ApiManagementBackend#header}.'''
        result = self._values.get("header")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def query(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#query ApiManagementBackend#query}.'''
        result = self._values.get("query")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementBackendCredentials(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementBackend.ApiManagementBackendCredentialsAuthorization",
    jsii_struct_bases=[],
    name_mapping={"parameter": "parameter", "scheme": "scheme"},
)
class ApiManagementBackendCredentialsAuthorization:
    def __init__(
        self,
        *,
        parameter: typing.Optional[builtins.str] = None,
        scheme: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param parameter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#parameter ApiManagementBackend#parameter}.
        :param scheme: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#scheme ApiManagementBackend#scheme}.
        '''
        if __debug__:
            def stub(
                *,
                parameter: typing.Optional[builtins.str] = None,
                scheme: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument parameter", value=parameter, expected_type=type_hints["parameter"])
            check_type(argname="argument scheme", value=scheme, expected_type=type_hints["scheme"])
        self._values: typing.Dict[str, typing.Any] = {}
        if parameter is not None:
            self._values["parameter"] = parameter
        if scheme is not None:
            self._values["scheme"] = scheme

    @builtins.property
    def parameter(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#parameter ApiManagementBackend#parameter}.'''
        result = self._values.get("parameter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scheme(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#scheme ApiManagementBackend#scheme}.'''
        result = self._values.get("scheme")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementBackendCredentialsAuthorization(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementBackendCredentialsAuthorizationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementBackend.ApiManagementBackendCredentialsAuthorizationOutputReference",
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

    @jsii.member(jsii_name="resetParameter")
    def reset_parameter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameter", []))

    @jsii.member(jsii_name="resetScheme")
    def reset_scheme(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheme", []))

    @builtins.property
    @jsii.member(jsii_name="parameterInput")
    def parameter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterInput"))

    @builtins.property
    @jsii.member(jsii_name="schemeInput")
    def scheme_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemeInput"))

    @builtins.property
    @jsii.member(jsii_name="parameter")
    def parameter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameter"))

    @parameter.setter
    def parameter(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameter", value)

    @builtins.property
    @jsii.member(jsii_name="scheme")
    def scheme(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scheme"))

    @scheme.setter
    def scheme(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheme", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApiManagementBackendCredentialsAuthorization]:
        return typing.cast(typing.Optional[ApiManagementBackendCredentialsAuthorization], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementBackendCredentialsAuthorization],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[ApiManagementBackendCredentialsAuthorization],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementBackendCredentialsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementBackend.ApiManagementBackendCredentialsOutputReference",
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

    @jsii.member(jsii_name="putAuthorization")
    def put_authorization(
        self,
        *,
        parameter: typing.Optional[builtins.str] = None,
        scheme: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param parameter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#parameter ApiManagementBackend#parameter}.
        :param scheme: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#scheme ApiManagementBackend#scheme}.
        '''
        value = ApiManagementBackendCredentialsAuthorization(
            parameter=parameter, scheme=scheme
        )

        return typing.cast(None, jsii.invoke(self, "putAuthorization", [value]))

    @jsii.member(jsii_name="resetAuthorization")
    def reset_authorization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorization", []))

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetHeader")
    def reset_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeader", []))

    @jsii.member(jsii_name="resetQuery")
    def reset_query(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQuery", []))

    @builtins.property
    @jsii.member(jsii_name="authorization")
    def authorization(
        self,
    ) -> ApiManagementBackendCredentialsAuthorizationOutputReference:
        return typing.cast(ApiManagementBackendCredentialsAuthorizationOutputReference, jsii.get(self, "authorization"))

    @builtins.property
    @jsii.member(jsii_name="authorizationInput")
    def authorization_input(
        self,
    ) -> typing.Optional[ApiManagementBackendCredentialsAuthorization]:
        return typing.cast(typing.Optional[ApiManagementBackendCredentialsAuthorization], jsii.get(self, "authorizationInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="headerInput")
    def header_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "headerInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="header")
    def header(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "header"))

    @header.setter
    def header(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "header", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "query"))

    @query.setter
    def query(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApiManagementBackendCredentials]:
        return typing.cast(typing.Optional[ApiManagementBackendCredentials], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementBackendCredentials],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[ApiManagementBackendCredentials]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementBackend.ApiManagementBackendProxy",
    jsii_struct_bases=[],
    name_mapping={"url": "url", "username": "username", "password": "password"},
)
class ApiManagementBackendProxy:
    def __init__(
        self,
        *,
        url: builtins.str,
        username: builtins.str,
        password: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#url ApiManagementBackend#url}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#username ApiManagementBackend#username}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#password ApiManagementBackend#password}.
        '''
        if __debug__:
            def stub(
                *,
                url: builtins.str,
                username: builtins.str,
                password: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
        self._values: typing.Dict[str, typing.Any] = {
            "url": url,
            "username": username,
        }
        if password is not None:
            self._values["password"] = password

    @builtins.property
    def url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#url ApiManagementBackend#url}.'''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#username ApiManagementBackend#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#password ApiManagementBackend#password}.'''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementBackendProxy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementBackendProxyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementBackend.ApiManagementBackendProxyOutputReference",
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

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApiManagementBackendProxy]:
        return typing.cast(typing.Optional[ApiManagementBackendProxy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ApiManagementBackendProxy]) -> None:
        if __debug__:
            def stub(value: typing.Optional[ApiManagementBackendProxy]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementBackend.ApiManagementBackendServiceFabricCluster",
    jsii_struct_bases=[],
    name_mapping={
        "management_endpoints": "managementEndpoints",
        "max_partition_resolution_retries": "maxPartitionResolutionRetries",
        "client_certificate_id": "clientCertificateId",
        "client_certificate_thumbprint": "clientCertificateThumbprint",
        "server_certificate_thumbprints": "serverCertificateThumbprints",
        "server_x509_name": "serverX509Name",
    },
)
class ApiManagementBackendServiceFabricCluster:
    def __init__(
        self,
        *,
        management_endpoints: typing.Sequence[builtins.str],
        max_partition_resolution_retries: jsii.Number,
        client_certificate_id: typing.Optional[builtins.str] = None,
        client_certificate_thumbprint: typing.Optional[builtins.str] = None,
        server_certificate_thumbprints: typing.Optional[typing.Sequence[builtins.str]] = None,
        server_x509_name: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementBackendServiceFabricClusterServerX509Name", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param management_endpoints: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#management_endpoints ApiManagementBackend#management_endpoints}.
        :param max_partition_resolution_retries: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#max_partition_resolution_retries ApiManagementBackend#max_partition_resolution_retries}.
        :param client_certificate_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#client_certificate_id ApiManagementBackend#client_certificate_id}.
        :param client_certificate_thumbprint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#client_certificate_thumbprint ApiManagementBackend#client_certificate_thumbprint}.
        :param server_certificate_thumbprints: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#server_certificate_thumbprints ApiManagementBackend#server_certificate_thumbprints}.
        :param server_x509_name: server_x509_name block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#server_x509_name ApiManagementBackend#server_x509_name}
        '''
        if __debug__:
            def stub(
                *,
                management_endpoints: typing.Sequence[builtins.str],
                max_partition_resolution_retries: jsii.Number,
                client_certificate_id: typing.Optional[builtins.str] = None,
                client_certificate_thumbprint: typing.Optional[builtins.str] = None,
                server_certificate_thumbprints: typing.Optional[typing.Sequence[builtins.str]] = None,
                server_x509_name: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementBackendServiceFabricClusterServerX509Name, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument management_endpoints", value=management_endpoints, expected_type=type_hints["management_endpoints"])
            check_type(argname="argument max_partition_resolution_retries", value=max_partition_resolution_retries, expected_type=type_hints["max_partition_resolution_retries"])
            check_type(argname="argument client_certificate_id", value=client_certificate_id, expected_type=type_hints["client_certificate_id"])
            check_type(argname="argument client_certificate_thumbprint", value=client_certificate_thumbprint, expected_type=type_hints["client_certificate_thumbprint"])
            check_type(argname="argument server_certificate_thumbprints", value=server_certificate_thumbprints, expected_type=type_hints["server_certificate_thumbprints"])
            check_type(argname="argument server_x509_name", value=server_x509_name, expected_type=type_hints["server_x509_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "management_endpoints": management_endpoints,
            "max_partition_resolution_retries": max_partition_resolution_retries,
        }
        if client_certificate_id is not None:
            self._values["client_certificate_id"] = client_certificate_id
        if client_certificate_thumbprint is not None:
            self._values["client_certificate_thumbprint"] = client_certificate_thumbprint
        if server_certificate_thumbprints is not None:
            self._values["server_certificate_thumbprints"] = server_certificate_thumbprints
        if server_x509_name is not None:
            self._values["server_x509_name"] = server_x509_name

    @builtins.property
    def management_endpoints(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#management_endpoints ApiManagementBackend#management_endpoints}.'''
        result = self._values.get("management_endpoints")
        assert result is not None, "Required property 'management_endpoints' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def max_partition_resolution_retries(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#max_partition_resolution_retries ApiManagementBackend#max_partition_resolution_retries}.'''
        result = self._values.get("max_partition_resolution_retries")
        assert result is not None, "Required property 'max_partition_resolution_retries' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def client_certificate_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#client_certificate_id ApiManagementBackend#client_certificate_id}.'''
        result = self._values.get("client_certificate_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_certificate_thumbprint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#client_certificate_thumbprint ApiManagementBackend#client_certificate_thumbprint}.'''
        result = self._values.get("client_certificate_thumbprint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_certificate_thumbprints(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#server_certificate_thumbprints ApiManagementBackend#server_certificate_thumbprints}.'''
        result = self._values.get("server_certificate_thumbprints")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def server_x509_name(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementBackendServiceFabricClusterServerX509Name"]]]:
        '''server_x509_name block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#server_x509_name ApiManagementBackend#server_x509_name}
        '''
        result = self._values.get("server_x509_name")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementBackendServiceFabricClusterServerX509Name"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementBackendServiceFabricCluster(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementBackendServiceFabricClusterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementBackend.ApiManagementBackendServiceFabricClusterOutputReference",
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

    @jsii.member(jsii_name="putServerX509Name")
    def put_server_x509_name(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementBackendServiceFabricClusterServerX509Name", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementBackendServiceFabricClusterServerX509Name, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putServerX509Name", [value]))

    @jsii.member(jsii_name="resetClientCertificateId")
    def reset_client_certificate_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCertificateId", []))

    @jsii.member(jsii_name="resetClientCertificateThumbprint")
    def reset_client_certificate_thumbprint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCertificateThumbprint", []))

    @jsii.member(jsii_name="resetServerCertificateThumbprints")
    def reset_server_certificate_thumbprints(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerCertificateThumbprints", []))

    @jsii.member(jsii_name="resetServerX509Name")
    def reset_server_x509_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerX509Name", []))

    @builtins.property
    @jsii.member(jsii_name="serverX509Name")
    def server_x509_name(
        self,
    ) -> "ApiManagementBackendServiceFabricClusterServerX509NameList":
        return typing.cast("ApiManagementBackendServiceFabricClusterServerX509NameList", jsii.get(self, "serverX509Name"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificateIdInput")
    def client_certificate_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertificateIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificateThumbprintInput")
    def client_certificate_thumbprint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertificateThumbprintInput"))

    @builtins.property
    @jsii.member(jsii_name="managementEndpointsInput")
    def management_endpoints_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "managementEndpointsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxPartitionResolutionRetriesInput")
    def max_partition_resolution_retries_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxPartitionResolutionRetriesInput"))

    @builtins.property
    @jsii.member(jsii_name="serverCertificateThumbprintsInput")
    def server_certificate_thumbprints_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "serverCertificateThumbprintsInput"))

    @builtins.property
    @jsii.member(jsii_name="serverX509NameInput")
    def server_x509_name_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementBackendServiceFabricClusterServerX509Name"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementBackendServiceFabricClusterServerX509Name"]]], jsii.get(self, "serverX509NameInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificateId")
    def client_certificate_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientCertificateId"))

    @client_certificate_id.setter
    def client_certificate_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCertificateId", value)

    @builtins.property
    @jsii.member(jsii_name="clientCertificateThumbprint")
    def client_certificate_thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientCertificateThumbprint"))

    @client_certificate_thumbprint.setter
    def client_certificate_thumbprint(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCertificateThumbprint", value)

    @builtins.property
    @jsii.member(jsii_name="managementEndpoints")
    def management_endpoints(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "managementEndpoints"))

    @management_endpoints.setter
    def management_endpoints(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managementEndpoints", value)

    @builtins.property
    @jsii.member(jsii_name="maxPartitionResolutionRetries")
    def max_partition_resolution_retries(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxPartitionResolutionRetries"))

    @max_partition_resolution_retries.setter
    def max_partition_resolution_retries(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxPartitionResolutionRetries", value)

    @builtins.property
    @jsii.member(jsii_name="serverCertificateThumbprints")
    def server_certificate_thumbprints(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "serverCertificateThumbprints"))

    @server_certificate_thumbprints.setter
    def server_certificate_thumbprints(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverCertificateThumbprints", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApiManagementBackendServiceFabricCluster]:
        return typing.cast(typing.Optional[ApiManagementBackendServiceFabricCluster], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementBackendServiceFabricCluster],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[ApiManagementBackendServiceFabricCluster],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementBackend.ApiManagementBackendServiceFabricClusterServerX509Name",
    jsii_struct_bases=[],
    name_mapping={
        "issuer_certificate_thumbprint": "issuerCertificateThumbprint",
        "name": "name",
    },
)
class ApiManagementBackendServiceFabricClusterServerX509Name:
    def __init__(
        self,
        *,
        issuer_certificate_thumbprint: builtins.str,
        name: builtins.str,
    ) -> None:
        '''
        :param issuer_certificate_thumbprint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#issuer_certificate_thumbprint ApiManagementBackend#issuer_certificate_thumbprint}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#name ApiManagementBackend#name}.
        '''
        if __debug__:
            def stub(
                *,
                issuer_certificate_thumbprint: builtins.str,
                name: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument issuer_certificate_thumbprint", value=issuer_certificate_thumbprint, expected_type=type_hints["issuer_certificate_thumbprint"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "issuer_certificate_thumbprint": issuer_certificate_thumbprint,
            "name": name,
        }

    @builtins.property
    def issuer_certificate_thumbprint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#issuer_certificate_thumbprint ApiManagementBackend#issuer_certificate_thumbprint}.'''
        result = self._values.get("issuer_certificate_thumbprint")
        assert result is not None, "Required property 'issuer_certificate_thumbprint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#name ApiManagementBackend#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementBackendServiceFabricClusterServerX509Name(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementBackendServiceFabricClusterServerX509NameList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementBackend.ApiManagementBackendServiceFabricClusterServerX509NameList",
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
    ) -> "ApiManagementBackendServiceFabricClusterServerX509NameOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementBackendServiceFabricClusterServerX509NameOutputReference", jsii.invoke(self, "get", [index]))

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

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementBackendServiceFabricClusterServerX509Name]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementBackendServiceFabricClusterServerX509Name]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementBackendServiceFabricClusterServerX509Name]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementBackendServiceFabricClusterServerX509Name]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementBackendServiceFabricClusterServerX509NameOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementBackend.ApiManagementBackendServiceFabricClusterServerX509NameOutputReference",
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
    @jsii.member(jsii_name="issuerCertificateThumbprintInput")
    def issuer_certificate_thumbprint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issuerCertificateThumbprintInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="issuerCertificateThumbprint")
    def issuer_certificate_thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuerCertificateThumbprint"))

    @issuer_certificate_thumbprint.setter
    def issuer_certificate_thumbprint(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuerCertificateThumbprint", value)

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementBackendServiceFabricClusterServerX509Name, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementBackendServiceFabricClusterServerX509Name, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementBackendServiceFabricClusterServerX509Name, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[ApiManagementBackendServiceFabricClusterServerX509Name, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementBackend.ApiManagementBackendTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class ApiManagementBackendTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#create ApiManagementBackend#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#delete ApiManagementBackend#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#read ApiManagementBackend#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#update ApiManagementBackend#update}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#create ApiManagementBackend#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#delete ApiManagementBackend#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#read ApiManagementBackend#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#update ApiManagementBackend#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementBackendTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementBackendTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementBackend.ApiManagementBackendTimeoutsOutputReference",
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
    ) -> typing.Optional[typing.Union[ApiManagementBackendTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementBackendTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementBackendTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[ApiManagementBackendTimeouts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementBackend.ApiManagementBackendTls",
    jsii_struct_bases=[],
    name_mapping={
        "validate_certificate_chain": "validateCertificateChain",
        "validate_certificate_name": "validateCertificateName",
    },
)
class ApiManagementBackendTls:
    def __init__(
        self,
        *,
        validate_certificate_chain: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        validate_certificate_name: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param validate_certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#validate_certificate_chain ApiManagementBackend#validate_certificate_chain}.
        :param validate_certificate_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#validate_certificate_name ApiManagementBackend#validate_certificate_name}.
        '''
        if __debug__:
            def stub(
                *,
                validate_certificate_chain: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                validate_certificate_name: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument validate_certificate_chain", value=validate_certificate_chain, expected_type=type_hints["validate_certificate_chain"])
            check_type(argname="argument validate_certificate_name", value=validate_certificate_name, expected_type=type_hints["validate_certificate_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if validate_certificate_chain is not None:
            self._values["validate_certificate_chain"] = validate_certificate_chain
        if validate_certificate_name is not None:
            self._values["validate_certificate_name"] = validate_certificate_name

    @builtins.property
    def validate_certificate_chain(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#validate_certificate_chain ApiManagementBackend#validate_certificate_chain}.'''
        result = self._values.get("validate_certificate_chain")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def validate_certificate_name(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_backend#validate_certificate_name ApiManagementBackend#validate_certificate_name}.'''
        result = self._values.get("validate_certificate_name")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementBackendTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementBackendTlsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementBackend.ApiManagementBackendTlsOutputReference",
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

    @jsii.member(jsii_name="resetValidateCertificateChain")
    def reset_validate_certificate_chain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidateCertificateChain", []))

    @jsii.member(jsii_name="resetValidateCertificateName")
    def reset_validate_certificate_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidateCertificateName", []))

    @builtins.property
    @jsii.member(jsii_name="validateCertificateChainInput")
    def validate_certificate_chain_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "validateCertificateChainInput"))

    @builtins.property
    @jsii.member(jsii_name="validateCertificateNameInput")
    def validate_certificate_name_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "validateCertificateNameInput"))

    @builtins.property
    @jsii.member(jsii_name="validateCertificateChain")
    def validate_certificate_chain(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "validateCertificateChain"))

    @validate_certificate_chain.setter
    def validate_certificate_chain(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validateCertificateChain", value)

    @builtins.property
    @jsii.member(jsii_name="validateCertificateName")
    def validate_certificate_name(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "validateCertificateName"))

    @validate_certificate_name.setter
    def validate_certificate_name(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validateCertificateName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApiManagementBackendTls]:
        return typing.cast(typing.Optional[ApiManagementBackendTls], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ApiManagementBackendTls]) -> None:
        if __debug__:
            def stub(value: typing.Optional[ApiManagementBackendTls]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ApiManagementBackend",
    "ApiManagementBackendConfig",
    "ApiManagementBackendCredentials",
    "ApiManagementBackendCredentialsAuthorization",
    "ApiManagementBackendCredentialsAuthorizationOutputReference",
    "ApiManagementBackendCredentialsOutputReference",
    "ApiManagementBackendProxy",
    "ApiManagementBackendProxyOutputReference",
    "ApiManagementBackendServiceFabricCluster",
    "ApiManagementBackendServiceFabricClusterOutputReference",
    "ApiManagementBackendServiceFabricClusterServerX509Name",
    "ApiManagementBackendServiceFabricClusterServerX509NameList",
    "ApiManagementBackendServiceFabricClusterServerX509NameOutputReference",
    "ApiManagementBackendTimeouts",
    "ApiManagementBackendTimeoutsOutputReference",
    "ApiManagementBackendTls",
    "ApiManagementBackendTlsOutputReference",
]

publication.publish()
