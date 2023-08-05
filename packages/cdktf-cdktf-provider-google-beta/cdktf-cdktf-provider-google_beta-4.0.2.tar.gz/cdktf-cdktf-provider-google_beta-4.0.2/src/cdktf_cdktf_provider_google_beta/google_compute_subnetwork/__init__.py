'''
# `google_compute_subnetwork`

Refer to the Terraform Registory for docs: [`google_compute_subnetwork`](https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork).
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


class GoogleComputeSubnetwork(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeSubnetwork.GoogleComputeSubnetwork",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork google_compute_subnetwork}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        ip_cidr_range: builtins.str,
        name: builtins.str,
        network: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ipv6_access_type: typing.Optional[builtins.str] = None,
        log_config: typing.Optional[typing.Union["GoogleComputeSubnetworkLogConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        private_ip_google_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        private_ipv6_google_access: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        purpose: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        role: typing.Optional[builtins.str] = None,
        secondary_ip_range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleComputeSubnetworkSecondaryIpRange", typing.Dict[builtins.str, typing.Any]]]]] = None,
        stack_type: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeSubnetworkTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork google_compute_subnetwork} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param ip_cidr_range: The range of internal addresses that are owned by this subnetwork. Provide this property when you create the subnetwork. For example, 10.0.0.0/8 or 192.168.0.0/16. Ranges must be unique and non-overlapping within a network. Only IPv4 is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#ip_cidr_range GoogleComputeSubnetwork#ip_cidr_range}
        :param name: The name of the resource, provided by the client when initially creating the resource. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#name GoogleComputeSubnetwork#name}
        :param network: The network this subnet belongs to. Only networks that are in the distributed mode can have subnetworks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#network GoogleComputeSubnetwork#network}
        :param description: An optional description of this resource. Provide this property when you create the resource. This field can be set only at resource creation time. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#description GoogleComputeSubnetwork#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#id GoogleComputeSubnetwork#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ipv6_access_type: The access type of IPv6 address this subnet holds. It's immutable and can only be specified during creation or the first time the subnet is updated into IPV4_IPV6 dual stack. If the ipv6_type is EXTERNAL then this subnet cannot enable direct path. Possible values: ["EXTERNAL", "INTERNAL"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#ipv6_access_type GoogleComputeSubnetwork#ipv6_access_type}
        :param log_config: log_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#log_config GoogleComputeSubnetwork#log_config}
        :param private_ip_google_access: When enabled, VMs in this subnetwork without external IP addresses can access Google APIs and services by using Private Google Access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#private_ip_google_access GoogleComputeSubnetwork#private_ip_google_access}
        :param private_ipv6_google_access: The private IPv6 google access type for the VMs in this subnet. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#private_ipv6_google_access GoogleComputeSubnetwork#private_ipv6_google_access}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#project GoogleComputeSubnetwork#project}.
        :param purpose: The purpose of the resource. A subnetwork with purpose set to INTERNAL_HTTPS_LOAD_BALANCER is a user-created subnetwork that is reserved for Internal HTTP(S) Load Balancing. If set to INTERNAL_HTTPS_LOAD_BALANCER you must also set the 'role' field. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#purpose GoogleComputeSubnetwork#purpose}
        :param region: The GCP region for this subnetwork. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#region GoogleComputeSubnetwork#region}
        :param role: The role of subnetwork. Currently, this field is only used when purpose = INTERNAL_HTTPS_LOAD_BALANCER. The value can be set to ACTIVE or BACKUP. An ACTIVE subnetwork is one that is currently being used for Internal HTTP(S) Load Balancing. A BACKUP subnetwork is one that is ready to be promoted to ACTIVE or is currently draining. Possible values: ["ACTIVE", "BACKUP"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#role GoogleComputeSubnetwork#role}
        :param secondary_ip_range: An array of configurations for secondary IP ranges for VM instances contained in this subnetwork. The primary IP of such VM must belong to the primary ipCidrRange of the subnetwork. The alias IPs may belong to either primary or secondary ranges. *Note**: This field uses `attr-as-block mode <https://www.terraform.io/docs/configuration/attr-as-blocks.html>`_ to avoid breaking users during the 0.12 upgrade. To explicitly send a list of zero objects you must use the following syntax: 'example=[]' For more details about this behavior, see `this section <https://www.terraform.io/docs/configuration/attr-as-blocks.html#defining-a-fixed-object-collection-value>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#secondary_ip_range GoogleComputeSubnetwork#secondary_ip_range}
        :param stack_type: The stack type for this subnet to identify whether the IPv6 feature is enabled or not. If not specified IPV4_ONLY will be used. Possible values: ["IPV4_ONLY", "IPV4_IPV6"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#stack_type GoogleComputeSubnetwork#stack_type}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#timeouts GoogleComputeSubnetwork#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa2e0719972ae42ff6668cc201c87b78c5aad82b2d6be09df14ab5cc3cd06b39)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleComputeSubnetworkConfig(
            ip_cidr_range=ip_cidr_range,
            name=name,
            network=network,
            description=description,
            id=id,
            ipv6_access_type=ipv6_access_type,
            log_config=log_config,
            private_ip_google_access=private_ip_google_access,
            private_ipv6_google_access=private_ipv6_google_access,
            project=project,
            purpose=purpose,
            region=region,
            role=role,
            secondary_ip_range=secondary_ip_range,
            stack_type=stack_type,
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

    @jsii.member(jsii_name="putLogConfig")
    def put_log_config(
        self,
        *,
        aggregation_interval: typing.Optional[builtins.str] = None,
        filter_expr: typing.Optional[builtins.str] = None,
        flow_sampling: typing.Optional[jsii.Number] = None,
        metadata: typing.Optional[builtins.str] = None,
        metadata_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param aggregation_interval: Can only be specified if VPC flow logging for this subnetwork is enabled. Toggles the aggregation interval for collecting flow logs. Increasing the interval time will reduce the amount of generated flow logs for long lasting connections. Default is an interval of 5 seconds per connection. Default value: "INTERVAL_5_SEC" Possible values: ["INTERVAL_5_SEC", "INTERVAL_30_SEC", "INTERVAL_1_MIN", "INTERVAL_5_MIN", "INTERVAL_10_MIN", "INTERVAL_15_MIN"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#aggregation_interval GoogleComputeSubnetwork#aggregation_interval}
        :param filter_expr: Export filter used to define which VPC flow logs should be logged, as as CEL expression. See https://cloud.google.com/vpc/docs/flow-logs#filtering for details on how to format this field. The default value is 'true', which evaluates to include everything. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#filter_expr GoogleComputeSubnetwork#filter_expr}
        :param flow_sampling: Can only be specified if VPC flow logging for this subnetwork is enabled. The value of the field must be in [0, 1]. Set the sampling rate of VPC flow logs within the subnetwork where 1.0 means all collected logs are reported and 0.0 means no logs are reported. Default is 0.5 which means half of all collected logs are reported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#flow_sampling GoogleComputeSubnetwork#flow_sampling}
        :param metadata: Can only be specified if VPC flow logging for this subnetwork is enabled. Configures whether metadata fields should be added to the reported VPC flow logs. Default value: "INCLUDE_ALL_METADATA" Possible values: ["EXCLUDE_ALL_METADATA", "INCLUDE_ALL_METADATA", "CUSTOM_METADATA"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#metadata GoogleComputeSubnetwork#metadata}
        :param metadata_fields: List of metadata fields that should be added to reported logs. Can only be specified if VPC flow logs for this subnetwork is enabled and "metadata" is set to CUSTOM_METADATA. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#metadata_fields GoogleComputeSubnetwork#metadata_fields}
        '''
        value = GoogleComputeSubnetworkLogConfig(
            aggregation_interval=aggregation_interval,
            filter_expr=filter_expr,
            flow_sampling=flow_sampling,
            metadata=metadata,
            metadata_fields=metadata_fields,
        )

        return typing.cast(None, jsii.invoke(self, "putLogConfig", [value]))

    @jsii.member(jsii_name="putSecondaryIpRange")
    def put_secondary_ip_range(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleComputeSubnetworkSecondaryIpRange", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe6c6b14b8ba2dd51c9d40d983416bf9bb35d9886f27ccde949ef6d883361413)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSecondaryIpRange", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#create GoogleComputeSubnetwork#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#delete GoogleComputeSubnetwork#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#update GoogleComputeSubnetwork#update}.
        '''
        value = GoogleComputeSubnetworkTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIpv6AccessType")
    def reset_ipv6_access_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv6AccessType", []))

    @jsii.member(jsii_name="resetLogConfig")
    def reset_log_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogConfig", []))

    @jsii.member(jsii_name="resetPrivateIpGoogleAccess")
    def reset_private_ip_google_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateIpGoogleAccess", []))

    @jsii.member(jsii_name="resetPrivateIpv6GoogleAccess")
    def reset_private_ipv6_google_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateIpv6GoogleAccess", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetPurpose")
    def reset_purpose(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPurpose", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetRole")
    def reset_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRole", []))

    @jsii.member(jsii_name="resetSecondaryIpRange")
    def reset_secondary_ip_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecondaryIpRange", []))

    @jsii.member(jsii_name="resetStackType")
    def reset_stack_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStackType", []))

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
    @jsii.member(jsii_name="externalIpv6Prefix")
    def external_ipv6_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalIpv6Prefix"))

    @builtins.property
    @jsii.member(jsii_name="fingerprint")
    def fingerprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fingerprint"))

    @builtins.property
    @jsii.member(jsii_name="gatewayAddress")
    def gateway_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gatewayAddress"))

    @builtins.property
    @jsii.member(jsii_name="ipv6CidrRange")
    def ipv6_cidr_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipv6CidrRange"))

    @builtins.property
    @jsii.member(jsii_name="logConfig")
    def log_config(self) -> "GoogleComputeSubnetworkLogConfigOutputReference":
        return typing.cast("GoogleComputeSubnetworkLogConfigOutputReference", jsii.get(self, "logConfig"))

    @builtins.property
    @jsii.member(jsii_name="secondaryIpRange")
    def secondary_ip_range(self) -> "GoogleComputeSubnetworkSecondaryIpRangeList":
        return typing.cast("GoogleComputeSubnetworkSecondaryIpRangeList", jsii.get(self, "secondaryIpRange"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleComputeSubnetworkTimeoutsOutputReference":
        return typing.cast("GoogleComputeSubnetworkTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipCidrRangeInput")
    def ip_cidr_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipCidrRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv6AccessTypeInput")
    def ipv6_access_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipv6AccessTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="logConfigInput")
    def log_config_input(self) -> typing.Optional["GoogleComputeSubnetworkLogConfig"]:
        return typing.cast(typing.Optional["GoogleComputeSubnetworkLogConfig"], jsii.get(self, "logConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpGoogleAccessInput")
    def private_ip_google_access_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "privateIpGoogleAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpv6GoogleAccessInput")
    def private_ipv6_google_access_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateIpv6GoogleAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="purposeInput")
    def purpose_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "purposeInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="secondaryIpRangeInput")
    def secondary_ip_range_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleComputeSubnetworkSecondaryIpRange"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleComputeSubnetworkSecondaryIpRange"]]], jsii.get(self, "secondaryIpRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="stackTypeInput")
    def stack_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stackTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleComputeSubnetworkTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleComputeSubnetworkTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f72ae70a4f18794ead2a169c0b75ed75c5cfb403a175e33a16d520b5d481a8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a5e64c3b5d7bfe323deb9fba25479614e83cd60146f6116faeef78bffae8ea3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ipCidrRange")
    def ip_cidr_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipCidrRange"))

    @ip_cidr_range.setter
    def ip_cidr_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f6ab889de10b13b40bcbeb39b423a3f59295c461a4e72b36260fb4e509604de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipCidrRange", value)

    @builtins.property
    @jsii.member(jsii_name="ipv6AccessType")
    def ipv6_access_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipv6AccessType"))

    @ipv6_access_type.setter
    def ipv6_access_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d4b70825c7f90b057cffe25b6fd40d2de58deffbbcc32db60053dd529485bde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6AccessType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b3f4d4b5d081e2b8eb9e9708ed6fa83cf5d23e3a78b567de172fd86fe3bbaaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @network.setter
    def network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80078676d805c96993b70a704c9e4e92d02239805ae3ad3730eafa7c847d7e66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "network", value)

    @builtins.property
    @jsii.member(jsii_name="privateIpGoogleAccess")
    def private_ip_google_access(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "privateIpGoogleAccess"))

    @private_ip_google_access.setter
    def private_ip_google_access(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1eeeca86bcaf77b744e79ebab0757f8b1145035beb77dafa5d35077c33f01af0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIpGoogleAccess", value)

    @builtins.property
    @jsii.member(jsii_name="privateIpv6GoogleAccess")
    def private_ipv6_google_access(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIpv6GoogleAccess"))

    @private_ipv6_google_access.setter
    def private_ipv6_google_access(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5621ea0d6b532984da9956a79c9a543c7306ac51db7b968795915bf9f58abde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIpv6GoogleAccess", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c66078c6339c05d8d82fe085a0176cd777657b049da37e93470c82a6347472a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="purpose")
    def purpose(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "purpose"))

    @purpose.setter
    def purpose(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd4376966a33a93530a12428cf38ebbe0eff5d8754bfe1ac610128d89255f379)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "purpose", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__014ba8b5b8cb9a4d3761ef6573813d7dc71dc27e6d14191b259c0089ceab138a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0103f6f6f9292360f15f87ee55b54a61ebf9c7769b26a89c89534632a0d1a81c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)

    @builtins.property
    @jsii.member(jsii_name="stackType")
    def stack_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stackType"))

    @stack_type.setter
    def stack_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__653932d77e90f2754fdf6376d75cfbda4d3a61c0487f7b0c7a3606706ab23a81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stackType", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeSubnetwork.GoogleComputeSubnetworkConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "ip_cidr_range": "ipCidrRange",
        "name": "name",
        "network": "network",
        "description": "description",
        "id": "id",
        "ipv6_access_type": "ipv6AccessType",
        "log_config": "logConfig",
        "private_ip_google_access": "privateIpGoogleAccess",
        "private_ipv6_google_access": "privateIpv6GoogleAccess",
        "project": "project",
        "purpose": "purpose",
        "region": "region",
        "role": "role",
        "secondary_ip_range": "secondaryIpRange",
        "stack_type": "stackType",
        "timeouts": "timeouts",
    },
)
class GoogleComputeSubnetworkConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        ip_cidr_range: builtins.str,
        name: builtins.str,
        network: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ipv6_access_type: typing.Optional[builtins.str] = None,
        log_config: typing.Optional[typing.Union["GoogleComputeSubnetworkLogConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        private_ip_google_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        private_ipv6_google_access: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        purpose: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        role: typing.Optional[builtins.str] = None,
        secondary_ip_range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleComputeSubnetworkSecondaryIpRange", typing.Dict[builtins.str, typing.Any]]]]] = None,
        stack_type: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeSubnetworkTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param ip_cidr_range: The range of internal addresses that are owned by this subnetwork. Provide this property when you create the subnetwork. For example, 10.0.0.0/8 or 192.168.0.0/16. Ranges must be unique and non-overlapping within a network. Only IPv4 is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#ip_cidr_range GoogleComputeSubnetwork#ip_cidr_range}
        :param name: The name of the resource, provided by the client when initially creating the resource. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#name GoogleComputeSubnetwork#name}
        :param network: The network this subnet belongs to. Only networks that are in the distributed mode can have subnetworks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#network GoogleComputeSubnetwork#network}
        :param description: An optional description of this resource. Provide this property when you create the resource. This field can be set only at resource creation time. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#description GoogleComputeSubnetwork#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#id GoogleComputeSubnetwork#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ipv6_access_type: The access type of IPv6 address this subnet holds. It's immutable and can only be specified during creation or the first time the subnet is updated into IPV4_IPV6 dual stack. If the ipv6_type is EXTERNAL then this subnet cannot enable direct path. Possible values: ["EXTERNAL", "INTERNAL"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#ipv6_access_type GoogleComputeSubnetwork#ipv6_access_type}
        :param log_config: log_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#log_config GoogleComputeSubnetwork#log_config}
        :param private_ip_google_access: When enabled, VMs in this subnetwork without external IP addresses can access Google APIs and services by using Private Google Access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#private_ip_google_access GoogleComputeSubnetwork#private_ip_google_access}
        :param private_ipv6_google_access: The private IPv6 google access type for the VMs in this subnet. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#private_ipv6_google_access GoogleComputeSubnetwork#private_ipv6_google_access}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#project GoogleComputeSubnetwork#project}.
        :param purpose: The purpose of the resource. A subnetwork with purpose set to INTERNAL_HTTPS_LOAD_BALANCER is a user-created subnetwork that is reserved for Internal HTTP(S) Load Balancing. If set to INTERNAL_HTTPS_LOAD_BALANCER you must also set the 'role' field. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#purpose GoogleComputeSubnetwork#purpose}
        :param region: The GCP region for this subnetwork. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#region GoogleComputeSubnetwork#region}
        :param role: The role of subnetwork. Currently, this field is only used when purpose = INTERNAL_HTTPS_LOAD_BALANCER. The value can be set to ACTIVE or BACKUP. An ACTIVE subnetwork is one that is currently being used for Internal HTTP(S) Load Balancing. A BACKUP subnetwork is one that is ready to be promoted to ACTIVE or is currently draining. Possible values: ["ACTIVE", "BACKUP"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#role GoogleComputeSubnetwork#role}
        :param secondary_ip_range: An array of configurations for secondary IP ranges for VM instances contained in this subnetwork. The primary IP of such VM must belong to the primary ipCidrRange of the subnetwork. The alias IPs may belong to either primary or secondary ranges. *Note**: This field uses `attr-as-block mode <https://www.terraform.io/docs/configuration/attr-as-blocks.html>`_ to avoid breaking users during the 0.12 upgrade. To explicitly send a list of zero objects you must use the following syntax: 'example=[]' For more details about this behavior, see `this section <https://www.terraform.io/docs/configuration/attr-as-blocks.html#defining-a-fixed-object-collection-value>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#secondary_ip_range GoogleComputeSubnetwork#secondary_ip_range}
        :param stack_type: The stack type for this subnet to identify whether the IPv6 feature is enabled or not. If not specified IPV4_ONLY will be used. Possible values: ["IPV4_ONLY", "IPV4_IPV6"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#stack_type GoogleComputeSubnetwork#stack_type}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#timeouts GoogleComputeSubnetwork#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(log_config, dict):
            log_config = GoogleComputeSubnetworkLogConfig(**log_config)
        if isinstance(timeouts, dict):
            timeouts = GoogleComputeSubnetworkTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__845f5e103c79cbe7a01bd75482955102898db4ee47798b11fed7e90ba767e73b)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument ip_cidr_range", value=ip_cidr_range, expected_type=type_hints["ip_cidr_range"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ipv6_access_type", value=ipv6_access_type, expected_type=type_hints["ipv6_access_type"])
            check_type(argname="argument log_config", value=log_config, expected_type=type_hints["log_config"])
            check_type(argname="argument private_ip_google_access", value=private_ip_google_access, expected_type=type_hints["private_ip_google_access"])
            check_type(argname="argument private_ipv6_google_access", value=private_ipv6_google_access, expected_type=type_hints["private_ipv6_google_access"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument purpose", value=purpose, expected_type=type_hints["purpose"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument secondary_ip_range", value=secondary_ip_range, expected_type=type_hints["secondary_ip_range"])
            check_type(argname="argument stack_type", value=stack_type, expected_type=type_hints["stack_type"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ip_cidr_range": ip_cidr_range,
            "name": name,
            "network": network,
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
        if ipv6_access_type is not None:
            self._values["ipv6_access_type"] = ipv6_access_type
        if log_config is not None:
            self._values["log_config"] = log_config
        if private_ip_google_access is not None:
            self._values["private_ip_google_access"] = private_ip_google_access
        if private_ipv6_google_access is not None:
            self._values["private_ipv6_google_access"] = private_ipv6_google_access
        if project is not None:
            self._values["project"] = project
        if purpose is not None:
            self._values["purpose"] = purpose
        if region is not None:
            self._values["region"] = region
        if role is not None:
            self._values["role"] = role
        if secondary_ip_range is not None:
            self._values["secondary_ip_range"] = secondary_ip_range
        if stack_type is not None:
            self._values["stack_type"] = stack_type
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
    def ip_cidr_range(self) -> builtins.str:
        '''The range of internal addresses that are owned by this subnetwork.

        Provide this property when you create the subnetwork. For example,
        10.0.0.0/8 or 192.168.0.0/16. Ranges must be unique and
        non-overlapping within a network. Only IPv4 is supported.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#ip_cidr_range GoogleComputeSubnetwork#ip_cidr_range}
        '''
        result = self._values.get("ip_cidr_range")
        assert result is not None, "Required property 'ip_cidr_range' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the resource, provided by the client when initially creating the resource.

        The name must be 1-63 characters long, and
        comply with RFC1035. Specifically, the name must be 1-63 characters
        long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which
        means the first character must be a lowercase letter, and all
        following characters must be a dash, lowercase letter, or digit,
        except the last character, which cannot be a dash.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#name GoogleComputeSubnetwork#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network(self) -> builtins.str:
        '''The network this subnet belongs to. Only networks that are in the distributed mode can have subnetworks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#network GoogleComputeSubnetwork#network}
        '''
        result = self._values.get("network")
        assert result is not None, "Required property 'network' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of this resource.

        Provide this property when
        you create the resource. This field can be set only at resource
        creation time.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#description GoogleComputeSubnetwork#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#id GoogleComputeSubnetwork#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ipv6_access_type(self) -> typing.Optional[builtins.str]:
        '''The access type of IPv6 address this subnet holds.

        It's immutable and can only be specified during creation
        or the first time the subnet is updated into IPV4_IPV6 dual stack. If the ipv6_type is EXTERNAL then this subnet
        cannot enable direct path. Possible values: ["EXTERNAL", "INTERNAL"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#ipv6_access_type GoogleComputeSubnetwork#ipv6_access_type}
        '''
        result = self._values.get("ipv6_access_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_config(self) -> typing.Optional["GoogleComputeSubnetworkLogConfig"]:
        '''log_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#log_config GoogleComputeSubnetwork#log_config}
        '''
        result = self._values.get("log_config")
        return typing.cast(typing.Optional["GoogleComputeSubnetworkLogConfig"], result)

    @builtins.property
    def private_ip_google_access(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''When enabled, VMs in this subnetwork without external IP addresses can access Google APIs and services by using Private Google Access.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#private_ip_google_access GoogleComputeSubnetwork#private_ip_google_access}
        '''
        result = self._values.get("private_ip_google_access")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def private_ipv6_google_access(self) -> typing.Optional[builtins.str]:
        '''The private IPv6 google access type for the VMs in this subnet.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#private_ipv6_google_access GoogleComputeSubnetwork#private_ipv6_google_access}
        '''
        result = self._values.get("private_ipv6_google_access")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#project GoogleComputeSubnetwork#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def purpose(self) -> typing.Optional[builtins.str]:
        '''The purpose of the resource.

        A subnetwork with purpose set to
        INTERNAL_HTTPS_LOAD_BALANCER is a user-created subnetwork that is
        reserved for Internal HTTP(S) Load Balancing.

        If set to INTERNAL_HTTPS_LOAD_BALANCER you must also set the 'role' field.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#purpose GoogleComputeSubnetwork#purpose}
        '''
        result = self._values.get("purpose")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The GCP region for this subnetwork.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#region GoogleComputeSubnetwork#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[builtins.str]:
        '''The role of subnetwork.

        Currently, this field is only used when
        purpose = INTERNAL_HTTPS_LOAD_BALANCER. The value can be set to ACTIVE
        or BACKUP. An ACTIVE subnetwork is one that is currently being used
        for Internal HTTP(S) Load Balancing. A BACKUP subnetwork is one that
        is ready to be promoted to ACTIVE or is currently draining. Possible values: ["ACTIVE", "BACKUP"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#role GoogleComputeSubnetwork#role}
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secondary_ip_range(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleComputeSubnetworkSecondaryIpRange"]]]:
        '''An array of configurations for secondary IP ranges for VM instances contained in this subnetwork.

        The primary IP of such VM must belong
        to the primary ipCidrRange of the subnetwork. The alias IPs may belong
        to either primary or secondary ranges.

        *Note**: This field uses `attr-as-block mode <https://www.terraform.io/docs/configuration/attr-as-blocks.html>`_ to avoid
        breaking users during the 0.12 upgrade. To explicitly send a list
        of zero objects you must use the following syntax:
        'example=[]'
        For more details about this behavior, see `this section <https://www.terraform.io/docs/configuration/attr-as-blocks.html#defining-a-fixed-object-collection-value>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#secondary_ip_range GoogleComputeSubnetwork#secondary_ip_range}
        '''
        result = self._values.get("secondary_ip_range")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleComputeSubnetworkSecondaryIpRange"]]], result)

    @builtins.property
    def stack_type(self) -> typing.Optional[builtins.str]:
        '''The stack type for this subnet to identify whether the IPv6 feature is enabled or not.

        If not specified IPV4_ONLY will be used. Possible values: ["IPV4_ONLY", "IPV4_IPV6"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#stack_type GoogleComputeSubnetwork#stack_type}
        '''
        result = self._values.get("stack_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleComputeSubnetworkTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#timeouts GoogleComputeSubnetwork#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleComputeSubnetworkTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeSubnetworkConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeSubnetwork.GoogleComputeSubnetworkLogConfig",
    jsii_struct_bases=[],
    name_mapping={
        "aggregation_interval": "aggregationInterval",
        "filter_expr": "filterExpr",
        "flow_sampling": "flowSampling",
        "metadata": "metadata",
        "metadata_fields": "metadataFields",
    },
)
class GoogleComputeSubnetworkLogConfig:
    def __init__(
        self,
        *,
        aggregation_interval: typing.Optional[builtins.str] = None,
        filter_expr: typing.Optional[builtins.str] = None,
        flow_sampling: typing.Optional[jsii.Number] = None,
        metadata: typing.Optional[builtins.str] = None,
        metadata_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param aggregation_interval: Can only be specified if VPC flow logging for this subnetwork is enabled. Toggles the aggregation interval for collecting flow logs. Increasing the interval time will reduce the amount of generated flow logs for long lasting connections. Default is an interval of 5 seconds per connection. Default value: "INTERVAL_5_SEC" Possible values: ["INTERVAL_5_SEC", "INTERVAL_30_SEC", "INTERVAL_1_MIN", "INTERVAL_5_MIN", "INTERVAL_10_MIN", "INTERVAL_15_MIN"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#aggregation_interval GoogleComputeSubnetwork#aggregation_interval}
        :param filter_expr: Export filter used to define which VPC flow logs should be logged, as as CEL expression. See https://cloud.google.com/vpc/docs/flow-logs#filtering for details on how to format this field. The default value is 'true', which evaluates to include everything. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#filter_expr GoogleComputeSubnetwork#filter_expr}
        :param flow_sampling: Can only be specified if VPC flow logging for this subnetwork is enabled. The value of the field must be in [0, 1]. Set the sampling rate of VPC flow logs within the subnetwork where 1.0 means all collected logs are reported and 0.0 means no logs are reported. Default is 0.5 which means half of all collected logs are reported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#flow_sampling GoogleComputeSubnetwork#flow_sampling}
        :param metadata: Can only be specified if VPC flow logging for this subnetwork is enabled. Configures whether metadata fields should be added to the reported VPC flow logs. Default value: "INCLUDE_ALL_METADATA" Possible values: ["EXCLUDE_ALL_METADATA", "INCLUDE_ALL_METADATA", "CUSTOM_METADATA"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#metadata GoogleComputeSubnetwork#metadata}
        :param metadata_fields: List of metadata fields that should be added to reported logs. Can only be specified if VPC flow logs for this subnetwork is enabled and "metadata" is set to CUSTOM_METADATA. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#metadata_fields GoogleComputeSubnetwork#metadata_fields}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cefebab1ada692c167082a0e8caa8d11191cbb0d9e4efbe2066341df07c98d04)
            check_type(argname="argument aggregation_interval", value=aggregation_interval, expected_type=type_hints["aggregation_interval"])
            check_type(argname="argument filter_expr", value=filter_expr, expected_type=type_hints["filter_expr"])
            check_type(argname="argument flow_sampling", value=flow_sampling, expected_type=type_hints["flow_sampling"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument metadata_fields", value=metadata_fields, expected_type=type_hints["metadata_fields"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aggregation_interval is not None:
            self._values["aggregation_interval"] = aggregation_interval
        if filter_expr is not None:
            self._values["filter_expr"] = filter_expr
        if flow_sampling is not None:
            self._values["flow_sampling"] = flow_sampling
        if metadata is not None:
            self._values["metadata"] = metadata
        if metadata_fields is not None:
            self._values["metadata_fields"] = metadata_fields

    @builtins.property
    def aggregation_interval(self) -> typing.Optional[builtins.str]:
        '''Can only be specified if VPC flow logging for this subnetwork is enabled.

        Toggles the aggregation interval for collecting flow logs. Increasing the
        interval time will reduce the amount of generated flow logs for long
        lasting connections. Default is an interval of 5 seconds per connection. Default value: "INTERVAL_5_SEC" Possible values: ["INTERVAL_5_SEC", "INTERVAL_30_SEC", "INTERVAL_1_MIN", "INTERVAL_5_MIN", "INTERVAL_10_MIN", "INTERVAL_15_MIN"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#aggregation_interval GoogleComputeSubnetwork#aggregation_interval}
        '''
        result = self._values.get("aggregation_interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def filter_expr(self) -> typing.Optional[builtins.str]:
        '''Export filter used to define which VPC flow logs should be logged, as as CEL expression.

        See
        https://cloud.google.com/vpc/docs/flow-logs#filtering for details on how to format this field.
        The default value is 'true', which evaluates to include everything.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#filter_expr GoogleComputeSubnetwork#filter_expr}
        '''
        result = self._values.get("filter_expr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def flow_sampling(self) -> typing.Optional[jsii.Number]:
        '''Can only be specified if VPC flow logging for this subnetwork is enabled.

        The value of the field must be in [0, 1]. Set the sampling rate of VPC
        flow logs within the subnetwork where 1.0 means all collected logs are
        reported and 0.0 means no logs are reported. Default is 0.5 which means
        half of all collected logs are reported.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#flow_sampling GoogleComputeSubnetwork#flow_sampling}
        '''
        result = self._values.get("flow_sampling")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def metadata(self) -> typing.Optional[builtins.str]:
        '''Can only be specified if VPC flow logging for this subnetwork is enabled.

        Configures whether metadata fields should be added to the reported VPC
        flow logs. Default value: "INCLUDE_ALL_METADATA" Possible values: ["EXCLUDE_ALL_METADATA", "INCLUDE_ALL_METADATA", "CUSTOM_METADATA"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#metadata GoogleComputeSubnetwork#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metadata_fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of metadata fields that should be added to reported logs.

        Can only be specified if VPC flow logs for this subnetwork is enabled and "metadata" is set to CUSTOM_METADATA.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#metadata_fields GoogleComputeSubnetwork#metadata_fields}
        '''
        result = self._values.get("metadata_fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeSubnetworkLogConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeSubnetworkLogConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeSubnetwork.GoogleComputeSubnetworkLogConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__10e546fe44ae7c510e0f80815a1204590eed93b53c55ceb0b7c3314b95d005e9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAggregationInterval")
    def reset_aggregation_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAggregationInterval", []))

    @jsii.member(jsii_name="resetFilterExpr")
    def reset_filter_expr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilterExpr", []))

    @jsii.member(jsii_name="resetFlowSampling")
    def reset_flow_sampling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFlowSampling", []))

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

    @jsii.member(jsii_name="resetMetadataFields")
    def reset_metadata_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadataFields", []))

    @builtins.property
    @jsii.member(jsii_name="aggregationIntervalInput")
    def aggregation_interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aggregationIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="filterExprInput")
    def filter_expr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filterExprInput"))

    @builtins.property
    @jsii.member(jsii_name="flowSamplingInput")
    def flow_sampling_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "flowSamplingInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataFieldsInput")
    def metadata_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "metadataFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="aggregationInterval")
    def aggregation_interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aggregationInterval"))

    @aggregation_interval.setter
    def aggregation_interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b75fd07ef44aa167cfe2b4995a374e13ecd1bd0f8e8a1017321d701a148ae440)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aggregationInterval", value)

    @builtins.property
    @jsii.member(jsii_name="filterExpr")
    def filter_expr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filterExpr"))

    @filter_expr.setter
    def filter_expr(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67b60b4d17c0cd3d83f6ce4d856200ba69a16db4ffd1603daadb8dc3e4cec0e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterExpr", value)

    @builtins.property
    @jsii.member(jsii_name="flowSampling")
    def flow_sampling(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "flowSampling"))

    @flow_sampling.setter
    def flow_sampling(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d07d35349b2367130597de140355689b694f46789daaac6930128b7c71a4fa3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowSampling", value)

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de51b0d3d98750e06f51d9fd08f5b52ba7570f50b3a5e3af7ed7815f8a4a6fdb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="metadataFields")
    def metadata_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "metadataFields"))

    @metadata_fields.setter
    def metadata_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dd52444274e1a46ea44e3e64236b4cbfc2cbf8c4d9ae5aadaea9f519eb146ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadataFields", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleComputeSubnetworkLogConfig]:
        return typing.cast(typing.Optional[GoogleComputeSubnetworkLogConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeSubnetworkLogConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67a5565f5522d8f40e74f1d2fe815d4515bb64a00a1c180897771610c45f05f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeSubnetwork.GoogleComputeSubnetworkSecondaryIpRange",
    jsii_struct_bases=[],
    name_mapping={"ip_cidr_range": "ipCidrRange", "range_name": "rangeName"},
)
class GoogleComputeSubnetworkSecondaryIpRange:
    def __init__(
        self,
        *,
        ip_cidr_range: typing.Optional[builtins.str] = None,
        range_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ip_cidr_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#ip_cidr_range GoogleComputeSubnetwork#ip_cidr_range}.
        :param range_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#range_name GoogleComputeSubnetwork#range_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe219973ff60a2174a52378b9123754084bd1918fecf1c69d7d4c7cd2944df01)
            check_type(argname="argument ip_cidr_range", value=ip_cidr_range, expected_type=type_hints["ip_cidr_range"])
            check_type(argname="argument range_name", value=range_name, expected_type=type_hints["range_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ip_cidr_range is not None:
            self._values["ip_cidr_range"] = ip_cidr_range
        if range_name is not None:
            self._values["range_name"] = range_name

    @builtins.property
    def ip_cidr_range(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#ip_cidr_range GoogleComputeSubnetwork#ip_cidr_range}.'''
        result = self._values.get("ip_cidr_range")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def range_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#range_name GoogleComputeSubnetwork#range_name}.'''
        result = self._values.get("range_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeSubnetworkSecondaryIpRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeSubnetworkSecondaryIpRangeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeSubnetwork.GoogleComputeSubnetworkSecondaryIpRangeList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__387dfca7d248e2b50d5484f60efa3980245726811b1a1309b813fd331e239b58)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeSubnetworkSecondaryIpRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7942345aa57e88bfe55c4c190adbc393751cdb753ea7dc11126cfbdde98f959)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeSubnetworkSecondaryIpRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4cff7e3fc0e052ebbc3d19ced4350a97d2dbfd478689f359f00de2f80795a65)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2b9cbcd4a90de5d835c5ffa41b3213d375e5026ae30a9b7765fa933f1819ce16)
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
            type_hints = typing.get_type_hints(_typecheckingstub__85ee0ba094e582927b7f6f74f939686b277fe284b64bb1020475270c225159a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputeSubnetworkSecondaryIpRange]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputeSubnetworkSecondaryIpRange]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputeSubnetworkSecondaryIpRange]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b63e7567acb202d35704bbb3bb6430a664e8164ff5d82f66eb12cb2ff5b69e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeSubnetworkSecondaryIpRangeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeSubnetwork.GoogleComputeSubnetworkSecondaryIpRangeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__210ee7e4b980d1fb810fb573b5cc106f89fa0a4a3790c9e8a02ac5fd38455269)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIpCidrRange")
    def reset_ip_cidr_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpCidrRange", []))

    @jsii.member(jsii_name="resetRangeName")
    def reset_range_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRangeName", []))

    @builtins.property
    @jsii.member(jsii_name="ipCidrRangeInput")
    def ip_cidr_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipCidrRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeNameInput")
    def range_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rangeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="ipCidrRange")
    def ip_cidr_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipCidrRange"))

    @ip_cidr_range.setter
    def ip_cidr_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6db9b77decb40e1b184378d5df2ee13a6312894b86e25335b57c6691f7d490ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipCidrRange", value)

    @builtins.property
    @jsii.member(jsii_name="rangeName")
    def range_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rangeName"))

    @range_name.setter
    def range_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2cebe2844c13c669aeca94b51d67a0e684dede3f19e7c9789f0275056f7e0bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rangeName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeSubnetworkSecondaryIpRange, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeSubnetworkSecondaryIpRange, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeSubnetworkSecondaryIpRange, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a18ed5c26ee6a4a95bedc0e0076e46377d63819b62b12a0c6b1d486a66b8cf76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeSubnetwork.GoogleComputeSubnetworkTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleComputeSubnetworkTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#create GoogleComputeSubnetwork#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#delete GoogleComputeSubnetwork#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#update GoogleComputeSubnetwork#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e746b7ac9135c8c217f38c1b35d89e997c5146dcb495c9a7c6992c01e886b33)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#create GoogleComputeSubnetwork#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#delete GoogleComputeSubnetwork#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_subnetwork#update GoogleComputeSubnetwork#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeSubnetworkTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeSubnetworkTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeSubnetwork.GoogleComputeSubnetworkTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f029ea5f6f75800d1610862cf7a16ebc5ae9dc44f51f5709d602589e737510d6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e9cb8f0a991d7931ad1cc3b4650c1a5eb34f45e771ec30f4e15063b5dd82deeb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2a7efa36e4062c64c613cb91da52126a99cfaf2e4f67ce23daaef5f611ddefe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fe7d8efe0f5ad3bc06cec182eb336771ac02f745f042f195f7da48b394f3b2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeSubnetworkTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeSubnetworkTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeSubnetworkTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37eaeace23fa98c0ffe6bea3759a9cff09c23de79f77fd0390882e6e57c81416)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleComputeSubnetwork",
    "GoogleComputeSubnetworkConfig",
    "GoogleComputeSubnetworkLogConfig",
    "GoogleComputeSubnetworkLogConfigOutputReference",
    "GoogleComputeSubnetworkSecondaryIpRange",
    "GoogleComputeSubnetworkSecondaryIpRangeList",
    "GoogleComputeSubnetworkSecondaryIpRangeOutputReference",
    "GoogleComputeSubnetworkTimeouts",
    "GoogleComputeSubnetworkTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__fa2e0719972ae42ff6668cc201c87b78c5aad82b2d6be09df14ab5cc3cd06b39(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    ip_cidr_range: builtins.str,
    name: builtins.str,
    network: builtins.str,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    ipv6_access_type: typing.Optional[builtins.str] = None,
    log_config: typing.Optional[typing.Union[GoogleComputeSubnetworkLogConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    private_ip_google_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    private_ipv6_google_access: typing.Optional[builtins.str] = None,
    project: typing.Optional[builtins.str] = None,
    purpose: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    role: typing.Optional[builtins.str] = None,
    secondary_ip_range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleComputeSubnetworkSecondaryIpRange, typing.Dict[builtins.str, typing.Any]]]]] = None,
    stack_type: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[GoogleComputeSubnetworkTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__fe6c6b14b8ba2dd51c9d40d983416bf9bb35d9886f27ccde949ef6d883361413(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleComputeSubnetworkSecondaryIpRange, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f72ae70a4f18794ead2a169c0b75ed75c5cfb403a175e33a16d520b5d481a8e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a5e64c3b5d7bfe323deb9fba25479614e83cd60146f6116faeef78bffae8ea3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f6ab889de10b13b40bcbeb39b423a3f59295c461a4e72b36260fb4e509604de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d4b70825c7f90b057cffe25b6fd40d2de58deffbbcc32db60053dd529485bde(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b3f4d4b5d081e2b8eb9e9708ed6fa83cf5d23e3a78b567de172fd86fe3bbaaf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80078676d805c96993b70a704c9e4e92d02239805ae3ad3730eafa7c847d7e66(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1eeeca86bcaf77b744e79ebab0757f8b1145035beb77dafa5d35077c33f01af0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5621ea0d6b532984da9956a79c9a543c7306ac51db7b968795915bf9f58abde(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c66078c6339c05d8d82fe085a0176cd777657b049da37e93470c82a6347472a2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd4376966a33a93530a12428cf38ebbe0eff5d8754bfe1ac610128d89255f379(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__014ba8b5b8cb9a4d3761ef6573813d7dc71dc27e6d14191b259c0089ceab138a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0103f6f6f9292360f15f87ee55b54a61ebf9c7769b26a89c89534632a0d1a81c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__653932d77e90f2754fdf6376d75cfbda4d3a61c0487f7b0c7a3606706ab23a81(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__845f5e103c79cbe7a01bd75482955102898db4ee47798b11fed7e90ba767e73b(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ip_cidr_range: builtins.str,
    name: builtins.str,
    network: builtins.str,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    ipv6_access_type: typing.Optional[builtins.str] = None,
    log_config: typing.Optional[typing.Union[GoogleComputeSubnetworkLogConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    private_ip_google_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    private_ipv6_google_access: typing.Optional[builtins.str] = None,
    project: typing.Optional[builtins.str] = None,
    purpose: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    role: typing.Optional[builtins.str] = None,
    secondary_ip_range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleComputeSubnetworkSecondaryIpRange, typing.Dict[builtins.str, typing.Any]]]]] = None,
    stack_type: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[GoogleComputeSubnetworkTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cefebab1ada692c167082a0e8caa8d11191cbb0d9e4efbe2066341df07c98d04(
    *,
    aggregation_interval: typing.Optional[builtins.str] = None,
    filter_expr: typing.Optional[builtins.str] = None,
    flow_sampling: typing.Optional[jsii.Number] = None,
    metadata: typing.Optional[builtins.str] = None,
    metadata_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10e546fe44ae7c510e0f80815a1204590eed93b53c55ceb0b7c3314b95d005e9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b75fd07ef44aa167cfe2b4995a374e13ecd1bd0f8e8a1017321d701a148ae440(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67b60b4d17c0cd3d83f6ce4d856200ba69a16db4ffd1603daadb8dc3e4cec0e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d07d35349b2367130597de140355689b694f46789daaac6930128b7c71a4fa3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de51b0d3d98750e06f51d9fd08f5b52ba7570f50b3a5e3af7ed7815f8a4a6fdb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dd52444274e1a46ea44e3e64236b4cbfc2cbf8c4d9ae5aadaea9f519eb146ab(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67a5565f5522d8f40e74f1d2fe815d4515bb64a00a1c180897771610c45f05f2(
    value: typing.Optional[GoogleComputeSubnetworkLogConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe219973ff60a2174a52378b9123754084bd1918fecf1c69d7d4c7cd2944df01(
    *,
    ip_cidr_range: typing.Optional[builtins.str] = None,
    range_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__387dfca7d248e2b50d5484f60efa3980245726811b1a1309b813fd331e239b58(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7942345aa57e88bfe55c4c190adbc393751cdb753ea7dc11126cfbdde98f959(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4cff7e3fc0e052ebbc3d19ced4350a97d2dbfd478689f359f00de2f80795a65(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b9cbcd4a90de5d835c5ffa41b3213d375e5026ae30a9b7765fa933f1819ce16(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85ee0ba094e582927b7f6f74f939686b277fe284b64bb1020475270c225159a5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b63e7567acb202d35704bbb3bb6430a664e8164ff5d82f66eb12cb2ff5b69e3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputeSubnetworkSecondaryIpRange]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__210ee7e4b980d1fb810fb573b5cc106f89fa0a4a3790c9e8a02ac5fd38455269(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6db9b77decb40e1b184378d5df2ee13a6312894b86e25335b57c6691f7d490ef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2cebe2844c13c669aeca94b51d67a0e684dede3f19e7c9789f0275056f7e0bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a18ed5c26ee6a4a95bedc0e0076e46377d63819b62b12a0c6b1d486a66b8cf76(
    value: typing.Optional[typing.Union[GoogleComputeSubnetworkSecondaryIpRange, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e746b7ac9135c8c217f38c1b35d89e997c5146dcb495c9a7c6992c01e886b33(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f029ea5f6f75800d1610862cf7a16ebc5ae9dc44f51f5709d602589e737510d6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9cb8f0a991d7931ad1cc3b4650c1a5eb34f45e771ec30f4e15063b5dd82deeb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2a7efa36e4062c64c613cb91da52126a99cfaf2e4f67ce23daaef5f611ddefe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fe7d8efe0f5ad3bc06cec182eb336771ac02f745f042f195f7da48b394f3b2c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37eaeace23fa98c0ffe6bea3759a9cff09c23de79f77fd0390882e6e57c81416(
    value: typing.Optional[typing.Union[GoogleComputeSubnetworkTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
