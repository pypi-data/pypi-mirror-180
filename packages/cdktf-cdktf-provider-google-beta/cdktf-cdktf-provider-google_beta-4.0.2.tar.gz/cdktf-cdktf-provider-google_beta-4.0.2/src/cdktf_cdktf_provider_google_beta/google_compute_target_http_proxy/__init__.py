'''
# `google_compute_target_http_proxy`

Refer to the Terraform Registory for docs: [`google_compute_target_http_proxy`](https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy).
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

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class GoogleComputeTargetHttpProxy(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeTargetHttpProxy.GoogleComputeTargetHttpProxy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy google_compute_target_http_proxy}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        url_map: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        proxy_bind: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeTargetHttpProxyTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy google_compute_target_http_proxy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#name GoogleComputeTargetHttpProxy#name}
        :param url_map: A reference to the UrlMap resource that defines the mapping from URL to the BackendService. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#url_map GoogleComputeTargetHttpProxy#url_map}
        :param description: An optional description of this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#description GoogleComputeTargetHttpProxy#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#id GoogleComputeTargetHttpProxy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#project GoogleComputeTargetHttpProxy#project}.
        :param proxy_bind: This field only applies when the forwarding rule that references this target proxy has a loadBalancingScheme set to INTERNAL_SELF_MANAGED. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#proxy_bind GoogleComputeTargetHttpProxy#proxy_bind}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#timeouts GoogleComputeTargetHttpProxy#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15f03fee3f04a4dc916aed73bbefe4b38d917b6d5c92a2f8f125e085d6a69dbc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleComputeTargetHttpProxyConfig(
            name=name,
            url_map=url_map,
            description=description,
            id=id,
            project=project,
            proxy_bind=proxy_bind,
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

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#create GoogleComputeTargetHttpProxy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#delete GoogleComputeTargetHttpProxy#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#update GoogleComputeTargetHttpProxy#update}.
        '''
        value = GoogleComputeTargetHttpProxyTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetProxyBind")
    def reset_proxy_bind(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProxyBind", []))

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
    @jsii.member(jsii_name="creationTimestamp")
    def creation_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "creationTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="proxyId")
    def proxy_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "proxyId"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleComputeTargetHttpProxyTimeoutsOutputReference":
        return typing.cast("GoogleComputeTargetHttpProxyTimeoutsOutputReference", jsii.get(self, "timeouts"))

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
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="proxyBindInput")
    def proxy_bind_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "proxyBindInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleComputeTargetHttpProxyTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleComputeTargetHttpProxyTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="urlMapInput")
    def url_map_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlMapInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d01b2d27859268eeaa05d18176fa607ae5dc34de4af065c003c25bca41328480)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fea33390cb3af8b2fa017d3db7b9e97360ddcbb7264f837fc42d9b8fe9c3777d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a546e73895030641e304c58a387e61660818de6252b2433ee86e395bcfc397f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f21fa85b1a39c8d752adba63acefa65c9382ff4d521195637444eec81409387b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="proxyBind")
    def proxy_bind(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "proxyBind"))

    @proxy_bind.setter
    def proxy_bind(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__877c08b5104f0061666c515ca30d97025f6760687f72bf840cef7f54fe6c1986)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proxyBind", value)

    @builtins.property
    @jsii.member(jsii_name="urlMap")
    def url_map(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "urlMap"))

    @url_map.setter
    def url_map(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95bd3835e3249053d63d66b5e9221dbb9a3fbb8eeba6aad6384c2e4b505bdc73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "urlMap", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeTargetHttpProxy.GoogleComputeTargetHttpProxyConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "url_map": "urlMap",
        "description": "description",
        "id": "id",
        "project": "project",
        "proxy_bind": "proxyBind",
        "timeouts": "timeouts",
    },
)
class GoogleComputeTargetHttpProxyConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        name: builtins.str,
        url_map: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        proxy_bind: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeTargetHttpProxyTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#name GoogleComputeTargetHttpProxy#name}
        :param url_map: A reference to the UrlMap resource that defines the mapping from URL to the BackendService. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#url_map GoogleComputeTargetHttpProxy#url_map}
        :param description: An optional description of this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#description GoogleComputeTargetHttpProxy#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#id GoogleComputeTargetHttpProxy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#project GoogleComputeTargetHttpProxy#project}.
        :param proxy_bind: This field only applies when the forwarding rule that references this target proxy has a loadBalancingScheme set to INTERNAL_SELF_MANAGED. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#proxy_bind GoogleComputeTargetHttpProxy#proxy_bind}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#timeouts GoogleComputeTargetHttpProxy#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = GoogleComputeTargetHttpProxyTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7f8bd54f7ccfcceee0b06da5469986d31c97d64ece9110cac991eff0914de61)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument url_map", value=url_map, expected_type=type_hints["url_map"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument proxy_bind", value=proxy_bind, expected_type=type_hints["proxy_bind"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "url_map": url_map,
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
        if project is not None:
            self._values["project"] = project
        if proxy_bind is not None:
            self._values["proxy_bind"] = proxy_bind
        if timeouts is not None:
            self._values["timeouts"] = timeouts

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the resource.

        Provided by the client when the resource is
        created. The name must be 1-63 characters long, and comply with
        RFC1035. Specifically, the name must be 1-63 characters long and match
        the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the
        first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the last
        character, which cannot be a dash.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#name GoogleComputeTargetHttpProxy#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def url_map(self) -> builtins.str:
        '''A reference to the UrlMap resource that defines the mapping from URL to the BackendService.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#url_map GoogleComputeTargetHttpProxy#url_map}
        '''
        result = self._values.get("url_map")
        assert result is not None, "Required property 'url_map' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of this resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#description GoogleComputeTargetHttpProxy#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#id GoogleComputeTargetHttpProxy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#project GoogleComputeTargetHttpProxy#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def proxy_bind(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''This field only applies when the forwarding rule that references this target proxy has a loadBalancingScheme set to INTERNAL_SELF_MANAGED.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#proxy_bind GoogleComputeTargetHttpProxy#proxy_bind}
        '''
        result = self._values.get("proxy_bind")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleComputeTargetHttpProxyTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#timeouts GoogleComputeTargetHttpProxy#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleComputeTargetHttpProxyTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeTargetHttpProxyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeTargetHttpProxy.GoogleComputeTargetHttpProxyTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleComputeTargetHttpProxyTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#create GoogleComputeTargetHttpProxy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#delete GoogleComputeTargetHttpProxy#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#update GoogleComputeTargetHttpProxy#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40cf7cd321a7f9105ef01aaa5f6663a23bc22031aa600ab03257360e1dc05025)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#create GoogleComputeTargetHttpProxy#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#delete GoogleComputeTargetHttpProxy#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_target_http_proxy#update GoogleComputeTargetHttpProxy#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeTargetHttpProxyTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeTargetHttpProxyTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeTargetHttpProxy.GoogleComputeTargetHttpProxyTimeoutsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1a3c66ccea6c603e783fdacee89fc80c61f35da06148edc6641ee799f16f4c7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__04778b985cb4021bb095a685bd9e5938eb2794e6cfcdefa6f855cbee0704f5b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2d111169fc0270b9f710bd234e8563b46c12d6aeb4e2f398ff299847fafe35c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be7f1f3655a1497295a36848dd6343f50cff1f361f69950068a7b6f8772ccf82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeTargetHttpProxyTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeTargetHttpProxyTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeTargetHttpProxyTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1eec979607c4eaaa8029611dfa65b6481882c8d9263ce98098f5187183fe1cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleComputeTargetHttpProxy",
    "GoogleComputeTargetHttpProxyConfig",
    "GoogleComputeTargetHttpProxyTimeouts",
    "GoogleComputeTargetHttpProxyTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__15f03fee3f04a4dc916aed73bbefe4b38d917b6d5c92a2f8f125e085d6a69dbc(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    url_map: builtins.str,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    project: typing.Optional[builtins.str] = None,
    proxy_bind: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    timeouts: typing.Optional[typing.Union[GoogleComputeTargetHttpProxyTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d01b2d27859268eeaa05d18176fa607ae5dc34de4af065c003c25bca41328480(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fea33390cb3af8b2fa017d3db7b9e97360ddcbb7264f837fc42d9b8fe9c3777d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a546e73895030641e304c58a387e61660818de6252b2433ee86e395bcfc397f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f21fa85b1a39c8d752adba63acefa65c9382ff4d521195637444eec81409387b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__877c08b5104f0061666c515ca30d97025f6760687f72bf840cef7f54fe6c1986(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95bd3835e3249053d63d66b5e9221dbb9a3fbb8eeba6aad6384c2e4b505bdc73(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7f8bd54f7ccfcceee0b06da5469986d31c97d64ece9110cac991eff0914de61(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    url_map: builtins.str,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    project: typing.Optional[builtins.str] = None,
    proxy_bind: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    timeouts: typing.Optional[typing.Union[GoogleComputeTargetHttpProxyTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40cf7cd321a7f9105ef01aaa5f6663a23bc22031aa600ab03257360e1dc05025(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1a3c66ccea6c603e783fdacee89fc80c61f35da06148edc6641ee799f16f4c7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04778b985cb4021bb095a685bd9e5938eb2794e6cfcdefa6f855cbee0704f5b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2d111169fc0270b9f710bd234e8563b46c12d6aeb4e2f398ff299847fafe35c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be7f1f3655a1497295a36848dd6343f50cff1f361f69950068a7b6f8772ccf82(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1eec979607c4eaaa8029611dfa65b6481882c8d9263ce98098f5187183fe1cd(
    value: typing.Optional[typing.Union[GoogleComputeTargetHttpProxyTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
