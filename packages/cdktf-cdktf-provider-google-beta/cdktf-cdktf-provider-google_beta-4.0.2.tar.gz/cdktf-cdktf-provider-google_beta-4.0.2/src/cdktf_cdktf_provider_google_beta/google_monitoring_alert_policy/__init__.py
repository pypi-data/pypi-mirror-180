'''
# `google_monitoring_alert_policy`

Refer to the Terraform Registory for docs: [`google_monitoring_alert_policy`](https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy).
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


class GoogleMonitoringAlertPolicy(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy google_monitoring_alert_policy}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        combiner: builtins.str,
        conditions: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleMonitoringAlertPolicyConditions", typing.Dict[builtins.str, typing.Any]]]],
        display_name: builtins.str,
        alert_strategy: typing.Optional[typing.Union["GoogleMonitoringAlertPolicyAlertStrategy", typing.Dict[builtins.str, typing.Any]]] = None,
        documentation: typing.Optional[typing.Union["GoogleMonitoringAlertPolicyDocumentation", typing.Dict[builtins.str, typing.Any]]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        notification_channels: typing.Optional[typing.Sequence[builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleMonitoringAlertPolicyTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        user_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy google_monitoring_alert_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param combiner: How to combine the results of multiple conditions to determine if an incident should be opened. Possible values: ["AND", "OR", "AND_WITH_MATCHING_RESOURCE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#combiner GoogleMonitoringAlertPolicy#combiner}
        :param conditions: conditions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#conditions GoogleMonitoringAlertPolicy#conditions}
        :param display_name: A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion, don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#display_name GoogleMonitoringAlertPolicy#display_name}
        :param alert_strategy: alert_strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#alert_strategy GoogleMonitoringAlertPolicy#alert_strategy}
        :param documentation: documentation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#documentation GoogleMonitoringAlertPolicy#documentation}
        :param enabled: Whether or not the policy is enabled. The default is true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#enabled GoogleMonitoringAlertPolicy#enabled}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#id GoogleMonitoringAlertPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param notification_channels: Identifies the notification channels to which notifications should be sent when incidents are opened or closed or when new violations occur on an already opened incident. Each element of this array corresponds to the name field in each of the NotificationChannel objects that are returned from the notificationChannels.list method. The syntax of the entries in this field is 'projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#notification_channels GoogleMonitoringAlertPolicy#notification_channels}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#project GoogleMonitoringAlertPolicy#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#timeouts GoogleMonitoringAlertPolicy#timeouts}
        :param user_labels: This field is intended to be used for organizing and identifying the AlertPolicy objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#user_labels GoogleMonitoringAlertPolicy#user_labels}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b676cf9f0868f950faefca183808c2c490d719f773f06f4379b4bc94e4dc9a4f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleMonitoringAlertPolicyConfig(
            combiner=combiner,
            conditions=conditions,
            display_name=display_name,
            alert_strategy=alert_strategy,
            documentation=documentation,
            enabled=enabled,
            id=id,
            notification_channels=notification_channels,
            project=project,
            timeouts=timeouts,
            user_labels=user_labels,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAlertStrategy")
    def put_alert_strategy(
        self,
        *,
        auto_close: typing.Optional[builtins.str] = None,
        notification_rate_limit: typing.Optional[typing.Union["GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param auto_close: If an alert policy that was active has no data for this long, any open incidents will close. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#auto_close GoogleMonitoringAlertPolicy#auto_close}
        :param notification_rate_limit: notification_rate_limit block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#notification_rate_limit GoogleMonitoringAlertPolicy#notification_rate_limit}
        '''
        value = GoogleMonitoringAlertPolicyAlertStrategy(
            auto_close=auto_close, notification_rate_limit=notification_rate_limit
        )

        return typing.cast(None, jsii.invoke(self, "putAlertStrategy", [value]))

    @jsii.member(jsii_name="putConditions")
    def put_conditions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleMonitoringAlertPolicyConditions", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53c5c45a756c606a50f7f623665b61b2ea7c5b3fba9cdc60931e8312d28e9249)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConditions", [value]))

    @jsii.member(jsii_name="putDocumentation")
    def put_documentation(
        self,
        *,
        content: typing.Optional[builtins.str] = None,
        mime_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param content: The text of the documentation, interpreted according to mimeType. The content may not exceed 8,192 Unicode characters and may not exceed more than 10,240 bytes when encoded in UTF-8 format, whichever is smaller. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#content GoogleMonitoringAlertPolicy#content}
        :param mime_type: The format of the content field. Presently, only the value "text/markdown" is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#mime_type GoogleMonitoringAlertPolicy#mime_type}
        '''
        value = GoogleMonitoringAlertPolicyDocumentation(
            content=content, mime_type=mime_type
        )

        return typing.cast(None, jsii.invoke(self, "putDocumentation", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#create GoogleMonitoringAlertPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#delete GoogleMonitoringAlertPolicy#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#update GoogleMonitoringAlertPolicy#update}.
        '''
        value = GoogleMonitoringAlertPolicyTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAlertStrategy")
    def reset_alert_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlertStrategy", []))

    @jsii.member(jsii_name="resetDocumentation")
    def reset_documentation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocumentation", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNotificationChannels")
    def reset_notification_channels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationChannels", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUserLabels")
    def reset_user_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserLabels", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="alertStrategy")
    def alert_strategy(
        self,
    ) -> "GoogleMonitoringAlertPolicyAlertStrategyOutputReference":
        return typing.cast("GoogleMonitoringAlertPolicyAlertStrategyOutputReference", jsii.get(self, "alertStrategy"))

    @builtins.property
    @jsii.member(jsii_name="conditions")
    def conditions(self) -> "GoogleMonitoringAlertPolicyConditionsList":
        return typing.cast("GoogleMonitoringAlertPolicyConditionsList", jsii.get(self, "conditions"))

    @builtins.property
    @jsii.member(jsii_name="creationRecord")
    def creation_record(self) -> "GoogleMonitoringAlertPolicyCreationRecordList":
        return typing.cast("GoogleMonitoringAlertPolicyCreationRecordList", jsii.get(self, "creationRecord"))

    @builtins.property
    @jsii.member(jsii_name="documentation")
    def documentation(
        self,
    ) -> "GoogleMonitoringAlertPolicyDocumentationOutputReference":
        return typing.cast("GoogleMonitoringAlertPolicyDocumentationOutputReference", jsii.get(self, "documentation"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleMonitoringAlertPolicyTimeoutsOutputReference":
        return typing.cast("GoogleMonitoringAlertPolicyTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="alertStrategyInput")
    def alert_strategy_input(
        self,
    ) -> typing.Optional["GoogleMonitoringAlertPolicyAlertStrategy"]:
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyAlertStrategy"], jsii.get(self, "alertStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="combinerInput")
    def combiner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "combinerInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionsInput")
    def conditions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleMonitoringAlertPolicyConditions"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleMonitoringAlertPolicyConditions"]]], jsii.get(self, "conditionsInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="documentationInput")
    def documentation_input(
        self,
    ) -> typing.Optional["GoogleMonitoringAlertPolicyDocumentation"]:
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyDocumentation"], jsii.get(self, "documentationInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationChannelsInput")
    def notification_channels_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notificationChannelsInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleMonitoringAlertPolicyTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleMonitoringAlertPolicyTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="userLabelsInput")
    def user_labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "userLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="combiner")
    def combiner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "combiner"))

    @combiner.setter
    def combiner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb6f4c70b542db299f40546bbe220e2e6eca4cf76d641115b2d8d450a82176f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "combiner", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab8cc3066286fa54a192893f7d07396b1d83137e0197e89839ee49671260d0ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb6b0de4773ad5ed371b5772bea252ce538da75045a7bc86f653b70871961121)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20472b861bccf45b1ad809718ab460bc15f4365e35d2a24a3f98c66a23852aaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="notificationChannels")
    def notification_channels(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notificationChannels"))

    @notification_channels.setter
    def notification_channels(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__475a6e0a08db36a6ad2bde12d39cba0ef9df5f0cf75c63a184431653fe3165e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationChannels", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b5079d2e9426f13c62193284296b5fdd73c80fb925b06d50347944521fbb575)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="userLabels")
    def user_labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "userLabels"))

    @user_labels.setter
    def user_labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ff3d320068f669b56b665133ba509bc6175753a3f91ef36f34b67bdd880008d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userLabels", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyAlertStrategy",
    jsii_struct_bases=[],
    name_mapping={
        "auto_close": "autoClose",
        "notification_rate_limit": "notificationRateLimit",
    },
)
class GoogleMonitoringAlertPolicyAlertStrategy:
    def __init__(
        self,
        *,
        auto_close: typing.Optional[builtins.str] = None,
        notification_rate_limit: typing.Optional[typing.Union["GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param auto_close: If an alert policy that was active has no data for this long, any open incidents will close. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#auto_close GoogleMonitoringAlertPolicy#auto_close}
        :param notification_rate_limit: notification_rate_limit block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#notification_rate_limit GoogleMonitoringAlertPolicy#notification_rate_limit}
        '''
        if isinstance(notification_rate_limit, dict):
            notification_rate_limit = GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit(**notification_rate_limit)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba1267174d35830e16072259481dcc3e25581cbec7aa32aa539800dda910aaf4)
            check_type(argname="argument auto_close", value=auto_close, expected_type=type_hints["auto_close"])
            check_type(argname="argument notification_rate_limit", value=notification_rate_limit, expected_type=type_hints["notification_rate_limit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if auto_close is not None:
            self._values["auto_close"] = auto_close
        if notification_rate_limit is not None:
            self._values["notification_rate_limit"] = notification_rate_limit

    @builtins.property
    def auto_close(self) -> typing.Optional[builtins.str]:
        '''If an alert policy that was active has no data for this long, any open incidents will close.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#auto_close GoogleMonitoringAlertPolicy#auto_close}
        '''
        result = self._values.get("auto_close")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_rate_limit(
        self,
    ) -> typing.Optional["GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit"]:
        '''notification_rate_limit block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#notification_rate_limit GoogleMonitoringAlertPolicy#notification_rate_limit}
        '''
        result = self._values.get("notification_rate_limit")
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyAlertStrategy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit",
    jsii_struct_bases=[],
    name_mapping={"period": "period"},
)
class GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit:
    def __init__(self, *, period: typing.Optional[builtins.str] = None) -> None:
        '''
        :param period: Not more than one notification per period. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#period GoogleMonitoringAlertPolicy#period}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3de5bfc4b8c8d5040b7de66acc39deef1a82992c4d3407a48c9af617e5f8906)
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if period is not None:
            self._values["period"] = period

    @builtins.property
    def period(self) -> typing.Optional[builtins.str]:
        '''Not more than one notification per period.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#period GoogleMonitoringAlertPolicy#period}
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimitOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimitOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__37eb453aaa420a2f3a34aa1cb7eab7db7ce81c4f9f039bc80999b8748f309eca)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPeriod")
    def reset_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeriod", []))

    @builtins.property
    @jsii.member(jsii_name="periodInput")
    def period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "periodInput"))

    @builtins.property
    @jsii.member(jsii_name="period")
    def period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "period"))

    @period.setter
    def period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f4fcc94505105c197f876baa56a41771fdf4eb7f3d2221a87805fdf0d05c33c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "period", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9a5bb757226631bfd28873596b22f7e5924779bd2dc5809c6bc3c407a2cb93d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleMonitoringAlertPolicyAlertStrategyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyAlertStrategyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bece5930de9edfe294cc2cba2110ef5d2f4c4c03cd47421dbab957bf5bc9d24f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putNotificationRateLimit")
    def put_notification_rate_limit(
        self,
        *,
        period: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param period: Not more than one notification per period. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#period GoogleMonitoringAlertPolicy#period}
        '''
        value = GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit(
            period=period
        )

        return typing.cast(None, jsii.invoke(self, "putNotificationRateLimit", [value]))

    @jsii.member(jsii_name="resetAutoClose")
    def reset_auto_close(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoClose", []))

    @jsii.member(jsii_name="resetNotificationRateLimit")
    def reset_notification_rate_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationRateLimit", []))

    @builtins.property
    @jsii.member(jsii_name="notificationRateLimit")
    def notification_rate_limit(
        self,
    ) -> GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimitOutputReference:
        return typing.cast(GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimitOutputReference, jsii.get(self, "notificationRateLimit"))

    @builtins.property
    @jsii.member(jsii_name="autoCloseInput")
    def auto_close_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoCloseInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationRateLimitInput")
    def notification_rate_limit_input(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit], jsii.get(self, "notificationRateLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="autoClose")
    def auto_close(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoClose"))

    @auto_close.setter
    def auto_close(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1efaea8c321a04d2a59d21f96ae4696e032f86d61e42966d81d3b04dc68e2da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoClose", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyAlertStrategy]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyAlertStrategy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringAlertPolicyAlertStrategy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84094baed363937b712d405dbe530d763f2e9b8007fbec388cb0a14bc021ce91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditions",
    jsii_struct_bases=[],
    name_mapping={
        "display_name": "displayName",
        "condition_absent": "conditionAbsent",
        "condition_matched_log": "conditionMatchedLog",
        "condition_monitoring_query_language": "conditionMonitoringQueryLanguage",
        "condition_threshold": "conditionThreshold",
    },
)
class GoogleMonitoringAlertPolicyConditions:
    def __init__(
        self,
        *,
        display_name: builtins.str,
        condition_absent: typing.Optional[typing.Union["GoogleMonitoringAlertPolicyConditionsConditionAbsent", typing.Dict[builtins.str, typing.Any]]] = None,
        condition_matched_log: typing.Optional[typing.Union["GoogleMonitoringAlertPolicyConditionsConditionMatchedLog", typing.Dict[builtins.str, typing.Any]]] = None,
        condition_monitoring_query_language: typing.Optional[typing.Union["GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage", typing.Dict[builtins.str, typing.Any]]] = None,
        condition_threshold: typing.Optional[typing.Union["GoogleMonitoringAlertPolicyConditionsConditionThreshold", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param display_name: A short name or phrase used to identify the condition in dashboards, notifications, and incidents. To avoid confusion, don't use the same display name for multiple conditions in the same policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#display_name GoogleMonitoringAlertPolicy#display_name}
        :param condition_absent: condition_absent block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#condition_absent GoogleMonitoringAlertPolicy#condition_absent}
        :param condition_matched_log: condition_matched_log block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#condition_matched_log GoogleMonitoringAlertPolicy#condition_matched_log}
        :param condition_monitoring_query_language: condition_monitoring_query_language block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#condition_monitoring_query_language GoogleMonitoringAlertPolicy#condition_monitoring_query_language}
        :param condition_threshold: condition_threshold block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#condition_threshold GoogleMonitoringAlertPolicy#condition_threshold}
        '''
        if isinstance(condition_absent, dict):
            condition_absent = GoogleMonitoringAlertPolicyConditionsConditionAbsent(**condition_absent)
        if isinstance(condition_matched_log, dict):
            condition_matched_log = GoogleMonitoringAlertPolicyConditionsConditionMatchedLog(**condition_matched_log)
        if isinstance(condition_monitoring_query_language, dict):
            condition_monitoring_query_language = GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage(**condition_monitoring_query_language)
        if isinstance(condition_threshold, dict):
            condition_threshold = GoogleMonitoringAlertPolicyConditionsConditionThreshold(**condition_threshold)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__076db12d738ff26279094e1061a63e449bb78bf37b8b6cebaaf168c8b3240151)
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument condition_absent", value=condition_absent, expected_type=type_hints["condition_absent"])
            check_type(argname="argument condition_matched_log", value=condition_matched_log, expected_type=type_hints["condition_matched_log"])
            check_type(argname="argument condition_monitoring_query_language", value=condition_monitoring_query_language, expected_type=type_hints["condition_monitoring_query_language"])
            check_type(argname="argument condition_threshold", value=condition_threshold, expected_type=type_hints["condition_threshold"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "display_name": display_name,
        }
        if condition_absent is not None:
            self._values["condition_absent"] = condition_absent
        if condition_matched_log is not None:
            self._values["condition_matched_log"] = condition_matched_log
        if condition_monitoring_query_language is not None:
            self._values["condition_monitoring_query_language"] = condition_monitoring_query_language
        if condition_threshold is not None:
            self._values["condition_threshold"] = condition_threshold

    @builtins.property
    def display_name(self) -> builtins.str:
        '''A short name or phrase used to identify the condition in dashboards, notifications, and incidents.

        To avoid confusion, don't use the same
        display name for multiple conditions in the same
        policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#display_name GoogleMonitoringAlertPolicy#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def condition_absent(
        self,
    ) -> typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionAbsent"]:
        '''condition_absent block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#condition_absent GoogleMonitoringAlertPolicy#condition_absent}
        '''
        result = self._values.get("condition_absent")
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionAbsent"], result)

    @builtins.property
    def condition_matched_log(
        self,
    ) -> typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionMatchedLog"]:
        '''condition_matched_log block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#condition_matched_log GoogleMonitoringAlertPolicy#condition_matched_log}
        '''
        result = self._values.get("condition_matched_log")
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionMatchedLog"], result)

    @builtins.property
    def condition_monitoring_query_language(
        self,
    ) -> typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage"]:
        '''condition_monitoring_query_language block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#condition_monitoring_query_language GoogleMonitoringAlertPolicy#condition_monitoring_query_language}
        '''
        result = self._values.get("condition_monitoring_query_language")
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage"], result)

    @builtins.property
    def condition_threshold(
        self,
    ) -> typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionThreshold"]:
        '''condition_threshold block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#condition_threshold GoogleMonitoringAlertPolicy#condition_threshold}
        '''
        result = self._values.get("condition_threshold")
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionThreshold"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyConditions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionAbsent",
    jsii_struct_bases=[],
    name_mapping={
        "duration": "duration",
        "aggregations": "aggregations",
        "filter": "filter",
        "trigger": "trigger",
    },
)
class GoogleMonitoringAlertPolicyConditionsConditionAbsent:
    def __init__(
        self,
        *,
        duration: builtins.str,
        aggregations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations", typing.Dict[builtins.str, typing.Any]]]]] = None,
        filter: typing.Optional[builtins.str] = None,
        trigger: typing.Optional[typing.Union["GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param duration: The amount of time that a time series must fail to report new data to be considered failing. Currently, only values that are a multiple of a minute--e.g. 60s, 120s, or 300s --are supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#duration GoogleMonitoringAlertPolicy#duration}
        :param aggregations: aggregations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#aggregations GoogleMonitoringAlertPolicy#aggregations}
        :param filter: A filter that identifies which time series should be compared with the threshold.The filter is similar to the one that is specified in the MetricService.ListTimeSeries request (that call is useful to verify the time series that will be retrieved / processed) and must specify the metric type and optionally may contain restrictions on resource type, resource labels, and metric labels. This field may not exceed 2048 Unicode characters in length. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#filter GoogleMonitoringAlertPolicy#filter}
        :param trigger: trigger block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#trigger GoogleMonitoringAlertPolicy#trigger}
        '''
        if isinstance(trigger, dict):
            trigger = GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger(**trigger)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eefc984df64db235c93cad22009c95ffe03bb80fd9888d5d094d2ca9106b4fc3)
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument aggregations", value=aggregations, expected_type=type_hints["aggregations"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument trigger", value=trigger, expected_type=type_hints["trigger"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "duration": duration,
        }
        if aggregations is not None:
            self._values["aggregations"] = aggregations
        if filter is not None:
            self._values["filter"] = filter
        if trigger is not None:
            self._values["trigger"] = trigger

    @builtins.property
    def duration(self) -> builtins.str:
        '''The amount of time that a time series must fail to report new data to be considered failing.

        Currently, only values that are a
        multiple of a minute--e.g. 60s, 120s, or 300s
        --are supported.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#duration GoogleMonitoringAlertPolicy#duration}
        '''
        result = self._values.get("duration")
        assert result is not None, "Required property 'duration' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aggregations(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations"]]]:
        '''aggregations block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#aggregations GoogleMonitoringAlertPolicy#aggregations}
        '''
        result = self._values.get("aggregations")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations"]]], result)

    @builtins.property
    def filter(self) -> typing.Optional[builtins.str]:
        '''A filter that identifies which time series should be compared with the threshold.The filter is similar to the one that is specified in the MetricService.ListTimeSeries request (that call is useful to verify the time series that will be retrieved / processed) and must specify the metric type and optionally may contain restrictions on resource type, resource labels, and metric labels. This field may not exceed 2048 Unicode characters in length.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#filter GoogleMonitoringAlertPolicy#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trigger(
        self,
    ) -> typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger"]:
        '''trigger block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#trigger GoogleMonitoringAlertPolicy#trigger}
        '''
        result = self._values.get("trigger")
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyConditionsConditionAbsent(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations",
    jsii_struct_bases=[],
    name_mapping={
        "alignment_period": "alignmentPeriod",
        "cross_series_reducer": "crossSeriesReducer",
        "group_by_fields": "groupByFields",
        "per_series_aligner": "perSeriesAligner",
    },
)
class GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations:
    def __init__(
        self,
        *,
        alignment_period: typing.Optional[builtins.str] = None,
        cross_series_reducer: typing.Optional[builtins.str] = None,
        group_by_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        per_series_aligner: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param alignment_period: The alignment period for per-time series alignment. If present, alignmentPeriod must be at least 60 seconds. After per-time series alignment, each time series will contain data points only on the period boundaries. If perSeriesAligner is not specified or equals ALIGN_NONE, then this field is ignored. If perSeriesAligner is specified and does not equal ALIGN_NONE, then this field must be defined; otherwise an error is returned. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#alignment_period GoogleMonitoringAlertPolicy#alignment_period}
        :param cross_series_reducer: The approach to be used to combine time series. Not all reducer functions may be applied to all time series, depending on the metric type and the value type of the original time series. Reduction may change the metric type of value type of the time series.Time series data must be aligned in order to perform cross- time series reduction. If crossSeriesReducer is specified, then perSeriesAligner must be specified and not equal ALIGN_NONE and alignmentPeriod must be specified; otherwise, an error is returned. Possible values: ["REDUCE_NONE", "REDUCE_MEAN", "REDUCE_MIN", "REDUCE_MAX", "REDUCE_SUM", "REDUCE_STDDEV", "REDUCE_COUNT", "REDUCE_COUNT_TRUE", "REDUCE_COUNT_FALSE", "REDUCE_FRACTION_TRUE", "REDUCE_PERCENTILE_99", "REDUCE_PERCENTILE_95", "REDUCE_PERCENTILE_50", "REDUCE_PERCENTILE_05"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#cross_series_reducer GoogleMonitoringAlertPolicy#cross_series_reducer}
        :param group_by_fields: The set of fields to preserve when crossSeriesReducer is specified. The groupByFields determine how the time series are partitioned into subsets prior to applying the aggregation function. Each subset contains time series that have the same value for each of the grouping fields. Each individual time series is a member of exactly one subset. The crossSeriesReducer is applied to each subset of time series. It is not possible to reduce across different resource types, so this field implicitly contains resource.type. Fields not specified in groupByFields are aggregated away. If groupByFields is not specified and all the time series have the same resource type, then the time series are aggregated into a single output time series. If crossSeriesReducer is not defined, this field is ignored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#group_by_fields GoogleMonitoringAlertPolicy#group_by_fields}
        :param per_series_aligner: The approach to be used to align individual time series. Not all alignment functions may be applied to all time series, depending on the metric type and value type of the original time series. Alignment may change the metric type or the value type of the time series.Time series data must be aligned in order to perform cross- time series reduction. If crossSeriesReducer is specified, then perSeriesAligner must be specified and not equal ALIGN_NONE and alignmentPeriod must be specified; otherwise, an error is returned. Possible values: ["ALIGN_NONE", "ALIGN_DELTA", "ALIGN_RATE", "ALIGN_INTERPOLATE", "ALIGN_NEXT_OLDER", "ALIGN_MIN", "ALIGN_MAX", "ALIGN_MEAN", "ALIGN_COUNT", "ALIGN_SUM", "ALIGN_STDDEV", "ALIGN_COUNT_TRUE", "ALIGN_COUNT_FALSE", "ALIGN_FRACTION_TRUE", "ALIGN_PERCENTILE_99", "ALIGN_PERCENTILE_95", "ALIGN_PERCENTILE_50", "ALIGN_PERCENTILE_05", "ALIGN_PERCENT_CHANGE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#per_series_aligner GoogleMonitoringAlertPolicy#per_series_aligner}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17abfed6b0545f100ab427535e0340764496dc25fa8a9fd19f34bdec6734e365)
            check_type(argname="argument alignment_period", value=alignment_period, expected_type=type_hints["alignment_period"])
            check_type(argname="argument cross_series_reducer", value=cross_series_reducer, expected_type=type_hints["cross_series_reducer"])
            check_type(argname="argument group_by_fields", value=group_by_fields, expected_type=type_hints["group_by_fields"])
            check_type(argname="argument per_series_aligner", value=per_series_aligner, expected_type=type_hints["per_series_aligner"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if alignment_period is not None:
            self._values["alignment_period"] = alignment_period
        if cross_series_reducer is not None:
            self._values["cross_series_reducer"] = cross_series_reducer
        if group_by_fields is not None:
            self._values["group_by_fields"] = group_by_fields
        if per_series_aligner is not None:
            self._values["per_series_aligner"] = per_series_aligner

    @builtins.property
    def alignment_period(self) -> typing.Optional[builtins.str]:
        '''The alignment period for per-time series alignment.

        If present,
        alignmentPeriod must be at least
        60 seconds. After per-time series
        alignment, each time series will
        contain data points only on the
        period boundaries. If
        perSeriesAligner is not specified
        or equals ALIGN_NONE, then this
        field is ignored. If
        perSeriesAligner is specified and
        does not equal ALIGN_NONE, then
        this field must be defined;
        otherwise an error is returned.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#alignment_period GoogleMonitoringAlertPolicy#alignment_period}
        '''
        result = self._values.get("alignment_period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cross_series_reducer(self) -> typing.Optional[builtins.str]:
        '''The approach to be used to combine time series.

        Not all reducer
        functions may be applied to all
        time series, depending on the
        metric type and the value type of
        the original time series.
        Reduction may change the metric
        type of value type of the time
        series.Time series data must be
        aligned in order to perform cross-
        time series reduction. If
        crossSeriesReducer is specified,
        then perSeriesAligner must be
        specified and not equal ALIGN_NONE
        and alignmentPeriod must be
        specified; otherwise, an error is
        returned. Possible values: ["REDUCE_NONE", "REDUCE_MEAN", "REDUCE_MIN", "REDUCE_MAX", "REDUCE_SUM", "REDUCE_STDDEV", "REDUCE_COUNT", "REDUCE_COUNT_TRUE", "REDUCE_COUNT_FALSE", "REDUCE_FRACTION_TRUE", "REDUCE_PERCENTILE_99", "REDUCE_PERCENTILE_95", "REDUCE_PERCENTILE_50", "REDUCE_PERCENTILE_05"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#cross_series_reducer GoogleMonitoringAlertPolicy#cross_series_reducer}
        '''
        result = self._values.get("cross_series_reducer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_by_fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The set of fields to preserve when crossSeriesReducer is specified.

        The groupByFields determine how
        the time series are partitioned
        into subsets prior to applying the
        aggregation function. Each subset
        contains time series that have the
        same value for each of the
        grouping fields. Each individual
        time series is a member of exactly
        one subset. The crossSeriesReducer
        is applied to each subset of time
        series. It is not possible to
        reduce across different resource
        types, so this field implicitly
        contains resource.type. Fields not
        specified in groupByFields are
        aggregated away. If groupByFields
        is not specified and all the time
        series have the same resource
        type, then the time series are
        aggregated into a single output
        time series. If crossSeriesReducer
        is not defined, this field is
        ignored.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#group_by_fields GoogleMonitoringAlertPolicy#group_by_fields}
        '''
        result = self._values.get("group_by_fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def per_series_aligner(self) -> typing.Optional[builtins.str]:
        '''The approach to be used to align individual time series.

        Not all
        alignment functions may be applied
        to all time series, depending on
        the metric type and value type of
        the original time series.
        Alignment may change the metric
        type or the value type of the time
        series.Time series data must be
        aligned in order to perform cross-
        time series reduction. If
        crossSeriesReducer is specified,
        then perSeriesAligner must be
        specified and not equal ALIGN_NONE
        and alignmentPeriod must be
        specified; otherwise, an error is
        returned. Possible values: ["ALIGN_NONE", "ALIGN_DELTA", "ALIGN_RATE", "ALIGN_INTERPOLATE", "ALIGN_NEXT_OLDER", "ALIGN_MIN", "ALIGN_MAX", "ALIGN_MEAN", "ALIGN_COUNT", "ALIGN_SUM", "ALIGN_STDDEV", "ALIGN_COUNT_TRUE", "ALIGN_COUNT_FALSE", "ALIGN_FRACTION_TRUE", "ALIGN_PERCENTILE_99", "ALIGN_PERCENTILE_95", "ALIGN_PERCENTILE_50", "ALIGN_PERCENTILE_05", "ALIGN_PERCENT_CHANGE"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#per_series_aligner GoogleMonitoringAlertPolicy#per_series_aligner}
        '''
        result = self._values.get("per_series_aligner")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52749dea74f436346fdc3d9fb4b0a823925944cc51a769f133ba623ccdb2deda)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cf5029ea727df7f2980cdbd53862326bd7698c16476801e8049f6eb779acc5b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68fdbb367695e7157e33a54bde10578e4dab7eb0b914e973da1daeb0e36518d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27c96405b2ef3043e4b690bc55c3d32890c6823f05afe421a92904c430d1fddf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4b4f4ee147bdd093aa10bcdc7393b688f398f2cbaa724a4723fc5646f91eda59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad5fb1ae758c29776420c35cc0c60819e32cae15edb63f5f7dc55d6c7fec2cd3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
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
            type_hints = typing.get_type_hints(_typecheckingstub__35083242833c074bcc48e37864c5ee6ba18170690d7c116c94b1544c1c0d1110)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAlignmentPeriod")
    def reset_alignment_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlignmentPeriod", []))

    @jsii.member(jsii_name="resetCrossSeriesReducer")
    def reset_cross_series_reducer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrossSeriesReducer", []))

    @jsii.member(jsii_name="resetGroupByFields")
    def reset_group_by_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupByFields", []))

    @jsii.member(jsii_name="resetPerSeriesAligner")
    def reset_per_series_aligner(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerSeriesAligner", []))

    @builtins.property
    @jsii.member(jsii_name="alignmentPeriodInput")
    def alignment_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alignmentPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="crossSeriesReducerInput")
    def cross_series_reducer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "crossSeriesReducerInput"))

    @builtins.property
    @jsii.member(jsii_name="groupByFieldsInput")
    def group_by_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupByFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="perSeriesAlignerInput")
    def per_series_aligner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "perSeriesAlignerInput"))

    @builtins.property
    @jsii.member(jsii_name="alignmentPeriod")
    def alignment_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alignmentPeriod"))

    @alignment_period.setter
    def alignment_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43127057911cbb4cf1e530b3c31ae69ebff8e296ff72f730795d82f90e760d19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alignmentPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="crossSeriesReducer")
    def cross_series_reducer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "crossSeriesReducer"))

    @cross_series_reducer.setter
    def cross_series_reducer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9801168d6c93601f9eb511793c9fa2716bb22db697cc2840d6d28f6bc6af66c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crossSeriesReducer", value)

    @builtins.property
    @jsii.member(jsii_name="groupByFields")
    def group_by_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "groupByFields"))

    @group_by_fields.setter
    def group_by_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a3ae24820c7fa5a88c457c31e2ff0bd001951e30760f883deabb07ed4834ed3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupByFields", value)

    @builtins.property
    @jsii.member(jsii_name="perSeriesAligner")
    def per_series_aligner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "perSeriesAligner"))

    @per_series_aligner.setter
    def per_series_aligner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7db7ebe7acfa9cfcc16a14eac608efb480e1584b5b3b05d06f663a90ef62d586)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "perSeriesAligner", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6eb8dcb5e1a5d01263b4a1c8658a5bd39a532c8cfbfe9b8384d5f9b021483dcc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleMonitoringAlertPolicyConditionsConditionAbsentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionAbsentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__467f570c82b477fa30522889ad39e976a27e10a1739f6f88df8fa71d905d1cb4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAggregations")
    def put_aggregations(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9e11bda0f0f7f6df4301d2d7982ccf8748c17ba66c99281ade9fd61b42fda28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAggregations", [value]))

    @jsii.member(jsii_name="putTrigger")
    def put_trigger(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        percent: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param count: The absolute number of time series that must fail the predicate for the condition to be triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#count GoogleMonitoringAlertPolicy#count}
        :param percent: The percentage of time series that must fail the predicate for the condition to be triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#percent GoogleMonitoringAlertPolicy#percent}
        '''
        value = GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger(
            count=count, percent=percent
        )

        return typing.cast(None, jsii.invoke(self, "putTrigger", [value]))

    @jsii.member(jsii_name="resetAggregations")
    def reset_aggregations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAggregations", []))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

    @jsii.member(jsii_name="resetTrigger")
    def reset_trigger(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrigger", []))

    @builtins.property
    @jsii.member(jsii_name="aggregations")
    def aggregations(
        self,
    ) -> GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsList:
        return typing.cast(GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsList, jsii.get(self, "aggregations"))

    @builtins.property
    @jsii.member(jsii_name="trigger")
    def trigger(
        self,
    ) -> "GoogleMonitoringAlertPolicyConditionsConditionAbsentTriggerOutputReference":
        return typing.cast("GoogleMonitoringAlertPolicyConditionsConditionAbsentTriggerOutputReference", jsii.get(self, "trigger"))

    @builtins.property
    @jsii.member(jsii_name="aggregationsInput")
    def aggregations_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations]]], jsii.get(self, "aggregationsInput"))

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "durationInput"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerInput")
    def trigger_input(
        self,
    ) -> typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger"]:
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger"], jsii.get(self, "triggerInput"))

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d122e06cd4fa9bbd64e3a6588a7748e2e4b514ffb41b8e6cada356eb9fbc54d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duration", value)

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filter"))

    @filter.setter
    def filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4920e10bd4392bc6bf37e5bf13d42806d0ddd02ffb2b2517c68cd5a61debd30c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filter", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionAbsent]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionAbsent], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionAbsent],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09c3a25a3a7a48a79d31d54c1388383035662c4b4caa6067d2b554cf6069b3ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "percent": "percent"},
)
class GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger:
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        percent: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param count: The absolute number of time series that must fail the predicate for the condition to be triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#count GoogleMonitoringAlertPolicy#count}
        :param percent: The percentage of time series that must fail the predicate for the condition to be triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#percent GoogleMonitoringAlertPolicy#percent}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b447657c17e565fd0c8e9ed41fdc35d6813c3d30498008c3c2b2ca9bf0bcaa5)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument percent", value=percent, expected_type=type_hints["percent"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if percent is not None:
            self._values["percent"] = percent

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''The absolute number of time series that must fail the predicate for the condition to be triggered.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#count GoogleMonitoringAlertPolicy#count}
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def percent(self) -> typing.Optional[jsii.Number]:
        '''The percentage of time series that must fail the predicate for the condition to be triggered.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#percent GoogleMonitoringAlertPolicy#percent}
        '''
        result = self._values.get("percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringAlertPolicyConditionsConditionAbsentTriggerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionAbsentTriggerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5ded9e11baab52465dab9002f85df358e2535b3ced00846266e864285fc79723)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCount")
    def reset_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCount", []))

    @jsii.member(jsii_name="resetPercent")
    def reset_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPercent", []))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="percentInput")
    def percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "percentInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19de0fa1bf17744962636cba665991ab5fe64a9b54a1b7227394ed5f780e0bb0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="percent")
    def percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "percent"))

    @percent.setter
    def percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4308190ba76528a6b38976635be7b6c567e04e26597278adf92fa14fe501ef4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "percent", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bf12369c3e9da25a58fdfa7e99e5d81549f6a1f26ff619073c011952358a540)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionMatchedLog",
    jsii_struct_bases=[],
    name_mapping={"filter": "filter", "label_extractors": "labelExtractors"},
)
class GoogleMonitoringAlertPolicyConditionsConditionMatchedLog:
    def __init__(
        self,
        *,
        filter: builtins.str,
        label_extractors: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param filter: A logs-based filter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#filter GoogleMonitoringAlertPolicy#filter}
        :param label_extractors: A map from a label key to an extractor expression, which is used to extract the value for this label key. Each entry in this map is a specification for how data should be extracted from log entries that match filter. Each combination of extracted values is treated as a separate rule for the purposes of triggering notifications. Label keys and corresponding values can be used in notifications generated by this condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#label_extractors GoogleMonitoringAlertPolicy#label_extractors}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fda0cc62f8180a7fecaadad36329e36cbea5706c370bb415425bda8a2092716c)
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument label_extractors", value=label_extractors, expected_type=type_hints["label_extractors"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "filter": filter,
        }
        if label_extractors is not None:
            self._values["label_extractors"] = label_extractors

    @builtins.property
    def filter(self) -> builtins.str:
        '''A logs-based filter.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#filter GoogleMonitoringAlertPolicy#filter}
        '''
        result = self._values.get("filter")
        assert result is not None, "Required property 'filter' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def label_extractors(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map from a label key to an extractor expression, which is used to extract the value for this label key.

        Each entry in this map is
        a specification for how data should be extracted from log entries that
        match filter. Each combination of extracted values is treated as
        a separate rule for the purposes of triggering notifications.
        Label keys and corresponding values can be used in notifications
        generated by this condition.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#label_extractors GoogleMonitoringAlertPolicy#label_extractors}
        '''
        result = self._values.get("label_extractors")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyConditionsConditionMatchedLog(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringAlertPolicyConditionsConditionMatchedLogOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionMatchedLogOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4a260750df6dcd9ce57cc17f5960b21cecb521639985856598af3364f448a343)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLabelExtractors")
    def reset_label_extractors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabelExtractors", []))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="labelExtractorsInput")
    def label_extractors_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelExtractorsInput"))

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filter"))

    @filter.setter
    def filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf3c4e4c29dbec74b59306d9e6b5761d784d6baef8ffc81063e97dcbc61068a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filter", value)

    @builtins.property
    @jsii.member(jsii_name="labelExtractors")
    def label_extractors(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labelExtractors"))

    @label_extractors.setter
    def label_extractors(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2564fd3feb08ac503ed11e9dc54910f0da6e43a4b314d0f084db38fbc4e0302e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labelExtractors", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionMatchedLog]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionMatchedLog], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionMatchedLog],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29c857ce3fdda3c9609ae1247fa1edc28d74029a51da884dd45c7738d90ba7c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage",
    jsii_struct_bases=[],
    name_mapping={
        "duration": "duration",
        "query": "query",
        "evaluation_missing_data": "evaluationMissingData",
        "trigger": "trigger",
    },
)
class GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage:
    def __init__(
        self,
        *,
        duration: builtins.str,
        query: builtins.str,
        evaluation_missing_data: typing.Optional[builtins.str] = None,
        trigger: typing.Optional[typing.Union["GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param duration: The amount of time that a time series must violate the threshold to be considered failing. Currently, only values that are a multiple of a minute--e.g., 0, 60, 120, or 300 seconds--are supported. If an invalid value is given, an error will be returned. When choosing a duration, it is useful to keep in mind the frequency of the underlying time series data (which may also be affected by any alignments specified in the aggregations field); a good duration is long enough so that a single outlier does not generate spurious alerts, but short enough that unhealthy states are detected and alerted on quickly. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#duration GoogleMonitoringAlertPolicy#duration}
        :param query: Monitoring Query Language query that outputs a boolean stream. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#query GoogleMonitoringAlertPolicy#query}
        :param evaluation_missing_data: A condition control that determines how metric-threshold conditions are evaluated when data stops arriving. Possible values: ["EVALUATION_MISSING_DATA_INACTIVE", "EVALUATION_MISSING_DATA_ACTIVE", "EVALUATION_MISSING_DATA_NO_OP"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#evaluation_missing_data GoogleMonitoringAlertPolicy#evaluation_missing_data}
        :param trigger: trigger block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#trigger GoogleMonitoringAlertPolicy#trigger}
        '''
        if isinstance(trigger, dict):
            trigger = GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger(**trigger)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b68d50107253bb8e6cb13cfafabce9d3456d3946124ea1cb9a9004b0d8c5f38)
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument evaluation_missing_data", value=evaluation_missing_data, expected_type=type_hints["evaluation_missing_data"])
            check_type(argname="argument trigger", value=trigger, expected_type=type_hints["trigger"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "duration": duration,
            "query": query,
        }
        if evaluation_missing_data is not None:
            self._values["evaluation_missing_data"] = evaluation_missing_data
        if trigger is not None:
            self._values["trigger"] = trigger

    @builtins.property
    def duration(self) -> builtins.str:
        '''The amount of time that a time series must violate the threshold to be considered failing.

        Currently, only values that are a
        multiple of a minute--e.g., 0, 60, 120, or
        300 seconds--are supported. If an invalid
        value is given, an error will be returned.
        When choosing a duration, it is useful to
        keep in mind the frequency of the underlying
        time series data (which may also be affected
        by any alignments specified in the
        aggregations field); a good duration is long
        enough so that a single outlier does not
        generate spurious alerts, but short enough
        that unhealthy states are detected and
        alerted on quickly.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#duration GoogleMonitoringAlertPolicy#duration}
        '''
        result = self._values.get("duration")
        assert result is not None, "Required property 'duration' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query(self) -> builtins.str:
        '''Monitoring Query Language query that outputs a boolean stream.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#query GoogleMonitoringAlertPolicy#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def evaluation_missing_data(self) -> typing.Optional[builtins.str]:
        '''A condition control that determines how metric-threshold conditions are evaluated when data stops arriving. Possible values: ["EVALUATION_MISSING_DATA_INACTIVE", "EVALUATION_MISSING_DATA_ACTIVE", "EVALUATION_MISSING_DATA_NO_OP"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#evaluation_missing_data GoogleMonitoringAlertPolicy#evaluation_missing_data}
        '''
        result = self._values.get("evaluation_missing_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trigger(
        self,
    ) -> typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger"]:
        '''trigger block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#trigger GoogleMonitoringAlertPolicy#trigger}
        '''
        result = self._values.get("trigger")
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__645d2b8b463d46ec6fb10db36f1f1df61306db07be313a2ceb61cca68332435c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTrigger")
    def put_trigger(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        percent: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param count: The absolute number of time series that must fail the predicate for the condition to be triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#count GoogleMonitoringAlertPolicy#count}
        :param percent: The percentage of time series that must fail the predicate for the condition to be triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#percent GoogleMonitoringAlertPolicy#percent}
        '''
        value = GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger(
            count=count, percent=percent
        )

        return typing.cast(None, jsii.invoke(self, "putTrigger", [value]))

    @jsii.member(jsii_name="resetEvaluationMissingData")
    def reset_evaluation_missing_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluationMissingData", []))

    @jsii.member(jsii_name="resetTrigger")
    def reset_trigger(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrigger", []))

    @builtins.property
    @jsii.member(jsii_name="trigger")
    def trigger(
        self,
    ) -> "GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTriggerOutputReference":
        return typing.cast("GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTriggerOutputReference", jsii.get(self, "trigger"))

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "durationInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluationMissingDataInput")
    def evaluation_missing_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "evaluationMissingDataInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerInput")
    def trigger_input(
        self,
    ) -> typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger"]:
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger"], jsii.get(self, "triggerInput"))

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b455f65455c6990143af9864e7d3dadebbfaf202643f3aa65cbf71a289ee92ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duration", value)

    @builtins.property
    @jsii.member(jsii_name="evaluationMissingData")
    def evaluation_missing_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "evaluationMissingData"))

    @evaluation_missing_data.setter
    def evaluation_missing_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2599dfca99f3a1103c3d77a9f416a0215b57a36699bcc6283158890018ef8c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationMissingData", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1461b9df06204b462f5988f9546d21639fa9d0437fcc362284b6c10154e8862c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1badc7b3e48c7177fe51fa46ed0080d4036c850e135baf8ecf07c32b99c8d73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "percent": "percent"},
)
class GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger:
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        percent: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param count: The absolute number of time series that must fail the predicate for the condition to be triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#count GoogleMonitoringAlertPolicy#count}
        :param percent: The percentage of time series that must fail the predicate for the condition to be triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#percent GoogleMonitoringAlertPolicy#percent}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79d5c009917e96b01b9242f82433828d19a0c3df5b336eb39b7dd188aade2a5e)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument percent", value=percent, expected_type=type_hints["percent"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if percent is not None:
            self._values["percent"] = percent

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''The absolute number of time series that must fail the predicate for the condition to be triggered.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#count GoogleMonitoringAlertPolicy#count}
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def percent(self) -> typing.Optional[jsii.Number]:
        '''The percentage of time series that must fail the predicate for the condition to be triggered.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#percent GoogleMonitoringAlertPolicy#percent}
        '''
        result = self._values.get("percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTriggerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTriggerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b341dba5019c4151ef30489213242c3b3a774d617b06a112a268f57367d59aec)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCount")
    def reset_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCount", []))

    @jsii.member(jsii_name="resetPercent")
    def reset_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPercent", []))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="percentInput")
    def percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "percentInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f80e59c07506226c4fb92a3eb4ffe305ea2170bf11b3beb1b019808d2be1253)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="percent")
    def percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "percent"))

    @percent.setter
    def percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7acdcda14f63fdff8d8d065e24d4e9e14a7c1c1cc698aadff2e8a7507ba3fd9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "percent", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af5bf9e9e5ef2e23e948e46a89660963a12a0f56d87fcdfa5a04e382d9f256f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionThreshold",
    jsii_struct_bases=[],
    name_mapping={
        "comparison": "comparison",
        "duration": "duration",
        "aggregations": "aggregations",
        "denominator_aggregations": "denominatorAggregations",
        "denominator_filter": "denominatorFilter",
        "evaluation_missing_data": "evaluationMissingData",
        "filter": "filter",
        "threshold_value": "thresholdValue",
        "trigger": "trigger",
    },
)
class GoogleMonitoringAlertPolicyConditionsConditionThreshold:
    def __init__(
        self,
        *,
        comparison: builtins.str,
        duration: builtins.str,
        aggregations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations", typing.Dict[builtins.str, typing.Any]]]]] = None,
        denominator_aggregations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations", typing.Dict[builtins.str, typing.Any]]]]] = None,
        denominator_filter: typing.Optional[builtins.str] = None,
        evaluation_missing_data: typing.Optional[builtins.str] = None,
        filter: typing.Optional[builtins.str] = None,
        threshold_value: typing.Optional[jsii.Number] = None,
        trigger: typing.Optional[typing.Union["GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param comparison: The comparison to apply between the time series (indicated by filter and aggregation) and the threshold (indicated by threshold_value). The comparison is applied on each time series, with the time series on the left-hand side and the threshold on the right-hand side. Only COMPARISON_LT and COMPARISON_GT are supported currently. Possible values: ["COMPARISON_GT", "COMPARISON_GE", "COMPARISON_LT", "COMPARISON_LE", "COMPARISON_EQ", "COMPARISON_NE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#comparison GoogleMonitoringAlertPolicy#comparison}
        :param duration: The amount of time that a time series must violate the threshold to be considered failing. Currently, only values that are a multiple of a minute--e.g., 0, 60, 120, or 300 seconds--are supported. If an invalid value is given, an error will be returned. When choosing a duration, it is useful to keep in mind the frequency of the underlying time series data (which may also be affected by any alignments specified in the aggregations field); a good duration is long enough so that a single outlier does not generate spurious alerts, but short enough that unhealthy states are detected and alerted on quickly. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#duration GoogleMonitoringAlertPolicy#duration}
        :param aggregations: aggregations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#aggregations GoogleMonitoringAlertPolicy#aggregations}
        :param denominator_aggregations: denominator_aggregations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#denominator_aggregations GoogleMonitoringAlertPolicy#denominator_aggregations}
        :param denominator_filter: A filter that identifies a time series that should be used as the denominator of a ratio that will be compared with the threshold. If a denominator_filter is specified, the time series specified by the filter field will be used as the numerator.The filter is similar to the one that is specified in the MetricService.ListTimeSeries request (that call is useful to verify the time series that will be retrieved / processed) and must specify the metric type and optionally may contain restrictions on resource type, resource labels, and metric labels. This field may not exceed 2048 Unicode characters in length. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#denominator_filter GoogleMonitoringAlertPolicy#denominator_filter}
        :param evaluation_missing_data: A condition control that determines how metric-threshold conditions are evaluated when data stops arriving. Possible values: ["EVALUATION_MISSING_DATA_INACTIVE", "EVALUATION_MISSING_DATA_ACTIVE", "EVALUATION_MISSING_DATA_NO_OP"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#evaluation_missing_data GoogleMonitoringAlertPolicy#evaluation_missing_data}
        :param filter: A filter that identifies which time series should be compared with the threshold.The filter is similar to the one that is specified in the MetricService.ListTimeSeries request (that call is useful to verify the time series that will be retrieved / processed) and must specify the metric type and optionally may contain restrictions on resource type, resource labels, and metric labels. This field may not exceed 2048 Unicode characters in length. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#filter GoogleMonitoringAlertPolicy#filter}
        :param threshold_value: A value against which to compare the time series. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#threshold_value GoogleMonitoringAlertPolicy#threshold_value}
        :param trigger: trigger block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#trigger GoogleMonitoringAlertPolicy#trigger}
        '''
        if isinstance(trigger, dict):
            trigger = GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger(**trigger)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29ea0561e17834109603262cd4c17249a064e6bdcc49316b13c97783e1dc9921)
            check_type(argname="argument comparison", value=comparison, expected_type=type_hints["comparison"])
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument aggregations", value=aggregations, expected_type=type_hints["aggregations"])
            check_type(argname="argument denominator_aggregations", value=denominator_aggregations, expected_type=type_hints["denominator_aggregations"])
            check_type(argname="argument denominator_filter", value=denominator_filter, expected_type=type_hints["denominator_filter"])
            check_type(argname="argument evaluation_missing_data", value=evaluation_missing_data, expected_type=type_hints["evaluation_missing_data"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument threshold_value", value=threshold_value, expected_type=type_hints["threshold_value"])
            check_type(argname="argument trigger", value=trigger, expected_type=type_hints["trigger"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "comparison": comparison,
            "duration": duration,
        }
        if aggregations is not None:
            self._values["aggregations"] = aggregations
        if denominator_aggregations is not None:
            self._values["denominator_aggregations"] = denominator_aggregations
        if denominator_filter is not None:
            self._values["denominator_filter"] = denominator_filter
        if evaluation_missing_data is not None:
            self._values["evaluation_missing_data"] = evaluation_missing_data
        if filter is not None:
            self._values["filter"] = filter
        if threshold_value is not None:
            self._values["threshold_value"] = threshold_value
        if trigger is not None:
            self._values["trigger"] = trigger

    @builtins.property
    def comparison(self) -> builtins.str:
        '''The comparison to apply between the time series (indicated by filter and aggregation) and the threshold (indicated by threshold_value).

        The comparison is applied
        on each time series, with the time series on
        the left-hand side and the threshold on the
        right-hand side. Only COMPARISON_LT and
        COMPARISON_GT are supported currently. Possible values: ["COMPARISON_GT", "COMPARISON_GE", "COMPARISON_LT", "COMPARISON_LE", "COMPARISON_EQ", "COMPARISON_NE"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#comparison GoogleMonitoringAlertPolicy#comparison}
        '''
        result = self._values.get("comparison")
        assert result is not None, "Required property 'comparison' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def duration(self) -> builtins.str:
        '''The amount of time that a time series must violate the threshold to be considered failing.

        Currently, only values that are a
        multiple of a minute--e.g., 0, 60, 120, or
        300 seconds--are supported. If an invalid
        value is given, an error will be returned.
        When choosing a duration, it is useful to
        keep in mind the frequency of the underlying
        time series data (which may also be affected
        by any alignments specified in the
        aggregations field); a good duration is long
        enough so that a single outlier does not
        generate spurious alerts, but short enough
        that unhealthy states are detected and
        alerted on quickly.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#duration GoogleMonitoringAlertPolicy#duration}
        '''
        result = self._values.get("duration")
        assert result is not None, "Required property 'duration' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aggregations(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations"]]]:
        '''aggregations block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#aggregations GoogleMonitoringAlertPolicy#aggregations}
        '''
        result = self._values.get("aggregations")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations"]]], result)

    @builtins.property
    def denominator_aggregations(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations"]]]:
        '''denominator_aggregations block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#denominator_aggregations GoogleMonitoringAlertPolicy#denominator_aggregations}
        '''
        result = self._values.get("denominator_aggregations")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations"]]], result)

    @builtins.property
    def denominator_filter(self) -> typing.Optional[builtins.str]:
        '''A filter that identifies a time series that should be used as the denominator of a ratio that will be compared with the threshold.

        If
        a denominator_filter is specified, the time
        series specified by the filter field will be
        used as the numerator.The filter is similar
        to the one that is specified in the
        MetricService.ListTimeSeries request (that
        call is useful to verify the time series
        that will be retrieved / processed) and must
        specify the metric type and optionally may
        contain restrictions on resource type,
        resource labels, and metric labels. This
        field may not exceed 2048 Unicode characters
        in length.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#denominator_filter GoogleMonitoringAlertPolicy#denominator_filter}
        '''
        result = self._values.get("denominator_filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def evaluation_missing_data(self) -> typing.Optional[builtins.str]:
        '''A condition control that determines how metric-threshold conditions are evaluated when data stops arriving. Possible values: ["EVALUATION_MISSING_DATA_INACTIVE", "EVALUATION_MISSING_DATA_ACTIVE", "EVALUATION_MISSING_DATA_NO_OP"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#evaluation_missing_data GoogleMonitoringAlertPolicy#evaluation_missing_data}
        '''
        result = self._values.get("evaluation_missing_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def filter(self) -> typing.Optional[builtins.str]:
        '''A filter that identifies which time series should be compared with the threshold.The filter is similar to the one that is specified in the MetricService.ListTimeSeries request (that call is useful to verify the time series that will be retrieved / processed) and must specify the metric type and optionally may contain restrictions on resource type, resource labels, and metric labels. This field may not exceed 2048 Unicode characters in length.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#filter GoogleMonitoringAlertPolicy#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def threshold_value(self) -> typing.Optional[jsii.Number]:
        '''A value against which to compare the time series.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#threshold_value GoogleMonitoringAlertPolicy#threshold_value}
        '''
        result = self._values.get("threshold_value")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def trigger(
        self,
    ) -> typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger"]:
        '''trigger block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#trigger GoogleMonitoringAlertPolicy#trigger}
        '''
        result = self._values.get("trigger")
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyConditionsConditionThreshold(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations",
    jsii_struct_bases=[],
    name_mapping={
        "alignment_period": "alignmentPeriod",
        "cross_series_reducer": "crossSeriesReducer",
        "group_by_fields": "groupByFields",
        "per_series_aligner": "perSeriesAligner",
    },
)
class GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations:
    def __init__(
        self,
        *,
        alignment_period: typing.Optional[builtins.str] = None,
        cross_series_reducer: typing.Optional[builtins.str] = None,
        group_by_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        per_series_aligner: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param alignment_period: The alignment period for per-time series alignment. If present, alignmentPeriod must be at least 60 seconds. After per-time series alignment, each time series will contain data points only on the period boundaries. If perSeriesAligner is not specified or equals ALIGN_NONE, then this field is ignored. If perSeriesAligner is specified and does not equal ALIGN_NONE, then this field must be defined; otherwise an error is returned. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#alignment_period GoogleMonitoringAlertPolicy#alignment_period}
        :param cross_series_reducer: The approach to be used to combine time series. Not all reducer functions may be applied to all time series, depending on the metric type and the value type of the original time series. Reduction may change the metric type of value type of the time series.Time series data must be aligned in order to perform cross- time series reduction. If crossSeriesReducer is specified, then perSeriesAligner must be specified and not equal ALIGN_NONE and alignmentPeriod must be specified; otherwise, an error is returned. Possible values: ["REDUCE_NONE", "REDUCE_MEAN", "REDUCE_MIN", "REDUCE_MAX", "REDUCE_SUM", "REDUCE_STDDEV", "REDUCE_COUNT", "REDUCE_COUNT_TRUE", "REDUCE_COUNT_FALSE", "REDUCE_FRACTION_TRUE", "REDUCE_PERCENTILE_99", "REDUCE_PERCENTILE_95", "REDUCE_PERCENTILE_50", "REDUCE_PERCENTILE_05"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#cross_series_reducer GoogleMonitoringAlertPolicy#cross_series_reducer}
        :param group_by_fields: The set of fields to preserve when crossSeriesReducer is specified. The groupByFields determine how the time series are partitioned into subsets prior to applying the aggregation function. Each subset contains time series that have the same value for each of the grouping fields. Each individual time series is a member of exactly one subset. The crossSeriesReducer is applied to each subset of time series. It is not possible to reduce across different resource types, so this field implicitly contains resource.type. Fields not specified in groupByFields are aggregated away. If groupByFields is not specified and all the time series have the same resource type, then the time series are aggregated into a single output time series. If crossSeriesReducer is not defined, this field is ignored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#group_by_fields GoogleMonitoringAlertPolicy#group_by_fields}
        :param per_series_aligner: The approach to be used to align individual time series. Not all alignment functions may be applied to all time series, depending on the metric type and value type of the original time series. Alignment may change the metric type or the value type of the time series.Time series data must be aligned in order to perform cross- time series reduction. If crossSeriesReducer is specified, then perSeriesAligner must be specified and not equal ALIGN_NONE and alignmentPeriod must be specified; otherwise, an error is returned. Possible values: ["ALIGN_NONE", "ALIGN_DELTA", "ALIGN_RATE", "ALIGN_INTERPOLATE", "ALIGN_NEXT_OLDER", "ALIGN_MIN", "ALIGN_MAX", "ALIGN_MEAN", "ALIGN_COUNT", "ALIGN_SUM", "ALIGN_STDDEV", "ALIGN_COUNT_TRUE", "ALIGN_COUNT_FALSE", "ALIGN_FRACTION_TRUE", "ALIGN_PERCENTILE_99", "ALIGN_PERCENTILE_95", "ALIGN_PERCENTILE_50", "ALIGN_PERCENTILE_05", "ALIGN_PERCENT_CHANGE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#per_series_aligner GoogleMonitoringAlertPolicy#per_series_aligner}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ba53b0de8fbdde35caf06f0c12ef8869296dc81f72bcbfb03139b775aef2596)
            check_type(argname="argument alignment_period", value=alignment_period, expected_type=type_hints["alignment_period"])
            check_type(argname="argument cross_series_reducer", value=cross_series_reducer, expected_type=type_hints["cross_series_reducer"])
            check_type(argname="argument group_by_fields", value=group_by_fields, expected_type=type_hints["group_by_fields"])
            check_type(argname="argument per_series_aligner", value=per_series_aligner, expected_type=type_hints["per_series_aligner"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if alignment_period is not None:
            self._values["alignment_period"] = alignment_period
        if cross_series_reducer is not None:
            self._values["cross_series_reducer"] = cross_series_reducer
        if group_by_fields is not None:
            self._values["group_by_fields"] = group_by_fields
        if per_series_aligner is not None:
            self._values["per_series_aligner"] = per_series_aligner

    @builtins.property
    def alignment_period(self) -> typing.Optional[builtins.str]:
        '''The alignment period for per-time series alignment.

        If present,
        alignmentPeriod must be at least
        60 seconds. After per-time series
        alignment, each time series will
        contain data points only on the
        period boundaries. If
        perSeriesAligner is not specified
        or equals ALIGN_NONE, then this
        field is ignored. If
        perSeriesAligner is specified and
        does not equal ALIGN_NONE, then
        this field must be defined;
        otherwise an error is returned.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#alignment_period GoogleMonitoringAlertPolicy#alignment_period}
        '''
        result = self._values.get("alignment_period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cross_series_reducer(self) -> typing.Optional[builtins.str]:
        '''The approach to be used to combine time series.

        Not all reducer
        functions may be applied to all
        time series, depending on the
        metric type and the value type of
        the original time series.
        Reduction may change the metric
        type of value type of the time
        series.Time series data must be
        aligned in order to perform cross-
        time series reduction. If
        crossSeriesReducer is specified,
        then perSeriesAligner must be
        specified and not equal ALIGN_NONE
        and alignmentPeriod must be
        specified; otherwise, an error is
        returned. Possible values: ["REDUCE_NONE", "REDUCE_MEAN", "REDUCE_MIN", "REDUCE_MAX", "REDUCE_SUM", "REDUCE_STDDEV", "REDUCE_COUNT", "REDUCE_COUNT_TRUE", "REDUCE_COUNT_FALSE", "REDUCE_FRACTION_TRUE", "REDUCE_PERCENTILE_99", "REDUCE_PERCENTILE_95", "REDUCE_PERCENTILE_50", "REDUCE_PERCENTILE_05"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#cross_series_reducer GoogleMonitoringAlertPolicy#cross_series_reducer}
        '''
        result = self._values.get("cross_series_reducer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_by_fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The set of fields to preserve when crossSeriesReducer is specified.

        The groupByFields determine how
        the time series are partitioned
        into subsets prior to applying the
        aggregation function. Each subset
        contains time series that have the
        same value for each of the
        grouping fields. Each individual
        time series is a member of exactly
        one subset. The crossSeriesReducer
        is applied to each subset of time
        series. It is not possible to
        reduce across different resource
        types, so this field implicitly
        contains resource.type. Fields not
        specified in groupByFields are
        aggregated away. If groupByFields
        is not specified and all the time
        series have the same resource
        type, then the time series are
        aggregated into a single output
        time series. If crossSeriesReducer
        is not defined, this field is
        ignored.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#group_by_fields GoogleMonitoringAlertPolicy#group_by_fields}
        '''
        result = self._values.get("group_by_fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def per_series_aligner(self) -> typing.Optional[builtins.str]:
        '''The approach to be used to align individual time series.

        Not all
        alignment functions may be applied
        to all time series, depending on
        the metric type and value type of
        the original time series.
        Alignment may change the metric
        type or the value type of the time
        series.Time series data must be
        aligned in order to perform cross-
        time series reduction. If
        crossSeriesReducer is specified,
        then perSeriesAligner must be
        specified and not equal ALIGN_NONE
        and alignmentPeriod must be
        specified; otherwise, an error is
        returned. Possible values: ["ALIGN_NONE", "ALIGN_DELTA", "ALIGN_RATE", "ALIGN_INTERPOLATE", "ALIGN_NEXT_OLDER", "ALIGN_MIN", "ALIGN_MAX", "ALIGN_MEAN", "ALIGN_COUNT", "ALIGN_SUM", "ALIGN_STDDEV", "ALIGN_COUNT_TRUE", "ALIGN_COUNT_FALSE", "ALIGN_FRACTION_TRUE", "ALIGN_PERCENTILE_99", "ALIGN_PERCENTILE_95", "ALIGN_PERCENTILE_50", "ALIGN_PERCENTILE_05", "ALIGN_PERCENT_CHANGE"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#per_series_aligner GoogleMonitoringAlertPolicy#per_series_aligner}
        '''
        result = self._values.get("per_series_aligner")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdfc59c4095596210e1ef50791fcfbff669b89187bd6f2d7f8ccd4cdd6e16dda)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c573e613d88410e13115cd6f5b824d8049d0b28c6a16726184a8a7fa6bb541d1)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c512af89406ee3f99c4725cd5d49e6efaa923a7d39a745f5de6e773ea5546b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec53d237333b959ab5ac2f547b01219975cd135d3b6f346f9601a194ecd53e9a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__33878a8474860a94ea24659dcecc58228993d1e796f3d73484b6837e3a5137e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85fb1f253e4ee8308786dd82b1c6d7ea5376d1019ea8a2bc05e90bf31b48948e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
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
            type_hints = typing.get_type_hints(_typecheckingstub__19e79989278d25fcae0f15b314a44dd1fdb585b285f82bef881e8dd25d1654db)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAlignmentPeriod")
    def reset_alignment_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlignmentPeriod", []))

    @jsii.member(jsii_name="resetCrossSeriesReducer")
    def reset_cross_series_reducer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrossSeriesReducer", []))

    @jsii.member(jsii_name="resetGroupByFields")
    def reset_group_by_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupByFields", []))

    @jsii.member(jsii_name="resetPerSeriesAligner")
    def reset_per_series_aligner(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerSeriesAligner", []))

    @builtins.property
    @jsii.member(jsii_name="alignmentPeriodInput")
    def alignment_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alignmentPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="crossSeriesReducerInput")
    def cross_series_reducer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "crossSeriesReducerInput"))

    @builtins.property
    @jsii.member(jsii_name="groupByFieldsInput")
    def group_by_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupByFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="perSeriesAlignerInput")
    def per_series_aligner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "perSeriesAlignerInput"))

    @builtins.property
    @jsii.member(jsii_name="alignmentPeriod")
    def alignment_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alignmentPeriod"))

    @alignment_period.setter
    def alignment_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edd46198e4601f0f880a46dfa8ab6e3de33606564241570f0deae5834ca7c91b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alignmentPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="crossSeriesReducer")
    def cross_series_reducer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "crossSeriesReducer"))

    @cross_series_reducer.setter
    def cross_series_reducer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a73cbcf5b3f186da033f56ddf1de80e7cdfa6a5a8fa339cf2679ceff96c7e9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crossSeriesReducer", value)

    @builtins.property
    @jsii.member(jsii_name="groupByFields")
    def group_by_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "groupByFields"))

    @group_by_fields.setter
    def group_by_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c45ae60c3a0fad04f04041b5ced248a96466854e4f6fa4ed9634e97e28ac319)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupByFields", value)

    @builtins.property
    @jsii.member(jsii_name="perSeriesAligner")
    def per_series_aligner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "perSeriesAligner"))

    @per_series_aligner.setter
    def per_series_aligner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fc0854ff068fe000d3d8274a68cd5892e12faddccf1e044afdce6927e95e405)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "perSeriesAligner", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__092990a03c27136546bb788a1ced1efe9be9abf705a4988672e850e9b902fd35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations",
    jsii_struct_bases=[],
    name_mapping={
        "alignment_period": "alignmentPeriod",
        "cross_series_reducer": "crossSeriesReducer",
        "group_by_fields": "groupByFields",
        "per_series_aligner": "perSeriesAligner",
    },
)
class GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations:
    def __init__(
        self,
        *,
        alignment_period: typing.Optional[builtins.str] = None,
        cross_series_reducer: typing.Optional[builtins.str] = None,
        group_by_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        per_series_aligner: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param alignment_period: The alignment period for per-time series alignment. If present, alignmentPeriod must be at least 60 seconds. After per-time series alignment, each time series will contain data points only on the period boundaries. If perSeriesAligner is not specified or equals ALIGN_NONE, then this field is ignored. If perSeriesAligner is specified and does not equal ALIGN_NONE, then this field must be defined; otherwise an error is returned. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#alignment_period GoogleMonitoringAlertPolicy#alignment_period}
        :param cross_series_reducer: The approach to be used to combine time series. Not all reducer functions may be applied to all time series, depending on the metric type and the value type of the original time series. Reduction may change the metric type of value type of the time series.Time series data must be aligned in order to perform cross- time series reduction. If crossSeriesReducer is specified, then perSeriesAligner must be specified and not equal ALIGN_NONE and alignmentPeriod must be specified; otherwise, an error is returned. Possible values: ["REDUCE_NONE", "REDUCE_MEAN", "REDUCE_MIN", "REDUCE_MAX", "REDUCE_SUM", "REDUCE_STDDEV", "REDUCE_COUNT", "REDUCE_COUNT_TRUE", "REDUCE_COUNT_FALSE", "REDUCE_FRACTION_TRUE", "REDUCE_PERCENTILE_99", "REDUCE_PERCENTILE_95", "REDUCE_PERCENTILE_50", "REDUCE_PERCENTILE_05"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#cross_series_reducer GoogleMonitoringAlertPolicy#cross_series_reducer}
        :param group_by_fields: The set of fields to preserve when crossSeriesReducer is specified. The groupByFields determine how the time series are partitioned into subsets prior to applying the aggregation function. Each subset contains time series that have the same value for each of the grouping fields. Each individual time series is a member of exactly one subset. The crossSeriesReducer is applied to each subset of time series. It is not possible to reduce across different resource types, so this field implicitly contains resource.type. Fields not specified in groupByFields are aggregated away. If groupByFields is not specified and all the time series have the same resource type, then the time series are aggregated into a single output time series. If crossSeriesReducer is not defined, this field is ignored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#group_by_fields GoogleMonitoringAlertPolicy#group_by_fields}
        :param per_series_aligner: The approach to be used to align individual time series. Not all alignment functions may be applied to all time series, depending on the metric type and value type of the original time series. Alignment may change the metric type or the value type of the time series.Time series data must be aligned in order to perform cross- time series reduction. If crossSeriesReducer is specified, then perSeriesAligner must be specified and not equal ALIGN_NONE and alignmentPeriod must be specified; otherwise, an error is returned. Possible values: ["ALIGN_NONE", "ALIGN_DELTA", "ALIGN_RATE", "ALIGN_INTERPOLATE", "ALIGN_NEXT_OLDER", "ALIGN_MIN", "ALIGN_MAX", "ALIGN_MEAN", "ALIGN_COUNT", "ALIGN_SUM", "ALIGN_STDDEV", "ALIGN_COUNT_TRUE", "ALIGN_COUNT_FALSE", "ALIGN_FRACTION_TRUE", "ALIGN_PERCENTILE_99", "ALIGN_PERCENTILE_95", "ALIGN_PERCENTILE_50", "ALIGN_PERCENTILE_05", "ALIGN_PERCENT_CHANGE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#per_series_aligner GoogleMonitoringAlertPolicy#per_series_aligner}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11a22636bdb75b0dac8627d0214261d8fa7049fbe8aebf1d999e4dcdd35e7c5e)
            check_type(argname="argument alignment_period", value=alignment_period, expected_type=type_hints["alignment_period"])
            check_type(argname="argument cross_series_reducer", value=cross_series_reducer, expected_type=type_hints["cross_series_reducer"])
            check_type(argname="argument group_by_fields", value=group_by_fields, expected_type=type_hints["group_by_fields"])
            check_type(argname="argument per_series_aligner", value=per_series_aligner, expected_type=type_hints["per_series_aligner"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if alignment_period is not None:
            self._values["alignment_period"] = alignment_period
        if cross_series_reducer is not None:
            self._values["cross_series_reducer"] = cross_series_reducer
        if group_by_fields is not None:
            self._values["group_by_fields"] = group_by_fields
        if per_series_aligner is not None:
            self._values["per_series_aligner"] = per_series_aligner

    @builtins.property
    def alignment_period(self) -> typing.Optional[builtins.str]:
        '''The alignment period for per-time series alignment.

        If present,
        alignmentPeriod must be at least
        60 seconds. After per-time series
        alignment, each time series will
        contain data points only on the
        period boundaries. If
        perSeriesAligner is not specified
        or equals ALIGN_NONE, then this
        field is ignored. If
        perSeriesAligner is specified and
        does not equal ALIGN_NONE, then
        this field must be defined;
        otherwise an error is returned.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#alignment_period GoogleMonitoringAlertPolicy#alignment_period}
        '''
        result = self._values.get("alignment_period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cross_series_reducer(self) -> typing.Optional[builtins.str]:
        '''The approach to be used to combine time series.

        Not all reducer
        functions may be applied to all
        time series, depending on the
        metric type and the value type of
        the original time series.
        Reduction may change the metric
        type of value type of the time
        series.Time series data must be
        aligned in order to perform cross-
        time series reduction. If
        crossSeriesReducer is specified,
        then perSeriesAligner must be
        specified and not equal ALIGN_NONE
        and alignmentPeriod must be
        specified; otherwise, an error is
        returned. Possible values: ["REDUCE_NONE", "REDUCE_MEAN", "REDUCE_MIN", "REDUCE_MAX", "REDUCE_SUM", "REDUCE_STDDEV", "REDUCE_COUNT", "REDUCE_COUNT_TRUE", "REDUCE_COUNT_FALSE", "REDUCE_FRACTION_TRUE", "REDUCE_PERCENTILE_99", "REDUCE_PERCENTILE_95", "REDUCE_PERCENTILE_50", "REDUCE_PERCENTILE_05"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#cross_series_reducer GoogleMonitoringAlertPolicy#cross_series_reducer}
        '''
        result = self._values.get("cross_series_reducer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_by_fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The set of fields to preserve when crossSeriesReducer is specified.

        The groupByFields determine how
        the time series are partitioned
        into subsets prior to applying the
        aggregation function. Each subset
        contains time series that have the
        same value for each of the
        grouping fields. Each individual
        time series is a member of exactly
        one subset. The crossSeriesReducer
        is applied to each subset of time
        series. It is not possible to
        reduce across different resource
        types, so this field implicitly
        contains resource.type. Fields not
        specified in groupByFields are
        aggregated away. If groupByFields
        is not specified and all the time
        series have the same resource
        type, then the time series are
        aggregated into a single output
        time series. If crossSeriesReducer
        is not defined, this field is
        ignored.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#group_by_fields GoogleMonitoringAlertPolicy#group_by_fields}
        '''
        result = self._values.get("group_by_fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def per_series_aligner(self) -> typing.Optional[builtins.str]:
        '''The approach to be used to align individual time series.

        Not all
        alignment functions may be applied
        to all time series, depending on
        the metric type and value type of
        the original time series.
        Alignment may change the metric
        type or the value type of the time
        series.Time series data must be
        aligned in order to perform cross-
        time series reduction. If
        crossSeriesReducer is specified,
        then perSeriesAligner must be
        specified and not equal ALIGN_NONE
        and alignmentPeriod must be
        specified; otherwise, an error is
        returned. Possible values: ["ALIGN_NONE", "ALIGN_DELTA", "ALIGN_RATE", "ALIGN_INTERPOLATE", "ALIGN_NEXT_OLDER", "ALIGN_MIN", "ALIGN_MAX", "ALIGN_MEAN", "ALIGN_COUNT", "ALIGN_SUM", "ALIGN_STDDEV", "ALIGN_COUNT_TRUE", "ALIGN_COUNT_FALSE", "ALIGN_FRACTION_TRUE", "ALIGN_PERCENTILE_99", "ALIGN_PERCENTILE_95", "ALIGN_PERCENTILE_50", "ALIGN_PERCENTILE_05", "ALIGN_PERCENT_CHANGE"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#per_series_aligner GoogleMonitoringAlertPolicy#per_series_aligner}
        '''
        result = self._values.get("per_series_aligner")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__644c63baceda630d63bf15e77fad9c38e2538f6a6a4e3efe96ae45b93dd1da1a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75cbbbe83667a429be7ee1e2def7457a4efa11abd665e3015327c45ae65340b7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3162ac10558e825cbe5fec86e638a575d3fd62c839e4e51559d0c7b6a1bb2ae8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__646cce21faa990a8119783e0a2069eae054d641199e3cf2a88caadd37337f216)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dbb3f7745c84720f0034293f0d47f47b0a9a7ab86ded6c153bb203aae486395c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d08607cdbbc04b47c50b7cff7760fb4d5762ae8afacbe296ad1919a0385db7d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
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
            type_hints = typing.get_type_hints(_typecheckingstub__90eccc5d61bf52866e74c4552260fd1cd3c531b65c5ea517818505824f545fae)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAlignmentPeriod")
    def reset_alignment_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlignmentPeriod", []))

    @jsii.member(jsii_name="resetCrossSeriesReducer")
    def reset_cross_series_reducer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrossSeriesReducer", []))

    @jsii.member(jsii_name="resetGroupByFields")
    def reset_group_by_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupByFields", []))

    @jsii.member(jsii_name="resetPerSeriesAligner")
    def reset_per_series_aligner(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerSeriesAligner", []))

    @builtins.property
    @jsii.member(jsii_name="alignmentPeriodInput")
    def alignment_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alignmentPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="crossSeriesReducerInput")
    def cross_series_reducer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "crossSeriesReducerInput"))

    @builtins.property
    @jsii.member(jsii_name="groupByFieldsInput")
    def group_by_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupByFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="perSeriesAlignerInput")
    def per_series_aligner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "perSeriesAlignerInput"))

    @builtins.property
    @jsii.member(jsii_name="alignmentPeriod")
    def alignment_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alignmentPeriod"))

    @alignment_period.setter
    def alignment_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b68e7c816c43c6009be8f5d7a0fd84300e81b1915cc813fa2d495c5f39a994e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alignmentPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="crossSeriesReducer")
    def cross_series_reducer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "crossSeriesReducer"))

    @cross_series_reducer.setter
    def cross_series_reducer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f961136c3f3a3a508abe4aac043c5bd19c7709e9237eb60eb97acfbd53173ce8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crossSeriesReducer", value)

    @builtins.property
    @jsii.member(jsii_name="groupByFields")
    def group_by_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "groupByFields"))

    @group_by_fields.setter
    def group_by_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f2747267d6a37a251fbc7a1327a0b1fdd7f6caa1a140a2ac229f234ec1da1ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupByFields", value)

    @builtins.property
    @jsii.member(jsii_name="perSeriesAligner")
    def per_series_aligner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "perSeriesAligner"))

    @per_series_aligner.setter
    def per_series_aligner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24ac47c12ccac01d9d35b47b8ead14eac86e364a65b6883bf888c52c69f69057)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "perSeriesAligner", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f628c0b37518cc369779ec5d29a2d9bfc2b7908d8c8aa574f53e2cdfdc39d75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleMonitoringAlertPolicyConditionsConditionThresholdOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionThresholdOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__683e03f3a837b830b1cd4c8c67f0cf92042e7c6263894e451d7fe76f3d4f58b2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAggregations")
    def put_aggregations(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4827ddc3ff99bd22ad356480743761cd6305ea2bda7dc033805220029d39ee1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAggregations", [value]))

    @jsii.member(jsii_name="putDenominatorAggregations")
    def put_denominator_aggregations(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17d694f545f2440a004426a4b0040b70bee043204296621bc3048c3c18ab180f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDenominatorAggregations", [value]))

    @jsii.member(jsii_name="putTrigger")
    def put_trigger(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        percent: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param count: The absolute number of time series that must fail the predicate for the condition to be triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#count GoogleMonitoringAlertPolicy#count}
        :param percent: The percentage of time series that must fail the predicate for the condition to be triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#percent GoogleMonitoringAlertPolicy#percent}
        '''
        value = GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger(
            count=count, percent=percent
        )

        return typing.cast(None, jsii.invoke(self, "putTrigger", [value]))

    @jsii.member(jsii_name="resetAggregations")
    def reset_aggregations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAggregations", []))

    @jsii.member(jsii_name="resetDenominatorAggregations")
    def reset_denominator_aggregations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDenominatorAggregations", []))

    @jsii.member(jsii_name="resetDenominatorFilter")
    def reset_denominator_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDenominatorFilter", []))

    @jsii.member(jsii_name="resetEvaluationMissingData")
    def reset_evaluation_missing_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluationMissingData", []))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

    @jsii.member(jsii_name="resetThresholdValue")
    def reset_threshold_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThresholdValue", []))

    @jsii.member(jsii_name="resetTrigger")
    def reset_trigger(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrigger", []))

    @builtins.property
    @jsii.member(jsii_name="aggregations")
    def aggregations(
        self,
    ) -> GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsList:
        return typing.cast(GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsList, jsii.get(self, "aggregations"))

    @builtins.property
    @jsii.member(jsii_name="denominatorAggregations")
    def denominator_aggregations(
        self,
    ) -> GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsList:
        return typing.cast(GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsList, jsii.get(self, "denominatorAggregations"))

    @builtins.property
    @jsii.member(jsii_name="trigger")
    def trigger(
        self,
    ) -> "GoogleMonitoringAlertPolicyConditionsConditionThresholdTriggerOutputReference":
        return typing.cast("GoogleMonitoringAlertPolicyConditionsConditionThresholdTriggerOutputReference", jsii.get(self, "trigger"))

    @builtins.property
    @jsii.member(jsii_name="aggregationsInput")
    def aggregations_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations]]], jsii.get(self, "aggregationsInput"))

    @builtins.property
    @jsii.member(jsii_name="comparisonInput")
    def comparison_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "comparisonInput"))

    @builtins.property
    @jsii.member(jsii_name="denominatorAggregationsInput")
    def denominator_aggregations_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations]]], jsii.get(self, "denominatorAggregationsInput"))

    @builtins.property
    @jsii.member(jsii_name="denominatorFilterInput")
    def denominator_filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "denominatorFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "durationInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluationMissingDataInput")
    def evaluation_missing_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "evaluationMissingDataInput"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdValueInput")
    def threshold_value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdValueInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerInput")
    def trigger_input(
        self,
    ) -> typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger"]:
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger"], jsii.get(self, "triggerInput"))

    @builtins.property
    @jsii.member(jsii_name="comparison")
    def comparison(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comparison"))

    @comparison.setter
    def comparison(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fe91d6496f7c87ad100edcd21ea88f19e953739e950b7207c3d3cfba0376fd5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comparison", value)

    @builtins.property
    @jsii.member(jsii_name="denominatorFilter")
    def denominator_filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "denominatorFilter"))

    @denominator_filter.setter
    def denominator_filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__773a5ec6024609ab9a6c543782972706edc16ac4b1a7f91ffc987fb4decca359)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "denominatorFilter", value)

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c694bdb2fef5a85d49057c0726fee63cef481d20023b080dddb83478f0ae55ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duration", value)

    @builtins.property
    @jsii.member(jsii_name="evaluationMissingData")
    def evaluation_missing_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "evaluationMissingData"))

    @evaluation_missing_data.setter
    def evaluation_missing_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdb8820565b48d156aa29486791035261adb54447287ef83964aeb4b2ea5f57e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationMissingData", value)

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filter"))

    @filter.setter
    def filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7eacd250ea5272cc1ef064246caba11ec75cc88cf8f42809d949bfed1eabc195)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filter", value)

    @builtins.property
    @jsii.member(jsii_name="thresholdValue")
    def threshold_value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "thresholdValue"))

    @threshold_value.setter
    def threshold_value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f69b53fba9d51e71fb53fab1ca6acff94989e4273078fe965c2198b373f5a0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thresholdValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionThreshold]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionThreshold], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionThreshold],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecca3e8d0a5989620e7f291f7e435dd66e0e36a03bbff505be4a94c105b550e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "percent": "percent"},
)
class GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger:
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        percent: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param count: The absolute number of time series that must fail the predicate for the condition to be triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#count GoogleMonitoringAlertPolicy#count}
        :param percent: The percentage of time series that must fail the predicate for the condition to be triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#percent GoogleMonitoringAlertPolicy#percent}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de369282353c0f13b41187b8c1ef3e9a4654810458d9925deaf4baa0f0116fa1)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument percent", value=percent, expected_type=type_hints["percent"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if percent is not None:
            self._values["percent"] = percent

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''The absolute number of time series that must fail the predicate for the condition to be triggered.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#count GoogleMonitoringAlertPolicy#count}
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def percent(self) -> typing.Optional[jsii.Number]:
        '''The percentage of time series that must fail the predicate for the condition to be triggered.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#percent GoogleMonitoringAlertPolicy#percent}
        '''
        result = self._values.get("percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringAlertPolicyConditionsConditionThresholdTriggerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionThresholdTriggerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d413cb0e5668d2bd555e8bff93d972cb6685ca731d25fc112a1a637412766805)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCount")
    def reset_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCount", []))

    @jsii.member(jsii_name="resetPercent")
    def reset_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPercent", []))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="percentInput")
    def percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "percentInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6db0e7e7019a2ba5b14004bac4599fbc2a072b98b73c117a09d483cd1caf590)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="percent")
    def percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "percent"))

    @percent.setter
    def percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e660ce0cc9e74b34f5d8d892e3b2d29bfe77bfaad91bbe92a911bccfbc73500)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "percent", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb5de7b717aac2d0025687416339b7e69f20ec75f810ebaea1052857301e90bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleMonitoringAlertPolicyConditionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f622051e2803eb7abc3cc339073103067e8854cfa1beacd015c37b9c44e354b8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleMonitoringAlertPolicyConditionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60ddaa17bce80301df3be097f44b07be7570f9af02723daa6118a1c38ac29c99)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleMonitoringAlertPolicyConditionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee6818423edb25136df32c4ff1626dc0626d84bb65ba2421c4a6c3061bc6d613)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29d74f6131c5bb0f704ca0525b22bb726a20d526b403a36201eef07915743266)
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
            type_hints = typing.get_type_hints(_typecheckingstub__501015c45852f7743c8121fae29d4f4d7864b5ef5085611f787296a55038d8fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e456639158164dd4448c19b4dc558d1a625ce2463f0e6d6b856d2a731965a9de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleMonitoringAlertPolicyConditionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
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
            type_hints = typing.get_type_hints(_typecheckingstub__413ae3337a6a04e541582e5abb45daa641fb01895fe888c7a74d481a301cde2e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putConditionAbsent")
    def put_condition_absent(
        self,
        *,
        duration: builtins.str,
        aggregations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations, typing.Dict[builtins.str, typing.Any]]]]] = None,
        filter: typing.Optional[builtins.str] = None,
        trigger: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param duration: The amount of time that a time series must fail to report new data to be considered failing. Currently, only values that are a multiple of a minute--e.g. 60s, 120s, or 300s --are supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#duration GoogleMonitoringAlertPolicy#duration}
        :param aggregations: aggregations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#aggregations GoogleMonitoringAlertPolicy#aggregations}
        :param filter: A filter that identifies which time series should be compared with the threshold.The filter is similar to the one that is specified in the MetricService.ListTimeSeries request (that call is useful to verify the time series that will be retrieved / processed) and must specify the metric type and optionally may contain restrictions on resource type, resource labels, and metric labels. This field may not exceed 2048 Unicode characters in length. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#filter GoogleMonitoringAlertPolicy#filter}
        :param trigger: trigger block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#trigger GoogleMonitoringAlertPolicy#trigger}
        '''
        value = GoogleMonitoringAlertPolicyConditionsConditionAbsent(
            duration=duration,
            aggregations=aggregations,
            filter=filter,
            trigger=trigger,
        )

        return typing.cast(None, jsii.invoke(self, "putConditionAbsent", [value]))

    @jsii.member(jsii_name="putConditionMatchedLog")
    def put_condition_matched_log(
        self,
        *,
        filter: builtins.str,
        label_extractors: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param filter: A logs-based filter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#filter GoogleMonitoringAlertPolicy#filter}
        :param label_extractors: A map from a label key to an extractor expression, which is used to extract the value for this label key. Each entry in this map is a specification for how data should be extracted from log entries that match filter. Each combination of extracted values is treated as a separate rule for the purposes of triggering notifications. Label keys and corresponding values can be used in notifications generated by this condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#label_extractors GoogleMonitoringAlertPolicy#label_extractors}
        '''
        value = GoogleMonitoringAlertPolicyConditionsConditionMatchedLog(
            filter=filter, label_extractors=label_extractors
        )

        return typing.cast(None, jsii.invoke(self, "putConditionMatchedLog", [value]))

    @jsii.member(jsii_name="putConditionMonitoringQueryLanguage")
    def put_condition_monitoring_query_language(
        self,
        *,
        duration: builtins.str,
        query: builtins.str,
        evaluation_missing_data: typing.Optional[builtins.str] = None,
        trigger: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param duration: The amount of time that a time series must violate the threshold to be considered failing. Currently, only values that are a multiple of a minute--e.g., 0, 60, 120, or 300 seconds--are supported. If an invalid value is given, an error will be returned. When choosing a duration, it is useful to keep in mind the frequency of the underlying time series data (which may also be affected by any alignments specified in the aggregations field); a good duration is long enough so that a single outlier does not generate spurious alerts, but short enough that unhealthy states are detected and alerted on quickly. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#duration GoogleMonitoringAlertPolicy#duration}
        :param query: Monitoring Query Language query that outputs a boolean stream. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#query GoogleMonitoringAlertPolicy#query}
        :param evaluation_missing_data: A condition control that determines how metric-threshold conditions are evaluated when data stops arriving. Possible values: ["EVALUATION_MISSING_DATA_INACTIVE", "EVALUATION_MISSING_DATA_ACTIVE", "EVALUATION_MISSING_DATA_NO_OP"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#evaluation_missing_data GoogleMonitoringAlertPolicy#evaluation_missing_data}
        :param trigger: trigger block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#trigger GoogleMonitoringAlertPolicy#trigger}
        '''
        value = GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage(
            duration=duration,
            query=query,
            evaluation_missing_data=evaluation_missing_data,
            trigger=trigger,
        )

        return typing.cast(None, jsii.invoke(self, "putConditionMonitoringQueryLanguage", [value]))

    @jsii.member(jsii_name="putConditionThreshold")
    def put_condition_threshold(
        self,
        *,
        comparison: builtins.str,
        duration: builtins.str,
        aggregations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations, typing.Dict[builtins.str, typing.Any]]]]] = None,
        denominator_aggregations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations, typing.Dict[builtins.str, typing.Any]]]]] = None,
        denominator_filter: typing.Optional[builtins.str] = None,
        evaluation_missing_data: typing.Optional[builtins.str] = None,
        filter: typing.Optional[builtins.str] = None,
        threshold_value: typing.Optional[jsii.Number] = None,
        trigger: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param comparison: The comparison to apply between the time series (indicated by filter and aggregation) and the threshold (indicated by threshold_value). The comparison is applied on each time series, with the time series on the left-hand side and the threshold on the right-hand side. Only COMPARISON_LT and COMPARISON_GT are supported currently. Possible values: ["COMPARISON_GT", "COMPARISON_GE", "COMPARISON_LT", "COMPARISON_LE", "COMPARISON_EQ", "COMPARISON_NE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#comparison GoogleMonitoringAlertPolicy#comparison}
        :param duration: The amount of time that a time series must violate the threshold to be considered failing. Currently, only values that are a multiple of a minute--e.g., 0, 60, 120, or 300 seconds--are supported. If an invalid value is given, an error will be returned. When choosing a duration, it is useful to keep in mind the frequency of the underlying time series data (which may also be affected by any alignments specified in the aggregations field); a good duration is long enough so that a single outlier does not generate spurious alerts, but short enough that unhealthy states are detected and alerted on quickly. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#duration GoogleMonitoringAlertPolicy#duration}
        :param aggregations: aggregations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#aggregations GoogleMonitoringAlertPolicy#aggregations}
        :param denominator_aggregations: denominator_aggregations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#denominator_aggregations GoogleMonitoringAlertPolicy#denominator_aggregations}
        :param denominator_filter: A filter that identifies a time series that should be used as the denominator of a ratio that will be compared with the threshold. If a denominator_filter is specified, the time series specified by the filter field will be used as the numerator.The filter is similar to the one that is specified in the MetricService.ListTimeSeries request (that call is useful to verify the time series that will be retrieved / processed) and must specify the metric type and optionally may contain restrictions on resource type, resource labels, and metric labels. This field may not exceed 2048 Unicode characters in length. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#denominator_filter GoogleMonitoringAlertPolicy#denominator_filter}
        :param evaluation_missing_data: A condition control that determines how metric-threshold conditions are evaluated when data stops arriving. Possible values: ["EVALUATION_MISSING_DATA_INACTIVE", "EVALUATION_MISSING_DATA_ACTIVE", "EVALUATION_MISSING_DATA_NO_OP"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#evaluation_missing_data GoogleMonitoringAlertPolicy#evaluation_missing_data}
        :param filter: A filter that identifies which time series should be compared with the threshold.The filter is similar to the one that is specified in the MetricService.ListTimeSeries request (that call is useful to verify the time series that will be retrieved / processed) and must specify the metric type and optionally may contain restrictions on resource type, resource labels, and metric labels. This field may not exceed 2048 Unicode characters in length. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#filter GoogleMonitoringAlertPolicy#filter}
        :param threshold_value: A value against which to compare the time series. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#threshold_value GoogleMonitoringAlertPolicy#threshold_value}
        :param trigger: trigger block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#trigger GoogleMonitoringAlertPolicy#trigger}
        '''
        value = GoogleMonitoringAlertPolicyConditionsConditionThreshold(
            comparison=comparison,
            duration=duration,
            aggregations=aggregations,
            denominator_aggregations=denominator_aggregations,
            denominator_filter=denominator_filter,
            evaluation_missing_data=evaluation_missing_data,
            filter=filter,
            threshold_value=threshold_value,
            trigger=trigger,
        )

        return typing.cast(None, jsii.invoke(self, "putConditionThreshold", [value]))

    @jsii.member(jsii_name="resetConditionAbsent")
    def reset_condition_absent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConditionAbsent", []))

    @jsii.member(jsii_name="resetConditionMatchedLog")
    def reset_condition_matched_log(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConditionMatchedLog", []))

    @jsii.member(jsii_name="resetConditionMonitoringQueryLanguage")
    def reset_condition_monitoring_query_language(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConditionMonitoringQueryLanguage", []))

    @jsii.member(jsii_name="resetConditionThreshold")
    def reset_condition_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConditionThreshold", []))

    @builtins.property
    @jsii.member(jsii_name="conditionAbsent")
    def condition_absent(
        self,
    ) -> GoogleMonitoringAlertPolicyConditionsConditionAbsentOutputReference:
        return typing.cast(GoogleMonitoringAlertPolicyConditionsConditionAbsentOutputReference, jsii.get(self, "conditionAbsent"))

    @builtins.property
    @jsii.member(jsii_name="conditionMatchedLog")
    def condition_matched_log(
        self,
    ) -> GoogleMonitoringAlertPolicyConditionsConditionMatchedLogOutputReference:
        return typing.cast(GoogleMonitoringAlertPolicyConditionsConditionMatchedLogOutputReference, jsii.get(self, "conditionMatchedLog"))

    @builtins.property
    @jsii.member(jsii_name="conditionMonitoringQueryLanguage")
    def condition_monitoring_query_language(
        self,
    ) -> GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageOutputReference:
        return typing.cast(GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageOutputReference, jsii.get(self, "conditionMonitoringQueryLanguage"))

    @builtins.property
    @jsii.member(jsii_name="conditionThreshold")
    def condition_threshold(
        self,
    ) -> GoogleMonitoringAlertPolicyConditionsConditionThresholdOutputReference:
        return typing.cast(GoogleMonitoringAlertPolicyConditionsConditionThresholdOutputReference, jsii.get(self, "conditionThreshold"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="conditionAbsentInput")
    def condition_absent_input(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionAbsent]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionAbsent], jsii.get(self, "conditionAbsentInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionMatchedLogInput")
    def condition_matched_log_input(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionMatchedLog]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionMatchedLog], jsii.get(self, "conditionMatchedLogInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionMonitoringQueryLanguageInput")
    def condition_monitoring_query_language_input(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage], jsii.get(self, "conditionMonitoringQueryLanguageInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionThresholdInput")
    def condition_threshold_input(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionThreshold]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionThreshold], jsii.get(self, "conditionThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23907189001f87754e1915188f4133c34b9e55d6a2b445f22a95df41dd93b00d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d79a0c2fe0cb4a4e04fe0f1fd161cbbe88bf35550ba75ef314808fade7872c48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "combiner": "combiner",
        "conditions": "conditions",
        "display_name": "displayName",
        "alert_strategy": "alertStrategy",
        "documentation": "documentation",
        "enabled": "enabled",
        "id": "id",
        "notification_channels": "notificationChannels",
        "project": "project",
        "timeouts": "timeouts",
        "user_labels": "userLabels",
    },
)
class GoogleMonitoringAlertPolicyConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        combiner: builtins.str,
        conditions: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleMonitoringAlertPolicyConditions, typing.Dict[builtins.str, typing.Any]]]],
        display_name: builtins.str,
        alert_strategy: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyAlertStrategy, typing.Dict[builtins.str, typing.Any]]] = None,
        documentation: typing.Optional[typing.Union["GoogleMonitoringAlertPolicyDocumentation", typing.Dict[builtins.str, typing.Any]]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        notification_channels: typing.Optional[typing.Sequence[builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleMonitoringAlertPolicyTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        user_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param combiner: How to combine the results of multiple conditions to determine if an incident should be opened. Possible values: ["AND", "OR", "AND_WITH_MATCHING_RESOURCE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#combiner GoogleMonitoringAlertPolicy#combiner}
        :param conditions: conditions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#conditions GoogleMonitoringAlertPolicy#conditions}
        :param display_name: A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion, don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#display_name GoogleMonitoringAlertPolicy#display_name}
        :param alert_strategy: alert_strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#alert_strategy GoogleMonitoringAlertPolicy#alert_strategy}
        :param documentation: documentation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#documentation GoogleMonitoringAlertPolicy#documentation}
        :param enabled: Whether or not the policy is enabled. The default is true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#enabled GoogleMonitoringAlertPolicy#enabled}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#id GoogleMonitoringAlertPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param notification_channels: Identifies the notification channels to which notifications should be sent when incidents are opened or closed or when new violations occur on an already opened incident. Each element of this array corresponds to the name field in each of the NotificationChannel objects that are returned from the notificationChannels.list method. The syntax of the entries in this field is 'projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#notification_channels GoogleMonitoringAlertPolicy#notification_channels}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#project GoogleMonitoringAlertPolicy#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#timeouts GoogleMonitoringAlertPolicy#timeouts}
        :param user_labels: This field is intended to be used for organizing and identifying the AlertPolicy objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#user_labels GoogleMonitoringAlertPolicy#user_labels}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(alert_strategy, dict):
            alert_strategy = GoogleMonitoringAlertPolicyAlertStrategy(**alert_strategy)
        if isinstance(documentation, dict):
            documentation = GoogleMonitoringAlertPolicyDocumentation(**documentation)
        if isinstance(timeouts, dict):
            timeouts = GoogleMonitoringAlertPolicyTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b80d32bcf548ced82bb8f856a9ca19d175614711866bcd6e3df96a81d055847)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument combiner", value=combiner, expected_type=type_hints["combiner"])
            check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument alert_strategy", value=alert_strategy, expected_type=type_hints["alert_strategy"])
            check_type(argname="argument documentation", value=documentation, expected_type=type_hints["documentation"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument notification_channels", value=notification_channels, expected_type=type_hints["notification_channels"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument user_labels", value=user_labels, expected_type=type_hints["user_labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "combiner": combiner,
            "conditions": conditions,
            "display_name": display_name,
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
        if alert_strategy is not None:
            self._values["alert_strategy"] = alert_strategy
        if documentation is not None:
            self._values["documentation"] = documentation
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id
        if notification_channels is not None:
            self._values["notification_channels"] = notification_channels
        if project is not None:
            self._values["project"] = project
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if user_labels is not None:
            self._values["user_labels"] = user_labels

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
    def combiner(self) -> builtins.str:
        '''How to combine the results of multiple conditions to determine if an incident should be opened.

        Possible values: ["AND", "OR", "AND_WITH_MATCHING_RESOURCE"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#combiner GoogleMonitoringAlertPolicy#combiner}
        '''
        result = self._values.get("combiner")
        assert result is not None, "Required property 'combiner' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def conditions(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditions]]:
        '''conditions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#conditions GoogleMonitoringAlertPolicy#conditions}
        '''
        result = self._values.get("conditions")
        assert result is not None, "Required property 'conditions' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditions]], result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''A short name or phrase used to identify the policy in dashboards, notifications, and incidents.

        To avoid confusion, don't use
        the same display name for multiple policies in the same project. The
        name is limited to 512 Unicode characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#display_name GoogleMonitoringAlertPolicy#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alert_strategy(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyAlertStrategy]:
        '''alert_strategy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#alert_strategy GoogleMonitoringAlertPolicy#alert_strategy}
        '''
        result = self._values.get("alert_strategy")
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyAlertStrategy], result)

    @builtins.property
    def documentation(
        self,
    ) -> typing.Optional["GoogleMonitoringAlertPolicyDocumentation"]:
        '''documentation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#documentation GoogleMonitoringAlertPolicy#documentation}
        '''
        result = self._values.get("documentation")
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyDocumentation"], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether or not the policy is enabled. The default is true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#enabled GoogleMonitoringAlertPolicy#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#id GoogleMonitoringAlertPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_channels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Identifies the notification channels to which notifications should be sent when incidents are opened or closed or when new violations occur on an already opened incident.

        Each element of this array corresponds
        to the name field in each of the NotificationChannel objects that are
        returned from the notificationChannels.list method. The syntax of the
        entries in this field is
        'projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]'

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#notification_channels GoogleMonitoringAlertPolicy#notification_channels}
        '''
        result = self._values.get("notification_channels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#project GoogleMonitoringAlertPolicy#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleMonitoringAlertPolicyTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#timeouts GoogleMonitoringAlertPolicy#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyTimeouts"], result)

    @builtins.property
    def user_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''This field is intended to be used for organizing and identifying the AlertPolicy objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#user_labels GoogleMonitoringAlertPolicy#user_labels}
        '''
        result = self._values.get("user_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyCreationRecord",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleMonitoringAlertPolicyCreationRecord:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyCreationRecord(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringAlertPolicyCreationRecordList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyCreationRecordList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e8ad35708efc6ee70dbb18b14608837dec80d6d6a4937241f4955c9ab759ceb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleMonitoringAlertPolicyCreationRecordOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bd8b9d6066369f8150aaaf43f136f8597a682788e89cd04ce435717857ed591)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleMonitoringAlertPolicyCreationRecordOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9457b1ec035e5800e62f97e9551bde5361ecca7c7336fc6fc74e16e88a6c2bb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce1ef91e0f050a2ab852a7ae809dcf6b554622a47fc0cef10ba262a417e1dee3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8239664f3dab5da1ed734fd583cc5fdeb5a18fdeec3b0aada93d6a347df06e87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GoogleMonitoringAlertPolicyCreationRecordOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyCreationRecordOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
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
            type_hints = typing.get_type_hints(_typecheckingstub__e3c1fa378b82f2b07bb9e280fb272bf73679ab5c72d807878d5b36baf7f58702)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="mutatedBy")
    def mutated_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mutatedBy"))

    @builtins.property
    @jsii.member(jsii_name="mutateTime")
    def mutate_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mutateTime"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyCreationRecord]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyCreationRecord], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringAlertPolicyCreationRecord],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__615515ae3acf4bfecc4a1bdba33664cb1da1f1a59b9ca4aa9eeb4db73121b054)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyDocumentation",
    jsii_struct_bases=[],
    name_mapping={"content": "content", "mime_type": "mimeType"},
)
class GoogleMonitoringAlertPolicyDocumentation:
    def __init__(
        self,
        *,
        content: typing.Optional[builtins.str] = None,
        mime_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param content: The text of the documentation, interpreted according to mimeType. The content may not exceed 8,192 Unicode characters and may not exceed more than 10,240 bytes when encoded in UTF-8 format, whichever is smaller. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#content GoogleMonitoringAlertPolicy#content}
        :param mime_type: The format of the content field. Presently, only the value "text/markdown" is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#mime_type GoogleMonitoringAlertPolicy#mime_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12ab4b5b9b27568573292c40f02813b4fc6cb2df64779a9fe602a2ae32e5079b)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument mime_type", value=mime_type, expected_type=type_hints["mime_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if content is not None:
            self._values["content"] = content
        if mime_type is not None:
            self._values["mime_type"] = mime_type

    @builtins.property
    def content(self) -> typing.Optional[builtins.str]:
        '''The text of the documentation, interpreted according to mimeType.

        The content may not exceed 8,192 Unicode characters and may not
        exceed more than 10,240 bytes when encoded in UTF-8 format,
        whichever is smaller.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#content GoogleMonitoringAlertPolicy#content}
        '''
        result = self._values.get("content")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mime_type(self) -> typing.Optional[builtins.str]:
        '''The format of the content field. Presently, only the value "text/markdown" is supported.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#mime_type GoogleMonitoringAlertPolicy#mime_type}
        '''
        result = self._values.get("mime_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyDocumentation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringAlertPolicyDocumentationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyDocumentationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9e77ed805bb6e86dff61110097b8c1d39ac3d7cf9f9af3659618860b47d260de)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetContent")
    def reset_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContent", []))

    @jsii.member(jsii_name="resetMimeType")
    def reset_mime_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMimeType", []))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="mimeTypeInput")
    def mime_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mimeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6c79894b36d36365ddaec8c96a0c7838d5bc7ba4e51e5420dc4bc2d7e7f9433)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="mimeType")
    def mime_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mimeType"))

    @mime_type.setter
    def mime_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fd11c759f3e73cc57cb72d50a8fa696d03e7deb841c3a1c1d124c583eca27e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mimeType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyDocumentation]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyDocumentation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringAlertPolicyDocumentation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__454c2f7c80918c1dfe658ec91640a8e53739b1caf8b6ab80bd9670262bbbd66a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleMonitoringAlertPolicyTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#create GoogleMonitoringAlertPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#delete GoogleMonitoringAlertPolicy#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#update GoogleMonitoringAlertPolicy#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ea7bf7b597c41adb468dabbd8702337dd6be7365661826f0669d385ee97052b)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#create GoogleMonitoringAlertPolicy#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#delete GoogleMonitoringAlertPolicy#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#update GoogleMonitoringAlertPolicy#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringAlertPolicyTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8a37ab45b6b57338c764e99f57eb1669f1808942cd60548ed87a0fa56c31f2ca)
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
            type_hints = typing.get_type_hints(_typecheckingstub__db71dac654d3e0b7ea12d89188e13f66fa806f00f71c4a4eb88028ce004b000c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__162e6672d2c6c0bc168ce56302ffc63749426972667348ee0a823f99e8d87722)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe9165e9f59355928efc4473ad54c9913551cc3ef1080a3f8646ce5837d51f25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleMonitoringAlertPolicyTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleMonitoringAlertPolicyTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78d6cb6c1fa0286847b9a7ea10ee6639d481368d4eeddcf5a31e14676386883c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleMonitoringAlertPolicy",
    "GoogleMonitoringAlertPolicyAlertStrategy",
    "GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit",
    "GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimitOutputReference",
    "GoogleMonitoringAlertPolicyAlertStrategyOutputReference",
    "GoogleMonitoringAlertPolicyConditions",
    "GoogleMonitoringAlertPolicyConditionsConditionAbsent",
    "GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations",
    "GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsList",
    "GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsOutputReference",
    "GoogleMonitoringAlertPolicyConditionsConditionAbsentOutputReference",
    "GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger",
    "GoogleMonitoringAlertPolicyConditionsConditionAbsentTriggerOutputReference",
    "GoogleMonitoringAlertPolicyConditionsConditionMatchedLog",
    "GoogleMonitoringAlertPolicyConditionsConditionMatchedLogOutputReference",
    "GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage",
    "GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageOutputReference",
    "GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger",
    "GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTriggerOutputReference",
    "GoogleMonitoringAlertPolicyConditionsConditionThreshold",
    "GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations",
    "GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsList",
    "GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsOutputReference",
    "GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations",
    "GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsList",
    "GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsOutputReference",
    "GoogleMonitoringAlertPolicyConditionsConditionThresholdOutputReference",
    "GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger",
    "GoogleMonitoringAlertPolicyConditionsConditionThresholdTriggerOutputReference",
    "GoogleMonitoringAlertPolicyConditionsList",
    "GoogleMonitoringAlertPolicyConditionsOutputReference",
    "GoogleMonitoringAlertPolicyConfig",
    "GoogleMonitoringAlertPolicyCreationRecord",
    "GoogleMonitoringAlertPolicyCreationRecordList",
    "GoogleMonitoringAlertPolicyCreationRecordOutputReference",
    "GoogleMonitoringAlertPolicyDocumentation",
    "GoogleMonitoringAlertPolicyDocumentationOutputReference",
    "GoogleMonitoringAlertPolicyTimeouts",
    "GoogleMonitoringAlertPolicyTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__b676cf9f0868f950faefca183808c2c490d719f773f06f4379b4bc94e4dc9a4f(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    combiner: builtins.str,
    conditions: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleMonitoringAlertPolicyConditions, typing.Dict[builtins.str, typing.Any]]]],
    display_name: builtins.str,
    alert_strategy: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyAlertStrategy, typing.Dict[builtins.str, typing.Any]]] = None,
    documentation: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyDocumentation, typing.Dict[builtins.str, typing.Any]]] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    notification_channels: typing.Optional[typing.Sequence[builtins.str]] = None,
    project: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    user_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
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

def _typecheckingstub__53c5c45a756c606a50f7f623665b61b2ea7c5b3fba9cdc60931e8312d28e9249(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleMonitoringAlertPolicyConditions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb6f4c70b542db299f40546bbe220e2e6eca4cf76d641115b2d8d450a82176f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab8cc3066286fa54a192893f7d07396b1d83137e0197e89839ee49671260d0ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb6b0de4773ad5ed371b5772bea252ce538da75045a7bc86f653b70871961121(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20472b861bccf45b1ad809718ab460bc15f4365e35d2a24a3f98c66a23852aaf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__475a6e0a08db36a6ad2bde12d39cba0ef9df5f0cf75c63a184431653fe3165e8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b5079d2e9426f13c62193284296b5fdd73c80fb925b06d50347944521fbb575(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ff3d320068f669b56b665133ba509bc6175753a3f91ef36f34b67bdd880008d(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba1267174d35830e16072259481dcc3e25581cbec7aa32aa539800dda910aaf4(
    *,
    auto_close: typing.Optional[builtins.str] = None,
    notification_rate_limit: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3de5bfc4b8c8d5040b7de66acc39deef1a82992c4d3407a48c9af617e5f8906(
    *,
    period: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37eb453aaa420a2f3a34aa1cb7eab7db7ce81c4f9f039bc80999b8748f309eca(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f4fcc94505105c197f876baa56a41771fdf4eb7f3d2221a87805fdf0d05c33c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9a5bb757226631bfd28873596b22f7e5924779bd2dc5809c6bc3c407a2cb93d(
    value: typing.Optional[GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bece5930de9edfe294cc2cba2110ef5d2f4c4c03cd47421dbab957bf5bc9d24f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1efaea8c321a04d2a59d21f96ae4696e032f86d61e42966d81d3b04dc68e2da(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84094baed363937b712d405dbe530d763f2e9b8007fbec388cb0a14bc021ce91(
    value: typing.Optional[GoogleMonitoringAlertPolicyAlertStrategy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__076db12d738ff26279094e1061a63e449bb78bf37b8b6cebaaf168c8b3240151(
    *,
    display_name: builtins.str,
    condition_absent: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionAbsent, typing.Dict[builtins.str, typing.Any]]] = None,
    condition_matched_log: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionMatchedLog, typing.Dict[builtins.str, typing.Any]]] = None,
    condition_monitoring_query_language: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage, typing.Dict[builtins.str, typing.Any]]] = None,
    condition_threshold: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThreshold, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eefc984df64db235c93cad22009c95ffe03bb80fd9888d5d094d2ca9106b4fc3(
    *,
    duration: builtins.str,
    aggregations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations, typing.Dict[builtins.str, typing.Any]]]]] = None,
    filter: typing.Optional[builtins.str] = None,
    trigger: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17abfed6b0545f100ab427535e0340764496dc25fa8a9fd19f34bdec6734e365(
    *,
    alignment_period: typing.Optional[builtins.str] = None,
    cross_series_reducer: typing.Optional[builtins.str] = None,
    group_by_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
    per_series_aligner: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52749dea74f436346fdc3d9fb4b0a823925944cc51a769f133ba623ccdb2deda(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cf5029ea727df7f2980cdbd53862326bd7698c16476801e8049f6eb779acc5b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68fdbb367695e7157e33a54bde10578e4dab7eb0b914e973da1daeb0e36518d7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27c96405b2ef3043e4b690bc55c3d32890c6823f05afe421a92904c430d1fddf(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b4f4ee147bdd093aa10bcdc7393b688f398f2cbaa724a4723fc5646f91eda59(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad5fb1ae758c29776420c35cc0c60819e32cae15edb63f5f7dc55d6c7fec2cd3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35083242833c074bcc48e37864c5ee6ba18170690d7c116c94b1544c1c0d1110(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43127057911cbb4cf1e530b3c31ae69ebff8e296ff72f730795d82f90e760d19(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9801168d6c93601f9eb511793c9fa2716bb22db697cc2840d6d28f6bc6af66c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a3ae24820c7fa5a88c457c31e2ff0bd001951e30760f883deabb07ed4834ed3(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7db7ebe7acfa9cfcc16a14eac608efb480e1584b5b3b05d06f663a90ef62d586(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6eb8dcb5e1a5d01263b4a1c8658a5bd39a532c8cfbfe9b8384d5f9b021483dcc(
    value: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__467f570c82b477fa30522889ad39e976a27e10a1739f6f88df8fa71d905d1cb4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9e11bda0f0f7f6df4301d2d7982ccf8748c17ba66c99281ade9fd61b42fda28(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d122e06cd4fa9bbd64e3a6588a7748e2e4b514ffb41b8e6cada356eb9fbc54d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4920e10bd4392bc6bf37e5bf13d42806d0ddd02ffb2b2517c68cd5a61debd30c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09c3a25a3a7a48a79d31d54c1388383035662c4b4caa6067d2b554cf6069b3ae(
    value: typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionAbsent],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b447657c17e565fd0c8e9ed41fdc35d6813c3d30498008c3c2b2ca9bf0bcaa5(
    *,
    count: typing.Optional[jsii.Number] = None,
    percent: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ded9e11baab52465dab9002f85df358e2535b3ced00846266e864285fc79723(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19de0fa1bf17744962636cba665991ab5fe64a9b54a1b7227394ed5f780e0bb0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4308190ba76528a6b38976635be7b6c567e04e26597278adf92fa14fe501ef4c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bf12369c3e9da25a58fdfa7e99e5d81549f6a1f26ff619073c011952358a540(
    value: typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fda0cc62f8180a7fecaadad36329e36cbea5706c370bb415425bda8a2092716c(
    *,
    filter: builtins.str,
    label_extractors: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a260750df6dcd9ce57cc17f5960b21cecb521639985856598af3364f448a343(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf3c4e4c29dbec74b59306d9e6b5761d784d6baef8ffc81063e97dcbc61068a3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2564fd3feb08ac503ed11e9dc54910f0da6e43a4b314d0f084db38fbc4e0302e(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29c857ce3fdda3c9609ae1247fa1edc28d74029a51da884dd45c7738d90ba7c4(
    value: typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionMatchedLog],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b68d50107253bb8e6cb13cfafabce9d3456d3946124ea1cb9a9004b0d8c5f38(
    *,
    duration: builtins.str,
    query: builtins.str,
    evaluation_missing_data: typing.Optional[builtins.str] = None,
    trigger: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__645d2b8b463d46ec6fb10db36f1f1df61306db07be313a2ceb61cca68332435c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b455f65455c6990143af9864e7d3dadebbfaf202643f3aa65cbf71a289ee92ff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2599dfca99f3a1103c3d77a9f416a0215b57a36699bcc6283158890018ef8c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1461b9df06204b462f5988f9546d21639fa9d0437fcc362284b6c10154e8862c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1badc7b3e48c7177fe51fa46ed0080d4036c850e135baf8ecf07c32b99c8d73(
    value: typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79d5c009917e96b01b9242f82433828d19a0c3df5b336eb39b7dd188aade2a5e(
    *,
    count: typing.Optional[jsii.Number] = None,
    percent: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b341dba5019c4151ef30489213242c3b3a774d617b06a112a268f57367d59aec(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f80e59c07506226c4fb92a3eb4ffe305ea2170bf11b3beb1b019808d2be1253(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7acdcda14f63fdff8d8d065e24d4e9e14a7c1c1cc698aadff2e8a7507ba3fd9b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af5bf9e9e5ef2e23e948e46a89660963a12a0f56d87fcdfa5a04e382d9f256f5(
    value: typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29ea0561e17834109603262cd4c17249a064e6bdcc49316b13c97783e1dc9921(
    *,
    comparison: builtins.str,
    duration: builtins.str,
    aggregations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations, typing.Dict[builtins.str, typing.Any]]]]] = None,
    denominator_aggregations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations, typing.Dict[builtins.str, typing.Any]]]]] = None,
    denominator_filter: typing.Optional[builtins.str] = None,
    evaluation_missing_data: typing.Optional[builtins.str] = None,
    filter: typing.Optional[builtins.str] = None,
    threshold_value: typing.Optional[jsii.Number] = None,
    trigger: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ba53b0de8fbdde35caf06f0c12ef8869296dc81f72bcbfb03139b775aef2596(
    *,
    alignment_period: typing.Optional[builtins.str] = None,
    cross_series_reducer: typing.Optional[builtins.str] = None,
    group_by_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
    per_series_aligner: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdfc59c4095596210e1ef50791fcfbff669b89187bd6f2d7f8ccd4cdd6e16dda(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c573e613d88410e13115cd6f5b824d8049d0b28c6a16726184a8a7fa6bb541d1(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c512af89406ee3f99c4725cd5d49e6efaa923a7d39a745f5de6e773ea5546b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec53d237333b959ab5ac2f547b01219975cd135d3b6f346f9601a194ecd53e9a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33878a8474860a94ea24659dcecc58228993d1e796f3d73484b6837e3a5137e2(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85fb1f253e4ee8308786dd82b1c6d7ea5376d1019ea8a2bc05e90bf31b48948e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19e79989278d25fcae0f15b314a44dd1fdb585b285f82bef881e8dd25d1654db(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edd46198e4601f0f880a46dfa8ab6e3de33606564241570f0deae5834ca7c91b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a73cbcf5b3f186da033f56ddf1de80e7cdfa6a5a8fa339cf2679ceff96c7e9a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c45ae60c3a0fad04f04041b5ced248a96466854e4f6fa4ed9634e97e28ac319(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fc0854ff068fe000d3d8274a68cd5892e12faddccf1e044afdce6927e95e405(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__092990a03c27136546bb788a1ced1efe9be9abf705a4988672e850e9b902fd35(
    value: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11a22636bdb75b0dac8627d0214261d8fa7049fbe8aebf1d999e4dcdd35e7c5e(
    *,
    alignment_period: typing.Optional[builtins.str] = None,
    cross_series_reducer: typing.Optional[builtins.str] = None,
    group_by_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
    per_series_aligner: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__644c63baceda630d63bf15e77fad9c38e2538f6a6a4e3efe96ae45b93dd1da1a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75cbbbe83667a429be7ee1e2def7457a4efa11abd665e3015327c45ae65340b7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3162ac10558e825cbe5fec86e638a575d3fd62c839e4e51559d0c7b6a1bb2ae8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__646cce21faa990a8119783e0a2069eae054d641199e3cf2a88caadd37337f216(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbb3f7745c84720f0034293f0d47f47b0a9a7ab86ded6c153bb203aae486395c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d08607cdbbc04b47c50b7cff7760fb4d5762ae8afacbe296ad1919a0385db7d1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90eccc5d61bf52866e74c4552260fd1cd3c531b65c5ea517818505824f545fae(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b68e7c816c43c6009be8f5d7a0fd84300e81b1915cc813fa2d495c5f39a994e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f961136c3f3a3a508abe4aac043c5bd19c7709e9237eb60eb97acfbd53173ce8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f2747267d6a37a251fbc7a1327a0b1fdd7f6caa1a140a2ac229f234ec1da1ff(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24ac47c12ccac01d9d35b47b8ead14eac86e364a65b6883bf888c52c69f69057(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f628c0b37518cc369779ec5d29a2d9bfc2b7908d8c8aa574f53e2cdfdc39d75(
    value: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__683e03f3a837b830b1cd4c8c67f0cf92042e7c6263894e451d7fe76f3d4f58b2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4827ddc3ff99bd22ad356480743761cd6305ea2bda7dc033805220029d39ee1a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17d694f545f2440a004426a4b0040b70bee043204296621bc3048c3c18ab180f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fe91d6496f7c87ad100edcd21ea88f19e953739e950b7207c3d3cfba0376fd5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__773a5ec6024609ab9a6c543782972706edc16ac4b1a7f91ffc987fb4decca359(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c694bdb2fef5a85d49057c0726fee63cef481d20023b080dddb83478f0ae55ca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdb8820565b48d156aa29486791035261adb54447287ef83964aeb4b2ea5f57e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7eacd250ea5272cc1ef064246caba11ec75cc88cf8f42809d949bfed1eabc195(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f69b53fba9d51e71fb53fab1ca6acff94989e4273078fe965c2198b373f5a0a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecca3e8d0a5989620e7f291f7e435dd66e0e36a03bbff505be4a94c105b550e0(
    value: typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionThreshold],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de369282353c0f13b41187b8c1ef3e9a4654810458d9925deaf4baa0f0116fa1(
    *,
    count: typing.Optional[jsii.Number] = None,
    percent: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d413cb0e5668d2bd555e8bff93d972cb6685ca731d25fc112a1a637412766805(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6db0e7e7019a2ba5b14004bac4599fbc2a072b98b73c117a09d483cd1caf590(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e660ce0cc9e74b34f5d8d892e3b2d29bfe77bfaad91bbe92a911bccfbc73500(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb5de7b717aac2d0025687416339b7e69f20ec75f810ebaea1052857301e90bf(
    value: typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f622051e2803eb7abc3cc339073103067e8854cfa1beacd015c37b9c44e354b8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60ddaa17bce80301df3be097f44b07be7570f9af02723daa6118a1c38ac29c99(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee6818423edb25136df32c4ff1626dc0626d84bb65ba2421c4a6c3061bc6d613(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29d74f6131c5bb0f704ca0525b22bb726a20d526b403a36201eef07915743266(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__501015c45852f7743c8121fae29d4f4d7864b5ef5085611f787296a55038d8fa(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e456639158164dd4448c19b4dc558d1a625ce2463f0e6d6b856d2a731965a9de(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__413ae3337a6a04e541582e5abb45daa641fb01895fe888c7a74d481a301cde2e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23907189001f87754e1915188f4133c34b9e55d6a2b445f22a95df41dd93b00d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d79a0c2fe0cb4a4e04fe0f1fd161cbbe88bf35550ba75ef314808fade7872c48(
    value: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b80d32bcf548ced82bb8f856a9ca19d175614711866bcd6e3df96a81d055847(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    combiner: builtins.str,
    conditions: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleMonitoringAlertPolicyConditions, typing.Dict[builtins.str, typing.Any]]]],
    display_name: builtins.str,
    alert_strategy: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyAlertStrategy, typing.Dict[builtins.str, typing.Any]]] = None,
    documentation: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyDocumentation, typing.Dict[builtins.str, typing.Any]]] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    notification_channels: typing.Optional[typing.Sequence[builtins.str]] = None,
    project: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    user_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e8ad35708efc6ee70dbb18b14608837dec80d6d6a4937241f4955c9ab759ceb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bd8b9d6066369f8150aaaf43f136f8597a682788e89cd04ce435717857ed591(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9457b1ec035e5800e62f97e9551bde5361ecca7c7336fc6fc74e16e88a6c2bb8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce1ef91e0f050a2ab852a7ae809dcf6b554622a47fc0cef10ba262a417e1dee3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8239664f3dab5da1ed734fd583cc5fdeb5a18fdeec3b0aada93d6a347df06e87(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3c1fa378b82f2b07bb9e280fb272bf73679ab5c72d807878d5b36baf7f58702(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__615515ae3acf4bfecc4a1bdba33664cb1da1f1a59b9ca4aa9eeb4db73121b054(
    value: typing.Optional[GoogleMonitoringAlertPolicyCreationRecord],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12ab4b5b9b27568573292c40f02813b4fc6cb2df64779a9fe602a2ae32e5079b(
    *,
    content: typing.Optional[builtins.str] = None,
    mime_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e77ed805bb6e86dff61110097b8c1d39ac3d7cf9f9af3659618860b47d260de(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6c79894b36d36365ddaec8c96a0c7838d5bc7ba4e51e5420dc4bc2d7e7f9433(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fd11c759f3e73cc57cb72d50a8fa696d03e7deb841c3a1c1d124c583eca27e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__454c2f7c80918c1dfe658ec91640a8e53739b1caf8b6ab80bd9670262bbbd66a(
    value: typing.Optional[GoogleMonitoringAlertPolicyDocumentation],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ea7bf7b597c41adb468dabbd8702337dd6be7365661826f0669d385ee97052b(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a37ab45b6b57338c764e99f57eb1669f1808942cd60548ed87a0fa56c31f2ca(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db71dac654d3e0b7ea12d89188e13f66fa806f00f71c4a4eb88028ce004b000c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__162e6672d2c6c0bc168ce56302ffc63749426972667348ee0a823f99e8d87722(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe9165e9f59355928efc4473ad54c9913551cc3ef1080a3f8646ce5837d51f25(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78d6cb6c1fa0286847b9a7ea10ee6639d481368d4eeddcf5a31e14676386883c(
    value: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
