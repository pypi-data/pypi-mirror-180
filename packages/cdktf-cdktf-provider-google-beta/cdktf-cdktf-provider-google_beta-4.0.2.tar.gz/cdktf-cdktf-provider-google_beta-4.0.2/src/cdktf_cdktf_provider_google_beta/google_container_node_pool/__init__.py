'''
# `google_container_node_pool`

Refer to the Terraform Registory for docs: [`google_container_node_pool`](https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool).
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


class GoogleContainerNodePool(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePool",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool google_container_node_pool}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        cluster: builtins.str,
        autoscaling: typing.Optional[typing.Union["GoogleContainerNodePoolAutoscaling", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        initial_node_count: typing.Optional[jsii.Number] = None,
        location: typing.Optional[builtins.str] = None,
        management: typing.Optional[typing.Union["GoogleContainerNodePoolManagement", typing.Dict[builtins.str, typing.Any]]] = None,
        max_pods_per_node: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        network_config: typing.Optional[typing.Union["GoogleContainerNodePoolNetworkConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        node_config: typing.Optional[typing.Union["GoogleContainerNodePoolNodeConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        node_count: typing.Optional[jsii.Number] = None,
        node_locations: typing.Optional[typing.Sequence[builtins.str]] = None,
        placement_policy: typing.Optional[typing.Union["GoogleContainerNodePoolPlacementPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleContainerNodePoolTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        upgrade_settings: typing.Optional[typing.Union["GoogleContainerNodePoolUpgradeSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        version: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool google_container_node_pool} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cluster: The cluster to create the node pool for. Cluster must be present in location provided for zonal clusters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#cluster GoogleContainerNodePool#cluster}
        :param autoscaling: autoscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#autoscaling GoogleContainerNodePool#autoscaling}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#id GoogleContainerNodePool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initial_node_count: The initial number of nodes for the pool. In regional or multi-zonal clusters, this is the number of nodes per zone. Changing this will force recreation of the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#initial_node_count GoogleContainerNodePool#initial_node_count}
        :param location: The location (region or zone) of the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#location GoogleContainerNodePool#location}
        :param management: management block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#management GoogleContainerNodePool#management}
        :param max_pods_per_node: The maximum number of pods per node in this node pool. Note that this does not work on node pools which are "route-based" - that is, node pools belonging to clusters that do not have IP Aliasing enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#max_pods_per_node GoogleContainerNodePool#max_pods_per_node}
        :param name: The name of the node pool. If left blank, Terraform will auto-generate a unique name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#name GoogleContainerNodePool#name}
        :param name_prefix: Creates a unique name for the node pool beginning with the specified prefix. Conflicts with name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#name_prefix GoogleContainerNodePool#name_prefix}
        :param network_config: network_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#network_config GoogleContainerNodePool#network_config}
        :param node_config: node_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#node_config GoogleContainerNodePool#node_config}
        :param node_count: The number of nodes per instance group. This field can be used to update the number of nodes per instance group but should not be used alongside autoscaling. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#node_count GoogleContainerNodePool#node_count}
        :param node_locations: The list of zones in which the node pool's nodes should be located. Nodes must be in the region of their regional cluster or in the same region as their cluster's zone for zonal clusters. If unspecified, the cluster-level node_locations will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#node_locations GoogleContainerNodePool#node_locations}
        :param placement_policy: placement_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#placement_policy GoogleContainerNodePool#placement_policy}
        :param project: The ID of the project in which to create the node pool. If blank, the provider-configured project will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#project GoogleContainerNodePool#project}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#timeouts GoogleContainerNodePool#timeouts}
        :param upgrade_settings: upgrade_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#upgrade_settings GoogleContainerNodePool#upgrade_settings}
        :param version: The Kubernetes version for the nodes in this pool. Note that if this field and auto_upgrade are both specified, they will fight each other for what the node version should be, so setting both is highly discouraged. While a fuzzy version can be specified, it's recommended that you specify explicit versions as Terraform will see spurious diffs when fuzzy versions are used. See the google_container_engine_versions data source's version_prefix field to approximate fuzzy versions in a Terraform-compatible way. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#version GoogleContainerNodePool#version}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f75cf1f4c113470aebc6bebc3ac0bd156d49a6d1cd6f50e192de6ed4291c711f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleContainerNodePoolConfig(
            cluster=cluster,
            autoscaling=autoscaling,
            id=id,
            initial_node_count=initial_node_count,
            location=location,
            management=management,
            max_pods_per_node=max_pods_per_node,
            name=name,
            name_prefix=name_prefix,
            network_config=network_config,
            node_config=node_config,
            node_count=node_count,
            node_locations=node_locations,
            placement_policy=placement_policy,
            project=project,
            timeouts=timeouts,
            upgrade_settings=upgrade_settings,
            version=version,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAutoscaling")
    def put_autoscaling(
        self,
        *,
        location_policy: typing.Optional[builtins.str] = None,
        max_node_count: typing.Optional[jsii.Number] = None,
        min_node_count: typing.Optional[jsii.Number] = None,
        total_max_node_count: typing.Optional[jsii.Number] = None,
        total_min_node_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param location_policy: Location policy specifies the algorithm used when scaling-up the node pool. "BALANCED" - Is a best effort policy that aims to balance the sizes of available zones. "ANY" - Instructs the cluster autoscaler to prioritize utilization of unused reservations, and reduces preemption risk for Spot VMs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#location_policy GoogleContainerNodePool#location_policy}
        :param max_node_count: Maximum number of nodes per zone in the node pool. Must be >= min_node_count. Cannot be used with total limits. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#max_node_count GoogleContainerNodePool#max_node_count}
        :param min_node_count: Minimum number of nodes per zone in the node pool. Must be >=0 and <= max_node_count. Cannot be used with total limits. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#min_node_count GoogleContainerNodePool#min_node_count}
        :param total_max_node_count: Maximum number of all nodes in the node pool. Must be >= total_min_node_count. Cannot be used with per zone limits. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#total_max_node_count GoogleContainerNodePool#total_max_node_count}
        :param total_min_node_count: Minimum number of all nodes in the node pool. Must be >=0 and <= total_max_node_count. Cannot be used with per zone limits. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#total_min_node_count GoogleContainerNodePool#total_min_node_count}
        '''
        value = GoogleContainerNodePoolAutoscaling(
            location_policy=location_policy,
            max_node_count=max_node_count,
            min_node_count=min_node_count,
            total_max_node_count=total_max_node_count,
            total_min_node_count=total_min_node_count,
        )

        return typing.cast(None, jsii.invoke(self, "putAutoscaling", [value]))

    @jsii.member(jsii_name="putManagement")
    def put_management(
        self,
        *,
        auto_repair: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auto_upgrade: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param auto_repair: Whether the nodes will be automatically repaired. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#auto_repair GoogleContainerNodePool#auto_repair}
        :param auto_upgrade: Whether the nodes will be automatically upgraded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#auto_upgrade GoogleContainerNodePool#auto_upgrade}
        '''
        value = GoogleContainerNodePoolManagement(
            auto_repair=auto_repair, auto_upgrade=auto_upgrade
        )

        return typing.cast(None, jsii.invoke(self, "putManagement", [value]))

    @jsii.member(jsii_name="putNetworkConfig")
    def put_network_config(
        self,
        *,
        create_pod_range: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_private_nodes: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        pod_ipv4_cidr_block: typing.Optional[builtins.str] = None,
        pod_range: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create_pod_range: Whether to create a new range for pod IPs in this node pool. Defaults are provided for pod_range and pod_ipv4_cidr_block if they are not specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#create_pod_range GoogleContainerNodePool#create_pod_range}
        :param enable_private_nodes: Whether nodes have internal IP addresses only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#enable_private_nodes GoogleContainerNodePool#enable_private_nodes}
        :param pod_ipv4_cidr_block: The IP address range for pod IPs in this node pool. Only applicable if create_pod_range is true. Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14) to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14) to pick a specific range to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#pod_ipv4_cidr_block GoogleContainerNodePool#pod_ipv4_cidr_block}
        :param pod_range: The ID of the secondary range for pod IPs. If create_pod_range is true, this ID is used for the new range. If create_pod_range is false, uses an existing secondary range with this ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#pod_range GoogleContainerNodePool#pod_range}
        '''
        value = GoogleContainerNodePoolNetworkConfig(
            create_pod_range=create_pod_range,
            enable_private_nodes=enable_private_nodes,
            pod_ipv4_cidr_block=pod_ipv4_cidr_block,
            pod_range=pod_range,
        )

        return typing.cast(None, jsii.invoke(self, "putNetworkConfig", [value]))

    @jsii.member(jsii_name="putNodeConfig")
    def put_node_config(
        self,
        *,
        boot_disk_kms_key: typing.Optional[builtins.str] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        disk_type: typing.Optional[builtins.str] = None,
        ephemeral_storage_config: typing.Optional[typing.Union["GoogleContainerNodePoolNodeConfigEphemeralStorageConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        gcfs_config: typing.Optional[typing.Union["GoogleContainerNodePoolNodeConfigGcfsConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        guest_accelerator: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleContainerNodePoolNodeConfigGuestAccelerator", typing.Dict[builtins.str, typing.Any]]]]] = None,
        gvnic: typing.Optional[typing.Union["GoogleContainerNodePoolNodeConfigGvnic", typing.Dict[builtins.str, typing.Any]]] = None,
        image_type: typing.Optional[builtins.str] = None,
        kubelet_config: typing.Optional[typing.Union["GoogleContainerNodePoolNodeConfigKubeletConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        linux_node_config: typing.Optional[typing.Union["GoogleContainerNodePoolNodeConfigLinuxNodeConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        local_ssd_count: typing.Optional[jsii.Number] = None,
        logging_variant: typing.Optional[builtins.str] = None,
        machine_type: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        min_cpu_platform: typing.Optional[builtins.str] = None,
        node_group: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        preemptible: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        reservation_affinity: typing.Optional[typing.Union["GoogleContainerNodePoolNodeConfigReservationAffinity", typing.Dict[builtins.str, typing.Any]]] = None,
        resource_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        sandbox_config: typing.Optional[typing.Union["GoogleContainerNodePoolNodeConfigSandboxConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        service_account: typing.Optional[builtins.str] = None,
        shielded_instance_config: typing.Optional[typing.Union["GoogleContainerNodePoolNodeConfigShieldedInstanceConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        spot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        taint: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleContainerNodePoolNodeConfigTaint", typing.Dict[builtins.str, typing.Any]]]]] = None,
        workload_metadata_config: typing.Optional[typing.Union["GoogleContainerNodePoolNodeConfigWorkloadMetadataConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param boot_disk_kms_key: The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#boot_disk_kms_key GoogleContainerNodePool#boot_disk_kms_key}
        :param disk_size_gb: Size of the disk attached to each node, specified in GB. The smallest allowed disk size is 10GB. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#disk_size_gb GoogleContainerNodePool#disk_size_gb}
        :param disk_type: Type of the disk attached to each node. Such as pd-standard, pd-balanced or pd-ssd. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#disk_type GoogleContainerNodePool#disk_type}
        :param ephemeral_storage_config: ephemeral_storage_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#ephemeral_storage_config GoogleContainerNodePool#ephemeral_storage_config}
        :param gcfs_config: gcfs_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#gcfs_config GoogleContainerNodePool#gcfs_config}
        :param guest_accelerator: List of the type and count of accelerator cards attached to the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#guest_accelerator GoogleContainerNodePool#guest_accelerator}
        :param gvnic: gvnic block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#gvnic GoogleContainerNodePool#gvnic}
        :param image_type: The image type to use for this node. Note that for a given image type, the latest version of it will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#image_type GoogleContainerNodePool#image_type}
        :param kubelet_config: kubelet_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#kubelet_config GoogleContainerNodePool#kubelet_config}
        :param labels: The map of Kubernetes labels (key/value pairs) to be applied to each node. These will added in addition to any default label(s) that Kubernetes may apply to the node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#labels GoogleContainerNodePool#labels}
        :param linux_node_config: linux_node_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#linux_node_config GoogleContainerNodePool#linux_node_config}
        :param local_ssd_count: The number of local SSD disks to be attached to the node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#local_ssd_count GoogleContainerNodePool#local_ssd_count}
        :param logging_variant: Type of logging agent that is used as the default value for node pools in the cluster. Valid values include DEFAULT and MAX_THROUGHPUT. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#logging_variant GoogleContainerNodePool#logging_variant}
        :param machine_type: The name of a Google Compute Engine machine type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#machine_type GoogleContainerNodePool#machine_type}
        :param metadata: The metadata key/value pairs assigned to instances in the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#metadata GoogleContainerNodePool#metadata}
        :param min_cpu_platform: Minimum CPU platform to be used by this instance. The instance may be scheduled on the specified or newer CPU platform. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#min_cpu_platform GoogleContainerNodePool#min_cpu_platform}
        :param node_group: Setting this field will assign instances of this pool to run on the specified node group. This is useful for running workloads on sole tenant nodes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#node_group GoogleContainerNodePool#node_group}
        :param oauth_scopes: The set of Google API scopes to be made available on all of the node VMs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#oauth_scopes GoogleContainerNodePool#oauth_scopes}
        :param preemptible: Whether the nodes are created as preemptible VM instances. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#preemptible GoogleContainerNodePool#preemptible}
        :param reservation_affinity: reservation_affinity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#reservation_affinity GoogleContainerNodePool#reservation_affinity}
        :param resource_labels: The GCE resource labels (a map of key/value pairs) to be applied to the node pool. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#resource_labels GoogleContainerNodePool#resource_labels}
        :param sandbox_config: sandbox_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#sandbox_config GoogleContainerNodePool#sandbox_config}
        :param service_account: The Google Cloud Platform Service Account to be used by the node VMs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#service_account GoogleContainerNodePool#service_account}
        :param shielded_instance_config: shielded_instance_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#shielded_instance_config GoogleContainerNodePool#shielded_instance_config}
        :param spot: Whether the nodes are created as spot VM instances. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#spot GoogleContainerNodePool#spot}
        :param tags: The list of instance tags applied to all nodes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#tags GoogleContainerNodePool#tags}
        :param taint: List of Kubernetes taints to be applied to each node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#taint GoogleContainerNodePool#taint}
        :param workload_metadata_config: workload_metadata_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#workload_metadata_config GoogleContainerNodePool#workload_metadata_config}
        '''
        value = GoogleContainerNodePoolNodeConfig(
            boot_disk_kms_key=boot_disk_kms_key,
            disk_size_gb=disk_size_gb,
            disk_type=disk_type,
            ephemeral_storage_config=ephemeral_storage_config,
            gcfs_config=gcfs_config,
            guest_accelerator=guest_accelerator,
            gvnic=gvnic,
            image_type=image_type,
            kubelet_config=kubelet_config,
            labels=labels,
            linux_node_config=linux_node_config,
            local_ssd_count=local_ssd_count,
            logging_variant=logging_variant,
            machine_type=machine_type,
            metadata=metadata,
            min_cpu_platform=min_cpu_platform,
            node_group=node_group,
            oauth_scopes=oauth_scopes,
            preemptible=preemptible,
            reservation_affinity=reservation_affinity,
            resource_labels=resource_labels,
            sandbox_config=sandbox_config,
            service_account=service_account,
            shielded_instance_config=shielded_instance_config,
            spot=spot,
            tags=tags,
            taint=taint,
            workload_metadata_config=workload_metadata_config,
        )

        return typing.cast(None, jsii.invoke(self, "putNodeConfig", [value]))

    @jsii.member(jsii_name="putPlacementPolicy")
    def put_placement_policy(self, *, type: builtins.str) -> None:
        '''
        :param type: Type defines the type of placement policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#type GoogleContainerNodePool#type}
        '''
        value = GoogleContainerNodePoolPlacementPolicy(type=type)

        return typing.cast(None, jsii.invoke(self, "putPlacementPolicy", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#create GoogleContainerNodePool#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#delete GoogleContainerNodePool#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#update GoogleContainerNodePool#update}.
        '''
        value = GoogleContainerNodePoolTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putUpgradeSettings")
    def put_upgrade_settings(
        self,
        *,
        blue_green_settings: typing.Optional[typing.Union["GoogleContainerNodePoolUpgradeSettingsBlueGreenSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        max_surge: typing.Optional[jsii.Number] = None,
        max_unavailable: typing.Optional[jsii.Number] = None,
        strategy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param blue_green_settings: blue_green_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#blue_green_settings GoogleContainerNodePool#blue_green_settings}
        :param max_surge: The number of additional nodes that can be added to the node pool during an upgrade. Increasing max_surge raises the number of nodes that can be upgraded simultaneously. Can be set to 0 or greater. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#max_surge GoogleContainerNodePool#max_surge}
        :param max_unavailable: The number of nodes that can be simultaneously unavailable during an upgrade. Increasing max_unavailable raises the number of nodes that can be upgraded in parallel. Can be set to 0 or greater. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#max_unavailable GoogleContainerNodePool#max_unavailable}
        :param strategy: Update strategy for the given nodepool. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#strategy GoogleContainerNodePool#strategy}
        '''
        value = GoogleContainerNodePoolUpgradeSettings(
            blue_green_settings=blue_green_settings,
            max_surge=max_surge,
            max_unavailable=max_unavailable,
            strategy=strategy,
        )

        return typing.cast(None, jsii.invoke(self, "putUpgradeSettings", [value]))

    @jsii.member(jsii_name="resetAutoscaling")
    def reset_autoscaling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscaling", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInitialNodeCount")
    def reset_initial_node_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialNodeCount", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetManagement")
    def reset_management(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagement", []))

    @jsii.member(jsii_name="resetMaxPodsPerNode")
    def reset_max_pods_per_node(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxPodsPerNode", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamePrefix")
    def reset_name_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamePrefix", []))

    @jsii.member(jsii_name="resetNetworkConfig")
    def reset_network_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkConfig", []))

    @jsii.member(jsii_name="resetNodeConfig")
    def reset_node_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeConfig", []))

    @jsii.member(jsii_name="resetNodeCount")
    def reset_node_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeCount", []))

    @jsii.member(jsii_name="resetNodeLocations")
    def reset_node_locations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeLocations", []))

    @jsii.member(jsii_name="resetPlacementPolicy")
    def reset_placement_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlacementPolicy", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUpgradeSettings")
    def reset_upgrade_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpgradeSettings", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="autoscaling")
    def autoscaling(self) -> "GoogleContainerNodePoolAutoscalingOutputReference":
        return typing.cast("GoogleContainerNodePoolAutoscalingOutputReference", jsii.get(self, "autoscaling"))

    @builtins.property
    @jsii.member(jsii_name="instanceGroupUrls")
    def instance_group_urls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "instanceGroupUrls"))

    @builtins.property
    @jsii.member(jsii_name="managedInstanceGroupUrls")
    def managed_instance_group_urls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "managedInstanceGroupUrls"))

    @builtins.property
    @jsii.member(jsii_name="management")
    def management(self) -> "GoogleContainerNodePoolManagementOutputReference":
        return typing.cast("GoogleContainerNodePoolManagementOutputReference", jsii.get(self, "management"))

    @builtins.property
    @jsii.member(jsii_name="networkConfig")
    def network_config(self) -> "GoogleContainerNodePoolNetworkConfigOutputReference":
        return typing.cast("GoogleContainerNodePoolNetworkConfigOutputReference", jsii.get(self, "networkConfig"))

    @builtins.property
    @jsii.member(jsii_name="nodeConfig")
    def node_config(self) -> "GoogleContainerNodePoolNodeConfigOutputReference":
        return typing.cast("GoogleContainerNodePoolNodeConfigOutputReference", jsii.get(self, "nodeConfig"))

    @builtins.property
    @jsii.member(jsii_name="operation")
    def operation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operation"))

    @builtins.property
    @jsii.member(jsii_name="placementPolicy")
    def placement_policy(
        self,
    ) -> "GoogleContainerNodePoolPlacementPolicyOutputReference":
        return typing.cast("GoogleContainerNodePoolPlacementPolicyOutputReference", jsii.get(self, "placementPolicy"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleContainerNodePoolTimeoutsOutputReference":
        return typing.cast("GoogleContainerNodePoolTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="upgradeSettings")
    def upgrade_settings(
        self,
    ) -> "GoogleContainerNodePoolUpgradeSettingsOutputReference":
        return typing.cast("GoogleContainerNodePoolUpgradeSettingsOutputReference", jsii.get(self, "upgradeSettings"))

    @builtins.property
    @jsii.member(jsii_name="autoscalingInput")
    def autoscaling_input(
        self,
    ) -> typing.Optional["GoogleContainerNodePoolAutoscaling"]:
        return typing.cast(typing.Optional["GoogleContainerNodePoolAutoscaling"], jsii.get(self, "autoscalingInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterInput")
    def cluster_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="initialNodeCountInput")
    def initial_node_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "initialNodeCountInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="managementInput")
    def management_input(self) -> typing.Optional["GoogleContainerNodePoolManagement"]:
        return typing.cast(typing.Optional["GoogleContainerNodePoolManagement"], jsii.get(self, "managementInput"))

    @builtins.property
    @jsii.member(jsii_name="maxPodsPerNodeInput")
    def max_pods_per_node_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxPodsPerNodeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namePrefixInput")
    def name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="networkConfigInput")
    def network_config_input(
        self,
    ) -> typing.Optional["GoogleContainerNodePoolNetworkConfig"]:
        return typing.cast(typing.Optional["GoogleContainerNodePoolNetworkConfig"], jsii.get(self, "networkConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeConfigInput")
    def node_config_input(self) -> typing.Optional["GoogleContainerNodePoolNodeConfig"]:
        return typing.cast(typing.Optional["GoogleContainerNodePoolNodeConfig"], jsii.get(self, "nodeConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeCountInput")
    def node_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nodeCountInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeLocationsInput")
    def node_locations_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "nodeLocationsInput"))

    @builtins.property
    @jsii.member(jsii_name="placementPolicyInput")
    def placement_policy_input(
        self,
    ) -> typing.Optional["GoogleContainerNodePoolPlacementPolicy"]:
        return typing.cast(typing.Optional["GoogleContainerNodePoolPlacementPolicy"], jsii.get(self, "placementPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleContainerNodePoolTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleContainerNodePoolTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="upgradeSettingsInput")
    def upgrade_settings_input(
        self,
    ) -> typing.Optional["GoogleContainerNodePoolUpgradeSettings"]:
        return typing.cast(typing.Optional["GoogleContainerNodePoolUpgradeSettings"], jsii.get(self, "upgradeSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="cluster")
    def cluster(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cluster"))

    @cluster.setter
    def cluster(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81585b084a75592c5e3706d4af74e68f36aa22552975bfc892fabe709cd68a93)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cluster", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c48c4bf2a2e4b93438ccc44e9e308390e16c2f93480729af0864bf8fcdb7794)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="initialNodeCount")
    def initial_node_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "initialNodeCount"))

    @initial_node_count.setter
    def initial_node_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c61929a40bb8705acf4362b8eaf62f2baafd7567509c759af365e149731a020)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialNodeCount", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__704c1758a74418784eae7802f36846db75082e7402be0ebfa99e848d7f40c078)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="maxPodsPerNode")
    def max_pods_per_node(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxPodsPerNode"))

    @max_pods_per_node.setter
    def max_pods_per_node(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2c02dee5f56c3abdc39bb4e8bff7e7810c84b6b802fc3ad1ed11a0cdcd53bc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxPodsPerNode", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__415f2d44014be5f55268a27092218cbdfa10c6db46eff6f23725b42d3d7b28f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namePrefix")
    def name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namePrefix"))

    @name_prefix.setter
    def name_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3d9c0c424628c611ef7cf1e04ee271b3e5085940c2d1ef9a8ee6ca572735e77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="nodeCount")
    def node_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nodeCount"))

    @node_count.setter
    def node_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80ecfcd52d0067562ef6c905b0ce3c1cb7dce917af196328f8cf80bcffb9778b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeCount", value)

    @builtins.property
    @jsii.member(jsii_name="nodeLocations")
    def node_locations(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "nodeLocations"))

    @node_locations.setter
    def node_locations(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__816e68d06296456ca033c553ee6656cb4a59fd19d5e07d2fe98f8620fab55da1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeLocations", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfed50f56cb91855a1001533be060dc5ad6cbdd28d8308e6734de92794386f47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84e6080263da48bee69e742df775d7961bc11f1f69da78eca068c2632dfa54a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolAutoscaling",
    jsii_struct_bases=[],
    name_mapping={
        "location_policy": "locationPolicy",
        "max_node_count": "maxNodeCount",
        "min_node_count": "minNodeCount",
        "total_max_node_count": "totalMaxNodeCount",
        "total_min_node_count": "totalMinNodeCount",
    },
)
class GoogleContainerNodePoolAutoscaling:
    def __init__(
        self,
        *,
        location_policy: typing.Optional[builtins.str] = None,
        max_node_count: typing.Optional[jsii.Number] = None,
        min_node_count: typing.Optional[jsii.Number] = None,
        total_max_node_count: typing.Optional[jsii.Number] = None,
        total_min_node_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param location_policy: Location policy specifies the algorithm used when scaling-up the node pool. "BALANCED" - Is a best effort policy that aims to balance the sizes of available zones. "ANY" - Instructs the cluster autoscaler to prioritize utilization of unused reservations, and reduces preemption risk for Spot VMs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#location_policy GoogleContainerNodePool#location_policy}
        :param max_node_count: Maximum number of nodes per zone in the node pool. Must be >= min_node_count. Cannot be used with total limits. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#max_node_count GoogleContainerNodePool#max_node_count}
        :param min_node_count: Minimum number of nodes per zone in the node pool. Must be >=0 and <= max_node_count. Cannot be used with total limits. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#min_node_count GoogleContainerNodePool#min_node_count}
        :param total_max_node_count: Maximum number of all nodes in the node pool. Must be >= total_min_node_count. Cannot be used with per zone limits. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#total_max_node_count GoogleContainerNodePool#total_max_node_count}
        :param total_min_node_count: Minimum number of all nodes in the node pool. Must be >=0 and <= total_max_node_count. Cannot be used with per zone limits. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#total_min_node_count GoogleContainerNodePool#total_min_node_count}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62328d6aae5eae7f3d514da0e78b03c79612e2e5f431951301ae48f85e56bab6)
            check_type(argname="argument location_policy", value=location_policy, expected_type=type_hints["location_policy"])
            check_type(argname="argument max_node_count", value=max_node_count, expected_type=type_hints["max_node_count"])
            check_type(argname="argument min_node_count", value=min_node_count, expected_type=type_hints["min_node_count"])
            check_type(argname="argument total_max_node_count", value=total_max_node_count, expected_type=type_hints["total_max_node_count"])
            check_type(argname="argument total_min_node_count", value=total_min_node_count, expected_type=type_hints["total_min_node_count"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if location_policy is not None:
            self._values["location_policy"] = location_policy
        if max_node_count is not None:
            self._values["max_node_count"] = max_node_count
        if min_node_count is not None:
            self._values["min_node_count"] = min_node_count
        if total_max_node_count is not None:
            self._values["total_max_node_count"] = total_max_node_count
        if total_min_node_count is not None:
            self._values["total_min_node_count"] = total_min_node_count

    @builtins.property
    def location_policy(self) -> typing.Optional[builtins.str]:
        '''Location policy specifies the algorithm used when scaling-up the node pool.

        "BALANCED" - Is a best effort policy that aims to balance the sizes of available zones. "ANY" - Instructs the cluster autoscaler to prioritize utilization of unused reservations, and reduces preemption risk for Spot VMs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#location_policy GoogleContainerNodePool#location_policy}
        '''
        result = self._values.get("location_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_node_count(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of nodes per zone in the node pool.

        Must be >= min_node_count. Cannot be used with total limits.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#max_node_count GoogleContainerNodePool#max_node_count}
        '''
        result = self._values.get("max_node_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_node_count(self) -> typing.Optional[jsii.Number]:
        '''Minimum number of nodes per zone in the node pool.

        Must be >=0 and <= max_node_count. Cannot be used with total limits.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#min_node_count GoogleContainerNodePool#min_node_count}
        '''
        result = self._values.get("min_node_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def total_max_node_count(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of all nodes in the node pool.

        Must be >= total_min_node_count. Cannot be used with per zone limits.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#total_max_node_count GoogleContainerNodePool#total_max_node_count}
        '''
        result = self._values.get("total_max_node_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def total_min_node_count(self) -> typing.Optional[jsii.Number]:
        '''Minimum number of all nodes in the node pool.

        Must be >=0 and <= total_max_node_count. Cannot be used with per zone limits.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#total_min_node_count GoogleContainerNodePool#total_min_node_count}
        '''
        result = self._values.get("total_min_node_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerNodePoolAutoscaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerNodePoolAutoscalingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolAutoscalingOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ea6e7409413f0fc48829caa13d817fd8015042db5fadbbbdfe306cc470b16230)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLocationPolicy")
    def reset_location_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocationPolicy", []))

    @jsii.member(jsii_name="resetMaxNodeCount")
    def reset_max_node_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxNodeCount", []))

    @jsii.member(jsii_name="resetMinNodeCount")
    def reset_min_node_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinNodeCount", []))

    @jsii.member(jsii_name="resetTotalMaxNodeCount")
    def reset_total_max_node_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTotalMaxNodeCount", []))

    @jsii.member(jsii_name="resetTotalMinNodeCount")
    def reset_total_min_node_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTotalMinNodeCount", []))

    @builtins.property
    @jsii.member(jsii_name="locationPolicyInput")
    def location_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="maxNodeCountInput")
    def max_node_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxNodeCountInput"))

    @builtins.property
    @jsii.member(jsii_name="minNodeCountInput")
    def min_node_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minNodeCountInput"))

    @builtins.property
    @jsii.member(jsii_name="totalMaxNodeCountInput")
    def total_max_node_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "totalMaxNodeCountInput"))

    @builtins.property
    @jsii.member(jsii_name="totalMinNodeCountInput")
    def total_min_node_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "totalMinNodeCountInput"))

    @builtins.property
    @jsii.member(jsii_name="locationPolicy")
    def location_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "locationPolicy"))

    @location_policy.setter
    def location_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0c15ce7b2fe3ff14ba262606cf60c325f83fa6c6553f7be2686039f8ea3b0f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locationPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="maxNodeCount")
    def max_node_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxNodeCount"))

    @max_node_count.setter
    def max_node_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91f7cb34e10e8a57ff9e3ba6c95adc6369aaf96b12061399856f9f6ace845e0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxNodeCount", value)

    @builtins.property
    @jsii.member(jsii_name="minNodeCount")
    def min_node_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minNodeCount"))

    @min_node_count.setter
    def min_node_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__487660a99f7c64d19c4190435a15b38388a4da154a4661c594e749bbb6bee17c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minNodeCount", value)

    @builtins.property
    @jsii.member(jsii_name="totalMaxNodeCount")
    def total_max_node_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "totalMaxNodeCount"))

    @total_max_node_count.setter
    def total_max_node_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5aaa234adc7ed238d1b00176d3cad8de2e782a4a36e27414cb0651b7f1f3ff75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "totalMaxNodeCount", value)

    @builtins.property
    @jsii.member(jsii_name="totalMinNodeCount")
    def total_min_node_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "totalMinNodeCount"))

    @total_min_node_count.setter
    def total_min_node_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__515d47a796a60062d7644cae62cb074d21be87201210aea0c046c701e5540a04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "totalMinNodeCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleContainerNodePoolAutoscaling]:
        return typing.cast(typing.Optional[GoogleContainerNodePoolAutoscaling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleContainerNodePoolAutoscaling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb9a1cc5dfd72df0873603c99766e896fdbe8dcf5f4aef19ba20980d351b4041)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cluster": "cluster",
        "autoscaling": "autoscaling",
        "id": "id",
        "initial_node_count": "initialNodeCount",
        "location": "location",
        "management": "management",
        "max_pods_per_node": "maxPodsPerNode",
        "name": "name",
        "name_prefix": "namePrefix",
        "network_config": "networkConfig",
        "node_config": "nodeConfig",
        "node_count": "nodeCount",
        "node_locations": "nodeLocations",
        "placement_policy": "placementPolicy",
        "project": "project",
        "timeouts": "timeouts",
        "upgrade_settings": "upgradeSettings",
        "version": "version",
    },
)
class GoogleContainerNodePoolConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        cluster: builtins.str,
        autoscaling: typing.Optional[typing.Union[GoogleContainerNodePoolAutoscaling, typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        initial_node_count: typing.Optional[jsii.Number] = None,
        location: typing.Optional[builtins.str] = None,
        management: typing.Optional[typing.Union["GoogleContainerNodePoolManagement", typing.Dict[builtins.str, typing.Any]]] = None,
        max_pods_per_node: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        network_config: typing.Optional[typing.Union["GoogleContainerNodePoolNetworkConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        node_config: typing.Optional[typing.Union["GoogleContainerNodePoolNodeConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        node_count: typing.Optional[jsii.Number] = None,
        node_locations: typing.Optional[typing.Sequence[builtins.str]] = None,
        placement_policy: typing.Optional[typing.Union["GoogleContainerNodePoolPlacementPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleContainerNodePoolTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        upgrade_settings: typing.Optional[typing.Union["GoogleContainerNodePoolUpgradeSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cluster: The cluster to create the node pool for. Cluster must be present in location provided for zonal clusters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#cluster GoogleContainerNodePool#cluster}
        :param autoscaling: autoscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#autoscaling GoogleContainerNodePool#autoscaling}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#id GoogleContainerNodePool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initial_node_count: The initial number of nodes for the pool. In regional or multi-zonal clusters, this is the number of nodes per zone. Changing this will force recreation of the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#initial_node_count GoogleContainerNodePool#initial_node_count}
        :param location: The location (region or zone) of the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#location GoogleContainerNodePool#location}
        :param management: management block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#management GoogleContainerNodePool#management}
        :param max_pods_per_node: The maximum number of pods per node in this node pool. Note that this does not work on node pools which are "route-based" - that is, node pools belonging to clusters that do not have IP Aliasing enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#max_pods_per_node GoogleContainerNodePool#max_pods_per_node}
        :param name: The name of the node pool. If left blank, Terraform will auto-generate a unique name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#name GoogleContainerNodePool#name}
        :param name_prefix: Creates a unique name for the node pool beginning with the specified prefix. Conflicts with name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#name_prefix GoogleContainerNodePool#name_prefix}
        :param network_config: network_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#network_config GoogleContainerNodePool#network_config}
        :param node_config: node_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#node_config GoogleContainerNodePool#node_config}
        :param node_count: The number of nodes per instance group. This field can be used to update the number of nodes per instance group but should not be used alongside autoscaling. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#node_count GoogleContainerNodePool#node_count}
        :param node_locations: The list of zones in which the node pool's nodes should be located. Nodes must be in the region of their regional cluster or in the same region as their cluster's zone for zonal clusters. If unspecified, the cluster-level node_locations will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#node_locations GoogleContainerNodePool#node_locations}
        :param placement_policy: placement_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#placement_policy GoogleContainerNodePool#placement_policy}
        :param project: The ID of the project in which to create the node pool. If blank, the provider-configured project will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#project GoogleContainerNodePool#project}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#timeouts GoogleContainerNodePool#timeouts}
        :param upgrade_settings: upgrade_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#upgrade_settings GoogleContainerNodePool#upgrade_settings}
        :param version: The Kubernetes version for the nodes in this pool. Note that if this field and auto_upgrade are both specified, they will fight each other for what the node version should be, so setting both is highly discouraged. While a fuzzy version can be specified, it's recommended that you specify explicit versions as Terraform will see spurious diffs when fuzzy versions are used. See the google_container_engine_versions data source's version_prefix field to approximate fuzzy versions in a Terraform-compatible way. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#version GoogleContainerNodePool#version}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(autoscaling, dict):
            autoscaling = GoogleContainerNodePoolAutoscaling(**autoscaling)
        if isinstance(management, dict):
            management = GoogleContainerNodePoolManagement(**management)
        if isinstance(network_config, dict):
            network_config = GoogleContainerNodePoolNetworkConfig(**network_config)
        if isinstance(node_config, dict):
            node_config = GoogleContainerNodePoolNodeConfig(**node_config)
        if isinstance(placement_policy, dict):
            placement_policy = GoogleContainerNodePoolPlacementPolicy(**placement_policy)
        if isinstance(timeouts, dict):
            timeouts = GoogleContainerNodePoolTimeouts(**timeouts)
        if isinstance(upgrade_settings, dict):
            upgrade_settings = GoogleContainerNodePoolUpgradeSettings(**upgrade_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ea29e6dbff83ef660066146f8c46000f2e00cb18bdc726304a3af1ba3895fbe)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument autoscaling", value=autoscaling, expected_type=type_hints["autoscaling"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument initial_node_count", value=initial_node_count, expected_type=type_hints["initial_node_count"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument management", value=management, expected_type=type_hints["management"])
            check_type(argname="argument max_pods_per_node", value=max_pods_per_node, expected_type=type_hints["max_pods_per_node"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument name_prefix", value=name_prefix, expected_type=type_hints["name_prefix"])
            check_type(argname="argument network_config", value=network_config, expected_type=type_hints["network_config"])
            check_type(argname="argument node_config", value=node_config, expected_type=type_hints["node_config"])
            check_type(argname="argument node_count", value=node_count, expected_type=type_hints["node_count"])
            check_type(argname="argument node_locations", value=node_locations, expected_type=type_hints["node_locations"])
            check_type(argname="argument placement_policy", value=placement_policy, expected_type=type_hints["placement_policy"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument upgrade_settings", value=upgrade_settings, expected_type=type_hints["upgrade_settings"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster": cluster,
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
        if autoscaling is not None:
            self._values["autoscaling"] = autoscaling
        if id is not None:
            self._values["id"] = id
        if initial_node_count is not None:
            self._values["initial_node_count"] = initial_node_count
        if location is not None:
            self._values["location"] = location
        if management is not None:
            self._values["management"] = management
        if max_pods_per_node is not None:
            self._values["max_pods_per_node"] = max_pods_per_node
        if name is not None:
            self._values["name"] = name
        if name_prefix is not None:
            self._values["name_prefix"] = name_prefix
        if network_config is not None:
            self._values["network_config"] = network_config
        if node_config is not None:
            self._values["node_config"] = node_config
        if node_count is not None:
            self._values["node_count"] = node_count
        if node_locations is not None:
            self._values["node_locations"] = node_locations
        if placement_policy is not None:
            self._values["placement_policy"] = placement_policy
        if project is not None:
            self._values["project"] = project
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if upgrade_settings is not None:
            self._values["upgrade_settings"] = upgrade_settings
        if version is not None:
            self._values["version"] = version

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
    def cluster(self) -> builtins.str:
        '''The cluster to create the node pool for. Cluster must be present in location provided for zonal clusters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#cluster GoogleContainerNodePool#cluster}
        '''
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def autoscaling(self) -> typing.Optional[GoogleContainerNodePoolAutoscaling]:
        '''autoscaling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#autoscaling GoogleContainerNodePool#autoscaling}
        '''
        result = self._values.get("autoscaling")
        return typing.cast(typing.Optional[GoogleContainerNodePoolAutoscaling], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#id GoogleContainerNodePool#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initial_node_count(self) -> typing.Optional[jsii.Number]:
        '''The initial number of nodes for the pool.

        In regional or multi-zonal clusters, this is the number of nodes per zone. Changing this will force recreation of the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#initial_node_count GoogleContainerNodePool#initial_node_count}
        '''
        result = self._values.get("initial_node_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''The location (region or zone) of the cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#location GoogleContainerNodePool#location}
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def management(self) -> typing.Optional["GoogleContainerNodePoolManagement"]:
        '''management block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#management GoogleContainerNodePool#management}
        '''
        result = self._values.get("management")
        return typing.cast(typing.Optional["GoogleContainerNodePoolManagement"], result)

    @builtins.property
    def max_pods_per_node(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of pods per node in this node pool.

        Note that this does not work on node pools which are "route-based" - that is, node pools belonging to clusters that do not have IP Aliasing enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#max_pods_per_node GoogleContainerNodePool#max_pods_per_node}
        '''
        result = self._values.get("max_pods_per_node")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the node pool. If left blank, Terraform will auto-generate a unique name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#name GoogleContainerNodePool#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_prefix(self) -> typing.Optional[builtins.str]:
        '''Creates a unique name for the node pool beginning with the specified prefix. Conflicts with name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#name_prefix GoogleContainerNodePool#name_prefix}
        '''
        result = self._values.get("name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_config(self) -> typing.Optional["GoogleContainerNodePoolNetworkConfig"]:
        '''network_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#network_config GoogleContainerNodePool#network_config}
        '''
        result = self._values.get("network_config")
        return typing.cast(typing.Optional["GoogleContainerNodePoolNetworkConfig"], result)

    @builtins.property
    def node_config(self) -> typing.Optional["GoogleContainerNodePoolNodeConfig"]:
        '''node_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#node_config GoogleContainerNodePool#node_config}
        '''
        result = self._values.get("node_config")
        return typing.cast(typing.Optional["GoogleContainerNodePoolNodeConfig"], result)

    @builtins.property
    def node_count(self) -> typing.Optional[jsii.Number]:
        '''The number of nodes per instance group.

        This field can be used to update the number of nodes per instance group but should not be used alongside autoscaling.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#node_count GoogleContainerNodePool#node_count}
        '''
        result = self._values.get("node_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def node_locations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of zones in which the node pool's nodes should be located.

        Nodes must be in the region of their regional cluster or in the same region as their cluster's zone for zonal clusters. If unspecified, the cluster-level node_locations will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#node_locations GoogleContainerNodePool#node_locations}
        '''
        result = self._values.get("node_locations")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def placement_policy(
        self,
    ) -> typing.Optional["GoogleContainerNodePoolPlacementPolicy"]:
        '''placement_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#placement_policy GoogleContainerNodePool#placement_policy}
        '''
        result = self._values.get("placement_policy")
        return typing.cast(typing.Optional["GoogleContainerNodePoolPlacementPolicy"], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The ID of the project in which to create the node pool.

        If blank, the provider-configured project will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#project GoogleContainerNodePool#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleContainerNodePoolTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#timeouts GoogleContainerNodePool#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleContainerNodePoolTimeouts"], result)

    @builtins.property
    def upgrade_settings(
        self,
    ) -> typing.Optional["GoogleContainerNodePoolUpgradeSettings"]:
        '''upgrade_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#upgrade_settings GoogleContainerNodePool#upgrade_settings}
        '''
        result = self._values.get("upgrade_settings")
        return typing.cast(typing.Optional["GoogleContainerNodePoolUpgradeSettings"], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''The Kubernetes version for the nodes in this pool.

        Note that if this field and auto_upgrade are both specified, they will fight each other for what the node version should be, so setting both is highly discouraged. While a fuzzy version can be specified, it's recommended that you specify explicit versions as Terraform will see spurious diffs when fuzzy versions are used. See the google_container_engine_versions data source's version_prefix field to approximate fuzzy versions in a Terraform-compatible way.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#version GoogleContainerNodePool#version}
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerNodePoolConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolManagement",
    jsii_struct_bases=[],
    name_mapping={"auto_repair": "autoRepair", "auto_upgrade": "autoUpgrade"},
)
class GoogleContainerNodePoolManagement:
    def __init__(
        self,
        *,
        auto_repair: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auto_upgrade: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param auto_repair: Whether the nodes will be automatically repaired. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#auto_repair GoogleContainerNodePool#auto_repair}
        :param auto_upgrade: Whether the nodes will be automatically upgraded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#auto_upgrade GoogleContainerNodePool#auto_upgrade}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf662b569af6c32395030e1a62cb8531d6641c45b30b92fe348b218de7658497)
            check_type(argname="argument auto_repair", value=auto_repair, expected_type=type_hints["auto_repair"])
            check_type(argname="argument auto_upgrade", value=auto_upgrade, expected_type=type_hints["auto_upgrade"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if auto_repair is not None:
            self._values["auto_repair"] = auto_repair
        if auto_upgrade is not None:
            self._values["auto_upgrade"] = auto_upgrade

    @builtins.property
    def auto_repair(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether the nodes will be automatically repaired.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#auto_repair GoogleContainerNodePool#auto_repair}
        '''
        result = self._values.get("auto_repair")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def auto_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether the nodes will be automatically upgraded.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#auto_upgrade GoogleContainerNodePool#auto_upgrade}
        '''
        result = self._values.get("auto_upgrade")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerNodePoolManagement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerNodePoolManagementOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolManagementOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__aab11aa58f47591b5a7f082a3b5abeddb63a02a365fb84966dc36fd6654a8299)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAutoRepair")
    def reset_auto_repair(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoRepair", []))

    @jsii.member(jsii_name="resetAutoUpgrade")
    def reset_auto_upgrade(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoUpgrade", []))

    @builtins.property
    @jsii.member(jsii_name="autoRepairInput")
    def auto_repair_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "autoRepairInput"))

    @builtins.property
    @jsii.member(jsii_name="autoUpgradeInput")
    def auto_upgrade_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "autoUpgradeInput"))

    @builtins.property
    @jsii.member(jsii_name="autoRepair")
    def auto_repair(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "autoRepair"))

    @auto_repair.setter
    def auto_repair(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__435f8fabeac9592a57908302f97e6e5268f60ac9d6b2be5802a49cbb3debed1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoRepair", value)

    @builtins.property
    @jsii.member(jsii_name="autoUpgrade")
    def auto_upgrade(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "autoUpgrade"))

    @auto_upgrade.setter
    def auto_upgrade(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29fb9077729ae66d34d07b367bdea13e3cf79db36d53a7e0cacac9fb3106dc18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleContainerNodePoolManagement]:
        return typing.cast(typing.Optional[GoogleContainerNodePoolManagement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleContainerNodePoolManagement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ed1eb8fc1eb08adaf661424db47ad79f9030d9dcb8d9e913a3c3c6f7d8f41ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNetworkConfig",
    jsii_struct_bases=[],
    name_mapping={
        "create_pod_range": "createPodRange",
        "enable_private_nodes": "enablePrivateNodes",
        "pod_ipv4_cidr_block": "podIpv4CidrBlock",
        "pod_range": "podRange",
    },
)
class GoogleContainerNodePoolNetworkConfig:
    def __init__(
        self,
        *,
        create_pod_range: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_private_nodes: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        pod_ipv4_cidr_block: typing.Optional[builtins.str] = None,
        pod_range: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create_pod_range: Whether to create a new range for pod IPs in this node pool. Defaults are provided for pod_range and pod_ipv4_cidr_block if they are not specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#create_pod_range GoogleContainerNodePool#create_pod_range}
        :param enable_private_nodes: Whether nodes have internal IP addresses only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#enable_private_nodes GoogleContainerNodePool#enable_private_nodes}
        :param pod_ipv4_cidr_block: The IP address range for pod IPs in this node pool. Only applicable if create_pod_range is true. Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14) to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14) to pick a specific range to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#pod_ipv4_cidr_block GoogleContainerNodePool#pod_ipv4_cidr_block}
        :param pod_range: The ID of the secondary range for pod IPs. If create_pod_range is true, this ID is used for the new range. If create_pod_range is false, uses an existing secondary range with this ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#pod_range GoogleContainerNodePool#pod_range}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eed8a5d314ec03f5556cab7d069325b6923f0374080c64eb741ae1245cb45d5c)
            check_type(argname="argument create_pod_range", value=create_pod_range, expected_type=type_hints["create_pod_range"])
            check_type(argname="argument enable_private_nodes", value=enable_private_nodes, expected_type=type_hints["enable_private_nodes"])
            check_type(argname="argument pod_ipv4_cidr_block", value=pod_ipv4_cidr_block, expected_type=type_hints["pod_ipv4_cidr_block"])
            check_type(argname="argument pod_range", value=pod_range, expected_type=type_hints["pod_range"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create_pod_range is not None:
            self._values["create_pod_range"] = create_pod_range
        if enable_private_nodes is not None:
            self._values["enable_private_nodes"] = enable_private_nodes
        if pod_ipv4_cidr_block is not None:
            self._values["pod_ipv4_cidr_block"] = pod_ipv4_cidr_block
        if pod_range is not None:
            self._values["pod_range"] = pod_range

    @builtins.property
    def create_pod_range(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to create a new range for pod IPs in this node pool.

        Defaults are provided for pod_range and pod_ipv4_cidr_block if they are not specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#create_pod_range GoogleContainerNodePool#create_pod_range}
        '''
        result = self._values.get("create_pod_range")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_private_nodes(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether nodes have internal IP addresses only.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#enable_private_nodes GoogleContainerNodePool#enable_private_nodes}
        '''
        result = self._values.get("enable_private_nodes")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def pod_ipv4_cidr_block(self) -> typing.Optional[builtins.str]:
        '''The IP address range for pod IPs in this node pool.

        Only applicable if create_pod_range is true. Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14) to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14) to pick a specific range to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#pod_ipv4_cidr_block GoogleContainerNodePool#pod_ipv4_cidr_block}
        '''
        result = self._values.get("pod_ipv4_cidr_block")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pod_range(self) -> typing.Optional[builtins.str]:
        '''The ID of the secondary range for pod IPs.

        If create_pod_range is true, this ID is used for the new range. If create_pod_range is false, uses an existing secondary range with this ID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#pod_range GoogleContainerNodePool#pod_range}
        '''
        result = self._values.get("pod_range")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerNodePoolNetworkConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerNodePoolNetworkConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNetworkConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__86ab47c099914e4d193e3ce84817fba39f48f162ab5d644a8f692b1135d4eb49)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreatePodRange")
    def reset_create_pod_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreatePodRange", []))

    @jsii.member(jsii_name="resetEnablePrivateNodes")
    def reset_enable_private_nodes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnablePrivateNodes", []))

    @jsii.member(jsii_name="resetPodIpv4CidrBlock")
    def reset_pod_ipv4_cidr_block(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPodIpv4CidrBlock", []))

    @jsii.member(jsii_name="resetPodRange")
    def reset_pod_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPodRange", []))

    @builtins.property
    @jsii.member(jsii_name="createPodRangeInput")
    def create_pod_range_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "createPodRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="enablePrivateNodesInput")
    def enable_private_nodes_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enablePrivateNodesInput"))

    @builtins.property
    @jsii.member(jsii_name="podIpv4CidrBlockInput")
    def pod_ipv4_cidr_block_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "podIpv4CidrBlockInput"))

    @builtins.property
    @jsii.member(jsii_name="podRangeInput")
    def pod_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "podRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="createPodRange")
    def create_pod_range(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "createPodRange"))

    @create_pod_range.setter
    def create_pod_range(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1508f8ee2ce08b8323c5176b5638d953797d29df6548da0cf78e3e321de31b46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createPodRange", value)

    @builtins.property
    @jsii.member(jsii_name="enablePrivateNodes")
    def enable_private_nodes(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enablePrivateNodes"))

    @enable_private_nodes.setter
    def enable_private_nodes(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14a0cfca3262e83c0e154372d222247345ed04f4c2e2266f03b60acefaba6d3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablePrivateNodes", value)

    @builtins.property
    @jsii.member(jsii_name="podIpv4CidrBlock")
    def pod_ipv4_cidr_block(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "podIpv4CidrBlock"))

    @pod_ipv4_cidr_block.setter
    def pod_ipv4_cidr_block(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7579b112e2f8956c9323cbde9c6225ba942280f541f9a94cf18adf7083cce62d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "podIpv4CidrBlock", value)

    @builtins.property
    @jsii.member(jsii_name="podRange")
    def pod_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "podRange"))

    @pod_range.setter
    def pod_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8bd9618d182a54a7314488aeda425a360a6040213e325fab75b28b3562ce8bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "podRange", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleContainerNodePoolNetworkConfig]:
        return typing.cast(typing.Optional[GoogleContainerNodePoolNetworkConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleContainerNodePoolNetworkConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dede1c406015eb91bc1ef6b774a5c323f0705bb993708882c958e72423c6e2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNodeConfig",
    jsii_struct_bases=[],
    name_mapping={
        "boot_disk_kms_key": "bootDiskKmsKey",
        "disk_size_gb": "diskSizeGb",
        "disk_type": "diskType",
        "ephemeral_storage_config": "ephemeralStorageConfig",
        "gcfs_config": "gcfsConfig",
        "guest_accelerator": "guestAccelerator",
        "gvnic": "gvnic",
        "image_type": "imageType",
        "kubelet_config": "kubeletConfig",
        "labels": "labels",
        "linux_node_config": "linuxNodeConfig",
        "local_ssd_count": "localSsdCount",
        "logging_variant": "loggingVariant",
        "machine_type": "machineType",
        "metadata": "metadata",
        "min_cpu_platform": "minCpuPlatform",
        "node_group": "nodeGroup",
        "oauth_scopes": "oauthScopes",
        "preemptible": "preemptible",
        "reservation_affinity": "reservationAffinity",
        "resource_labels": "resourceLabels",
        "sandbox_config": "sandboxConfig",
        "service_account": "serviceAccount",
        "shielded_instance_config": "shieldedInstanceConfig",
        "spot": "spot",
        "tags": "tags",
        "taint": "taint",
        "workload_metadata_config": "workloadMetadataConfig",
    },
)
class GoogleContainerNodePoolNodeConfig:
    def __init__(
        self,
        *,
        boot_disk_kms_key: typing.Optional[builtins.str] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        disk_type: typing.Optional[builtins.str] = None,
        ephemeral_storage_config: typing.Optional[typing.Union["GoogleContainerNodePoolNodeConfigEphemeralStorageConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        gcfs_config: typing.Optional[typing.Union["GoogleContainerNodePoolNodeConfigGcfsConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        guest_accelerator: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleContainerNodePoolNodeConfigGuestAccelerator", typing.Dict[builtins.str, typing.Any]]]]] = None,
        gvnic: typing.Optional[typing.Union["GoogleContainerNodePoolNodeConfigGvnic", typing.Dict[builtins.str, typing.Any]]] = None,
        image_type: typing.Optional[builtins.str] = None,
        kubelet_config: typing.Optional[typing.Union["GoogleContainerNodePoolNodeConfigKubeletConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        linux_node_config: typing.Optional[typing.Union["GoogleContainerNodePoolNodeConfigLinuxNodeConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        local_ssd_count: typing.Optional[jsii.Number] = None,
        logging_variant: typing.Optional[builtins.str] = None,
        machine_type: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        min_cpu_platform: typing.Optional[builtins.str] = None,
        node_group: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        preemptible: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        reservation_affinity: typing.Optional[typing.Union["GoogleContainerNodePoolNodeConfigReservationAffinity", typing.Dict[builtins.str, typing.Any]]] = None,
        resource_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        sandbox_config: typing.Optional[typing.Union["GoogleContainerNodePoolNodeConfigSandboxConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        service_account: typing.Optional[builtins.str] = None,
        shielded_instance_config: typing.Optional[typing.Union["GoogleContainerNodePoolNodeConfigShieldedInstanceConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        spot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        taint: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleContainerNodePoolNodeConfigTaint", typing.Dict[builtins.str, typing.Any]]]]] = None,
        workload_metadata_config: typing.Optional[typing.Union["GoogleContainerNodePoolNodeConfigWorkloadMetadataConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param boot_disk_kms_key: The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#boot_disk_kms_key GoogleContainerNodePool#boot_disk_kms_key}
        :param disk_size_gb: Size of the disk attached to each node, specified in GB. The smallest allowed disk size is 10GB. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#disk_size_gb GoogleContainerNodePool#disk_size_gb}
        :param disk_type: Type of the disk attached to each node. Such as pd-standard, pd-balanced or pd-ssd. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#disk_type GoogleContainerNodePool#disk_type}
        :param ephemeral_storage_config: ephemeral_storage_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#ephemeral_storage_config GoogleContainerNodePool#ephemeral_storage_config}
        :param gcfs_config: gcfs_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#gcfs_config GoogleContainerNodePool#gcfs_config}
        :param guest_accelerator: List of the type and count of accelerator cards attached to the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#guest_accelerator GoogleContainerNodePool#guest_accelerator}
        :param gvnic: gvnic block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#gvnic GoogleContainerNodePool#gvnic}
        :param image_type: The image type to use for this node. Note that for a given image type, the latest version of it will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#image_type GoogleContainerNodePool#image_type}
        :param kubelet_config: kubelet_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#kubelet_config GoogleContainerNodePool#kubelet_config}
        :param labels: The map of Kubernetes labels (key/value pairs) to be applied to each node. These will added in addition to any default label(s) that Kubernetes may apply to the node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#labels GoogleContainerNodePool#labels}
        :param linux_node_config: linux_node_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#linux_node_config GoogleContainerNodePool#linux_node_config}
        :param local_ssd_count: The number of local SSD disks to be attached to the node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#local_ssd_count GoogleContainerNodePool#local_ssd_count}
        :param logging_variant: Type of logging agent that is used as the default value for node pools in the cluster. Valid values include DEFAULT and MAX_THROUGHPUT. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#logging_variant GoogleContainerNodePool#logging_variant}
        :param machine_type: The name of a Google Compute Engine machine type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#machine_type GoogleContainerNodePool#machine_type}
        :param metadata: The metadata key/value pairs assigned to instances in the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#metadata GoogleContainerNodePool#metadata}
        :param min_cpu_platform: Minimum CPU platform to be used by this instance. The instance may be scheduled on the specified or newer CPU platform. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#min_cpu_platform GoogleContainerNodePool#min_cpu_platform}
        :param node_group: Setting this field will assign instances of this pool to run on the specified node group. This is useful for running workloads on sole tenant nodes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#node_group GoogleContainerNodePool#node_group}
        :param oauth_scopes: The set of Google API scopes to be made available on all of the node VMs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#oauth_scopes GoogleContainerNodePool#oauth_scopes}
        :param preemptible: Whether the nodes are created as preemptible VM instances. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#preemptible GoogleContainerNodePool#preemptible}
        :param reservation_affinity: reservation_affinity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#reservation_affinity GoogleContainerNodePool#reservation_affinity}
        :param resource_labels: The GCE resource labels (a map of key/value pairs) to be applied to the node pool. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#resource_labels GoogleContainerNodePool#resource_labels}
        :param sandbox_config: sandbox_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#sandbox_config GoogleContainerNodePool#sandbox_config}
        :param service_account: The Google Cloud Platform Service Account to be used by the node VMs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#service_account GoogleContainerNodePool#service_account}
        :param shielded_instance_config: shielded_instance_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#shielded_instance_config GoogleContainerNodePool#shielded_instance_config}
        :param spot: Whether the nodes are created as spot VM instances. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#spot GoogleContainerNodePool#spot}
        :param tags: The list of instance tags applied to all nodes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#tags GoogleContainerNodePool#tags}
        :param taint: List of Kubernetes taints to be applied to each node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#taint GoogleContainerNodePool#taint}
        :param workload_metadata_config: workload_metadata_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#workload_metadata_config GoogleContainerNodePool#workload_metadata_config}
        '''
        if isinstance(ephemeral_storage_config, dict):
            ephemeral_storage_config = GoogleContainerNodePoolNodeConfigEphemeralStorageConfig(**ephemeral_storage_config)
        if isinstance(gcfs_config, dict):
            gcfs_config = GoogleContainerNodePoolNodeConfigGcfsConfig(**gcfs_config)
        if isinstance(gvnic, dict):
            gvnic = GoogleContainerNodePoolNodeConfigGvnic(**gvnic)
        if isinstance(kubelet_config, dict):
            kubelet_config = GoogleContainerNodePoolNodeConfigKubeletConfig(**kubelet_config)
        if isinstance(linux_node_config, dict):
            linux_node_config = GoogleContainerNodePoolNodeConfigLinuxNodeConfig(**linux_node_config)
        if isinstance(reservation_affinity, dict):
            reservation_affinity = GoogleContainerNodePoolNodeConfigReservationAffinity(**reservation_affinity)
        if isinstance(sandbox_config, dict):
            sandbox_config = GoogleContainerNodePoolNodeConfigSandboxConfig(**sandbox_config)
        if isinstance(shielded_instance_config, dict):
            shielded_instance_config = GoogleContainerNodePoolNodeConfigShieldedInstanceConfig(**shielded_instance_config)
        if isinstance(workload_metadata_config, dict):
            workload_metadata_config = GoogleContainerNodePoolNodeConfigWorkloadMetadataConfig(**workload_metadata_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa1fcd02cbce130e12742899615c9eba8ee7c5fbe33fdb8aaf3b5ba306a4073c)
            check_type(argname="argument boot_disk_kms_key", value=boot_disk_kms_key, expected_type=type_hints["boot_disk_kms_key"])
            check_type(argname="argument disk_size_gb", value=disk_size_gb, expected_type=type_hints["disk_size_gb"])
            check_type(argname="argument disk_type", value=disk_type, expected_type=type_hints["disk_type"])
            check_type(argname="argument ephemeral_storage_config", value=ephemeral_storage_config, expected_type=type_hints["ephemeral_storage_config"])
            check_type(argname="argument gcfs_config", value=gcfs_config, expected_type=type_hints["gcfs_config"])
            check_type(argname="argument guest_accelerator", value=guest_accelerator, expected_type=type_hints["guest_accelerator"])
            check_type(argname="argument gvnic", value=gvnic, expected_type=type_hints["gvnic"])
            check_type(argname="argument image_type", value=image_type, expected_type=type_hints["image_type"])
            check_type(argname="argument kubelet_config", value=kubelet_config, expected_type=type_hints["kubelet_config"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument linux_node_config", value=linux_node_config, expected_type=type_hints["linux_node_config"])
            check_type(argname="argument local_ssd_count", value=local_ssd_count, expected_type=type_hints["local_ssd_count"])
            check_type(argname="argument logging_variant", value=logging_variant, expected_type=type_hints["logging_variant"])
            check_type(argname="argument machine_type", value=machine_type, expected_type=type_hints["machine_type"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument min_cpu_platform", value=min_cpu_platform, expected_type=type_hints["min_cpu_platform"])
            check_type(argname="argument node_group", value=node_group, expected_type=type_hints["node_group"])
            check_type(argname="argument oauth_scopes", value=oauth_scopes, expected_type=type_hints["oauth_scopes"])
            check_type(argname="argument preemptible", value=preemptible, expected_type=type_hints["preemptible"])
            check_type(argname="argument reservation_affinity", value=reservation_affinity, expected_type=type_hints["reservation_affinity"])
            check_type(argname="argument resource_labels", value=resource_labels, expected_type=type_hints["resource_labels"])
            check_type(argname="argument sandbox_config", value=sandbox_config, expected_type=type_hints["sandbox_config"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
            check_type(argname="argument shielded_instance_config", value=shielded_instance_config, expected_type=type_hints["shielded_instance_config"])
            check_type(argname="argument spot", value=spot, expected_type=type_hints["spot"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument taint", value=taint, expected_type=type_hints["taint"])
            check_type(argname="argument workload_metadata_config", value=workload_metadata_config, expected_type=type_hints["workload_metadata_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if boot_disk_kms_key is not None:
            self._values["boot_disk_kms_key"] = boot_disk_kms_key
        if disk_size_gb is not None:
            self._values["disk_size_gb"] = disk_size_gb
        if disk_type is not None:
            self._values["disk_type"] = disk_type
        if ephemeral_storage_config is not None:
            self._values["ephemeral_storage_config"] = ephemeral_storage_config
        if gcfs_config is not None:
            self._values["gcfs_config"] = gcfs_config
        if guest_accelerator is not None:
            self._values["guest_accelerator"] = guest_accelerator
        if gvnic is not None:
            self._values["gvnic"] = gvnic
        if image_type is not None:
            self._values["image_type"] = image_type
        if kubelet_config is not None:
            self._values["kubelet_config"] = kubelet_config
        if labels is not None:
            self._values["labels"] = labels
        if linux_node_config is not None:
            self._values["linux_node_config"] = linux_node_config
        if local_ssd_count is not None:
            self._values["local_ssd_count"] = local_ssd_count
        if logging_variant is not None:
            self._values["logging_variant"] = logging_variant
        if machine_type is not None:
            self._values["machine_type"] = machine_type
        if metadata is not None:
            self._values["metadata"] = metadata
        if min_cpu_platform is not None:
            self._values["min_cpu_platform"] = min_cpu_platform
        if node_group is not None:
            self._values["node_group"] = node_group
        if oauth_scopes is not None:
            self._values["oauth_scopes"] = oauth_scopes
        if preemptible is not None:
            self._values["preemptible"] = preemptible
        if reservation_affinity is not None:
            self._values["reservation_affinity"] = reservation_affinity
        if resource_labels is not None:
            self._values["resource_labels"] = resource_labels
        if sandbox_config is not None:
            self._values["sandbox_config"] = sandbox_config
        if service_account is not None:
            self._values["service_account"] = service_account
        if shielded_instance_config is not None:
            self._values["shielded_instance_config"] = shielded_instance_config
        if spot is not None:
            self._values["spot"] = spot
        if tags is not None:
            self._values["tags"] = tags
        if taint is not None:
            self._values["taint"] = taint
        if workload_metadata_config is not None:
            self._values["workload_metadata_config"] = workload_metadata_config

    @builtins.property
    def boot_disk_kms_key(self) -> typing.Optional[builtins.str]:
        '''The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#boot_disk_kms_key GoogleContainerNodePool#boot_disk_kms_key}
        '''
        result = self._values.get("boot_disk_kms_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''Size of the disk attached to each node, specified in GB. The smallest allowed disk size is 10GB.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#disk_size_gb GoogleContainerNodePool#disk_size_gb}
        '''
        result = self._values.get("disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def disk_type(self) -> typing.Optional[builtins.str]:
        '''Type of the disk attached to each node. Such as pd-standard, pd-balanced or pd-ssd.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#disk_type GoogleContainerNodePool#disk_type}
        '''
        result = self._values.get("disk_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ephemeral_storage_config(
        self,
    ) -> typing.Optional["GoogleContainerNodePoolNodeConfigEphemeralStorageConfig"]:
        '''ephemeral_storage_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#ephemeral_storage_config GoogleContainerNodePool#ephemeral_storage_config}
        '''
        result = self._values.get("ephemeral_storage_config")
        return typing.cast(typing.Optional["GoogleContainerNodePoolNodeConfigEphemeralStorageConfig"], result)

    @builtins.property
    def gcfs_config(
        self,
    ) -> typing.Optional["GoogleContainerNodePoolNodeConfigGcfsConfig"]:
        '''gcfs_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#gcfs_config GoogleContainerNodePool#gcfs_config}
        '''
        result = self._values.get("gcfs_config")
        return typing.cast(typing.Optional["GoogleContainerNodePoolNodeConfigGcfsConfig"], result)

    @builtins.property
    def guest_accelerator(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleContainerNodePoolNodeConfigGuestAccelerator"]]]:
        '''List of the type and count of accelerator cards attached to the instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#guest_accelerator GoogleContainerNodePool#guest_accelerator}
        '''
        result = self._values.get("guest_accelerator")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleContainerNodePoolNodeConfigGuestAccelerator"]]], result)

    @builtins.property
    def gvnic(self) -> typing.Optional["GoogleContainerNodePoolNodeConfigGvnic"]:
        '''gvnic block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#gvnic GoogleContainerNodePool#gvnic}
        '''
        result = self._values.get("gvnic")
        return typing.cast(typing.Optional["GoogleContainerNodePoolNodeConfigGvnic"], result)

    @builtins.property
    def image_type(self) -> typing.Optional[builtins.str]:
        '''The image type to use for this node.

        Note that for a given image type, the latest version of it will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#image_type GoogleContainerNodePool#image_type}
        '''
        result = self._values.get("image_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kubelet_config(
        self,
    ) -> typing.Optional["GoogleContainerNodePoolNodeConfigKubeletConfig"]:
        '''kubelet_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#kubelet_config GoogleContainerNodePool#kubelet_config}
        '''
        result = self._values.get("kubelet_config")
        return typing.cast(typing.Optional["GoogleContainerNodePoolNodeConfigKubeletConfig"], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The map of Kubernetes labels (key/value pairs) to be applied to each node.

        These will added in addition to any default label(s) that Kubernetes may apply to the node.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#labels GoogleContainerNodePool#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def linux_node_config(
        self,
    ) -> typing.Optional["GoogleContainerNodePoolNodeConfigLinuxNodeConfig"]:
        '''linux_node_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#linux_node_config GoogleContainerNodePool#linux_node_config}
        '''
        result = self._values.get("linux_node_config")
        return typing.cast(typing.Optional["GoogleContainerNodePoolNodeConfigLinuxNodeConfig"], result)

    @builtins.property
    def local_ssd_count(self) -> typing.Optional[jsii.Number]:
        '''The number of local SSD disks to be attached to the node.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#local_ssd_count GoogleContainerNodePool#local_ssd_count}
        '''
        result = self._values.get("local_ssd_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def logging_variant(self) -> typing.Optional[builtins.str]:
        '''Type of logging agent that is used as the default value for node pools in the cluster.

        Valid values include DEFAULT and MAX_THROUGHPUT.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#logging_variant GoogleContainerNodePool#logging_variant}
        '''
        result = self._values.get("logging_variant")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def machine_type(self) -> typing.Optional[builtins.str]:
        '''The name of a Google Compute Engine machine type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#machine_type GoogleContainerNodePool#machine_type}
        '''
        result = self._values.get("machine_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metadata(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The metadata key/value pairs assigned to instances in the cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#metadata GoogleContainerNodePool#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def min_cpu_platform(self) -> typing.Optional[builtins.str]:
        '''Minimum CPU platform to be used by this instance.

        The instance may be scheduled on the specified or newer CPU platform.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#min_cpu_platform GoogleContainerNodePool#min_cpu_platform}
        '''
        result = self._values.get("min_cpu_platform")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_group(self) -> typing.Optional[builtins.str]:
        '''Setting this field will assign instances of this pool to run on the specified node group.

        This is useful for running workloads on sole tenant nodes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#node_group GoogleContainerNodePool#node_group}
        '''
        result = self._values.get("node_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The set of Google API scopes to be made available on all of the node VMs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#oauth_scopes GoogleContainerNodePool#oauth_scopes}
        '''
        result = self._values.get("oauth_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def preemptible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether the nodes are created as preemptible VM instances.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#preemptible GoogleContainerNodePool#preemptible}
        '''
        result = self._values.get("preemptible")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def reservation_affinity(
        self,
    ) -> typing.Optional["GoogleContainerNodePoolNodeConfigReservationAffinity"]:
        '''reservation_affinity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#reservation_affinity GoogleContainerNodePool#reservation_affinity}
        '''
        result = self._values.get("reservation_affinity")
        return typing.cast(typing.Optional["GoogleContainerNodePoolNodeConfigReservationAffinity"], result)

    @builtins.property
    def resource_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The GCE resource labels (a map of key/value pairs) to be applied to the node pool.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#resource_labels GoogleContainerNodePool#resource_labels}
        '''
        result = self._values.get("resource_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def sandbox_config(
        self,
    ) -> typing.Optional["GoogleContainerNodePoolNodeConfigSandboxConfig"]:
        '''sandbox_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#sandbox_config GoogleContainerNodePool#sandbox_config}
        '''
        result = self._values.get("sandbox_config")
        return typing.cast(typing.Optional["GoogleContainerNodePoolNodeConfigSandboxConfig"], result)

    @builtins.property
    def service_account(self) -> typing.Optional[builtins.str]:
        '''The Google Cloud Platform Service Account to be used by the node VMs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#service_account GoogleContainerNodePool#service_account}
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def shielded_instance_config(
        self,
    ) -> typing.Optional["GoogleContainerNodePoolNodeConfigShieldedInstanceConfig"]:
        '''shielded_instance_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#shielded_instance_config GoogleContainerNodePool#shielded_instance_config}
        '''
        result = self._values.get("shielded_instance_config")
        return typing.cast(typing.Optional["GoogleContainerNodePoolNodeConfigShieldedInstanceConfig"], result)

    @builtins.property
    def spot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether the nodes are created as spot VM instances.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#spot GoogleContainerNodePool#spot}
        '''
        result = self._values.get("spot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of instance tags applied to all nodes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#tags GoogleContainerNodePool#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def taint(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleContainerNodePoolNodeConfigTaint"]]]:
        '''List of Kubernetes taints to be applied to each node.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#taint GoogleContainerNodePool#taint}
        '''
        result = self._values.get("taint")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleContainerNodePoolNodeConfigTaint"]]], result)

    @builtins.property
    def workload_metadata_config(
        self,
    ) -> typing.Optional["GoogleContainerNodePoolNodeConfigWorkloadMetadataConfig"]:
        '''workload_metadata_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#workload_metadata_config GoogleContainerNodePool#workload_metadata_config}
        '''
        result = self._values.get("workload_metadata_config")
        return typing.cast(typing.Optional["GoogleContainerNodePoolNodeConfigWorkloadMetadataConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerNodePoolNodeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNodeConfigEphemeralStorageConfig",
    jsii_struct_bases=[],
    name_mapping={"local_ssd_count": "localSsdCount"},
)
class GoogleContainerNodePoolNodeConfigEphemeralStorageConfig:
    def __init__(self, *, local_ssd_count: jsii.Number) -> None:
        '''
        :param local_ssd_count: Number of local SSDs to use to back ephemeral storage. Uses NVMe interfaces. Each local SSD is 375 GB in size. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#local_ssd_count GoogleContainerNodePool#local_ssd_count}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e4de41b3a5eeca70b8a075b44132986bb2842de83e958f57914380eef48945d)
            check_type(argname="argument local_ssd_count", value=local_ssd_count, expected_type=type_hints["local_ssd_count"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "local_ssd_count": local_ssd_count,
        }

    @builtins.property
    def local_ssd_count(self) -> jsii.Number:
        '''Number of local SSDs to use to back ephemeral storage.

        Uses NVMe interfaces. Each local SSD is 375 GB in size.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#local_ssd_count GoogleContainerNodePool#local_ssd_count}
        '''
        result = self._values.get("local_ssd_count")
        assert result is not None, "Required property 'local_ssd_count' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerNodePoolNodeConfigEphemeralStorageConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerNodePoolNodeConfigEphemeralStorageConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNodeConfigEphemeralStorageConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__344c60f8b220c63426f707c185c087ba749eed3c7c69515f211bddf3ef036e85)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="localSsdCountInput")
    def local_ssd_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "localSsdCountInput"))

    @builtins.property
    @jsii.member(jsii_name="localSsdCount")
    def local_ssd_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "localSsdCount"))

    @local_ssd_count.setter
    def local_ssd_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__019b87e238833b05dc5c8fdac2040bebafbf42a3608f08329418747f6eb82e8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localSsdCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleContainerNodePoolNodeConfigEphemeralStorageConfig]:
        return typing.cast(typing.Optional[GoogleContainerNodePoolNodeConfigEphemeralStorageConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleContainerNodePoolNodeConfigEphemeralStorageConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6b4cfd6ade39b17c0cc0b5cd8ea7c183a365615a792af8a143710e1d207dfe4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNodeConfigGcfsConfig",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class GoogleContainerNodePoolNodeConfigGcfsConfig:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param enabled: Whether or not GCFS is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#enabled GoogleContainerNodePool#enabled}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1b709504c119dee33ef8ff6ab54d0395563750ab640de101fb3ead0f8d935e9)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Whether or not GCFS is enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#enabled GoogleContainerNodePool#enabled}
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerNodePoolNodeConfigGcfsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerNodePoolNodeConfigGcfsConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNodeConfigGcfsConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e48fa4e7df987f256ed87baef93dc10b06d7f67979a84d114596e6e99b251c37)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__da39bf9303463707f2509086f4cb45679818c58710b7099c3d8405facb33cf03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleContainerNodePoolNodeConfigGcfsConfig]:
        return typing.cast(typing.Optional[GoogleContainerNodePoolNodeConfigGcfsConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleContainerNodePoolNodeConfigGcfsConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20727639c6efea9f563e4281e2802bbc316b01bd4f3541a4b0e1bf5537eecf2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNodeConfigGuestAccelerator",
    jsii_struct_bases=[],
    name_mapping={
        "count": "count",
        "gpu_partition_size": "gpuPartitionSize",
        "gpu_sharing_config": "gpuSharingConfig",
        "type": "type",
    },
)
class GoogleContainerNodePoolNodeConfigGuestAccelerator:
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        gpu_partition_size: typing.Optional[builtins.str] = None,
        gpu_sharing_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfig", typing.Dict[builtins.str, typing.Any]]]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#count GoogleContainerNodePool#count}.
        :param gpu_partition_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#gpu_partition_size GoogleContainerNodePool#gpu_partition_size}.
        :param gpu_sharing_config: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#gpu_sharing_config GoogleContainerNodePool#gpu_sharing_config}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#type GoogleContainerNodePool#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5371a78d3348f7984f3252a3b413a231d4d0d94d0af67d13539e315d1941f3ce)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument gpu_partition_size", value=gpu_partition_size, expected_type=type_hints["gpu_partition_size"])
            check_type(argname="argument gpu_sharing_config", value=gpu_sharing_config, expected_type=type_hints["gpu_sharing_config"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if gpu_partition_size is not None:
            self._values["gpu_partition_size"] = gpu_partition_size
        if gpu_sharing_config is not None:
            self._values["gpu_sharing_config"] = gpu_sharing_config
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#count GoogleContainerNodePool#count}.'''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def gpu_partition_size(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#gpu_partition_size GoogleContainerNodePool#gpu_partition_size}.'''
        result = self._values.get("gpu_partition_size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gpu_sharing_config(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfig"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#gpu_sharing_config GoogleContainerNodePool#gpu_sharing_config}.'''
        result = self._values.get("gpu_sharing_config")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfig"]]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#type GoogleContainerNodePool#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerNodePoolNodeConfigGuestAccelerator(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfig",
    jsii_struct_bases=[],
    name_mapping={
        "gpu_sharing_strategy": "gpuSharingStrategy",
        "max_shared_clients_per_gpu": "maxSharedClientsPerGpu",
    },
)
class GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfig:
    def __init__(
        self,
        *,
        gpu_sharing_strategy: typing.Optional[builtins.str] = None,
        max_shared_clients_per_gpu: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param gpu_sharing_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#gpu_sharing_strategy GoogleContainerNodePool#gpu_sharing_strategy}.
        :param max_shared_clients_per_gpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#max_shared_clients_per_gpu GoogleContainerNodePool#max_shared_clients_per_gpu}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__681761950d528de7826057d9ef1c2f105d6ede87838fa1e6c8a4d24479466885)
            check_type(argname="argument gpu_sharing_strategy", value=gpu_sharing_strategy, expected_type=type_hints["gpu_sharing_strategy"])
            check_type(argname="argument max_shared_clients_per_gpu", value=max_shared_clients_per_gpu, expected_type=type_hints["max_shared_clients_per_gpu"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if gpu_sharing_strategy is not None:
            self._values["gpu_sharing_strategy"] = gpu_sharing_strategy
        if max_shared_clients_per_gpu is not None:
            self._values["max_shared_clients_per_gpu"] = max_shared_clients_per_gpu

    @builtins.property
    def gpu_sharing_strategy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#gpu_sharing_strategy GoogleContainerNodePool#gpu_sharing_strategy}.'''
        result = self._values.get("gpu_sharing_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_shared_clients_per_gpu(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#max_shared_clients_per_gpu GoogleContainerNodePool#max_shared_clients_per_gpu}.'''
        result = self._values.get("max_shared_clients_per_gpu")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfigList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfigList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6fd51b11c7edc42244c969f64096f54e1019cc51f820ae7ee9413c5257b85eef)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__737aea2c25f9e00ff88935d7282e7cdf989192415dcac7a959bd28baa3536561)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf00de5e527da2ee4e1665be36f2e253d353db6f484896563d944bdc649c4728)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e2bade05c35cabd6101274af69bcec19be8eb0d6076edb2ae4f32734dda98a4f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__11bb92eb940f14117c2ee1724005f927d33aaca2ba6a9e339202527d1d6ebf8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfig]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfig]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfig]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83c792f0c4111dd26d8ef85d34a9ff7052d2b34ab3cb04c3ded772b3c0a07da8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb760b365268447fe30cad3acfd57cf6c28dcb846a40eb7ee790c19e8a668024)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetGpuSharingStrategy")
    def reset_gpu_sharing_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGpuSharingStrategy", []))

    @jsii.member(jsii_name="resetMaxSharedClientsPerGpu")
    def reset_max_shared_clients_per_gpu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxSharedClientsPerGpu", []))

    @builtins.property
    @jsii.member(jsii_name="gpuSharingStrategyInput")
    def gpu_sharing_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gpuSharingStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="maxSharedClientsPerGpuInput")
    def max_shared_clients_per_gpu_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxSharedClientsPerGpuInput"))

    @builtins.property
    @jsii.member(jsii_name="gpuSharingStrategy")
    def gpu_sharing_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gpuSharingStrategy"))

    @gpu_sharing_strategy.setter
    def gpu_sharing_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1db7dae7e97c577e68472b3506cb4ecb4c3d191569185d972803008ef790eb5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gpuSharingStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="maxSharedClientsPerGpu")
    def max_shared_clients_per_gpu(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxSharedClientsPerGpu"))

    @max_shared_clients_per_gpu.setter
    def max_shared_clients_per_gpu(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cdef1c0518a7c9fdfde9088b5d7ddd782a3196c57ebb9fc8628a5711c824547)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxSharedClientsPerGpu", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfig, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfig, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfig, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4b626e52af88754879d936808df10f9ce6fd33cb3fc20fc36b1f049bd8a27d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleContainerNodePoolNodeConfigGuestAcceleratorList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNodeConfigGuestAcceleratorList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dd296edd6212e1afff0426f1b33eee419329d7f930e96bb23c33f053351f5ef9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleContainerNodePoolNodeConfigGuestAcceleratorOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28d6be7ca89367e72ecb1910247d2e24d9b35b970887843cecff78cd31831680)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleContainerNodePoolNodeConfigGuestAcceleratorOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7ea263de560bb796241fbd1b0e58bf4605847182743e213dc72216ee43af68b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1a0134108a27f693ae7d8fb8cddf87d44fa8bfd0714e153df56890d98d83eefe)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b392f148eb02a59634e2119dbf341fd9b17c7098d58097200b4d2ec7150db008)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleContainerNodePoolNodeConfigGuestAccelerator]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleContainerNodePoolNodeConfigGuestAccelerator]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleContainerNodePoolNodeConfigGuestAccelerator]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6525e8399f8fa6ced47f29d699211eebeb5f8b114df9b7a05649df8c8ff2bc21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleContainerNodePoolNodeConfigGuestAcceleratorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNodeConfigGuestAcceleratorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ce672a064851ab01a2bb45f73a5243a5686380cc0bff14f08e506404a46cfc7e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putGpuSharingConfig")
    def put_gpu_sharing_config(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfig, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f46579e330aa61211cd9c024af53b6326e800ce4b4d54c31b7967acf09239ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGpuSharingConfig", [value]))

    @jsii.member(jsii_name="resetCount")
    def reset_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCount", []))

    @jsii.member(jsii_name="resetGpuPartitionSize")
    def reset_gpu_partition_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGpuPartitionSize", []))

    @jsii.member(jsii_name="resetGpuSharingConfig")
    def reset_gpu_sharing_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGpuSharingConfig", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="gpuSharingConfig")
    def gpu_sharing_config(
        self,
    ) -> GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfigList:
        return typing.cast(GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfigList, jsii.get(self, "gpuSharingConfig"))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="gpuPartitionSizeInput")
    def gpu_partition_size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gpuPartitionSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="gpuSharingConfigInput")
    def gpu_sharing_config_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfig]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfig]]], jsii.get(self, "gpuSharingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11f02a0d59b4e0d4f71412b0fbe11b32913e0729875e3ceb3966acd60f13023d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="gpuPartitionSize")
    def gpu_partition_size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gpuPartitionSize"))

    @gpu_partition_size.setter
    def gpu_partition_size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b9ba13b7c6bc01e03cf3e8f07c920e343308d293a0fc5d618174d757c60175f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gpuPartitionSize", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ec2dbd50590745f9d559e0e173dd0bc81d1b6c88a1c7d2e7e95018d4289df5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleContainerNodePoolNodeConfigGuestAccelerator, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleContainerNodePoolNodeConfigGuestAccelerator, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleContainerNodePoolNodeConfigGuestAccelerator, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3250a4ba2d60a794d39355578b33a5271f4f826cb6e0d3a616c68298132b3013)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNodeConfigGvnic",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class GoogleContainerNodePoolNodeConfigGvnic:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param enabled: Whether or not gvnic is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#enabled GoogleContainerNodePool#enabled}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a784eba60afd6892f06ce6edd56de6874823ff2cd61e7ad7a3102dd310100cf2)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Whether or not gvnic is enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#enabled GoogleContainerNodePool#enabled}
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerNodePoolNodeConfigGvnic(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerNodePoolNodeConfigGvnicOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNodeConfigGvnicOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5a0d7ebc71ac66550adb434ded1f0aca8ddcb306ec0f62e42d97b842a24de60a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__5ca809342a91d202196945d7a5c097493b8a6e576ad3ec0a6b9fe3572f33b911)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleContainerNodePoolNodeConfigGvnic]:
        return typing.cast(typing.Optional[GoogleContainerNodePoolNodeConfigGvnic], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleContainerNodePoolNodeConfigGvnic],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c85b741cbf8ae3ee9473ebbf2343cf8d2efa077678545556e8de91d7b4f628c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNodeConfigKubeletConfig",
    jsii_struct_bases=[],
    name_mapping={
        "cpu_manager_policy": "cpuManagerPolicy",
        "cpu_cfs_quota": "cpuCfsQuota",
        "cpu_cfs_quota_period": "cpuCfsQuotaPeriod",
    },
)
class GoogleContainerNodePoolNodeConfigKubeletConfig:
    def __init__(
        self,
        *,
        cpu_manager_policy: builtins.str,
        cpu_cfs_quota: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cpu_cfs_quota_period: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cpu_manager_policy: Control the CPU management policy on the node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#cpu_manager_policy GoogleContainerNodePool#cpu_manager_policy}
        :param cpu_cfs_quota: Enable CPU CFS quota enforcement for containers that specify CPU limits. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#cpu_cfs_quota GoogleContainerNodePool#cpu_cfs_quota}
        :param cpu_cfs_quota_period: Set the CPU CFS quota period value 'cpu.cfs_period_us'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#cpu_cfs_quota_period GoogleContainerNodePool#cpu_cfs_quota_period}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34db26051499479a18ff1e6dc64f594f6dcae2949fd17e7e3473c9b06d80726d)
            check_type(argname="argument cpu_manager_policy", value=cpu_manager_policy, expected_type=type_hints["cpu_manager_policy"])
            check_type(argname="argument cpu_cfs_quota", value=cpu_cfs_quota, expected_type=type_hints["cpu_cfs_quota"])
            check_type(argname="argument cpu_cfs_quota_period", value=cpu_cfs_quota_period, expected_type=type_hints["cpu_cfs_quota_period"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cpu_manager_policy": cpu_manager_policy,
        }
        if cpu_cfs_quota is not None:
            self._values["cpu_cfs_quota"] = cpu_cfs_quota
        if cpu_cfs_quota_period is not None:
            self._values["cpu_cfs_quota_period"] = cpu_cfs_quota_period

    @builtins.property
    def cpu_manager_policy(self) -> builtins.str:
        '''Control the CPU management policy on the node.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#cpu_manager_policy GoogleContainerNodePool#cpu_manager_policy}
        '''
        result = self._values.get("cpu_manager_policy")
        assert result is not None, "Required property 'cpu_manager_policy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cpu_cfs_quota(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enable CPU CFS quota enforcement for containers that specify CPU limits.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#cpu_cfs_quota GoogleContainerNodePool#cpu_cfs_quota}
        '''
        result = self._values.get("cpu_cfs_quota")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def cpu_cfs_quota_period(self) -> typing.Optional[builtins.str]:
        '''Set the CPU CFS quota period value 'cpu.cfs_period_us'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#cpu_cfs_quota_period GoogleContainerNodePool#cpu_cfs_quota_period}
        '''
        result = self._values.get("cpu_cfs_quota_period")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerNodePoolNodeConfigKubeletConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerNodePoolNodeConfigKubeletConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNodeConfigKubeletConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c6d0bf9edeb1c08edf2cfe8c2355ac0d7f0beb7abac47803138a966c6bb7be8c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCpuCfsQuota")
    def reset_cpu_cfs_quota(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuCfsQuota", []))

    @jsii.member(jsii_name="resetCpuCfsQuotaPeriod")
    def reset_cpu_cfs_quota_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuCfsQuotaPeriod", []))

    @builtins.property
    @jsii.member(jsii_name="cpuCfsQuotaInput")
    def cpu_cfs_quota_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "cpuCfsQuotaInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuCfsQuotaPeriodInput")
    def cpu_cfs_quota_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cpuCfsQuotaPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuManagerPolicyInput")
    def cpu_manager_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cpuManagerPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuCfsQuota")
    def cpu_cfs_quota(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "cpuCfsQuota"))

    @cpu_cfs_quota.setter
    def cpu_cfs_quota(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d6c6d46f20646f7da20479d097f77be95fd7ae9a5beb7af3e109cf2406eb758)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuCfsQuota", value)

    @builtins.property
    @jsii.member(jsii_name="cpuCfsQuotaPeriod")
    def cpu_cfs_quota_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cpuCfsQuotaPeriod"))

    @cpu_cfs_quota_period.setter
    def cpu_cfs_quota_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0fa442bad972a2c29cb7b2e17328a1c0828f6a2fe63e66491143b4d5f6599df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuCfsQuotaPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="cpuManagerPolicy")
    def cpu_manager_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cpuManagerPolicy"))

    @cpu_manager_policy.setter
    def cpu_manager_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d56e058197a0ee50991ace50fac3578496896e48e24a819597e69b49bc730abe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuManagerPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleContainerNodePoolNodeConfigKubeletConfig]:
        return typing.cast(typing.Optional[GoogleContainerNodePoolNodeConfigKubeletConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleContainerNodePoolNodeConfigKubeletConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d30880a0d548ca19268a3873ba14d341efcd3daa24050f2dd7826b406e5d0c89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNodeConfigLinuxNodeConfig",
    jsii_struct_bases=[],
    name_mapping={"sysctls": "sysctls"},
)
class GoogleContainerNodePoolNodeConfigLinuxNodeConfig:
    def __init__(self, *, sysctls: typing.Mapping[builtins.str, builtins.str]) -> None:
        '''
        :param sysctls: The Linux kernel parameters to be applied to the nodes and all pods running on the nodes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#sysctls GoogleContainerNodePool#sysctls}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a712ff524db4e52be373615e9bd7f1e34a126a9685238d1ef0a28b04661f4da)
            check_type(argname="argument sysctls", value=sysctls, expected_type=type_hints["sysctls"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "sysctls": sysctls,
        }

    @builtins.property
    def sysctls(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''The Linux kernel parameters to be applied to the nodes and all pods running on the nodes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#sysctls GoogleContainerNodePool#sysctls}
        '''
        result = self._values.get("sysctls")
        assert result is not None, "Required property 'sysctls' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerNodePoolNodeConfigLinuxNodeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerNodePoolNodeConfigLinuxNodeConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNodeConfigLinuxNodeConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4478269cb6a32f3df965ffc117217f6f41204ca47b623cb874c6d5c106c2cfce)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="sysctlsInput")
    def sysctls_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "sysctlsInput"))

    @builtins.property
    @jsii.member(jsii_name="sysctls")
    def sysctls(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "sysctls"))

    @sysctls.setter
    def sysctls(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9919da74f17a45705ac745cf25042d4fc5962c02aa38dfcd13375668fa424b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sysctls", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleContainerNodePoolNodeConfigLinuxNodeConfig]:
        return typing.cast(typing.Optional[GoogleContainerNodePoolNodeConfigLinuxNodeConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleContainerNodePoolNodeConfigLinuxNodeConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a3daa46502f797d8e0408b364a42d8e8374bd42fd5bd93306d52f36c97d2bb4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleContainerNodePoolNodeConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNodeConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__083a2dc299fe6145c85bfe549560b3684f3c8c908254f492952cf089b05da164)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putEphemeralStorageConfig")
    def put_ephemeral_storage_config(self, *, local_ssd_count: jsii.Number) -> None:
        '''
        :param local_ssd_count: Number of local SSDs to use to back ephemeral storage. Uses NVMe interfaces. Each local SSD is 375 GB in size. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#local_ssd_count GoogleContainerNodePool#local_ssd_count}
        '''
        value = GoogleContainerNodePoolNodeConfigEphemeralStorageConfig(
            local_ssd_count=local_ssd_count
        )

        return typing.cast(None, jsii.invoke(self, "putEphemeralStorageConfig", [value]))

    @jsii.member(jsii_name="putGcfsConfig")
    def put_gcfs_config(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param enabled: Whether or not GCFS is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#enabled GoogleContainerNodePool#enabled}
        '''
        value = GoogleContainerNodePoolNodeConfigGcfsConfig(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putGcfsConfig", [value]))

    @jsii.member(jsii_name="putGuestAccelerator")
    def put_guest_accelerator(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleContainerNodePoolNodeConfigGuestAccelerator, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__430914745b249e68eef82335fa5df4f1ec0f5c9c715cae42d0ef9564525c8856)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGuestAccelerator", [value]))

    @jsii.member(jsii_name="putGvnic")
    def put_gvnic(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param enabled: Whether or not gvnic is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#enabled GoogleContainerNodePool#enabled}
        '''
        value = GoogleContainerNodePoolNodeConfigGvnic(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putGvnic", [value]))

    @jsii.member(jsii_name="putKubeletConfig")
    def put_kubelet_config(
        self,
        *,
        cpu_manager_policy: builtins.str,
        cpu_cfs_quota: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cpu_cfs_quota_period: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cpu_manager_policy: Control the CPU management policy on the node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#cpu_manager_policy GoogleContainerNodePool#cpu_manager_policy}
        :param cpu_cfs_quota: Enable CPU CFS quota enforcement for containers that specify CPU limits. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#cpu_cfs_quota GoogleContainerNodePool#cpu_cfs_quota}
        :param cpu_cfs_quota_period: Set the CPU CFS quota period value 'cpu.cfs_period_us'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#cpu_cfs_quota_period GoogleContainerNodePool#cpu_cfs_quota_period}
        '''
        value = GoogleContainerNodePoolNodeConfigKubeletConfig(
            cpu_manager_policy=cpu_manager_policy,
            cpu_cfs_quota=cpu_cfs_quota,
            cpu_cfs_quota_period=cpu_cfs_quota_period,
        )

        return typing.cast(None, jsii.invoke(self, "putKubeletConfig", [value]))

    @jsii.member(jsii_name="putLinuxNodeConfig")
    def put_linux_node_config(
        self,
        *,
        sysctls: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        '''
        :param sysctls: The Linux kernel parameters to be applied to the nodes and all pods running on the nodes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#sysctls GoogleContainerNodePool#sysctls}
        '''
        value = GoogleContainerNodePoolNodeConfigLinuxNodeConfig(sysctls=sysctls)

        return typing.cast(None, jsii.invoke(self, "putLinuxNodeConfig", [value]))

    @jsii.member(jsii_name="putReservationAffinity")
    def put_reservation_affinity(
        self,
        *,
        consume_reservation_type: builtins.str,
        key: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param consume_reservation_type: Corresponds to the type of reservation consumption. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#consume_reservation_type GoogleContainerNodePool#consume_reservation_type}
        :param key: The label key of a reservation resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#key GoogleContainerNodePool#key}
        :param values: The label values of the reservation resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#values GoogleContainerNodePool#values}
        '''
        value = GoogleContainerNodePoolNodeConfigReservationAffinity(
            consume_reservation_type=consume_reservation_type, key=key, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putReservationAffinity", [value]))

    @jsii.member(jsii_name="putSandboxConfig")
    def put_sandbox_config(self, *, sandbox_type: builtins.str) -> None:
        '''
        :param sandbox_type: Type of the sandbox to use for the node (e.g. 'gvisor'). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#sandbox_type GoogleContainerNodePool#sandbox_type}
        '''
        value = GoogleContainerNodePoolNodeConfigSandboxConfig(
            sandbox_type=sandbox_type
        )

        return typing.cast(None, jsii.invoke(self, "putSandboxConfig", [value]))

    @jsii.member(jsii_name="putShieldedInstanceConfig")
    def put_shielded_instance_config(
        self,
        *,
        enable_integrity_monitoring: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_secure_boot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enable_integrity_monitoring: Defines whether the instance has integrity monitoring enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#enable_integrity_monitoring GoogleContainerNodePool#enable_integrity_monitoring}
        :param enable_secure_boot: Defines whether the instance has Secure Boot enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#enable_secure_boot GoogleContainerNodePool#enable_secure_boot}
        '''
        value = GoogleContainerNodePoolNodeConfigShieldedInstanceConfig(
            enable_integrity_monitoring=enable_integrity_monitoring,
            enable_secure_boot=enable_secure_boot,
        )

        return typing.cast(None, jsii.invoke(self, "putShieldedInstanceConfig", [value]))

    @jsii.member(jsii_name="putTaint")
    def put_taint(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleContainerNodePoolNodeConfigTaint", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fc7a8e8b61631a29f9319151abe11b15733da3854e6d474ad8a514e2097f3d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTaint", [value]))

    @jsii.member(jsii_name="putWorkloadMetadataConfig")
    def put_workload_metadata_config(self, *, mode: builtins.str) -> None:
        '''
        :param mode: Mode is the configuration for how to expose metadata to workloads running on the node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#mode GoogleContainerNodePool#mode}
        '''
        value = GoogleContainerNodePoolNodeConfigWorkloadMetadataConfig(mode=mode)

        return typing.cast(None, jsii.invoke(self, "putWorkloadMetadataConfig", [value]))

    @jsii.member(jsii_name="resetBootDiskKmsKey")
    def reset_boot_disk_kms_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootDiskKmsKey", []))

    @jsii.member(jsii_name="resetDiskSizeGb")
    def reset_disk_size_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskSizeGb", []))

    @jsii.member(jsii_name="resetDiskType")
    def reset_disk_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskType", []))

    @jsii.member(jsii_name="resetEphemeralStorageConfig")
    def reset_ephemeral_storage_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEphemeralStorageConfig", []))

    @jsii.member(jsii_name="resetGcfsConfig")
    def reset_gcfs_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcfsConfig", []))

    @jsii.member(jsii_name="resetGuestAccelerator")
    def reset_guest_accelerator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGuestAccelerator", []))

    @jsii.member(jsii_name="resetGvnic")
    def reset_gvnic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGvnic", []))

    @jsii.member(jsii_name="resetImageType")
    def reset_image_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageType", []))

    @jsii.member(jsii_name="resetKubeletConfig")
    def reset_kubelet_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKubeletConfig", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetLinuxNodeConfig")
    def reset_linux_node_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinuxNodeConfig", []))

    @jsii.member(jsii_name="resetLocalSsdCount")
    def reset_local_ssd_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalSsdCount", []))

    @jsii.member(jsii_name="resetLoggingVariant")
    def reset_logging_variant(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoggingVariant", []))

    @jsii.member(jsii_name="resetMachineType")
    def reset_machine_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMachineType", []))

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

    @jsii.member(jsii_name="resetMinCpuPlatform")
    def reset_min_cpu_platform(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinCpuPlatform", []))

    @jsii.member(jsii_name="resetNodeGroup")
    def reset_node_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeGroup", []))

    @jsii.member(jsii_name="resetOauthScopes")
    def reset_oauth_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthScopes", []))

    @jsii.member(jsii_name="resetPreemptible")
    def reset_preemptible(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreemptible", []))

    @jsii.member(jsii_name="resetReservationAffinity")
    def reset_reservation_affinity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReservationAffinity", []))

    @jsii.member(jsii_name="resetResourceLabels")
    def reset_resource_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceLabels", []))

    @jsii.member(jsii_name="resetSandboxConfig")
    def reset_sandbox_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSandboxConfig", []))

    @jsii.member(jsii_name="resetServiceAccount")
    def reset_service_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccount", []))

    @jsii.member(jsii_name="resetShieldedInstanceConfig")
    def reset_shielded_instance_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShieldedInstanceConfig", []))

    @jsii.member(jsii_name="resetSpot")
    def reset_spot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpot", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTaint")
    def reset_taint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaint", []))

    @jsii.member(jsii_name="resetWorkloadMetadataConfig")
    def reset_workload_metadata_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkloadMetadataConfig", []))

    @builtins.property
    @jsii.member(jsii_name="ephemeralStorageConfig")
    def ephemeral_storage_config(
        self,
    ) -> GoogleContainerNodePoolNodeConfigEphemeralStorageConfigOutputReference:
        return typing.cast(GoogleContainerNodePoolNodeConfigEphemeralStorageConfigOutputReference, jsii.get(self, "ephemeralStorageConfig"))

    @builtins.property
    @jsii.member(jsii_name="gcfsConfig")
    def gcfs_config(self) -> GoogleContainerNodePoolNodeConfigGcfsConfigOutputReference:
        return typing.cast(GoogleContainerNodePoolNodeConfigGcfsConfigOutputReference, jsii.get(self, "gcfsConfig"))

    @builtins.property
    @jsii.member(jsii_name="guestAccelerator")
    def guest_accelerator(
        self,
    ) -> GoogleContainerNodePoolNodeConfigGuestAcceleratorList:
        return typing.cast(GoogleContainerNodePoolNodeConfigGuestAcceleratorList, jsii.get(self, "guestAccelerator"))

    @builtins.property
    @jsii.member(jsii_name="gvnic")
    def gvnic(self) -> GoogleContainerNodePoolNodeConfigGvnicOutputReference:
        return typing.cast(GoogleContainerNodePoolNodeConfigGvnicOutputReference, jsii.get(self, "gvnic"))

    @builtins.property
    @jsii.member(jsii_name="kubeletConfig")
    def kubelet_config(
        self,
    ) -> GoogleContainerNodePoolNodeConfigKubeletConfigOutputReference:
        return typing.cast(GoogleContainerNodePoolNodeConfigKubeletConfigOutputReference, jsii.get(self, "kubeletConfig"))

    @builtins.property
    @jsii.member(jsii_name="linuxNodeConfig")
    def linux_node_config(
        self,
    ) -> GoogleContainerNodePoolNodeConfigLinuxNodeConfigOutputReference:
        return typing.cast(GoogleContainerNodePoolNodeConfigLinuxNodeConfigOutputReference, jsii.get(self, "linuxNodeConfig"))

    @builtins.property
    @jsii.member(jsii_name="reservationAffinity")
    def reservation_affinity(
        self,
    ) -> "GoogleContainerNodePoolNodeConfigReservationAffinityOutputReference":
        return typing.cast("GoogleContainerNodePoolNodeConfigReservationAffinityOutputReference", jsii.get(self, "reservationAffinity"))

    @builtins.property
    @jsii.member(jsii_name="sandboxConfig")
    def sandbox_config(
        self,
    ) -> "GoogleContainerNodePoolNodeConfigSandboxConfigOutputReference":
        return typing.cast("GoogleContainerNodePoolNodeConfigSandboxConfigOutputReference", jsii.get(self, "sandboxConfig"))

    @builtins.property
    @jsii.member(jsii_name="shieldedInstanceConfig")
    def shielded_instance_config(
        self,
    ) -> "GoogleContainerNodePoolNodeConfigShieldedInstanceConfigOutputReference":
        return typing.cast("GoogleContainerNodePoolNodeConfigShieldedInstanceConfigOutputReference", jsii.get(self, "shieldedInstanceConfig"))

    @builtins.property
    @jsii.member(jsii_name="taint")
    def taint(self) -> "GoogleContainerNodePoolNodeConfigTaintList":
        return typing.cast("GoogleContainerNodePoolNodeConfigTaintList", jsii.get(self, "taint"))

    @builtins.property
    @jsii.member(jsii_name="workloadMetadataConfig")
    def workload_metadata_config(
        self,
    ) -> "GoogleContainerNodePoolNodeConfigWorkloadMetadataConfigOutputReference":
        return typing.cast("GoogleContainerNodePoolNodeConfigWorkloadMetadataConfigOutputReference", jsii.get(self, "workloadMetadataConfig"))

    @builtins.property
    @jsii.member(jsii_name="bootDiskKmsKeyInput")
    def boot_disk_kms_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bootDiskKmsKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="diskSizeGbInput")
    def disk_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="diskTypeInput")
    def disk_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="ephemeralStorageConfigInput")
    def ephemeral_storage_config_input(
        self,
    ) -> typing.Optional[GoogleContainerNodePoolNodeConfigEphemeralStorageConfig]:
        return typing.cast(typing.Optional[GoogleContainerNodePoolNodeConfigEphemeralStorageConfig], jsii.get(self, "ephemeralStorageConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="gcfsConfigInput")
    def gcfs_config_input(
        self,
    ) -> typing.Optional[GoogleContainerNodePoolNodeConfigGcfsConfig]:
        return typing.cast(typing.Optional[GoogleContainerNodePoolNodeConfigGcfsConfig], jsii.get(self, "gcfsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="guestAcceleratorInput")
    def guest_accelerator_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleContainerNodePoolNodeConfigGuestAccelerator]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleContainerNodePoolNodeConfigGuestAccelerator]]], jsii.get(self, "guestAcceleratorInput"))

    @builtins.property
    @jsii.member(jsii_name="gvnicInput")
    def gvnic_input(self) -> typing.Optional[GoogleContainerNodePoolNodeConfigGvnic]:
        return typing.cast(typing.Optional[GoogleContainerNodePoolNodeConfigGvnic], jsii.get(self, "gvnicInput"))

    @builtins.property
    @jsii.member(jsii_name="imageTypeInput")
    def image_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="kubeletConfigInput")
    def kubelet_config_input(
        self,
    ) -> typing.Optional[GoogleContainerNodePoolNodeConfigKubeletConfig]:
        return typing.cast(typing.Optional[GoogleContainerNodePoolNodeConfigKubeletConfig], jsii.get(self, "kubeletConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="linuxNodeConfigInput")
    def linux_node_config_input(
        self,
    ) -> typing.Optional[GoogleContainerNodePoolNodeConfigLinuxNodeConfig]:
        return typing.cast(typing.Optional[GoogleContainerNodePoolNodeConfigLinuxNodeConfig], jsii.get(self, "linuxNodeConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="localSsdCountInput")
    def local_ssd_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "localSsdCountInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingVariantInput")
    def logging_variant_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loggingVariantInput"))

    @builtins.property
    @jsii.member(jsii_name="machineTypeInput")
    def machine_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "machineTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="minCpuPlatformInput")
    def min_cpu_platform_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minCpuPlatformInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeGroupInput")
    def node_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodeGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthScopesInput")
    def oauth_scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "oauthScopesInput"))

    @builtins.property
    @jsii.member(jsii_name="preemptibleInput")
    def preemptible_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "preemptibleInput"))

    @builtins.property
    @jsii.member(jsii_name="reservationAffinityInput")
    def reservation_affinity_input(
        self,
    ) -> typing.Optional["GoogleContainerNodePoolNodeConfigReservationAffinity"]:
        return typing.cast(typing.Optional["GoogleContainerNodePoolNodeConfigReservationAffinity"], jsii.get(self, "reservationAffinityInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceLabelsInput")
    def resource_labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "resourceLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="sandboxConfigInput")
    def sandbox_config_input(
        self,
    ) -> typing.Optional["GoogleContainerNodePoolNodeConfigSandboxConfig"]:
        return typing.cast(typing.Optional["GoogleContainerNodePoolNodeConfigSandboxConfig"], jsii.get(self, "sandboxConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountInput")
    def service_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="shieldedInstanceConfigInput")
    def shielded_instance_config_input(
        self,
    ) -> typing.Optional["GoogleContainerNodePoolNodeConfigShieldedInstanceConfig"]:
        return typing.cast(typing.Optional["GoogleContainerNodePoolNodeConfigShieldedInstanceConfig"], jsii.get(self, "shieldedInstanceConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="spotInput")
    def spot_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "spotInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="taintInput")
    def taint_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleContainerNodePoolNodeConfigTaint"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleContainerNodePoolNodeConfigTaint"]]], jsii.get(self, "taintInput"))

    @builtins.property
    @jsii.member(jsii_name="workloadMetadataConfigInput")
    def workload_metadata_config_input(
        self,
    ) -> typing.Optional["GoogleContainerNodePoolNodeConfigWorkloadMetadataConfig"]:
        return typing.cast(typing.Optional["GoogleContainerNodePoolNodeConfigWorkloadMetadataConfig"], jsii.get(self, "workloadMetadataConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="bootDiskKmsKey")
    def boot_disk_kms_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bootDiskKmsKey"))

    @boot_disk_kms_key.setter
    def boot_disk_kms_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e682e5865c527f5cb6077013cf771e1c350c2b1174b3fe861a44dd2ff99df6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootDiskKmsKey", value)

    @builtins.property
    @jsii.member(jsii_name="diskSizeGb")
    def disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskSizeGb"))

    @disk_size_gb.setter
    def disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c1fcb99d6f2f8b5faf70392de7d0e5b09973cdf838da97b37a3a66bfb3f0573)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="diskType")
    def disk_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskType"))

    @disk_type.setter
    def disk_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49cd5414ef90e98e356ed3fb10d95c614d01096c1780d1bccb8960bde4754c0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskType", value)

    @builtins.property
    @jsii.member(jsii_name="imageType")
    def image_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageType"))

    @image_type.setter
    def image_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b7af0a4f9d15ba8b06f0307f00574b87fc4a24cfea1e2b9950ca456d2e8698f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageType", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ed1fc1e97d24235af2e23f59a2313b73a795fb82e35f86d683adba3c93603ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="localSsdCount")
    def local_ssd_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "localSsdCount"))

    @local_ssd_count.setter
    def local_ssd_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd31ab7a7ed6e9b548d8610df0a3ad2e2746ae21d1e6745adef23db664b3539d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localSsdCount", value)

    @builtins.property
    @jsii.member(jsii_name="loggingVariant")
    def logging_variant(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loggingVariant"))

    @logging_variant.setter
    def logging_variant(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d3be33935e83a6a3021fac7f119be8890231f4e5008bc3a448464d3f1889e38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loggingVariant", value)

    @builtins.property
    @jsii.member(jsii_name="machineType")
    def machine_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "machineType"))

    @machine_type.setter
    def machine_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2a5c3f62da835a37b7f31b5e4518552a60b06fd62f4f0c26551bb26ced75f5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "machineType", value)

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ec81278e703260ace9aaa7665336a977da1a7214164dc04592374d584f44936)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="minCpuPlatform")
    def min_cpu_platform(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minCpuPlatform"))

    @min_cpu_platform.setter
    def min_cpu_platform(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88e24168b227957a66c71c7055f00119442e623f067ac50714a98c20b24419f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minCpuPlatform", value)

    @builtins.property
    @jsii.member(jsii_name="nodeGroup")
    def node_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeGroup"))

    @node_group.setter
    def node_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2dc69c0db50ecc53a733d01bf1759316d86abca0884cfbfb2f525fe60a54f77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeGroup", value)

    @builtins.property
    @jsii.member(jsii_name="oauthScopes")
    def oauth_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "oauthScopes"))

    @oauth_scopes.setter
    def oauth_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96ff12302b86f1fb4480f4e08f109c82bd19972d642829c4338aeb99095580c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthScopes", value)

    @builtins.property
    @jsii.member(jsii_name="preemptible")
    def preemptible(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "preemptible"))

    @preemptible.setter
    def preemptible(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26b2d8bbc6b9ee59ee1c0371c8927782bd89d1e227d9ca9348a07c938e0b1629)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preemptible", value)

    @builtins.property
    @jsii.member(jsii_name="resourceLabels")
    def resource_labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "resourceLabels"))

    @resource_labels.setter
    def resource_labels(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__005c0f9f55ae67b0657c42b02946f51251557548c7dc54d8e85a54c84fcb2af7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceLabels", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccount")
    def service_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccount"))

    @service_account.setter
    def service_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f76c8a79c7be3e64990423d2732776e857502e27101127c6a64471b583f475e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccount", value)

    @builtins.property
    @jsii.member(jsii_name="spot")
    def spot(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "spot"))

    @spot.setter
    def spot(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a4da15d6e027e9d872b5f17fc10a9f77e4a515bd19fe4c4bbcd1ffb4fc408e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spot", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__172219d24714c011f42cf338aae3f37088bc119a31c76d00cf9d6c41ac217c88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleContainerNodePoolNodeConfig]:
        return typing.cast(typing.Optional[GoogleContainerNodePoolNodeConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleContainerNodePoolNodeConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17c3310f67f012f91ac82a292866e11ef88825d77e88ffc8b2f255c98a5949a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNodeConfigReservationAffinity",
    jsii_struct_bases=[],
    name_mapping={
        "consume_reservation_type": "consumeReservationType",
        "key": "key",
        "values": "values",
    },
)
class GoogleContainerNodePoolNodeConfigReservationAffinity:
    def __init__(
        self,
        *,
        consume_reservation_type: builtins.str,
        key: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param consume_reservation_type: Corresponds to the type of reservation consumption. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#consume_reservation_type GoogleContainerNodePool#consume_reservation_type}
        :param key: The label key of a reservation resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#key GoogleContainerNodePool#key}
        :param values: The label values of the reservation resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#values GoogleContainerNodePool#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4da75a11d74f34a2d86b26a212ef59bbd6ba8b2d25fefa448a97b453892b385e)
            check_type(argname="argument consume_reservation_type", value=consume_reservation_type, expected_type=type_hints["consume_reservation_type"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "consume_reservation_type": consume_reservation_type,
        }
        if key is not None:
            self._values["key"] = key
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def consume_reservation_type(self) -> builtins.str:
        '''Corresponds to the type of reservation consumption.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#consume_reservation_type GoogleContainerNodePool#consume_reservation_type}
        '''
        result = self._values.get("consume_reservation_type")
        assert result is not None, "Required property 'consume_reservation_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The label key of a reservation resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#key GoogleContainerNodePool#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The label values of the reservation resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#values GoogleContainerNodePool#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerNodePoolNodeConfigReservationAffinity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerNodePoolNodeConfigReservationAffinityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNodeConfigReservationAffinityOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__170f0f021381907dbd31821afbf330731a41418450daac7a47860a9ebf6db740)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="consumeReservationTypeInput")
    def consume_reservation_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "consumeReservationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="consumeReservationType")
    def consume_reservation_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consumeReservationType"))

    @consume_reservation_type.setter
    def consume_reservation_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db0a63dd42155c563d781c8d5971df716f889a9bb96fddd2d06695fd9aeece75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consumeReservationType", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc6bed937ed104aa55beafe6dfc3e9ccd423a6ef60082de6c1f74f6f2bdc3840)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8a73ac024dadacc137c35e153b21d62269c06d82418a5c3e461057ca2f8201e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleContainerNodePoolNodeConfigReservationAffinity]:
        return typing.cast(typing.Optional[GoogleContainerNodePoolNodeConfigReservationAffinity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleContainerNodePoolNodeConfigReservationAffinity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f01c015db06843e7ee7c3a12a5c88dadf2e09e1909d1229f0471861874a3ae0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNodeConfigSandboxConfig",
    jsii_struct_bases=[],
    name_mapping={"sandbox_type": "sandboxType"},
)
class GoogleContainerNodePoolNodeConfigSandboxConfig:
    def __init__(self, *, sandbox_type: builtins.str) -> None:
        '''
        :param sandbox_type: Type of the sandbox to use for the node (e.g. 'gvisor'). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#sandbox_type GoogleContainerNodePool#sandbox_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d5c575f7ae9cea24a8a831a10c5e8a5e52e78f25b2f52987ac889ff8b42c7d8)
            check_type(argname="argument sandbox_type", value=sandbox_type, expected_type=type_hints["sandbox_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "sandbox_type": sandbox_type,
        }

    @builtins.property
    def sandbox_type(self) -> builtins.str:
        '''Type of the sandbox to use for the node (e.g. 'gvisor').

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#sandbox_type GoogleContainerNodePool#sandbox_type}
        '''
        result = self._values.get("sandbox_type")
        assert result is not None, "Required property 'sandbox_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerNodePoolNodeConfigSandboxConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerNodePoolNodeConfigSandboxConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNodeConfigSandboxConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f904bcfcc6edf5f3eea0738fee72edf59e1705299f0496d408a9ff62e5b372fa)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="sandboxTypeInput")
    def sandbox_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sandboxTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="sandboxType")
    def sandbox_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sandboxType"))

    @sandbox_type.setter
    def sandbox_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01867d97bdc00764faf098c67627d1c7583763414db4169bd158606a719808eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sandboxType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleContainerNodePoolNodeConfigSandboxConfig]:
        return typing.cast(typing.Optional[GoogleContainerNodePoolNodeConfigSandboxConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleContainerNodePoolNodeConfigSandboxConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc5d8485307675a141340c8478c20b45ef37c503c7e29f2171d65d55e88e91c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNodeConfigShieldedInstanceConfig",
    jsii_struct_bases=[],
    name_mapping={
        "enable_integrity_monitoring": "enableIntegrityMonitoring",
        "enable_secure_boot": "enableSecureBoot",
    },
)
class GoogleContainerNodePoolNodeConfigShieldedInstanceConfig:
    def __init__(
        self,
        *,
        enable_integrity_monitoring: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_secure_boot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enable_integrity_monitoring: Defines whether the instance has integrity monitoring enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#enable_integrity_monitoring GoogleContainerNodePool#enable_integrity_monitoring}
        :param enable_secure_boot: Defines whether the instance has Secure Boot enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#enable_secure_boot GoogleContainerNodePool#enable_secure_boot}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d30d3e12add344b754741b55e899c279f80b43f7669599fa42aa919b682a354)
            check_type(argname="argument enable_integrity_monitoring", value=enable_integrity_monitoring, expected_type=type_hints["enable_integrity_monitoring"])
            check_type(argname="argument enable_secure_boot", value=enable_secure_boot, expected_type=type_hints["enable_secure_boot"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enable_integrity_monitoring is not None:
            self._values["enable_integrity_monitoring"] = enable_integrity_monitoring
        if enable_secure_boot is not None:
            self._values["enable_secure_boot"] = enable_secure_boot

    @builtins.property
    def enable_integrity_monitoring(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Defines whether the instance has integrity monitoring enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#enable_integrity_monitoring GoogleContainerNodePool#enable_integrity_monitoring}
        '''
        result = self._values.get("enable_integrity_monitoring")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_secure_boot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Defines whether the instance has Secure Boot enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#enable_secure_boot GoogleContainerNodePool#enable_secure_boot}
        '''
        result = self._values.get("enable_secure_boot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerNodePoolNodeConfigShieldedInstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerNodePoolNodeConfigShieldedInstanceConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNodeConfigShieldedInstanceConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__074a8824f4189fa0f3b487e51506232a56c64c138a54423f52de07a056d01695)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnableIntegrityMonitoring")
    def reset_enable_integrity_monitoring(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableIntegrityMonitoring", []))

    @jsii.member(jsii_name="resetEnableSecureBoot")
    def reset_enable_secure_boot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableSecureBoot", []))

    @builtins.property
    @jsii.member(jsii_name="enableIntegrityMonitoringInput")
    def enable_integrity_monitoring_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableIntegrityMonitoringInput"))

    @builtins.property
    @jsii.member(jsii_name="enableSecureBootInput")
    def enable_secure_boot_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableSecureBootInput"))

    @builtins.property
    @jsii.member(jsii_name="enableIntegrityMonitoring")
    def enable_integrity_monitoring(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableIntegrityMonitoring"))

    @enable_integrity_monitoring.setter
    def enable_integrity_monitoring(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f12be696c4d1eb3739c5329fc1f57d52002af8d4b1cfe401e10b79038f59288)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableIntegrityMonitoring", value)

    @builtins.property
    @jsii.member(jsii_name="enableSecureBoot")
    def enable_secure_boot(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableSecureBoot"))

    @enable_secure_boot.setter
    def enable_secure_boot(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92f10df846228f3951c9cce63b82187640b521dc7cac4a829bac6ce1673cbccf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableSecureBoot", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleContainerNodePoolNodeConfigShieldedInstanceConfig]:
        return typing.cast(typing.Optional[GoogleContainerNodePoolNodeConfigShieldedInstanceConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleContainerNodePoolNodeConfigShieldedInstanceConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c89a29e3ff2cdffa5769dda9a58b9ff09afac4ba2712fe83ff9d0274a5a783b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNodeConfigTaint",
    jsii_struct_bases=[],
    name_mapping={"effect": "effect", "key": "key", "value": "value"},
)
class GoogleContainerNodePoolNodeConfigTaint:
    def __init__(
        self,
        *,
        effect: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param effect: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#effect GoogleContainerNodePool#effect}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#key GoogleContainerNodePool#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#value GoogleContainerNodePool#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__224f81127254286dab77b4de47c1b26ca36daf23b5392f6fc288c9950e5e0749)
            check_type(argname="argument effect", value=effect, expected_type=type_hints["effect"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if effect is not None:
            self._values["effect"] = effect
        if key is not None:
            self._values["key"] = key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def effect(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#effect GoogleContainerNodePool#effect}.'''
        result = self._values.get("effect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#key GoogleContainerNodePool#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#value GoogleContainerNodePool#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerNodePoolNodeConfigTaint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerNodePoolNodeConfigTaintList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNodeConfigTaintList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__61b5c54ce78178bdbc708afadf1345f2840914436d975a0a2a5d9290c1d8f4dd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleContainerNodePoolNodeConfigTaintOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13320fcdeecd7c12e1b64d7da141bd0c2654a66f65ee4a0bb8fe80b2e354834b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleContainerNodePoolNodeConfigTaintOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5a518fc02367eedf6091f8e392af22576dca52e112c5d8af3c729b193974c8b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__51e3a8a32400b4de02b639ba4fd73b522133b6bbba25d2d8eb12b9173863e72f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4d73f3ab06b109825a617fa3c0e0708763a56b6dfc99da76cde7c2a30c8885d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleContainerNodePoolNodeConfigTaint]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleContainerNodePoolNodeConfigTaint]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleContainerNodePoolNodeConfigTaint]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__487c4224289a73764532f09c809e9b861f987548be9e77f7b649dd1fd952b32d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleContainerNodePoolNodeConfigTaintOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNodeConfigTaintOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2563df036fc207ba1c691a321907288589907b1317b84369decb79173487458f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEffect")
    def reset_effect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEffect", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="effectInput")
    def effect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "effectInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="effect")
    def effect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "effect"))

    @effect.setter
    def effect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ed24bb5735290623c794efe56d216076fabc2dc99fc59d7a7ba69ea53dfabbb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "effect", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cac8133b2281a075a450179ee2621a4b67297454ae0e1c38486dc9c3420ce7a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d86242c967062aa108f0cdfd603457913714ec5e4f9fdc3a581d1562be2cf494)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleContainerNodePoolNodeConfigTaint, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleContainerNodePoolNodeConfigTaint, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleContainerNodePoolNodeConfigTaint, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61614be0f0a57e9f3a0934ff5bf9c0c841e2a2462492fbdbce76cfd1993a00eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNodeConfigWorkloadMetadataConfig",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode"},
)
class GoogleContainerNodePoolNodeConfigWorkloadMetadataConfig:
    def __init__(self, *, mode: builtins.str) -> None:
        '''
        :param mode: Mode is the configuration for how to expose metadata to workloads running on the node. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#mode GoogleContainerNodePool#mode}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b83ab657230f1126004d64d5867a5f41647747550c6d00c4e9ed4c0e2050f56)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mode": mode,
        }

    @builtins.property
    def mode(self) -> builtins.str:
        '''Mode is the configuration for how to expose metadata to workloads running on the node.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#mode GoogleContainerNodePool#mode}
        '''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerNodePoolNodeConfigWorkloadMetadataConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerNodePoolNodeConfigWorkloadMetadataConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolNodeConfigWorkloadMetadataConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bdbcb7e4fd2622518c403b6afdc63db8febc2d492867510537dc11868e123155)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__756f7dcf18b7a5d4e0f183746c7731145bc8035f07c5cceb75fca59e40a71029)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleContainerNodePoolNodeConfigWorkloadMetadataConfig]:
        return typing.cast(typing.Optional[GoogleContainerNodePoolNodeConfigWorkloadMetadataConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleContainerNodePoolNodeConfigWorkloadMetadataConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08ee79e7c3b541b59e59c16bdac5ae15619c863bc855ca42c577d530dde23f60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolPlacementPolicy",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class GoogleContainerNodePoolPlacementPolicy:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: Type defines the type of placement policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#type GoogleContainerNodePool#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66829d3b46e9e34ed947a48c35f153bcb2495c283653c64d6722bad05fa65f60)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''Type defines the type of placement policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#type GoogleContainerNodePool#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerNodePoolPlacementPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerNodePoolPlacementPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolPlacementPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0b047ca53213df25a4d17647a6b862812aa7a87a2abb1832a1dcc198c4d934c7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b43fbe4b3dbdd56b027a35c3c1b3c90592841311d6cdb068468ecc9d0c8a0624)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleContainerNodePoolPlacementPolicy]:
        return typing.cast(typing.Optional[GoogleContainerNodePoolPlacementPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleContainerNodePoolPlacementPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fd5a443fe462b4d296b11941668ef312731e9d206548caed64871f0ef51b2a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleContainerNodePoolTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#create GoogleContainerNodePool#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#delete GoogleContainerNodePool#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#update GoogleContainerNodePool#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1ef94cdeb888213f7213948ef71334530b24d3f312bba6b881e35f29e1149fa)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#create GoogleContainerNodePool#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#delete GoogleContainerNodePool#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#update GoogleContainerNodePool#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerNodePoolTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerNodePoolTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e39882dbed07a22399e5a8ef93f52663a5fb8fa2971465b8012d7d024c1808f9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eb7bedffbf2336aaa1d7db42da2c15e62993a9e6de13ebcfe46f1f2739a4f40c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27ac208a79f53e13719db31308600ca0e682bfa817f0e61161640a69b78de3e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88f22cbc5bdf0d5f8e61e1ad1f489a1d702259be99ac0bd10217b5132fbfa7ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleContainerNodePoolTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleContainerNodePoolTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleContainerNodePoolTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71a28ef4528ea4129ad85a8eee4d552fea146af9634dfd6f190a7090d6ccfba6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolUpgradeSettings",
    jsii_struct_bases=[],
    name_mapping={
        "blue_green_settings": "blueGreenSettings",
        "max_surge": "maxSurge",
        "max_unavailable": "maxUnavailable",
        "strategy": "strategy",
    },
)
class GoogleContainerNodePoolUpgradeSettings:
    def __init__(
        self,
        *,
        blue_green_settings: typing.Optional[typing.Union["GoogleContainerNodePoolUpgradeSettingsBlueGreenSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        max_surge: typing.Optional[jsii.Number] = None,
        max_unavailable: typing.Optional[jsii.Number] = None,
        strategy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param blue_green_settings: blue_green_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#blue_green_settings GoogleContainerNodePool#blue_green_settings}
        :param max_surge: The number of additional nodes that can be added to the node pool during an upgrade. Increasing max_surge raises the number of nodes that can be upgraded simultaneously. Can be set to 0 or greater. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#max_surge GoogleContainerNodePool#max_surge}
        :param max_unavailable: The number of nodes that can be simultaneously unavailable during an upgrade. Increasing max_unavailable raises the number of nodes that can be upgraded in parallel. Can be set to 0 or greater. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#max_unavailable GoogleContainerNodePool#max_unavailable}
        :param strategy: Update strategy for the given nodepool. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#strategy GoogleContainerNodePool#strategy}
        '''
        if isinstance(blue_green_settings, dict):
            blue_green_settings = GoogleContainerNodePoolUpgradeSettingsBlueGreenSettings(**blue_green_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ceae5e61bc3cc59dc916e9a682f0c33b5f2ff9c057244f29f173d2f3c781cfcd)
            check_type(argname="argument blue_green_settings", value=blue_green_settings, expected_type=type_hints["blue_green_settings"])
            check_type(argname="argument max_surge", value=max_surge, expected_type=type_hints["max_surge"])
            check_type(argname="argument max_unavailable", value=max_unavailable, expected_type=type_hints["max_unavailable"])
            check_type(argname="argument strategy", value=strategy, expected_type=type_hints["strategy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if blue_green_settings is not None:
            self._values["blue_green_settings"] = blue_green_settings
        if max_surge is not None:
            self._values["max_surge"] = max_surge
        if max_unavailable is not None:
            self._values["max_unavailable"] = max_unavailable
        if strategy is not None:
            self._values["strategy"] = strategy

    @builtins.property
    def blue_green_settings(
        self,
    ) -> typing.Optional["GoogleContainerNodePoolUpgradeSettingsBlueGreenSettings"]:
        '''blue_green_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#blue_green_settings GoogleContainerNodePool#blue_green_settings}
        '''
        result = self._values.get("blue_green_settings")
        return typing.cast(typing.Optional["GoogleContainerNodePoolUpgradeSettingsBlueGreenSettings"], result)

    @builtins.property
    def max_surge(self) -> typing.Optional[jsii.Number]:
        '''The number of additional nodes that can be added to the node pool during an upgrade.

        Increasing max_surge raises the number of nodes that can be upgraded simultaneously. Can be set to 0 or greater.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#max_surge GoogleContainerNodePool#max_surge}
        '''
        result = self._values.get("max_surge")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_unavailable(self) -> typing.Optional[jsii.Number]:
        '''The number of nodes that can be simultaneously unavailable during an upgrade.

        Increasing max_unavailable raises the number of nodes that can be upgraded in parallel. Can be set to 0 or greater.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#max_unavailable GoogleContainerNodePool#max_unavailable}
        '''
        result = self._values.get("max_unavailable")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def strategy(self) -> typing.Optional[builtins.str]:
        '''Update strategy for the given nodepool.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#strategy GoogleContainerNodePool#strategy}
        '''
        result = self._values.get("strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerNodePoolUpgradeSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolUpgradeSettingsBlueGreenSettings",
    jsii_struct_bases=[],
    name_mapping={
        "standard_rollout_policy": "standardRolloutPolicy",
        "node_pool_soak_duration": "nodePoolSoakDuration",
    },
)
class GoogleContainerNodePoolUpgradeSettingsBlueGreenSettings:
    def __init__(
        self,
        *,
        standard_rollout_policy: typing.Union["GoogleContainerNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicy", typing.Dict[builtins.str, typing.Any]],
        node_pool_soak_duration: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param standard_rollout_policy: standard_rollout_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#standard_rollout_policy GoogleContainerNodePool#standard_rollout_policy}
        :param node_pool_soak_duration: Time needed after draining entire blue pool. After this period, blue pool will be cleaned up. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#node_pool_soak_duration GoogleContainerNodePool#node_pool_soak_duration}
        '''
        if isinstance(standard_rollout_policy, dict):
            standard_rollout_policy = GoogleContainerNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicy(**standard_rollout_policy)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cb7777d935afe680d1432b069a74170722f58d400c5d6bae8cf5ee83193c839)
            check_type(argname="argument standard_rollout_policy", value=standard_rollout_policy, expected_type=type_hints["standard_rollout_policy"])
            check_type(argname="argument node_pool_soak_duration", value=node_pool_soak_duration, expected_type=type_hints["node_pool_soak_duration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "standard_rollout_policy": standard_rollout_policy,
        }
        if node_pool_soak_duration is not None:
            self._values["node_pool_soak_duration"] = node_pool_soak_duration

    @builtins.property
    def standard_rollout_policy(
        self,
    ) -> "GoogleContainerNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicy":
        '''standard_rollout_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#standard_rollout_policy GoogleContainerNodePool#standard_rollout_policy}
        '''
        result = self._values.get("standard_rollout_policy")
        assert result is not None, "Required property 'standard_rollout_policy' is missing"
        return typing.cast("GoogleContainerNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicy", result)

    @builtins.property
    def node_pool_soak_duration(self) -> typing.Optional[builtins.str]:
        '''Time needed after draining entire blue pool. After this period, blue pool will be cleaned up.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#node_pool_soak_duration GoogleContainerNodePool#node_pool_soak_duration}
        '''
        result = self._values.get("node_pool_soak_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerNodePoolUpgradeSettingsBlueGreenSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerNodePoolUpgradeSettingsBlueGreenSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolUpgradeSettingsBlueGreenSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__975413c35d8f76a098165bfb01a950161b321e0c75067cc05deacb7b1b885b0a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putStandardRolloutPolicy")
    def put_standard_rollout_policy(
        self,
        *,
        batch_node_count: typing.Optional[jsii.Number] = None,
        batch_percentage: typing.Optional[jsii.Number] = None,
        batch_soak_duration: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param batch_node_count: Number of blue nodes to drain in a batch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#batch_node_count GoogleContainerNodePool#batch_node_count}
        :param batch_percentage: Percentage of the blue pool nodes to drain in a batch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#batch_percentage GoogleContainerNodePool#batch_percentage}
        :param batch_soak_duration: Soak time after each batch gets drained. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#batch_soak_duration GoogleContainerNodePool#batch_soak_duration}
        '''
        value = GoogleContainerNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicy(
            batch_node_count=batch_node_count,
            batch_percentage=batch_percentage,
            batch_soak_duration=batch_soak_duration,
        )

        return typing.cast(None, jsii.invoke(self, "putStandardRolloutPolicy", [value]))

    @jsii.member(jsii_name="resetNodePoolSoakDuration")
    def reset_node_pool_soak_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodePoolSoakDuration", []))

    @builtins.property
    @jsii.member(jsii_name="standardRolloutPolicy")
    def standard_rollout_policy(
        self,
    ) -> "GoogleContainerNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicyOutputReference":
        return typing.cast("GoogleContainerNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicyOutputReference", jsii.get(self, "standardRolloutPolicy"))

    @builtins.property
    @jsii.member(jsii_name="nodePoolSoakDurationInput")
    def node_pool_soak_duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodePoolSoakDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="standardRolloutPolicyInput")
    def standard_rollout_policy_input(
        self,
    ) -> typing.Optional["GoogleContainerNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicy"]:
        return typing.cast(typing.Optional["GoogleContainerNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicy"], jsii.get(self, "standardRolloutPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="nodePoolSoakDuration")
    def node_pool_soak_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodePoolSoakDuration"))

    @node_pool_soak_duration.setter
    def node_pool_soak_duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__080f086450b74f1812863fa7749452bd02f15e322c7e52607b7314c0827032a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodePoolSoakDuration", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleContainerNodePoolUpgradeSettingsBlueGreenSettings]:
        return typing.cast(typing.Optional[GoogleContainerNodePoolUpgradeSettingsBlueGreenSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleContainerNodePoolUpgradeSettingsBlueGreenSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a22fa033c158b27d69c924dca9fc4dcdbda6ee57f888e0b7b9cb1c783cdb0ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "batch_node_count": "batchNodeCount",
        "batch_percentage": "batchPercentage",
        "batch_soak_duration": "batchSoakDuration",
    },
)
class GoogleContainerNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicy:
    def __init__(
        self,
        *,
        batch_node_count: typing.Optional[jsii.Number] = None,
        batch_percentage: typing.Optional[jsii.Number] = None,
        batch_soak_duration: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param batch_node_count: Number of blue nodes to drain in a batch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#batch_node_count GoogleContainerNodePool#batch_node_count}
        :param batch_percentage: Percentage of the blue pool nodes to drain in a batch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#batch_percentage GoogleContainerNodePool#batch_percentage}
        :param batch_soak_duration: Soak time after each batch gets drained. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#batch_soak_duration GoogleContainerNodePool#batch_soak_duration}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfdea5ffda802d3bbb187f7224742a81e717e91a5ac5633bd713ccf96777649a)
            check_type(argname="argument batch_node_count", value=batch_node_count, expected_type=type_hints["batch_node_count"])
            check_type(argname="argument batch_percentage", value=batch_percentage, expected_type=type_hints["batch_percentage"])
            check_type(argname="argument batch_soak_duration", value=batch_soak_duration, expected_type=type_hints["batch_soak_duration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if batch_node_count is not None:
            self._values["batch_node_count"] = batch_node_count
        if batch_percentage is not None:
            self._values["batch_percentage"] = batch_percentage
        if batch_soak_duration is not None:
            self._values["batch_soak_duration"] = batch_soak_duration

    @builtins.property
    def batch_node_count(self) -> typing.Optional[jsii.Number]:
        '''Number of blue nodes to drain in a batch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#batch_node_count GoogleContainerNodePool#batch_node_count}
        '''
        result = self._values.get("batch_node_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def batch_percentage(self) -> typing.Optional[jsii.Number]:
        '''Percentage of the blue pool nodes to drain in a batch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#batch_percentage GoogleContainerNodePool#batch_percentage}
        '''
        result = self._values.get("batch_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def batch_soak_duration(self) -> typing.Optional[builtins.str]:
        '''Soak time after each batch gets drained.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#batch_soak_duration GoogleContainerNodePool#batch_soak_duration}
        '''
        result = self._values.get("batch_soak_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleContainerNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleContainerNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ff7dd6f6285e246eac4553ab4fc1eabf036ab80023078edd608b44cfbaa3bf3a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBatchNodeCount")
    def reset_batch_node_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBatchNodeCount", []))

    @jsii.member(jsii_name="resetBatchPercentage")
    def reset_batch_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBatchPercentage", []))

    @jsii.member(jsii_name="resetBatchSoakDuration")
    def reset_batch_soak_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBatchSoakDuration", []))

    @builtins.property
    @jsii.member(jsii_name="batchNodeCountInput")
    def batch_node_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "batchNodeCountInput"))

    @builtins.property
    @jsii.member(jsii_name="batchPercentageInput")
    def batch_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "batchPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="batchSoakDurationInput")
    def batch_soak_duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "batchSoakDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="batchNodeCount")
    def batch_node_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "batchNodeCount"))

    @batch_node_count.setter
    def batch_node_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d914daea192bb1843251981f75ee70598065a4a112a213960d48dd358824e146)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "batchNodeCount", value)

    @builtins.property
    @jsii.member(jsii_name="batchPercentage")
    def batch_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "batchPercentage"))

    @batch_percentage.setter
    def batch_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__150e87eebd1e95c252804361d33c7a1e54ac7496da6382e90fc5d0f4fb80b9ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "batchPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="batchSoakDuration")
    def batch_soak_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "batchSoakDuration"))

    @batch_soak_duration.setter
    def batch_soak_duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f850a3f97a53065baa853ce3d75553b3b1865f6ca8bae624609e41ff81cc30b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "batchSoakDuration", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleContainerNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicy]:
        return typing.cast(typing.Optional[GoogleContainerNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleContainerNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae4472d403b2b910e73b907304d86a2587537c5fa185b9e88b2681be791bce06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleContainerNodePoolUpgradeSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleContainerNodePool.GoogleContainerNodePoolUpgradeSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3e9cbb60d7267d7b5aad81fd5ac5f26206942d6efcb21601ab3851af01f971c0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBlueGreenSettings")
    def put_blue_green_settings(
        self,
        *,
        standard_rollout_policy: typing.Union[GoogleContainerNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicy, typing.Dict[builtins.str, typing.Any]],
        node_pool_soak_duration: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param standard_rollout_policy: standard_rollout_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#standard_rollout_policy GoogleContainerNodePool#standard_rollout_policy}
        :param node_pool_soak_duration: Time needed after draining entire blue pool. After this period, blue pool will be cleaned up. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_container_node_pool#node_pool_soak_duration GoogleContainerNodePool#node_pool_soak_duration}
        '''
        value = GoogleContainerNodePoolUpgradeSettingsBlueGreenSettings(
            standard_rollout_policy=standard_rollout_policy,
            node_pool_soak_duration=node_pool_soak_duration,
        )

        return typing.cast(None, jsii.invoke(self, "putBlueGreenSettings", [value]))

    @jsii.member(jsii_name="resetBlueGreenSettings")
    def reset_blue_green_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlueGreenSettings", []))

    @jsii.member(jsii_name="resetMaxSurge")
    def reset_max_surge(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxSurge", []))

    @jsii.member(jsii_name="resetMaxUnavailable")
    def reset_max_unavailable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxUnavailable", []))

    @jsii.member(jsii_name="resetStrategy")
    def reset_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStrategy", []))

    @builtins.property
    @jsii.member(jsii_name="blueGreenSettings")
    def blue_green_settings(
        self,
    ) -> GoogleContainerNodePoolUpgradeSettingsBlueGreenSettingsOutputReference:
        return typing.cast(GoogleContainerNodePoolUpgradeSettingsBlueGreenSettingsOutputReference, jsii.get(self, "blueGreenSettings"))

    @builtins.property
    @jsii.member(jsii_name="blueGreenSettingsInput")
    def blue_green_settings_input(
        self,
    ) -> typing.Optional[GoogleContainerNodePoolUpgradeSettingsBlueGreenSettings]:
        return typing.cast(typing.Optional[GoogleContainerNodePoolUpgradeSettingsBlueGreenSettings], jsii.get(self, "blueGreenSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxSurgeInput")
    def max_surge_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxSurgeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxUnavailableInput")
    def max_unavailable_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxUnavailableInput"))

    @builtins.property
    @jsii.member(jsii_name="strategyInput")
    def strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "strategyInput"))

    @builtins.property
    @jsii.member(jsii_name="maxSurge")
    def max_surge(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxSurge"))

    @max_surge.setter
    def max_surge(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a0f76de9420c1b0da4ee7596557afa2b7ab40740872486c60e22a63302386db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxSurge", value)

    @builtins.property
    @jsii.member(jsii_name="maxUnavailable")
    def max_unavailable(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxUnavailable"))

    @max_unavailable.setter
    def max_unavailable(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8a3c174eaed15632662bbf0c80e1277d7a274d7f9de61c12c53ccd30c0028a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxUnavailable", value)

    @builtins.property
    @jsii.member(jsii_name="strategy")
    def strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "strategy"))

    @strategy.setter
    def strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e904f0c512e74ca592a65049e65941ad77f8ec9474837bc15446885effa1a290)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "strategy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleContainerNodePoolUpgradeSettings]:
        return typing.cast(typing.Optional[GoogleContainerNodePoolUpgradeSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleContainerNodePoolUpgradeSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b3e2aae4f43753f568b0caea8bdc1f1b7a226adcc5c592138e1e5c9756de06a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleContainerNodePool",
    "GoogleContainerNodePoolAutoscaling",
    "GoogleContainerNodePoolAutoscalingOutputReference",
    "GoogleContainerNodePoolConfig",
    "GoogleContainerNodePoolManagement",
    "GoogleContainerNodePoolManagementOutputReference",
    "GoogleContainerNodePoolNetworkConfig",
    "GoogleContainerNodePoolNetworkConfigOutputReference",
    "GoogleContainerNodePoolNodeConfig",
    "GoogleContainerNodePoolNodeConfigEphemeralStorageConfig",
    "GoogleContainerNodePoolNodeConfigEphemeralStorageConfigOutputReference",
    "GoogleContainerNodePoolNodeConfigGcfsConfig",
    "GoogleContainerNodePoolNodeConfigGcfsConfigOutputReference",
    "GoogleContainerNodePoolNodeConfigGuestAccelerator",
    "GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfig",
    "GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfigList",
    "GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfigOutputReference",
    "GoogleContainerNodePoolNodeConfigGuestAcceleratorList",
    "GoogleContainerNodePoolNodeConfigGuestAcceleratorOutputReference",
    "GoogleContainerNodePoolNodeConfigGvnic",
    "GoogleContainerNodePoolNodeConfigGvnicOutputReference",
    "GoogleContainerNodePoolNodeConfigKubeletConfig",
    "GoogleContainerNodePoolNodeConfigKubeletConfigOutputReference",
    "GoogleContainerNodePoolNodeConfigLinuxNodeConfig",
    "GoogleContainerNodePoolNodeConfigLinuxNodeConfigOutputReference",
    "GoogleContainerNodePoolNodeConfigOutputReference",
    "GoogleContainerNodePoolNodeConfigReservationAffinity",
    "GoogleContainerNodePoolNodeConfigReservationAffinityOutputReference",
    "GoogleContainerNodePoolNodeConfigSandboxConfig",
    "GoogleContainerNodePoolNodeConfigSandboxConfigOutputReference",
    "GoogleContainerNodePoolNodeConfigShieldedInstanceConfig",
    "GoogleContainerNodePoolNodeConfigShieldedInstanceConfigOutputReference",
    "GoogleContainerNodePoolNodeConfigTaint",
    "GoogleContainerNodePoolNodeConfigTaintList",
    "GoogleContainerNodePoolNodeConfigTaintOutputReference",
    "GoogleContainerNodePoolNodeConfigWorkloadMetadataConfig",
    "GoogleContainerNodePoolNodeConfigWorkloadMetadataConfigOutputReference",
    "GoogleContainerNodePoolPlacementPolicy",
    "GoogleContainerNodePoolPlacementPolicyOutputReference",
    "GoogleContainerNodePoolTimeouts",
    "GoogleContainerNodePoolTimeoutsOutputReference",
    "GoogleContainerNodePoolUpgradeSettings",
    "GoogleContainerNodePoolUpgradeSettingsBlueGreenSettings",
    "GoogleContainerNodePoolUpgradeSettingsBlueGreenSettingsOutputReference",
    "GoogleContainerNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicy",
    "GoogleContainerNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicyOutputReference",
    "GoogleContainerNodePoolUpgradeSettingsOutputReference",
]

publication.publish()

def _typecheckingstub__f75cf1f4c113470aebc6bebc3ac0bd156d49a6d1cd6f50e192de6ed4291c711f(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    cluster: builtins.str,
    autoscaling: typing.Optional[typing.Union[GoogleContainerNodePoolAutoscaling, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    initial_node_count: typing.Optional[jsii.Number] = None,
    location: typing.Optional[builtins.str] = None,
    management: typing.Optional[typing.Union[GoogleContainerNodePoolManagement, typing.Dict[builtins.str, typing.Any]]] = None,
    max_pods_per_node: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    name_prefix: typing.Optional[builtins.str] = None,
    network_config: typing.Optional[typing.Union[GoogleContainerNodePoolNetworkConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    node_config: typing.Optional[typing.Union[GoogleContainerNodePoolNodeConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    node_count: typing.Optional[jsii.Number] = None,
    node_locations: typing.Optional[typing.Sequence[builtins.str]] = None,
    placement_policy: typing.Optional[typing.Union[GoogleContainerNodePoolPlacementPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    project: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[GoogleContainerNodePoolTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    upgrade_settings: typing.Optional[typing.Union[GoogleContainerNodePoolUpgradeSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    version: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__81585b084a75592c5e3706d4af74e68f36aa22552975bfc892fabe709cd68a93(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c48c4bf2a2e4b93438ccc44e9e308390e16c2f93480729af0864bf8fcdb7794(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c61929a40bb8705acf4362b8eaf62f2baafd7567509c759af365e149731a020(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__704c1758a74418784eae7802f36846db75082e7402be0ebfa99e848d7f40c078(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2c02dee5f56c3abdc39bb4e8bff7e7810c84b6b802fc3ad1ed11a0cdcd53bc2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__415f2d44014be5f55268a27092218cbdfa10c6db46eff6f23725b42d3d7b28f4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3d9c0c424628c611ef7cf1e04ee271b3e5085940c2d1ef9a8ee6ca572735e77(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80ecfcd52d0067562ef6c905b0ce3c1cb7dce917af196328f8cf80bcffb9778b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__816e68d06296456ca033c553ee6656cb4a59fd19d5e07d2fe98f8620fab55da1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfed50f56cb91855a1001533be060dc5ad6cbdd28d8308e6734de92794386f47(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84e6080263da48bee69e742df775d7961bc11f1f69da78eca068c2632dfa54a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62328d6aae5eae7f3d514da0e78b03c79612e2e5f431951301ae48f85e56bab6(
    *,
    location_policy: typing.Optional[builtins.str] = None,
    max_node_count: typing.Optional[jsii.Number] = None,
    min_node_count: typing.Optional[jsii.Number] = None,
    total_max_node_count: typing.Optional[jsii.Number] = None,
    total_min_node_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea6e7409413f0fc48829caa13d817fd8015042db5fadbbbdfe306cc470b16230(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0c15ce7b2fe3ff14ba262606cf60c325f83fa6c6553f7be2686039f8ea3b0f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91f7cb34e10e8a57ff9e3ba6c95adc6369aaf96b12061399856f9f6ace845e0d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__487660a99f7c64d19c4190435a15b38388a4da154a4661c594e749bbb6bee17c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5aaa234adc7ed238d1b00176d3cad8de2e782a4a36e27414cb0651b7f1f3ff75(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__515d47a796a60062d7644cae62cb074d21be87201210aea0c046c701e5540a04(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb9a1cc5dfd72df0873603c99766e896fdbe8dcf5f4aef19ba20980d351b4041(
    value: typing.Optional[GoogleContainerNodePoolAutoscaling],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ea29e6dbff83ef660066146f8c46000f2e00cb18bdc726304a3af1ba3895fbe(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cluster: builtins.str,
    autoscaling: typing.Optional[typing.Union[GoogleContainerNodePoolAutoscaling, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    initial_node_count: typing.Optional[jsii.Number] = None,
    location: typing.Optional[builtins.str] = None,
    management: typing.Optional[typing.Union[GoogleContainerNodePoolManagement, typing.Dict[builtins.str, typing.Any]]] = None,
    max_pods_per_node: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    name_prefix: typing.Optional[builtins.str] = None,
    network_config: typing.Optional[typing.Union[GoogleContainerNodePoolNetworkConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    node_config: typing.Optional[typing.Union[GoogleContainerNodePoolNodeConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    node_count: typing.Optional[jsii.Number] = None,
    node_locations: typing.Optional[typing.Sequence[builtins.str]] = None,
    placement_policy: typing.Optional[typing.Union[GoogleContainerNodePoolPlacementPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    project: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[GoogleContainerNodePoolTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    upgrade_settings: typing.Optional[typing.Union[GoogleContainerNodePoolUpgradeSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf662b569af6c32395030e1a62cb8531d6641c45b30b92fe348b218de7658497(
    *,
    auto_repair: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    auto_upgrade: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aab11aa58f47591b5a7f082a3b5abeddb63a02a365fb84966dc36fd6654a8299(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__435f8fabeac9592a57908302f97e6e5268f60ac9d6b2be5802a49cbb3debed1c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29fb9077729ae66d34d07b367bdea13e3cf79db36d53a7e0cacac9fb3106dc18(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ed1eb8fc1eb08adaf661424db47ad79f9030d9dcb8d9e913a3c3c6f7d8f41ad(
    value: typing.Optional[GoogleContainerNodePoolManagement],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eed8a5d314ec03f5556cab7d069325b6923f0374080c64eb741ae1245cb45d5c(
    *,
    create_pod_range: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_private_nodes: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    pod_ipv4_cidr_block: typing.Optional[builtins.str] = None,
    pod_range: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86ab47c099914e4d193e3ce84817fba39f48f162ab5d644a8f692b1135d4eb49(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1508f8ee2ce08b8323c5176b5638d953797d29df6548da0cf78e3e321de31b46(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14a0cfca3262e83c0e154372d222247345ed04f4c2e2266f03b60acefaba6d3f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7579b112e2f8956c9323cbde9c6225ba942280f541f9a94cf18adf7083cce62d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8bd9618d182a54a7314488aeda425a360a6040213e325fab75b28b3562ce8bd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dede1c406015eb91bc1ef6b774a5c323f0705bb993708882c958e72423c6e2e(
    value: typing.Optional[GoogleContainerNodePoolNetworkConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa1fcd02cbce130e12742899615c9eba8ee7c5fbe33fdb8aaf3b5ba306a4073c(
    *,
    boot_disk_kms_key: typing.Optional[builtins.str] = None,
    disk_size_gb: typing.Optional[jsii.Number] = None,
    disk_type: typing.Optional[builtins.str] = None,
    ephemeral_storage_config: typing.Optional[typing.Union[GoogleContainerNodePoolNodeConfigEphemeralStorageConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    gcfs_config: typing.Optional[typing.Union[GoogleContainerNodePoolNodeConfigGcfsConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    guest_accelerator: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleContainerNodePoolNodeConfigGuestAccelerator, typing.Dict[builtins.str, typing.Any]]]]] = None,
    gvnic: typing.Optional[typing.Union[GoogleContainerNodePoolNodeConfigGvnic, typing.Dict[builtins.str, typing.Any]]] = None,
    image_type: typing.Optional[builtins.str] = None,
    kubelet_config: typing.Optional[typing.Union[GoogleContainerNodePoolNodeConfigKubeletConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    linux_node_config: typing.Optional[typing.Union[GoogleContainerNodePoolNodeConfigLinuxNodeConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    local_ssd_count: typing.Optional[jsii.Number] = None,
    logging_variant: typing.Optional[builtins.str] = None,
    machine_type: typing.Optional[builtins.str] = None,
    metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    min_cpu_platform: typing.Optional[builtins.str] = None,
    node_group: typing.Optional[builtins.str] = None,
    oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    preemptible: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    reservation_affinity: typing.Optional[typing.Union[GoogleContainerNodePoolNodeConfigReservationAffinity, typing.Dict[builtins.str, typing.Any]]] = None,
    resource_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    sandbox_config: typing.Optional[typing.Union[GoogleContainerNodePoolNodeConfigSandboxConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    service_account: typing.Optional[builtins.str] = None,
    shielded_instance_config: typing.Optional[typing.Union[GoogleContainerNodePoolNodeConfigShieldedInstanceConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    spot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    taint: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleContainerNodePoolNodeConfigTaint, typing.Dict[builtins.str, typing.Any]]]]] = None,
    workload_metadata_config: typing.Optional[typing.Union[GoogleContainerNodePoolNodeConfigWorkloadMetadataConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e4de41b3a5eeca70b8a075b44132986bb2842de83e958f57914380eef48945d(
    *,
    local_ssd_count: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__344c60f8b220c63426f707c185c087ba749eed3c7c69515f211bddf3ef036e85(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__019b87e238833b05dc5c8fdac2040bebafbf42a3608f08329418747f6eb82e8d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6b4cfd6ade39b17c0cc0b5cd8ea7c183a365615a792af8a143710e1d207dfe4(
    value: typing.Optional[GoogleContainerNodePoolNodeConfigEphemeralStorageConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1b709504c119dee33ef8ff6ab54d0395563750ab640de101fb3ead0f8d935e9(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e48fa4e7df987f256ed87baef93dc10b06d7f67979a84d114596e6e99b251c37(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da39bf9303463707f2509086f4cb45679818c58710b7099c3d8405facb33cf03(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20727639c6efea9f563e4281e2802bbc316b01bd4f3541a4b0e1bf5537eecf2e(
    value: typing.Optional[GoogleContainerNodePoolNodeConfigGcfsConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5371a78d3348f7984f3252a3b413a231d4d0d94d0af67d13539e315d1941f3ce(
    *,
    count: typing.Optional[jsii.Number] = None,
    gpu_partition_size: typing.Optional[builtins.str] = None,
    gpu_sharing_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfig, typing.Dict[builtins.str, typing.Any]]]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__681761950d528de7826057d9ef1c2f105d6ede87838fa1e6c8a4d24479466885(
    *,
    gpu_sharing_strategy: typing.Optional[builtins.str] = None,
    max_shared_clients_per_gpu: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fd51b11c7edc42244c969f64096f54e1019cc51f820ae7ee9413c5257b85eef(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__737aea2c25f9e00ff88935d7282e7cdf989192415dcac7a959bd28baa3536561(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf00de5e527da2ee4e1665be36f2e253d353db6f484896563d944bdc649c4728(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2bade05c35cabd6101274af69bcec19be8eb0d6076edb2ae4f32734dda98a4f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11bb92eb940f14117c2ee1724005f927d33aaca2ba6a9e339202527d1d6ebf8c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83c792f0c4111dd26d8ef85d34a9ff7052d2b34ab3cb04c3ded772b3c0a07da8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfig]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb760b365268447fe30cad3acfd57cf6c28dcb846a40eb7ee790c19e8a668024(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1db7dae7e97c577e68472b3506cb4ecb4c3d191569185d972803008ef790eb5b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cdef1c0518a7c9fdfde9088b5d7ddd782a3196c57ebb9fc8628a5711c824547(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4b626e52af88754879d936808df10f9ce6fd33cb3fc20fc36b1f049bd8a27d3(
    value: typing.Optional[typing.Union[GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfig, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd296edd6212e1afff0426f1b33eee419329d7f930e96bb23c33f053351f5ef9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28d6be7ca89367e72ecb1910247d2e24d9b35b970887843cecff78cd31831680(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7ea263de560bb796241fbd1b0e58bf4605847182743e213dc72216ee43af68b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a0134108a27f693ae7d8fb8cddf87d44fa8bfd0714e153df56890d98d83eefe(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b392f148eb02a59634e2119dbf341fd9b17c7098d58097200b4d2ec7150db008(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6525e8399f8fa6ced47f29d699211eebeb5f8b114df9b7a05649df8c8ff2bc21(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleContainerNodePoolNodeConfigGuestAccelerator]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce672a064851ab01a2bb45f73a5243a5686380cc0bff14f08e506404a46cfc7e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f46579e330aa61211cd9c024af53b6326e800ce4b4d54c31b7967acf09239ec(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleContainerNodePoolNodeConfigGuestAcceleratorGpuSharingConfig, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11f02a0d59b4e0d4f71412b0fbe11b32913e0729875e3ceb3966acd60f13023d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b9ba13b7c6bc01e03cf3e8f07c920e343308d293a0fc5d618174d757c60175f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ec2dbd50590745f9d559e0e173dd0bc81d1b6c88a1c7d2e7e95018d4289df5f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3250a4ba2d60a794d39355578b33a5271f4f826cb6e0d3a616c68298132b3013(
    value: typing.Optional[typing.Union[GoogleContainerNodePoolNodeConfigGuestAccelerator, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a784eba60afd6892f06ce6edd56de6874823ff2cd61e7ad7a3102dd310100cf2(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a0d7ebc71ac66550adb434ded1f0aca8ddcb306ec0f62e42d97b842a24de60a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ca809342a91d202196945d7a5c097493b8a6e576ad3ec0a6b9fe3572f33b911(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c85b741cbf8ae3ee9473ebbf2343cf8d2efa077678545556e8de91d7b4f628c8(
    value: typing.Optional[GoogleContainerNodePoolNodeConfigGvnic],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34db26051499479a18ff1e6dc64f594f6dcae2949fd17e7e3473c9b06d80726d(
    *,
    cpu_manager_policy: builtins.str,
    cpu_cfs_quota: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cpu_cfs_quota_period: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6d0bf9edeb1c08edf2cfe8c2355ac0d7f0beb7abac47803138a966c6bb7be8c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d6c6d46f20646f7da20479d097f77be95fd7ae9a5beb7af3e109cf2406eb758(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0fa442bad972a2c29cb7b2e17328a1c0828f6a2fe63e66491143b4d5f6599df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d56e058197a0ee50991ace50fac3578496896e48e24a819597e69b49bc730abe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d30880a0d548ca19268a3873ba14d341efcd3daa24050f2dd7826b406e5d0c89(
    value: typing.Optional[GoogleContainerNodePoolNodeConfigKubeletConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a712ff524db4e52be373615e9bd7f1e34a126a9685238d1ef0a28b04661f4da(
    *,
    sysctls: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4478269cb6a32f3df965ffc117217f6f41204ca47b623cb874c6d5c106c2cfce(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9919da74f17a45705ac745cf25042d4fc5962c02aa38dfcd13375668fa424b1(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a3daa46502f797d8e0408b364a42d8e8374bd42fd5bd93306d52f36c97d2bb4(
    value: typing.Optional[GoogleContainerNodePoolNodeConfigLinuxNodeConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__083a2dc299fe6145c85bfe549560b3684f3c8c908254f492952cf089b05da164(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__430914745b249e68eef82335fa5df4f1ec0f5c9c715cae42d0ef9564525c8856(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleContainerNodePoolNodeConfigGuestAccelerator, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fc7a8e8b61631a29f9319151abe11b15733da3854e6d474ad8a514e2097f3d0(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleContainerNodePoolNodeConfigTaint, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e682e5865c527f5cb6077013cf771e1c350c2b1174b3fe861a44dd2ff99df6c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c1fcb99d6f2f8b5faf70392de7d0e5b09973cdf838da97b37a3a66bfb3f0573(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49cd5414ef90e98e356ed3fb10d95c614d01096c1780d1bccb8960bde4754c0d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b7af0a4f9d15ba8b06f0307f00574b87fc4a24cfea1e2b9950ca456d2e8698f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ed1fc1e97d24235af2e23f59a2313b73a795fb82e35f86d683adba3c93603ee(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd31ab7a7ed6e9b548d8610df0a3ad2e2746ae21d1e6745adef23db664b3539d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d3be33935e83a6a3021fac7f119be8890231f4e5008bc3a448464d3f1889e38(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2a5c3f62da835a37b7f31b5e4518552a60b06fd62f4f0c26551bb26ced75f5f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ec81278e703260ace9aaa7665336a977da1a7214164dc04592374d584f44936(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88e24168b227957a66c71c7055f00119442e623f067ac50714a98c20b24419f4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2dc69c0db50ecc53a733d01bf1759316d86abca0884cfbfb2f525fe60a54f77(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96ff12302b86f1fb4480f4e08f109c82bd19972d642829c4338aeb99095580c3(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26b2d8bbc6b9ee59ee1c0371c8927782bd89d1e227d9ca9348a07c938e0b1629(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__005c0f9f55ae67b0657c42b02946f51251557548c7dc54d8e85a54c84fcb2af7(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f76c8a79c7be3e64990423d2732776e857502e27101127c6a64471b583f475e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a4da15d6e027e9d872b5f17fc10a9f77e4a515bd19fe4c4bbcd1ffb4fc408e0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__172219d24714c011f42cf338aae3f37088bc119a31c76d00cf9d6c41ac217c88(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17c3310f67f012f91ac82a292866e11ef88825d77e88ffc8b2f255c98a5949a8(
    value: typing.Optional[GoogleContainerNodePoolNodeConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4da75a11d74f34a2d86b26a212ef59bbd6ba8b2d25fefa448a97b453892b385e(
    *,
    consume_reservation_type: builtins.str,
    key: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__170f0f021381907dbd31821afbf330731a41418450daac7a47860a9ebf6db740(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db0a63dd42155c563d781c8d5971df716f889a9bb96fddd2d06695fd9aeece75(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc6bed937ed104aa55beafe6dfc3e9ccd423a6ef60082de6c1f74f6f2bdc3840(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8a73ac024dadacc137c35e153b21d62269c06d82418a5c3e461057ca2f8201e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f01c015db06843e7ee7c3a12a5c88dadf2e09e1909d1229f0471861874a3ae0(
    value: typing.Optional[GoogleContainerNodePoolNodeConfigReservationAffinity],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d5c575f7ae9cea24a8a831a10c5e8a5e52e78f25b2f52987ac889ff8b42c7d8(
    *,
    sandbox_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f904bcfcc6edf5f3eea0738fee72edf59e1705299f0496d408a9ff62e5b372fa(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01867d97bdc00764faf098c67627d1c7583763414db4169bd158606a719808eb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc5d8485307675a141340c8478c20b45ef37c503c7e29f2171d65d55e88e91c3(
    value: typing.Optional[GoogleContainerNodePoolNodeConfigSandboxConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d30d3e12add344b754741b55e899c279f80b43f7669599fa42aa919b682a354(
    *,
    enable_integrity_monitoring: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_secure_boot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__074a8824f4189fa0f3b487e51506232a56c64c138a54423f52de07a056d01695(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f12be696c4d1eb3739c5329fc1f57d52002af8d4b1cfe401e10b79038f59288(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92f10df846228f3951c9cce63b82187640b521dc7cac4a829bac6ce1673cbccf(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c89a29e3ff2cdffa5769dda9a58b9ff09afac4ba2712fe83ff9d0274a5a783b(
    value: typing.Optional[GoogleContainerNodePoolNodeConfigShieldedInstanceConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__224f81127254286dab77b4de47c1b26ca36daf23b5392f6fc288c9950e5e0749(
    *,
    effect: typing.Optional[builtins.str] = None,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61b5c54ce78178bdbc708afadf1345f2840914436d975a0a2a5d9290c1d8f4dd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13320fcdeecd7c12e1b64d7da141bd0c2654a66f65ee4a0bb8fe80b2e354834b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5a518fc02367eedf6091f8e392af22576dca52e112c5d8af3c729b193974c8b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51e3a8a32400b4de02b639ba4fd73b522133b6bbba25d2d8eb12b9173863e72f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d73f3ab06b109825a617fa3c0e0708763a56b6dfc99da76cde7c2a30c8885d4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__487c4224289a73764532f09c809e9b861f987548be9e77f7b649dd1fd952b32d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleContainerNodePoolNodeConfigTaint]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2563df036fc207ba1c691a321907288589907b1317b84369decb79173487458f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ed24bb5735290623c794efe56d216076fabc2dc99fc59d7a7ba69ea53dfabbb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cac8133b2281a075a450179ee2621a4b67297454ae0e1c38486dc9c3420ce7a8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d86242c967062aa108f0cdfd603457913714ec5e4f9fdc3a581d1562be2cf494(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61614be0f0a57e9f3a0934ff5bf9c0c841e2a2462492fbdbce76cfd1993a00eb(
    value: typing.Optional[typing.Union[GoogleContainerNodePoolNodeConfigTaint, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b83ab657230f1126004d64d5867a5f41647747550c6d00c4e9ed4c0e2050f56(
    *,
    mode: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdbcb7e4fd2622518c403b6afdc63db8febc2d492867510537dc11868e123155(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__756f7dcf18b7a5d4e0f183746c7731145bc8035f07c5cceb75fca59e40a71029(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08ee79e7c3b541b59e59c16bdac5ae15619c863bc855ca42c577d530dde23f60(
    value: typing.Optional[GoogleContainerNodePoolNodeConfigWorkloadMetadataConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66829d3b46e9e34ed947a48c35f153bcb2495c283653c64d6722bad05fa65f60(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b047ca53213df25a4d17647a6b862812aa7a87a2abb1832a1dcc198c4d934c7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b43fbe4b3dbdd56b027a35c3c1b3c90592841311d6cdb068468ecc9d0c8a0624(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fd5a443fe462b4d296b11941668ef312731e9d206548caed64871f0ef51b2a6(
    value: typing.Optional[GoogleContainerNodePoolPlacementPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1ef94cdeb888213f7213948ef71334530b24d3f312bba6b881e35f29e1149fa(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e39882dbed07a22399e5a8ef93f52663a5fb8fa2971465b8012d7d024c1808f9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb7bedffbf2336aaa1d7db42da2c15e62993a9e6de13ebcfe46f1f2739a4f40c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27ac208a79f53e13719db31308600ca0e682bfa817f0e61161640a69b78de3e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88f22cbc5bdf0d5f8e61e1ad1f489a1d702259be99ac0bd10217b5132fbfa7ef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71a28ef4528ea4129ad85a8eee4d552fea146af9634dfd6f190a7090d6ccfba6(
    value: typing.Optional[typing.Union[GoogleContainerNodePoolTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ceae5e61bc3cc59dc916e9a682f0c33b5f2ff9c057244f29f173d2f3c781cfcd(
    *,
    blue_green_settings: typing.Optional[typing.Union[GoogleContainerNodePoolUpgradeSettingsBlueGreenSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    max_surge: typing.Optional[jsii.Number] = None,
    max_unavailable: typing.Optional[jsii.Number] = None,
    strategy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cb7777d935afe680d1432b069a74170722f58d400c5d6bae8cf5ee83193c839(
    *,
    standard_rollout_policy: typing.Union[GoogleContainerNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicy, typing.Dict[builtins.str, typing.Any]],
    node_pool_soak_duration: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__975413c35d8f76a098165bfb01a950161b321e0c75067cc05deacb7b1b885b0a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__080f086450b74f1812863fa7749452bd02f15e322c7e52607b7314c0827032a8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a22fa033c158b27d69c924dca9fc4dcdbda6ee57f888e0b7b9cb1c783cdb0ee(
    value: typing.Optional[GoogleContainerNodePoolUpgradeSettingsBlueGreenSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfdea5ffda802d3bbb187f7224742a81e717e91a5ac5633bd713ccf96777649a(
    *,
    batch_node_count: typing.Optional[jsii.Number] = None,
    batch_percentage: typing.Optional[jsii.Number] = None,
    batch_soak_duration: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff7dd6f6285e246eac4553ab4fc1eabf036ab80023078edd608b44cfbaa3bf3a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d914daea192bb1843251981f75ee70598065a4a112a213960d48dd358824e146(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__150e87eebd1e95c252804361d33c7a1e54ac7496da6382e90fc5d0f4fb80b9ec(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f850a3f97a53065baa853ce3d75553b3b1865f6ca8bae624609e41ff81cc30b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae4472d403b2b910e73b907304d86a2587537c5fa185b9e88b2681be791bce06(
    value: typing.Optional[GoogleContainerNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e9cbb60d7267d7b5aad81fd5ac5f26206942d6efcb21601ab3851af01f971c0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a0f76de9420c1b0da4ee7596557afa2b7ab40740872486c60e22a63302386db(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8a3c174eaed15632662bbf0c80e1277d7a274d7f9de61c12c53ccd30c0028a3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e904f0c512e74ca592a65049e65941ad77f8ec9474837bc15446885effa1a290(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b3e2aae4f43753f568b0caea8bdc1f1b7a226adcc5c592138e1e5c9756de06a(
    value: typing.Optional[GoogleContainerNodePoolUpgradeSettings],
) -> None:
    """Type checking stubs"""
    pass
