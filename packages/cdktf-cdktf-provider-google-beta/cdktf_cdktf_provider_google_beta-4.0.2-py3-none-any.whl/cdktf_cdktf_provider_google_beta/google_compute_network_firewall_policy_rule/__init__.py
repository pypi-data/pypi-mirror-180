'''
# `google_compute_network_firewall_policy_rule`

Refer to the Terraform Registory for docs: [`google_compute_network_firewall_policy_rule`](https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule).
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


class GoogleComputeNetworkFirewallPolicyRule(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeNetworkFirewallPolicyRule.GoogleComputeNetworkFirewallPolicyRule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule google_compute_network_firewall_policy_rule}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        action: builtins.str,
        direction: builtins.str,
        firewall_policy: builtins.str,
        match: typing.Union["GoogleComputeNetworkFirewallPolicyRuleMatch", typing.Dict[builtins.str, typing.Any]],
        priority: jsii.Number,
        description: typing.Optional[builtins.str] = None,
        disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_logging: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target_secure_tags: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleComputeNetworkFirewallPolicyRuleTargetSecureTags", typing.Dict[builtins.str, typing.Any]]]]] = None,
        target_service_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeNetworkFirewallPolicyRuleTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule google_compute_network_firewall_policy_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param action: The Action to perform when the client connection triggers the rule. Can currently be either "allow" or "deny()" where valid values for status are 403, 404, and 502. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#action GoogleComputeNetworkFirewallPolicyRule#action}
        :param direction: The direction in which this rule applies. Possible values: INGRESS, EGRESS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#direction GoogleComputeNetworkFirewallPolicyRule#direction}
        :param firewall_policy: The firewall policy of the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#firewall_policy GoogleComputeNetworkFirewallPolicyRule#firewall_policy}
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#match GoogleComputeNetworkFirewallPolicyRule#match}
        :param priority: An integer indicating the priority of a rule in the list. The priority must be a positive value between 0 and 2147483647. Rules are evaluated from highest to lowest priority where 0 is the highest priority and 2147483647 is the lowest prority. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#priority GoogleComputeNetworkFirewallPolicyRule#priority}
        :param description: An optional description for this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#description GoogleComputeNetworkFirewallPolicyRule#description}
        :param disabled: Denotes whether the firewall policy rule is disabled. When set to true, the firewall policy rule is not enforced and traffic behaves as if it did not exist. If this is unspecified, the firewall policy rule will be enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#disabled GoogleComputeNetworkFirewallPolicyRule#disabled}
        :param enable_logging: Denotes whether to enable logging for a particular rule. If logging is enabled, logs will be exported to the configured export destination in Stackdriver. Logs may be exported to BigQuery or Pub/Sub. Note: you cannot enable logging on "goto_next" rules. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#enable_logging GoogleComputeNetworkFirewallPolicyRule#enable_logging}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#id GoogleComputeNetworkFirewallPolicyRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: The project for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#project GoogleComputeNetworkFirewallPolicyRule#project}
        :param rule_name: An optional name for the rule. This field is not a unique identifier and can be updated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#rule_name GoogleComputeNetworkFirewallPolicyRule#rule_name}
        :param target_secure_tags: target_secure_tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#target_secure_tags GoogleComputeNetworkFirewallPolicyRule#target_secure_tags}
        :param target_service_accounts: A list of service accounts indicating the sets of instances that are applied with this rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#target_service_accounts GoogleComputeNetworkFirewallPolicyRule#target_service_accounts}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#timeouts GoogleComputeNetworkFirewallPolicyRule#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7db175e8b931f72a10ad5cefdb9c83d9f0590110dc90ca8831fabd5a32d2e45)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleComputeNetworkFirewallPolicyRuleConfig(
            action=action,
            direction=direction,
            firewall_policy=firewall_policy,
            match=match,
            priority=priority,
            description=description,
            disabled=disabled,
            enable_logging=enable_logging,
            id=id,
            project=project,
            rule_name=rule_name,
            target_secure_tags=target_secure_tags,
            target_service_accounts=target_service_accounts,
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

    @jsii.member(jsii_name="putMatch")
    def put_match(
        self,
        *,
        layer4_configs: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleComputeNetworkFirewallPolicyRuleMatchLayer4Configs", typing.Dict[builtins.str, typing.Any]]]],
        dest_ip_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        src_ip_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        src_secure_tags: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTags", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param layer4_configs: layer4_configs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#layer4_configs GoogleComputeNetworkFirewallPolicyRule#layer4_configs}
        :param dest_ip_ranges: CIDR IP address range. Maximum number of destination CIDR IP ranges allowed is 5000. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#dest_ip_ranges GoogleComputeNetworkFirewallPolicyRule#dest_ip_ranges}
        :param src_ip_ranges: CIDR IP address range. Maximum number of source CIDR IP ranges allowed is 5000. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#src_ip_ranges GoogleComputeNetworkFirewallPolicyRule#src_ip_ranges}
        :param src_secure_tags: src_secure_tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#src_secure_tags GoogleComputeNetworkFirewallPolicyRule#src_secure_tags}
        '''
        value = GoogleComputeNetworkFirewallPolicyRuleMatch(
            layer4_configs=layer4_configs,
            dest_ip_ranges=dest_ip_ranges,
            src_ip_ranges=src_ip_ranges,
            src_secure_tags=src_secure_tags,
        )

        return typing.cast(None, jsii.invoke(self, "putMatch", [value]))

    @jsii.member(jsii_name="putTargetSecureTags")
    def put_target_secure_tags(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleComputeNetworkFirewallPolicyRuleTargetSecureTags", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f6cc443a3875608f926ff5437d61c7697152c6e96dfcbd5b894edc1c6f9eabf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTargetSecureTags", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#create GoogleComputeNetworkFirewallPolicyRule#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#delete GoogleComputeNetworkFirewallPolicyRule#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#update GoogleComputeNetworkFirewallPolicyRule#update}.
        '''
        value = GoogleComputeNetworkFirewallPolicyRuleTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDisabled")
    def reset_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabled", []))

    @jsii.member(jsii_name="resetEnableLogging")
    def reset_enable_logging(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableLogging", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRuleName")
    def reset_rule_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuleName", []))

    @jsii.member(jsii_name="resetTargetSecureTags")
    def reset_target_secure_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetSecureTags", []))

    @jsii.member(jsii_name="resetTargetServiceAccounts")
    def reset_target_service_accounts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetServiceAccounts", []))

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
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @builtins.property
    @jsii.member(jsii_name="match")
    def match(self) -> "GoogleComputeNetworkFirewallPolicyRuleMatchOutputReference":
        return typing.cast("GoogleComputeNetworkFirewallPolicyRuleMatchOutputReference", jsii.get(self, "match"))

    @builtins.property
    @jsii.member(jsii_name="ruleTupleCount")
    def rule_tuple_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ruleTupleCount"))

    @builtins.property
    @jsii.member(jsii_name="targetSecureTags")
    def target_secure_tags(
        self,
    ) -> "GoogleComputeNetworkFirewallPolicyRuleTargetSecureTagsList":
        return typing.cast("GoogleComputeNetworkFirewallPolicyRuleTargetSecureTagsList", jsii.get(self, "targetSecureTags"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(
        self,
    ) -> "GoogleComputeNetworkFirewallPolicyRuleTimeoutsOutputReference":
        return typing.cast("GoogleComputeNetworkFirewallPolicyRuleTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="directionInput")
    def direction_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directionInput"))

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="enableLoggingInput")
    def enable_logging_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableLoggingInput"))

    @builtins.property
    @jsii.member(jsii_name="firewallPolicyInput")
    def firewall_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firewallPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="matchInput")
    def match_input(
        self,
    ) -> typing.Optional["GoogleComputeNetworkFirewallPolicyRuleMatch"]:
        return typing.cast(typing.Optional["GoogleComputeNetworkFirewallPolicyRuleMatch"], jsii.get(self, "matchInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleNameInput")
    def rule_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleNameInput"))

    @builtins.property
    @jsii.member(jsii_name="targetSecureTagsInput")
    def target_secure_tags_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleComputeNetworkFirewallPolicyRuleTargetSecureTags"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleComputeNetworkFirewallPolicyRuleTargetSecureTags"]]], jsii.get(self, "targetSecureTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="targetServiceAccountsInput")
    def target_service_accounts_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetServiceAccountsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleComputeNetworkFirewallPolicyRuleTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleComputeNetworkFirewallPolicyRuleTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56bf489ca2e077f3a0e102131076bfcefbfa44a63114750faa54a5bd28c24b27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c511b0ae3e0c9e3303c9d5135e4347244e182df834b30caba7a5fcabf337ca45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="direction")
    def direction(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "direction"))

    @direction.setter
    def direction(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63ece0858cc60203a3bd57c1d5037a1c808720778df40d5de12629806d565b4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "direction", value)

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a85afbd242a1e3283660789d5dea79d84aab9124ddff00d328bbc87150381ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="enableLogging")
    def enable_logging(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableLogging"))

    @enable_logging.setter
    def enable_logging(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8d1cb951f51fd20388054221835b043d170942d962dfa88ecec35e286f01c44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableLogging", value)

    @builtins.property
    @jsii.member(jsii_name="firewallPolicy")
    def firewall_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firewallPolicy"))

    @firewall_policy.setter
    def firewall_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5bdb91963ce5f9b8ce0955e7d66fcc203b77c81d300721a43c9bd556373c375)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firewallPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc18f2d78f28e744dc8d7175d8681de9e8857b5d957af5d4ae4c62b398d62b6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3410eb00fc1922a8521cfcab580693a00157287b6a4c7d7c67114cf8db895770)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20954c532aa7bddaf94c2928e8e9f3095694d0f9f29a5fbdf250570a97489e04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="ruleName")
    def rule_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleName"))

    @rule_name.setter
    def rule_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87d9b19e5d56a9c9fe91c581973105050f82fad12282f395cba83e31d20d393b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleName", value)

    @builtins.property
    @jsii.member(jsii_name="targetServiceAccounts")
    def target_service_accounts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targetServiceAccounts"))

    @target_service_accounts.setter
    def target_service_accounts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6106c9da411b547768b824602dbff346ec5db6e581efac0849c6b867a42b2a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetServiceAccounts", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeNetworkFirewallPolicyRule.GoogleComputeNetworkFirewallPolicyRuleConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "action": "action",
        "direction": "direction",
        "firewall_policy": "firewallPolicy",
        "match": "match",
        "priority": "priority",
        "description": "description",
        "disabled": "disabled",
        "enable_logging": "enableLogging",
        "id": "id",
        "project": "project",
        "rule_name": "ruleName",
        "target_secure_tags": "targetSecureTags",
        "target_service_accounts": "targetServiceAccounts",
        "timeouts": "timeouts",
    },
)
class GoogleComputeNetworkFirewallPolicyRuleConfig(
    _cdktf_9a9027ec.TerraformMetaArguments,
):
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
        action: builtins.str,
        direction: builtins.str,
        firewall_policy: builtins.str,
        match: typing.Union["GoogleComputeNetworkFirewallPolicyRuleMatch", typing.Dict[builtins.str, typing.Any]],
        priority: jsii.Number,
        description: typing.Optional[builtins.str] = None,
        disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_logging: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target_secure_tags: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleComputeNetworkFirewallPolicyRuleTargetSecureTags", typing.Dict[builtins.str, typing.Any]]]]] = None,
        target_service_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeNetworkFirewallPolicyRuleTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param action: The Action to perform when the client connection triggers the rule. Can currently be either "allow" or "deny()" where valid values for status are 403, 404, and 502. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#action GoogleComputeNetworkFirewallPolicyRule#action}
        :param direction: The direction in which this rule applies. Possible values: INGRESS, EGRESS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#direction GoogleComputeNetworkFirewallPolicyRule#direction}
        :param firewall_policy: The firewall policy of the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#firewall_policy GoogleComputeNetworkFirewallPolicyRule#firewall_policy}
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#match GoogleComputeNetworkFirewallPolicyRule#match}
        :param priority: An integer indicating the priority of a rule in the list. The priority must be a positive value between 0 and 2147483647. Rules are evaluated from highest to lowest priority where 0 is the highest priority and 2147483647 is the lowest prority. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#priority GoogleComputeNetworkFirewallPolicyRule#priority}
        :param description: An optional description for this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#description GoogleComputeNetworkFirewallPolicyRule#description}
        :param disabled: Denotes whether the firewall policy rule is disabled. When set to true, the firewall policy rule is not enforced and traffic behaves as if it did not exist. If this is unspecified, the firewall policy rule will be enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#disabled GoogleComputeNetworkFirewallPolicyRule#disabled}
        :param enable_logging: Denotes whether to enable logging for a particular rule. If logging is enabled, logs will be exported to the configured export destination in Stackdriver. Logs may be exported to BigQuery or Pub/Sub. Note: you cannot enable logging on "goto_next" rules. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#enable_logging GoogleComputeNetworkFirewallPolicyRule#enable_logging}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#id GoogleComputeNetworkFirewallPolicyRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: The project for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#project GoogleComputeNetworkFirewallPolicyRule#project}
        :param rule_name: An optional name for the rule. This field is not a unique identifier and can be updated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#rule_name GoogleComputeNetworkFirewallPolicyRule#rule_name}
        :param target_secure_tags: target_secure_tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#target_secure_tags GoogleComputeNetworkFirewallPolicyRule#target_secure_tags}
        :param target_service_accounts: A list of service accounts indicating the sets of instances that are applied with this rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#target_service_accounts GoogleComputeNetworkFirewallPolicyRule#target_service_accounts}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#timeouts GoogleComputeNetworkFirewallPolicyRule#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(match, dict):
            match = GoogleComputeNetworkFirewallPolicyRuleMatch(**match)
        if isinstance(timeouts, dict):
            timeouts = GoogleComputeNetworkFirewallPolicyRuleTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84b261d63d793f1108a48dfeb779a3bb9d057117d017b185b33056ea762f262c)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument direction", value=direction, expected_type=type_hints["direction"])
            check_type(argname="argument firewall_policy", value=firewall_policy, expected_type=type_hints["firewall_policy"])
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
            check_type(argname="argument enable_logging", value=enable_logging, expected_type=type_hints["enable_logging"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
            check_type(argname="argument target_secure_tags", value=target_secure_tags, expected_type=type_hints["target_secure_tags"])
            check_type(argname="argument target_service_accounts", value=target_service_accounts, expected_type=type_hints["target_service_accounts"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
            "direction": direction,
            "firewall_policy": firewall_policy,
            "match": match,
            "priority": priority,
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
        if disabled is not None:
            self._values["disabled"] = disabled
        if enable_logging is not None:
            self._values["enable_logging"] = enable_logging
        if id is not None:
            self._values["id"] = id
        if project is not None:
            self._values["project"] = project
        if rule_name is not None:
            self._values["rule_name"] = rule_name
        if target_secure_tags is not None:
            self._values["target_secure_tags"] = target_secure_tags
        if target_service_accounts is not None:
            self._values["target_service_accounts"] = target_service_accounts
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
    def action(self) -> builtins.str:
        '''The Action to perform when the client connection triggers the rule.

        Can currently be either "allow" or "deny()" where valid values for status are 403, 404, and 502.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#action GoogleComputeNetworkFirewallPolicyRule#action}
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def direction(self) -> builtins.str:
        '''The direction in which this rule applies. Possible values: INGRESS, EGRESS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#direction GoogleComputeNetworkFirewallPolicyRule#direction}
        '''
        result = self._values.get("direction")
        assert result is not None, "Required property 'direction' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def firewall_policy(self) -> builtins.str:
        '''The firewall policy of the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#firewall_policy GoogleComputeNetworkFirewallPolicyRule#firewall_policy}
        '''
        result = self._values.get("firewall_policy")
        assert result is not None, "Required property 'firewall_policy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def match(self) -> "GoogleComputeNetworkFirewallPolicyRuleMatch":
        '''match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#match GoogleComputeNetworkFirewallPolicyRule#match}
        '''
        result = self._values.get("match")
        assert result is not None, "Required property 'match' is missing"
        return typing.cast("GoogleComputeNetworkFirewallPolicyRuleMatch", result)

    @builtins.property
    def priority(self) -> jsii.Number:
        '''An integer indicating the priority of a rule in the list.

        The priority must be a positive value between 0 and 2147483647. Rules are evaluated from highest to lowest priority where 0 is the highest priority and 2147483647 is the lowest prority.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#priority GoogleComputeNetworkFirewallPolicyRule#priority}
        '''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description for this resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#description GoogleComputeNetworkFirewallPolicyRule#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Denotes whether the firewall policy rule is disabled.

        When set to true, the firewall policy rule is not enforced and traffic behaves as if it did not exist. If this is unspecified, the firewall policy rule will be enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#disabled GoogleComputeNetworkFirewallPolicyRule#disabled}
        '''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_logging(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Denotes whether to enable logging for a particular rule.

        If logging is enabled, logs will be exported to the configured export destination in Stackdriver. Logs may be exported to BigQuery or Pub/Sub. Note: you cannot enable logging on "goto_next" rules.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#enable_logging GoogleComputeNetworkFirewallPolicyRule#enable_logging}
        '''
        result = self._values.get("enable_logging")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#id GoogleComputeNetworkFirewallPolicyRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The project for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#project GoogleComputeNetworkFirewallPolicyRule#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule_name(self) -> typing.Optional[builtins.str]:
        '''An optional name for the rule. This field is not a unique identifier and can be updated.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#rule_name GoogleComputeNetworkFirewallPolicyRule#rule_name}
        '''
        result = self._values.get("rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_secure_tags(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleComputeNetworkFirewallPolicyRuleTargetSecureTags"]]]:
        '''target_secure_tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#target_secure_tags GoogleComputeNetworkFirewallPolicyRule#target_secure_tags}
        '''
        result = self._values.get("target_secure_tags")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleComputeNetworkFirewallPolicyRuleTargetSecureTags"]]], result)

    @builtins.property
    def target_service_accounts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of service accounts indicating the sets of instances that are applied with this rule.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#target_service_accounts GoogleComputeNetworkFirewallPolicyRule#target_service_accounts}
        '''
        result = self._values.get("target_service_accounts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["GoogleComputeNetworkFirewallPolicyRuleTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#timeouts GoogleComputeNetworkFirewallPolicyRule#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleComputeNetworkFirewallPolicyRuleTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeNetworkFirewallPolicyRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeNetworkFirewallPolicyRule.GoogleComputeNetworkFirewallPolicyRuleMatch",
    jsii_struct_bases=[],
    name_mapping={
        "layer4_configs": "layer4Configs",
        "dest_ip_ranges": "destIpRanges",
        "src_ip_ranges": "srcIpRanges",
        "src_secure_tags": "srcSecureTags",
    },
)
class GoogleComputeNetworkFirewallPolicyRuleMatch:
    def __init__(
        self,
        *,
        layer4_configs: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleComputeNetworkFirewallPolicyRuleMatchLayer4Configs", typing.Dict[builtins.str, typing.Any]]]],
        dest_ip_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        src_ip_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        src_secure_tags: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTags", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param layer4_configs: layer4_configs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#layer4_configs GoogleComputeNetworkFirewallPolicyRule#layer4_configs}
        :param dest_ip_ranges: CIDR IP address range. Maximum number of destination CIDR IP ranges allowed is 5000. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#dest_ip_ranges GoogleComputeNetworkFirewallPolicyRule#dest_ip_ranges}
        :param src_ip_ranges: CIDR IP address range. Maximum number of source CIDR IP ranges allowed is 5000. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#src_ip_ranges GoogleComputeNetworkFirewallPolicyRule#src_ip_ranges}
        :param src_secure_tags: src_secure_tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#src_secure_tags GoogleComputeNetworkFirewallPolicyRule#src_secure_tags}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d9f442941aef3ea201e02aa3bb3a19c2829f094f7f599fbb0ec46a180b063d9)
            check_type(argname="argument layer4_configs", value=layer4_configs, expected_type=type_hints["layer4_configs"])
            check_type(argname="argument dest_ip_ranges", value=dest_ip_ranges, expected_type=type_hints["dest_ip_ranges"])
            check_type(argname="argument src_ip_ranges", value=src_ip_ranges, expected_type=type_hints["src_ip_ranges"])
            check_type(argname="argument src_secure_tags", value=src_secure_tags, expected_type=type_hints["src_secure_tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "layer4_configs": layer4_configs,
        }
        if dest_ip_ranges is not None:
            self._values["dest_ip_ranges"] = dest_ip_ranges
        if src_ip_ranges is not None:
            self._values["src_ip_ranges"] = src_ip_ranges
        if src_secure_tags is not None:
            self._values["src_secure_tags"] = src_secure_tags

    @builtins.property
    def layer4_configs(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleComputeNetworkFirewallPolicyRuleMatchLayer4Configs"]]:
        '''layer4_configs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#layer4_configs GoogleComputeNetworkFirewallPolicyRule#layer4_configs}
        '''
        result = self._values.get("layer4_configs")
        assert result is not None, "Required property 'layer4_configs' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleComputeNetworkFirewallPolicyRuleMatchLayer4Configs"]], result)

    @builtins.property
    def dest_ip_ranges(self) -> typing.Optional[typing.List[builtins.str]]:
        '''CIDR IP address range. Maximum number of destination CIDR IP ranges allowed is 5000.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#dest_ip_ranges GoogleComputeNetworkFirewallPolicyRule#dest_ip_ranges}
        '''
        result = self._values.get("dest_ip_ranges")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def src_ip_ranges(self) -> typing.Optional[typing.List[builtins.str]]:
        '''CIDR IP address range. Maximum number of source CIDR IP ranges allowed is 5000.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#src_ip_ranges GoogleComputeNetworkFirewallPolicyRule#src_ip_ranges}
        '''
        result = self._values.get("src_ip_ranges")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def src_secure_tags(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTags"]]]:
        '''src_secure_tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#src_secure_tags GoogleComputeNetworkFirewallPolicyRule#src_secure_tags}
        '''
        result = self._values.get("src_secure_tags")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTags"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeNetworkFirewallPolicyRuleMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeNetworkFirewallPolicyRule.GoogleComputeNetworkFirewallPolicyRuleMatchLayer4Configs",
    jsii_struct_bases=[],
    name_mapping={"ip_protocol": "ipProtocol", "ports": "ports"},
)
class GoogleComputeNetworkFirewallPolicyRuleMatchLayer4Configs:
    def __init__(
        self,
        *,
        ip_protocol: builtins.str,
        ports: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param ip_protocol: The IP protocol to which this rule applies. The protocol type is required when creating a firewall rule. This value can either be one of the following well known protocol strings (``tcp``, ``udp``, ``icmp``, ``esp``, ``ah``, ``ipip``, ``sctp``), or the IP protocol number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#ip_protocol GoogleComputeNetworkFirewallPolicyRule#ip_protocol}
        :param ports: An optional list of ports to which this rule applies. This field is only applicable for UDP or TCP protocol. Each entry must be either an integer or a range. If not specified, this rule applies to connections through any port. Example inputs include: ``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#ports GoogleComputeNetworkFirewallPolicyRule#ports}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5563016323856b2406b0eee8525de352015a578b8852acec1f1d436f33c23750)
            check_type(argname="argument ip_protocol", value=ip_protocol, expected_type=type_hints["ip_protocol"])
            check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ip_protocol": ip_protocol,
        }
        if ports is not None:
            self._values["ports"] = ports

    @builtins.property
    def ip_protocol(self) -> builtins.str:
        '''The IP protocol to which this rule applies.

        The protocol type is required when creating a firewall rule. This value can either be one of the following well known protocol strings (``tcp``, ``udp``, ``icmp``, ``esp``, ``ah``, ``ipip``, ``sctp``), or the IP protocol number.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#ip_protocol GoogleComputeNetworkFirewallPolicyRule#ip_protocol}
        '''
        result = self._values.get("ip_protocol")
        assert result is not None, "Required property 'ip_protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ports(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An optional list of ports to which this rule applies.

        This field is only applicable for UDP or TCP protocol. Each entry must be either an integer or a range. If not specified, this rule applies to connections through any port. Example inputs include: ``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#ports GoogleComputeNetworkFirewallPolicyRule#ports}
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeNetworkFirewallPolicyRuleMatchLayer4Configs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeNetworkFirewallPolicyRuleMatchLayer4ConfigsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeNetworkFirewallPolicyRule.GoogleComputeNetworkFirewallPolicyRuleMatchLayer4ConfigsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c9357d34e8cd34b58a5dbb2f1bebfdcc78b85b3675dc9bd3046edec4471cf2b2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeNetworkFirewallPolicyRuleMatchLayer4ConfigsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33a5cba3460c421932c68e5a3c13664d92d21c102fcd8f0d7d91691cd306cb07)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeNetworkFirewallPolicyRuleMatchLayer4ConfigsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f41321ed65bd29b997171b9e1225aabbe71e5dd966fdfa60a0644247ad569795)
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
            type_hints = typing.get_type_hints(_typecheckingstub__88be796027490927d1da274d660370c46b656b960b8a54478636e7413dcd2492)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f3b0a1296d96899794a27281871ad25b5030422eb0dc727f96848cc8810d7432)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputeNetworkFirewallPolicyRuleMatchLayer4Configs]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputeNetworkFirewallPolicyRuleMatchLayer4Configs]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputeNetworkFirewallPolicyRuleMatchLayer4Configs]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89968c39c96c35a9472ab59be6829400c6dc28822fce3ac9b9b0596c027b5888)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeNetworkFirewallPolicyRuleMatchLayer4ConfigsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeNetworkFirewallPolicyRule.GoogleComputeNetworkFirewallPolicyRuleMatchLayer4ConfigsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__801519d60c634f04b57ef3dc4f386096bf2bf38f8f498daddbf5e71e2e64f7c7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPorts")
    def reset_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPorts", []))

    @builtins.property
    @jsii.member(jsii_name="ipProtocolInput")
    def ip_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="portsInput")
    def ports_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "portsInput"))

    @builtins.property
    @jsii.member(jsii_name="ipProtocol")
    def ip_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipProtocol"))

    @ip_protocol.setter
    def ip_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e02575b95cbda3a0515be6d2034880756710cc3b888a3e174b4d1e555e28f559)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="ports")
    def ports(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ports"))

    @ports.setter
    def ports(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffc88fd6c81a5557391ecaccae5e7ba24ce7fbf7ec7bc4717293976a420ff34c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ports", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeNetworkFirewallPolicyRuleMatchLayer4Configs, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeNetworkFirewallPolicyRuleMatchLayer4Configs, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeNetworkFirewallPolicyRuleMatchLayer4Configs, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f15cc6f8c617a613d1388ec4f927f75dda97397d6c5634adcdbade3aa564c8f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeNetworkFirewallPolicyRuleMatchOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeNetworkFirewallPolicyRule.GoogleComputeNetworkFirewallPolicyRuleMatchOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4a7510ff11f36dc44074c220026e4d6ff71b924142b8287444962a2b90096522)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLayer4Configs")
    def put_layer4_configs(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleComputeNetworkFirewallPolicyRuleMatchLayer4Configs, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bf3d05e3f9d7cc8802d9a5df7b21a32a6f289b804ad7e21111c3859884dee37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLayer4Configs", [value]))

    @jsii.member(jsii_name="putSrcSecureTags")
    def put_src_secure_tags(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTags", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95b8b03cc65cd967752b792df066dfbeea6654a27f0e4fcbf4a31afcc5e28bc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSrcSecureTags", [value]))

    @jsii.member(jsii_name="resetDestIpRanges")
    def reset_dest_ip_ranges(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestIpRanges", []))

    @jsii.member(jsii_name="resetSrcIpRanges")
    def reset_src_ip_ranges(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSrcIpRanges", []))

    @jsii.member(jsii_name="resetSrcSecureTags")
    def reset_src_secure_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSrcSecureTags", []))

    @builtins.property
    @jsii.member(jsii_name="layer4Configs")
    def layer4_configs(
        self,
    ) -> GoogleComputeNetworkFirewallPolicyRuleMatchLayer4ConfigsList:
        return typing.cast(GoogleComputeNetworkFirewallPolicyRuleMatchLayer4ConfigsList, jsii.get(self, "layer4Configs"))

    @builtins.property
    @jsii.member(jsii_name="srcSecureTags")
    def src_secure_tags(
        self,
    ) -> "GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTagsList":
        return typing.cast("GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTagsList", jsii.get(self, "srcSecureTags"))

    @builtins.property
    @jsii.member(jsii_name="destIpRangesInput")
    def dest_ip_ranges_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "destIpRangesInput"))

    @builtins.property
    @jsii.member(jsii_name="layer4ConfigsInput")
    def layer4_configs_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputeNetworkFirewallPolicyRuleMatchLayer4Configs]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputeNetworkFirewallPolicyRuleMatchLayer4Configs]]], jsii.get(self, "layer4ConfigsInput"))

    @builtins.property
    @jsii.member(jsii_name="srcIpRangesInput")
    def src_ip_ranges_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "srcIpRangesInput"))

    @builtins.property
    @jsii.member(jsii_name="srcSecureTagsInput")
    def src_secure_tags_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTags"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTags"]]], jsii.get(self, "srcSecureTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="destIpRanges")
    def dest_ip_ranges(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destIpRanges"))

    @dest_ip_ranges.setter
    def dest_ip_ranges(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9f08dde65540c7f2114829f0e5ac3c456de1e2432319964ee32c1fc0e0a54bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destIpRanges", value)

    @builtins.property
    @jsii.member(jsii_name="srcIpRanges")
    def src_ip_ranges(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "srcIpRanges"))

    @src_ip_ranges.setter
    def src_ip_ranges(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a962543156af26d896d62115696f5ffc28ca8352a1961487cb76cf69ef0aa6ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "srcIpRanges", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeNetworkFirewallPolicyRuleMatch]:
        return typing.cast(typing.Optional[GoogleComputeNetworkFirewallPolicyRuleMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeNetworkFirewallPolicyRuleMatch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f6b6d12dabb6e906be3ca1dfafd7e19ab42011b345523c4d66aad3547abc785)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeNetworkFirewallPolicyRule.GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTags",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTags:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Name of the secure tag, created with TagManager's TagValue API. @pattern tagValues/[0-9]+. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#name GoogleComputeNetworkFirewallPolicyRule#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ea2653632553c2379c5e292294d179cf0456e26d4f0e536d8a32ca532c57049)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the secure tag, created with TagManager's TagValue API. @pattern tagValues/[0-9]+.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#name GoogleComputeNetworkFirewallPolicyRule#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTagsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeNetworkFirewallPolicyRule.GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTagsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8d68d346bae37ba082340edf3ae8b58b1fefef48cf667b1671ff61be36d14f84)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTagsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eaf84e51acb89590ebb63dc159c27766323be8c0cf5517da2c0e4751106b1da9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTagsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77a5e16909e7ac29d88c3f93a9c719ac5e047a66be4d6d1870b28bb8787a8128)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f712c9e6b8e4b06325a894a91fd1ddd6d5c876c3caf2f8e24692cf2dc46cba52)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f19ebee12360b965bdfb669f388301fed6c03a72b03da6205d7b3ca43d5e8a2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTags]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTags]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTags]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b09381d2f0319133c6a7fc37bbbc0ecdc4356d523ce7455c271e57253a3f897)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTagsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeNetworkFirewallPolicyRule.GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTagsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5ceb9d3047ca353c849c8c5a9f0183b6817e18a46cfe9e91d4dfb8ea1c272c22)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d3eaa32649cbb52ce44fbe2c41077c4e73911459dc7fecd85214ad42443ca33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTags, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTags, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTags, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b6817f48b6d125113bbcdb613c44eb61a1916e200bc054de4e405b588d4cfde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeNetworkFirewallPolicyRule.GoogleComputeNetworkFirewallPolicyRuleTargetSecureTags",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class GoogleComputeNetworkFirewallPolicyRuleTargetSecureTags:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Name of the secure tag, created with TagManager's TagValue API. @pattern tagValues/[0-9]+. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#name GoogleComputeNetworkFirewallPolicyRule#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d38769500dfb469f80adf96a7a607c8ad2a086899c72cc439987264ce9c1c22)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the secure tag, created with TagManager's TagValue API. @pattern tagValues/[0-9]+.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#name GoogleComputeNetworkFirewallPolicyRule#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeNetworkFirewallPolicyRuleTargetSecureTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeNetworkFirewallPolicyRuleTargetSecureTagsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeNetworkFirewallPolicyRule.GoogleComputeNetworkFirewallPolicyRuleTargetSecureTagsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__781fbcdba377974339c338e1596e88079f904b0a860f472809e5c2d7c5bcc1d6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeNetworkFirewallPolicyRuleTargetSecureTagsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f644be2f45b43c0a7fc05c8d87fe982a6108bfe2a83ccf6e0ac01fb1893e275)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeNetworkFirewallPolicyRuleTargetSecureTagsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dc66fd70f18ebb7948eadb18244f3d1b5616ff8d37aefbd3de43b7663e884dc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__56e0d275e3295245b39c85051a03e3ac118360f258daea7d3710ec0dd1a0b29b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7667c0d5df6cf74ad7b28bdc78637b1305c3e8840082d1bf292147fec919847d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputeNetworkFirewallPolicyRuleTargetSecureTags]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputeNetworkFirewallPolicyRuleTargetSecureTags]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputeNetworkFirewallPolicyRuleTargetSecureTags]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70244ab57165c635e82827211b7be28fd000afd618dcb2a6480d84e17738cf03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeNetworkFirewallPolicyRuleTargetSecureTagsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeNetworkFirewallPolicyRule.GoogleComputeNetworkFirewallPolicyRuleTargetSecureTagsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6a2d006158e57b9198b5776dedb7ebf886c5102711987b2f820905106ba83a9b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5181f02e68f8b6fc81de1b22e057ef26f006066bbf916d78d4f0c42a2ff38518)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeNetworkFirewallPolicyRuleTargetSecureTags, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeNetworkFirewallPolicyRuleTargetSecureTags, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeNetworkFirewallPolicyRuleTargetSecureTags, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af0de8d6a01cf71354c33abf4820a17b95c7882a1fc522b9b2aaa43d3fa760d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeNetworkFirewallPolicyRule.GoogleComputeNetworkFirewallPolicyRuleTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleComputeNetworkFirewallPolicyRuleTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#create GoogleComputeNetworkFirewallPolicyRule#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#delete GoogleComputeNetworkFirewallPolicyRule#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#update GoogleComputeNetworkFirewallPolicyRule#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aec987d6120afd07b282e017dc8cc52ade5cedc7871ebb0d91e2f60ef9348c96)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#create GoogleComputeNetworkFirewallPolicyRule#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#delete GoogleComputeNetworkFirewallPolicyRule#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_firewall_policy_rule#update GoogleComputeNetworkFirewallPolicyRule#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeNetworkFirewallPolicyRuleTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeNetworkFirewallPolicyRuleTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeNetworkFirewallPolicyRule.GoogleComputeNetworkFirewallPolicyRuleTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__93b350b8305270230fed6b11e79f2b1455f38913253522a8763da35ece27d6a6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__85600490207d128475af1794aeb437b7677fccbda6058759de6e0f538c7fa159)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ca1011026c065cf88bca622f7492e6c5c4f4a20498355b5b85e081c08889463)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05c3b2dec74b89de10d3490c9ce7a1d1e1f6ca9aeaafa791db7da2daaba91967)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeNetworkFirewallPolicyRuleTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeNetworkFirewallPolicyRuleTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeNetworkFirewallPolicyRuleTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a104650b5252c823d73ecac6fb73982a22bb426da791a407942981c1b328cd41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleComputeNetworkFirewallPolicyRule",
    "GoogleComputeNetworkFirewallPolicyRuleConfig",
    "GoogleComputeNetworkFirewallPolicyRuleMatch",
    "GoogleComputeNetworkFirewallPolicyRuleMatchLayer4Configs",
    "GoogleComputeNetworkFirewallPolicyRuleMatchLayer4ConfigsList",
    "GoogleComputeNetworkFirewallPolicyRuleMatchLayer4ConfigsOutputReference",
    "GoogleComputeNetworkFirewallPolicyRuleMatchOutputReference",
    "GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTags",
    "GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTagsList",
    "GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTagsOutputReference",
    "GoogleComputeNetworkFirewallPolicyRuleTargetSecureTags",
    "GoogleComputeNetworkFirewallPolicyRuleTargetSecureTagsList",
    "GoogleComputeNetworkFirewallPolicyRuleTargetSecureTagsOutputReference",
    "GoogleComputeNetworkFirewallPolicyRuleTimeouts",
    "GoogleComputeNetworkFirewallPolicyRuleTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__d7db175e8b931f72a10ad5cefdb9c83d9f0590110dc90ca8831fabd5a32d2e45(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    action: builtins.str,
    direction: builtins.str,
    firewall_policy: builtins.str,
    match: typing.Union[GoogleComputeNetworkFirewallPolicyRuleMatch, typing.Dict[builtins.str, typing.Any]],
    priority: jsii.Number,
    description: typing.Optional[builtins.str] = None,
    disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_logging: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    project: typing.Optional[builtins.str] = None,
    rule_name: typing.Optional[builtins.str] = None,
    target_secure_tags: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleComputeNetworkFirewallPolicyRuleTargetSecureTags, typing.Dict[builtins.str, typing.Any]]]]] = None,
    target_service_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[GoogleComputeNetworkFirewallPolicyRuleTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__9f6cc443a3875608f926ff5437d61c7697152c6e96dfcbd5b894edc1c6f9eabf(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleComputeNetworkFirewallPolicyRuleTargetSecureTags, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56bf489ca2e077f3a0e102131076bfcefbfa44a63114750faa54a5bd28c24b27(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c511b0ae3e0c9e3303c9d5135e4347244e182df834b30caba7a5fcabf337ca45(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63ece0858cc60203a3bd57c1d5037a1c808720778df40d5de12629806d565b4f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a85afbd242a1e3283660789d5dea79d84aab9124ddff00d328bbc87150381ba(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8d1cb951f51fd20388054221835b043d170942d962dfa88ecec35e286f01c44(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5bdb91963ce5f9b8ce0955e7d66fcc203b77c81d300721a43c9bd556373c375(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc18f2d78f28e744dc8d7175d8681de9e8857b5d957af5d4ae4c62b398d62b6c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3410eb00fc1922a8521cfcab580693a00157287b6a4c7d7c67114cf8db895770(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20954c532aa7bddaf94c2928e8e9f3095694d0f9f29a5fbdf250570a97489e04(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87d9b19e5d56a9c9fe91c581973105050f82fad12282f395cba83e31d20d393b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6106c9da411b547768b824602dbff346ec5db6e581efac0849c6b867a42b2a7(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84b261d63d793f1108a48dfeb779a3bb9d057117d017b185b33056ea762f262c(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    action: builtins.str,
    direction: builtins.str,
    firewall_policy: builtins.str,
    match: typing.Union[GoogleComputeNetworkFirewallPolicyRuleMatch, typing.Dict[builtins.str, typing.Any]],
    priority: jsii.Number,
    description: typing.Optional[builtins.str] = None,
    disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_logging: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    project: typing.Optional[builtins.str] = None,
    rule_name: typing.Optional[builtins.str] = None,
    target_secure_tags: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleComputeNetworkFirewallPolicyRuleTargetSecureTags, typing.Dict[builtins.str, typing.Any]]]]] = None,
    target_service_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[GoogleComputeNetworkFirewallPolicyRuleTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d9f442941aef3ea201e02aa3bb3a19c2829f094f7f599fbb0ec46a180b063d9(
    *,
    layer4_configs: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleComputeNetworkFirewallPolicyRuleMatchLayer4Configs, typing.Dict[builtins.str, typing.Any]]]],
    dest_ip_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
    src_ip_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
    src_secure_tags: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTags, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5563016323856b2406b0eee8525de352015a578b8852acec1f1d436f33c23750(
    *,
    ip_protocol: builtins.str,
    ports: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9357d34e8cd34b58a5dbb2f1bebfdcc78b85b3675dc9bd3046edec4471cf2b2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33a5cba3460c421932c68e5a3c13664d92d21c102fcd8f0d7d91691cd306cb07(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f41321ed65bd29b997171b9e1225aabbe71e5dd966fdfa60a0644247ad569795(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88be796027490927d1da274d660370c46b656b960b8a54478636e7413dcd2492(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3b0a1296d96899794a27281871ad25b5030422eb0dc727f96848cc8810d7432(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89968c39c96c35a9472ab59be6829400c6dc28822fce3ac9b9b0596c027b5888(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputeNetworkFirewallPolicyRuleMatchLayer4Configs]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__801519d60c634f04b57ef3dc4f386096bf2bf38f8f498daddbf5e71e2e64f7c7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e02575b95cbda3a0515be6d2034880756710cc3b888a3e174b4d1e555e28f559(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffc88fd6c81a5557391ecaccae5e7ba24ce7fbf7ec7bc4717293976a420ff34c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f15cc6f8c617a613d1388ec4f927f75dda97397d6c5634adcdbade3aa564c8f6(
    value: typing.Optional[typing.Union[GoogleComputeNetworkFirewallPolicyRuleMatchLayer4Configs, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a7510ff11f36dc44074c220026e4d6ff71b924142b8287444962a2b90096522(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bf3d05e3f9d7cc8802d9a5df7b21a32a6f289b804ad7e21111c3859884dee37(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleComputeNetworkFirewallPolicyRuleMatchLayer4Configs, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95b8b03cc65cd967752b792df066dfbeea6654a27f0e4fcbf4a31afcc5e28bc3(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTags, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9f08dde65540c7f2114829f0e5ac3c456de1e2432319964ee32c1fc0e0a54bb(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a962543156af26d896d62115696f5ffc28ca8352a1961487cb76cf69ef0aa6ea(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f6b6d12dabb6e906be3ca1dfafd7e19ab42011b345523c4d66aad3547abc785(
    value: typing.Optional[GoogleComputeNetworkFirewallPolicyRuleMatch],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ea2653632553c2379c5e292294d179cf0456e26d4f0e536d8a32ca532c57049(
    *,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d68d346bae37ba082340edf3ae8b58b1fefef48cf667b1671ff61be36d14f84(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eaf84e51acb89590ebb63dc159c27766323be8c0cf5517da2c0e4751106b1da9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77a5e16909e7ac29d88c3f93a9c719ac5e047a66be4d6d1870b28bb8787a8128(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f712c9e6b8e4b06325a894a91fd1ddd6d5c876c3caf2f8e24692cf2dc46cba52(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f19ebee12360b965bdfb669f388301fed6c03a72b03da6205d7b3ca43d5e8a2b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b09381d2f0319133c6a7fc37bbbc0ecdc4356d523ce7455c271e57253a3f897(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTags]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ceb9d3047ca353c849c8c5a9f0183b6817e18a46cfe9e91d4dfb8ea1c272c22(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d3eaa32649cbb52ce44fbe2c41077c4e73911459dc7fecd85214ad42443ca33(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b6817f48b6d125113bbcdb613c44eb61a1916e200bc054de4e405b588d4cfde(
    value: typing.Optional[typing.Union[GoogleComputeNetworkFirewallPolicyRuleMatchSrcSecureTags, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d38769500dfb469f80adf96a7a607c8ad2a086899c72cc439987264ce9c1c22(
    *,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__781fbcdba377974339c338e1596e88079f904b0a860f472809e5c2d7c5bcc1d6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f644be2f45b43c0a7fc05c8d87fe982a6108bfe2a83ccf6e0ac01fb1893e275(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dc66fd70f18ebb7948eadb18244f3d1b5616ff8d37aefbd3de43b7663e884dc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56e0d275e3295245b39c85051a03e3ac118360f258daea7d3710ec0dd1a0b29b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7667c0d5df6cf74ad7b28bdc78637b1305c3e8840082d1bf292147fec919847d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70244ab57165c635e82827211b7be28fd000afd618dcb2a6480d84e17738cf03(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputeNetworkFirewallPolicyRuleTargetSecureTags]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a2d006158e57b9198b5776dedb7ebf886c5102711987b2f820905106ba83a9b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5181f02e68f8b6fc81de1b22e057ef26f006066bbf916d78d4f0c42a2ff38518(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af0de8d6a01cf71354c33abf4820a17b95c7882a1fc522b9b2aaa43d3fa760d9(
    value: typing.Optional[typing.Union[GoogleComputeNetworkFirewallPolicyRuleTargetSecureTags, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aec987d6120afd07b282e017dc8cc52ade5cedc7871ebb0d91e2f60ef9348c96(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93b350b8305270230fed6b11e79f2b1455f38913253522a8763da35ece27d6a6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85600490207d128475af1794aeb437b7677fccbda6058759de6e0f538c7fa159(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ca1011026c065cf88bca622f7492e6c5c4f4a20498355b5b85e081c08889463(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05c3b2dec74b89de10d3490c9ce7a1d1e1f6ca9aeaafa791db7da2daaba91967(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a104650b5252c823d73ecac6fb73982a22bb426da791a407942981c1b328cd41(
    value: typing.Optional[typing.Union[GoogleComputeNetworkFirewallPolicyRuleTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
