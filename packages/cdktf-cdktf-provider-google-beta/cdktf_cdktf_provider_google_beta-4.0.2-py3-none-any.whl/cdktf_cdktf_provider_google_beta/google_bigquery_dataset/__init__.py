'''
# `google_bigquery_dataset`

Refer to the Terraform Registory for docs: [`google_bigquery_dataset`](https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset).
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


class GoogleBigqueryDataset(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryDataset.GoogleBigqueryDataset",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset google_bigquery_dataset}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        dataset_id: builtins.str,
        access: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleBigqueryDatasetAccess", typing.Dict[builtins.str, typing.Any]]]]] = None,
        default_encryption_configuration: typing.Optional[typing.Union["GoogleBigqueryDatasetDefaultEncryptionConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        default_partition_expiration_ms: typing.Optional[jsii.Number] = None,
        default_table_expiration_ms: typing.Optional[jsii.Number] = None,
        delete_contents_on_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        friendly_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        location: typing.Optional[builtins.str] = None,
        max_time_travel_hours: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleBigqueryDatasetTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset google_bigquery_dataset} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param dataset_id: A unique ID for this dataset, without the project name. The ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_). The maximum length is 1,024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#dataset_id GoogleBigqueryDataset#dataset_id}
        :param access: access block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#access GoogleBigqueryDataset#access}
        :param default_encryption_configuration: default_encryption_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#default_encryption_configuration GoogleBigqueryDataset#default_encryption_configuration}
        :param default_partition_expiration_ms: The default partition expiration for all partitioned tables in the dataset, in milliseconds. Once this property is set, all newly-created partitioned tables in the dataset will have an 'expirationMs' property in the 'timePartitioning' settings set to this value, and changing the value will only affect new tables, not existing ones. The storage in a partition will have an expiration time of its partition time plus this value. Setting this property overrides the use of 'defaultTableExpirationMs' for partitioned tables: only one of 'defaultTableExpirationMs' and 'defaultPartitionExpirationMs' will be used for any new partitioned table. If you provide an explicit 'timePartitioning.expirationMs' when creating or updating a partitioned table, that value takes precedence over the default partition expiration time indicated by this property. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#default_partition_expiration_ms GoogleBigqueryDataset#default_partition_expiration_ms}
        :param default_table_expiration_ms: The default lifetime of all tables in the dataset, in milliseconds. The minimum value is 3600000 milliseconds (one hour). Once this property is set, all newly-created tables in the dataset will have an 'expirationTime' property set to the creation time plus the value in this property, and changing the value will only affect new tables, not existing ones. When the 'expirationTime' for a given table is reached, that table will be deleted automatically. If a table's 'expirationTime' is modified or removed before the table expires, or if you provide an explicit 'expirationTime' when creating a table, that value takes precedence over the default expiration time indicated by this property. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#default_table_expiration_ms GoogleBigqueryDataset#default_table_expiration_ms}
        :param delete_contents_on_destroy: If set to 'true', delete all the tables in the dataset when destroying the resource; otherwise, destroying the resource will fail if tables are present. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#delete_contents_on_destroy GoogleBigqueryDataset#delete_contents_on_destroy}
        :param description: A user-friendly description of the dataset. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#description GoogleBigqueryDataset#description}
        :param friendly_name: A descriptive name for the dataset. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#friendly_name GoogleBigqueryDataset#friendly_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#id GoogleBigqueryDataset#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: The labels associated with this dataset. You can use these to organize and group your datasets. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#labels GoogleBigqueryDataset#labels}
        :param location: The geographic location where the dataset should reside. See `official docs <https://cloud.google.com/bigquery/docs/dataset-locations>`_. There are two types of locations, regional or multi-regional. A regional location is a specific geographic place, such as Tokyo, and a multi-regional location is a large geographic area, such as the United States, that contains at least two geographic places. The default value is multi-regional location 'US'. Changing this forces a new resource to be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#location GoogleBigqueryDataset#location}
        :param max_time_travel_hours: Defines the time travel window in hours. The value can be from 48 to 168 hours (2 to 7 days). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#max_time_travel_hours GoogleBigqueryDataset#max_time_travel_hours}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#project GoogleBigqueryDataset#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#timeouts GoogleBigqueryDataset#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01c9f131dddab1567761e838ffafa3f08e583d2ae9d88e87f7f5e3d1a8722d72)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleBigqueryDatasetConfig(
            dataset_id=dataset_id,
            access=access,
            default_encryption_configuration=default_encryption_configuration,
            default_partition_expiration_ms=default_partition_expiration_ms,
            default_table_expiration_ms=default_table_expiration_ms,
            delete_contents_on_destroy=delete_contents_on_destroy,
            description=description,
            friendly_name=friendly_name,
            id=id,
            labels=labels,
            location=location,
            max_time_travel_hours=max_time_travel_hours,
            project=project,
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

    @jsii.member(jsii_name="putAccess")
    def put_access(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleBigqueryDatasetAccess", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__816e95fb5b7b6c2e50fe6a012597df445d867eccb174761d7c5eb78924097fa1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAccess", [value]))

    @jsii.member(jsii_name="putDefaultEncryptionConfiguration")
    def put_default_encryption_configuration(
        self,
        *,
        kms_key_name: builtins.str,
    ) -> None:
        '''
        :param kms_key_name: Describes the Cloud KMS encryption key that will be used to protect destination BigQuery table. The BigQuery Service Account associated with your project requires access to this encryption key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#kms_key_name GoogleBigqueryDataset#kms_key_name}
        '''
        value = GoogleBigqueryDatasetDefaultEncryptionConfiguration(
            kms_key_name=kms_key_name
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultEncryptionConfiguration", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#create GoogleBigqueryDataset#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#delete GoogleBigqueryDataset#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#update GoogleBigqueryDataset#update}.
        '''
        value = GoogleBigqueryDatasetTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAccess")
    def reset_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccess", []))

    @jsii.member(jsii_name="resetDefaultEncryptionConfiguration")
    def reset_default_encryption_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultEncryptionConfiguration", []))

    @jsii.member(jsii_name="resetDefaultPartitionExpirationMs")
    def reset_default_partition_expiration_ms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultPartitionExpirationMs", []))

    @jsii.member(jsii_name="resetDefaultTableExpirationMs")
    def reset_default_table_expiration_ms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultTableExpirationMs", []))

    @jsii.member(jsii_name="resetDeleteContentsOnDestroy")
    def reset_delete_contents_on_destroy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteContentsOnDestroy", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetFriendlyName")
    def reset_friendly_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFriendlyName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetMaxTimeTravelHours")
    def reset_max_time_travel_hours(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxTimeTravelHours", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

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
    @jsii.member(jsii_name="access")
    def access(self) -> "GoogleBigqueryDatasetAccessList":
        return typing.cast("GoogleBigqueryDatasetAccessList", jsii.get(self, "access"))

    @builtins.property
    @jsii.member(jsii_name="creationTime")
    def creation_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "creationTime"))

    @builtins.property
    @jsii.member(jsii_name="defaultEncryptionConfiguration")
    def default_encryption_configuration(
        self,
    ) -> "GoogleBigqueryDatasetDefaultEncryptionConfigurationOutputReference":
        return typing.cast("GoogleBigqueryDatasetDefaultEncryptionConfigurationOutputReference", jsii.get(self, "defaultEncryptionConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="etag")
    def etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "etag"))

    @builtins.property
    @jsii.member(jsii_name="lastModifiedTime")
    def last_modified_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lastModifiedTime"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleBigqueryDatasetTimeoutsOutputReference":
        return typing.cast("GoogleBigqueryDatasetTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="accessInput")
    def access_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleBigqueryDatasetAccess"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleBigqueryDatasetAccess"]]], jsii.get(self, "accessInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetIdInput")
    def dataset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultEncryptionConfigurationInput")
    def default_encryption_configuration_input(
        self,
    ) -> typing.Optional["GoogleBigqueryDatasetDefaultEncryptionConfiguration"]:
        return typing.cast(typing.Optional["GoogleBigqueryDatasetDefaultEncryptionConfiguration"], jsii.get(self, "defaultEncryptionConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultPartitionExpirationMsInput")
    def default_partition_expiration_ms_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultPartitionExpirationMsInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultTableExpirationMsInput")
    def default_table_expiration_ms_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultTableExpirationMsInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteContentsOnDestroyInput")
    def delete_contents_on_destroy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "deleteContentsOnDestroyInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="friendlyNameInput")
    def friendly_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "friendlyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="maxTimeTravelHoursInput")
    def max_time_travel_hours_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxTimeTravelHoursInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleBigqueryDatasetTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleBigqueryDatasetTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetId")
    def dataset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetId"))

    @dataset_id.setter
    def dataset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13524e53781de2922306fba5e3fac43d7b843b110a2259cb05ef14e7d850d3b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetId", value)

    @builtins.property
    @jsii.member(jsii_name="defaultPartitionExpirationMs")
    def default_partition_expiration_ms(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultPartitionExpirationMs"))

    @default_partition_expiration_ms.setter
    def default_partition_expiration_ms(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c03835cfc643c099c3ffb9d36c37183db52067f27d6a6d3ea69506c4f1f70244)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultPartitionExpirationMs", value)

    @builtins.property
    @jsii.member(jsii_name="defaultTableExpirationMs")
    def default_table_expiration_ms(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultTableExpirationMs"))

    @default_table_expiration_ms.setter
    def default_table_expiration_ms(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25e1263daa5b22bed837072d8382c2800c7cc81b218a09e49a599ccb8faf8db3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultTableExpirationMs", value)

    @builtins.property
    @jsii.member(jsii_name="deleteContentsOnDestroy")
    def delete_contents_on_destroy(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "deleteContentsOnDestroy"))

    @delete_contents_on_destroy.setter
    def delete_contents_on_destroy(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2617e3ceee065f9500864d2ed3e7bc9897fc94142998bae2643cef868c062e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteContentsOnDestroy", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10d7121d4a1ef6d7d465c1510e9a62930f392e261ea127da99d826419a3c007c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="friendlyName")
    def friendly_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "friendlyName"))

    @friendly_name.setter
    def friendly_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9278ef18ed8be870b9bce403159ef31b2a1e8e8071d41c7134c6272752804d3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "friendlyName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__183679536beb31ccf8ee0e4ab1caef257a05c690bd5d6b57c67575591c64eeae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66a02fe6cbe42ebd4d5e47eb2d564fa4732acd4ced63191c5a63447a5949eb10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4156e636fde758e45ea75da7582c5b41d9558722cf41f23883079e14a1863a81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="maxTimeTravelHours")
    def max_time_travel_hours(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxTimeTravelHours"))

    @max_time_travel_hours.setter
    def max_time_travel_hours(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41cac7c4273699a3a1b014c2f71d76842db766cff92cccded9b5dd2ad5a7022e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxTimeTravelHours", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f05bf6adcbf676e11f8cb77f31a33f055acb96c0dc7cf66c7287f86fe56fa95a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryDataset.GoogleBigqueryDatasetAccess",
    jsii_struct_bases=[],
    name_mapping={
        "dataset": "dataset",
        "domain": "domain",
        "group_by_email": "groupByEmail",
        "role": "role",
        "routine": "routine",
        "special_group": "specialGroup",
        "user_by_email": "userByEmail",
        "view": "view",
    },
)
class GoogleBigqueryDatasetAccess:
    def __init__(
        self,
        *,
        dataset: typing.Optional[typing.Union["GoogleBigqueryDatasetAccessDataset", typing.Dict[builtins.str, typing.Any]]] = None,
        domain: typing.Optional[builtins.str] = None,
        group_by_email: typing.Optional[builtins.str] = None,
        role: typing.Optional[builtins.str] = None,
        routine: typing.Optional[typing.Union["GoogleBigqueryDatasetAccessRoutine", typing.Dict[builtins.str, typing.Any]]] = None,
        special_group: typing.Optional[builtins.str] = None,
        user_by_email: typing.Optional[builtins.str] = None,
        view: typing.Optional[typing.Union["GoogleBigqueryDatasetAccessView", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param dataset: dataset block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#dataset GoogleBigqueryDataset#dataset}
        :param domain: A domain to grant access to. Any users signed in with the domain specified will be granted the specified access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#domain GoogleBigqueryDataset#domain}
        :param group_by_email: An email address of a Google Group to grant access to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#group_by_email GoogleBigqueryDataset#group_by_email}
        :param role: Describes the rights granted to the user specified by the other member of the access object. Basic, predefined, and custom roles are supported. Predefined roles that have equivalent basic roles are swapped by the API to their basic counterparts. See `official docs <https://cloud.google.com/bigquery/docs/access-control>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#role GoogleBigqueryDataset#role}
        :param routine: routine block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#routine GoogleBigqueryDataset#routine}
        :param special_group: A special group to grant access to. Possible values include:. 'projectOwners': Owners of the enclosing project. 'projectReaders': Readers of the enclosing project. 'projectWriters': Writers of the enclosing project. 'allAuthenticatedUsers': All authenticated BigQuery users. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#special_group GoogleBigqueryDataset#special_group}
        :param user_by_email: An email address of a user to grant access to. For example: fred@example.com. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#user_by_email GoogleBigqueryDataset#user_by_email}
        :param view: view block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#view GoogleBigqueryDataset#view}
        '''
        if isinstance(dataset, dict):
            dataset = GoogleBigqueryDatasetAccessDataset(**dataset)
        if isinstance(routine, dict):
            routine = GoogleBigqueryDatasetAccessRoutine(**routine)
        if isinstance(view, dict):
            view = GoogleBigqueryDatasetAccessView(**view)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__613d381cedcf41848d324a342642216ada4ff55e14f6fcb8d4baaf0f8c3c7b1f)
            check_type(argname="argument dataset", value=dataset, expected_type=type_hints["dataset"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument group_by_email", value=group_by_email, expected_type=type_hints["group_by_email"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument routine", value=routine, expected_type=type_hints["routine"])
            check_type(argname="argument special_group", value=special_group, expected_type=type_hints["special_group"])
            check_type(argname="argument user_by_email", value=user_by_email, expected_type=type_hints["user_by_email"])
            check_type(argname="argument view", value=view, expected_type=type_hints["view"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dataset is not None:
            self._values["dataset"] = dataset
        if domain is not None:
            self._values["domain"] = domain
        if group_by_email is not None:
            self._values["group_by_email"] = group_by_email
        if role is not None:
            self._values["role"] = role
        if routine is not None:
            self._values["routine"] = routine
        if special_group is not None:
            self._values["special_group"] = special_group
        if user_by_email is not None:
            self._values["user_by_email"] = user_by_email
        if view is not None:
            self._values["view"] = view

    @builtins.property
    def dataset(self) -> typing.Optional["GoogleBigqueryDatasetAccessDataset"]:
        '''dataset block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#dataset GoogleBigqueryDataset#dataset}
        '''
        result = self._values.get("dataset")
        return typing.cast(typing.Optional["GoogleBigqueryDatasetAccessDataset"], result)

    @builtins.property
    def domain(self) -> typing.Optional[builtins.str]:
        '''A domain to grant access to. Any users signed in with the domain specified will be granted the specified access.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#domain GoogleBigqueryDataset#domain}
        '''
        result = self._values.get("domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_by_email(self) -> typing.Optional[builtins.str]:
        '''An email address of a Google Group to grant access to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#group_by_email GoogleBigqueryDataset#group_by_email}
        '''
        result = self._values.get("group_by_email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[builtins.str]:
        '''Describes the rights granted to the user specified by the other member of the access object.

        Basic, predefined, and custom roles
        are supported. Predefined roles that have equivalent basic roles
        are swapped by the API to their basic counterparts. See
        `official docs <https://cloud.google.com/bigquery/docs/access-control>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#role GoogleBigqueryDataset#role}
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def routine(self) -> typing.Optional["GoogleBigqueryDatasetAccessRoutine"]:
        '''routine block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#routine GoogleBigqueryDataset#routine}
        '''
        result = self._values.get("routine")
        return typing.cast(typing.Optional["GoogleBigqueryDatasetAccessRoutine"], result)

    @builtins.property
    def special_group(self) -> typing.Optional[builtins.str]:
        '''A special group to grant access to. Possible values include:.

        'projectOwners': Owners of the enclosing project.

        'projectReaders': Readers of the enclosing project.

        'projectWriters': Writers of the enclosing project.

        'allAuthenticatedUsers': All authenticated BigQuery users.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#special_group GoogleBigqueryDataset#special_group}
        '''
        result = self._values.get("special_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_by_email(self) -> typing.Optional[builtins.str]:
        '''An email address of a user to grant access to. For example: fred@example.com.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#user_by_email GoogleBigqueryDataset#user_by_email}
        '''
        result = self._values.get("user_by_email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def view(self) -> typing.Optional["GoogleBigqueryDatasetAccessView"]:
        '''view block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#view GoogleBigqueryDataset#view}
        '''
        result = self._values.get("view")
        return typing.cast(typing.Optional["GoogleBigqueryDatasetAccessView"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryDatasetAccess(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryDataset.GoogleBigqueryDatasetAccessDataset",
    jsii_struct_bases=[],
    name_mapping={"dataset": "dataset", "target_types": "targetTypes"},
)
class GoogleBigqueryDatasetAccessDataset:
    def __init__(
        self,
        *,
        dataset: typing.Union["GoogleBigqueryDatasetAccessDatasetDataset", typing.Dict[builtins.str, typing.Any]],
        target_types: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param dataset: dataset block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#dataset GoogleBigqueryDataset#dataset}
        :param target_types: Which resources in the dataset this entry applies to. Currently, only views are supported, but additional target types may be added in the future. Possible values: VIEWS Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#target_types GoogleBigqueryDataset#target_types}
        '''
        if isinstance(dataset, dict):
            dataset = GoogleBigqueryDatasetAccessDatasetDataset(**dataset)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acb014f214110e09e964d9c0d9703f66cdf5e7867e68f75d66c883854b5411e8)
            check_type(argname="argument dataset", value=dataset, expected_type=type_hints["dataset"])
            check_type(argname="argument target_types", value=target_types, expected_type=type_hints["target_types"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataset": dataset,
            "target_types": target_types,
        }

    @builtins.property
    def dataset(self) -> "GoogleBigqueryDatasetAccessDatasetDataset":
        '''dataset block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#dataset GoogleBigqueryDataset#dataset}
        '''
        result = self._values.get("dataset")
        assert result is not None, "Required property 'dataset' is missing"
        return typing.cast("GoogleBigqueryDatasetAccessDatasetDataset", result)

    @builtins.property
    def target_types(self) -> typing.List[builtins.str]:
        '''Which resources in the dataset this entry applies to.

        Currently, only views are supported,
        but additional target types may be added in the future. Possible values: VIEWS

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#target_types GoogleBigqueryDataset#target_types}
        '''
        result = self._values.get("target_types")
        assert result is not None, "Required property 'target_types' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryDatasetAccessDataset(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryDataset.GoogleBigqueryDatasetAccessDatasetDataset",
    jsii_struct_bases=[],
    name_mapping={"dataset_id": "datasetId", "project_id": "projectId"},
)
class GoogleBigqueryDatasetAccessDatasetDataset:
    def __init__(self, *, dataset_id: builtins.str, project_id: builtins.str) -> None:
        '''
        :param dataset_id: The ID of the dataset containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#dataset_id GoogleBigqueryDataset#dataset_id}
        :param project_id: The ID of the project containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#project_id GoogleBigqueryDataset#project_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38d38cd45eea1eab2f5df1c064e9af56d85e0b894280af381bc213ad0969871b)
            check_type(argname="argument dataset_id", value=dataset_id, expected_type=type_hints["dataset_id"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataset_id": dataset_id,
            "project_id": project_id,
        }

    @builtins.property
    def dataset_id(self) -> builtins.str:
        '''The ID of the dataset containing this table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#dataset_id GoogleBigqueryDataset#dataset_id}
        '''
        result = self._values.get("dataset_id")
        assert result is not None, "Required property 'dataset_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''The ID of the project containing this table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#project_id GoogleBigqueryDataset#project_id}
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryDatasetAccessDatasetDataset(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryDatasetAccessDatasetDatasetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryDataset.GoogleBigqueryDatasetAccessDatasetDatasetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b1997cdeaa5477a776314fd07ed596e7249a96bcb5eb7ead612387d67a3b3c63)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="datasetIdInput")
    def dataset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetId")
    def dataset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetId"))

    @dataset_id.setter
    def dataset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__684f48d1e8322e3f96d5d2ad4c5b6fba2c1512165fdc541548a57f55744f15ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetId", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b5bfb765c0f572d7b029a64dc14dd0dba1ee3be3a3daa904379be654c8fff1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBigqueryDatasetAccessDatasetDataset]:
        return typing.cast(typing.Optional[GoogleBigqueryDatasetAccessDatasetDataset], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryDatasetAccessDatasetDataset],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64fdc148017d4a0b1a9e18b24ca4b8e7f73a4e73713161ae78301ce97d2b7630)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleBigqueryDatasetAccessDatasetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryDataset.GoogleBigqueryDatasetAccessDatasetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__858a6428d7847b9ef010c5c41d6c6e3561912ca0733bb97b02bc241fd34cb0ed)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDataset")
    def put_dataset(
        self,
        *,
        dataset_id: builtins.str,
        project_id: builtins.str,
    ) -> None:
        '''
        :param dataset_id: The ID of the dataset containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#dataset_id GoogleBigqueryDataset#dataset_id}
        :param project_id: The ID of the project containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#project_id GoogleBigqueryDataset#project_id}
        '''
        value = GoogleBigqueryDatasetAccessDatasetDataset(
            dataset_id=dataset_id, project_id=project_id
        )

        return typing.cast(None, jsii.invoke(self, "putDataset", [value]))

    @builtins.property
    @jsii.member(jsii_name="dataset")
    def dataset(self) -> GoogleBigqueryDatasetAccessDatasetDatasetOutputReference:
        return typing.cast(GoogleBigqueryDatasetAccessDatasetDatasetOutputReference, jsii.get(self, "dataset"))

    @builtins.property
    @jsii.member(jsii_name="datasetInput")
    def dataset_input(
        self,
    ) -> typing.Optional[GoogleBigqueryDatasetAccessDatasetDataset]:
        return typing.cast(typing.Optional[GoogleBigqueryDatasetAccessDatasetDataset], jsii.get(self, "datasetInput"))

    @builtins.property
    @jsii.member(jsii_name="targetTypesInput")
    def target_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="targetTypes")
    def target_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targetTypes"))

    @target_types.setter
    def target_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91eff44f6aafb2ad15a81678d1ba4a17bc706974c237a9727d8945429b9772c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetTypes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryDatasetAccessDataset]:
        return typing.cast(typing.Optional[GoogleBigqueryDatasetAccessDataset], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryDatasetAccessDataset],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a0c2c90f636435a07d0aee8766d9e8cdb7f48b10142e88978e983ed91286937)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleBigqueryDatasetAccessList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryDataset.GoogleBigqueryDatasetAccessList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6f71a9317d9eaa1dbb6712be1937932c46eced2cffc5c3fac44c382512dea964)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GoogleBigqueryDatasetAccessOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4d8ab300b4079e9295b08d7ece1bef849090d079205aeaf563352837d056899)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleBigqueryDatasetAccessOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__689acfb4346973bb9c290bd631ee9bc79c135dd53833c285262da3f5e8b6195b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__facbbf7aafabd1745f4a512c1a0cc58f80250e02e39288193145118eca2bb94b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2d478cc27adaacc36fc9360c2ac532646482eda90bdbb3e52022e9ffed1b873a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleBigqueryDatasetAccess]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleBigqueryDatasetAccess]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleBigqueryDatasetAccess]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9de38e1e0cf7b8f81cdbd42bd8ec60f1c4b6b3c01ee503f08fa4249e9b6dcb3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleBigqueryDatasetAccessOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryDataset.GoogleBigqueryDatasetAccessOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5786e1b0d4ba8e7b2b0c8b3999d6efb9cbee526a543a84381996c96d69cadaa3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDataset")
    def put_dataset(
        self,
        *,
        dataset: typing.Union[GoogleBigqueryDatasetAccessDatasetDataset, typing.Dict[builtins.str, typing.Any]],
        target_types: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param dataset: dataset block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#dataset GoogleBigqueryDataset#dataset}
        :param target_types: Which resources in the dataset this entry applies to. Currently, only views are supported, but additional target types may be added in the future. Possible values: VIEWS Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#target_types GoogleBigqueryDataset#target_types}
        '''
        value = GoogleBigqueryDatasetAccessDataset(
            dataset=dataset, target_types=target_types
        )

        return typing.cast(None, jsii.invoke(self, "putDataset", [value]))

    @jsii.member(jsii_name="putRoutine")
    def put_routine(
        self,
        *,
        dataset_id: builtins.str,
        project_id: builtins.str,
        routine_id: builtins.str,
    ) -> None:
        '''
        :param dataset_id: The ID of the dataset containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#dataset_id GoogleBigqueryDataset#dataset_id}
        :param project_id: The ID of the project containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#project_id GoogleBigqueryDataset#project_id}
        :param routine_id: The ID of the routine. The ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_). The maximum length is 256 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#routine_id GoogleBigqueryDataset#routine_id}
        '''
        value = GoogleBigqueryDatasetAccessRoutine(
            dataset_id=dataset_id, project_id=project_id, routine_id=routine_id
        )

        return typing.cast(None, jsii.invoke(self, "putRoutine", [value]))

    @jsii.member(jsii_name="putView")
    def put_view(
        self,
        *,
        dataset_id: builtins.str,
        project_id: builtins.str,
        table_id: builtins.str,
    ) -> None:
        '''
        :param dataset_id: The ID of the dataset containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#dataset_id GoogleBigqueryDataset#dataset_id}
        :param project_id: The ID of the project containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#project_id GoogleBigqueryDataset#project_id}
        :param table_id: The ID of the table. The ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_). The maximum length is 1,024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#table_id GoogleBigqueryDataset#table_id}
        '''
        value = GoogleBigqueryDatasetAccessView(
            dataset_id=dataset_id, project_id=project_id, table_id=table_id
        )

        return typing.cast(None, jsii.invoke(self, "putView", [value]))

    @jsii.member(jsii_name="resetDataset")
    def reset_dataset(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataset", []))

    @jsii.member(jsii_name="resetDomain")
    def reset_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomain", []))

    @jsii.member(jsii_name="resetGroupByEmail")
    def reset_group_by_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupByEmail", []))

    @jsii.member(jsii_name="resetRole")
    def reset_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRole", []))

    @jsii.member(jsii_name="resetRoutine")
    def reset_routine(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoutine", []))

    @jsii.member(jsii_name="resetSpecialGroup")
    def reset_special_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpecialGroup", []))

    @jsii.member(jsii_name="resetUserByEmail")
    def reset_user_by_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserByEmail", []))

    @jsii.member(jsii_name="resetView")
    def reset_view(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetView", []))

    @builtins.property
    @jsii.member(jsii_name="dataset")
    def dataset(self) -> GoogleBigqueryDatasetAccessDatasetOutputReference:
        return typing.cast(GoogleBigqueryDatasetAccessDatasetOutputReference, jsii.get(self, "dataset"))

    @builtins.property
    @jsii.member(jsii_name="routine")
    def routine(self) -> "GoogleBigqueryDatasetAccessRoutineOutputReference":
        return typing.cast("GoogleBigqueryDatasetAccessRoutineOutputReference", jsii.get(self, "routine"))

    @builtins.property
    @jsii.member(jsii_name="view")
    def view(self) -> "GoogleBigqueryDatasetAccessViewOutputReference":
        return typing.cast("GoogleBigqueryDatasetAccessViewOutputReference", jsii.get(self, "view"))

    @builtins.property
    @jsii.member(jsii_name="datasetInput")
    def dataset_input(self) -> typing.Optional[GoogleBigqueryDatasetAccessDataset]:
        return typing.cast(typing.Optional[GoogleBigqueryDatasetAccessDataset], jsii.get(self, "datasetInput"))

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="groupByEmailInput")
    def group_by_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupByEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="routineInput")
    def routine_input(self) -> typing.Optional["GoogleBigqueryDatasetAccessRoutine"]:
        return typing.cast(typing.Optional["GoogleBigqueryDatasetAccessRoutine"], jsii.get(self, "routineInput"))

    @builtins.property
    @jsii.member(jsii_name="specialGroupInput")
    def special_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "specialGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="userByEmailInput")
    def user_by_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userByEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="viewInput")
    def view_input(self) -> typing.Optional["GoogleBigqueryDatasetAccessView"]:
        return typing.cast(typing.Optional["GoogleBigqueryDatasetAccessView"], jsii.get(self, "viewInput"))

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb1714425ad2b936ec5170d4731fbab3bd3fd5db4780471cdab3d48ba81e08ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="groupByEmail")
    def group_by_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupByEmail"))

    @group_by_email.setter
    def group_by_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b589f56ada34c40cff137af06bbfc285ece387bec23142553996da804a3e76a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupByEmail", value)

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f1bcb453ae2f2772b5e907f47f4dfd40864c79a39e5ae7d01a15f41a2db02cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)

    @builtins.property
    @jsii.member(jsii_name="specialGroup")
    def special_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "specialGroup"))

    @special_group.setter
    def special_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f71b6272bcbca378fe75b68d1236711e6c5e1807a5a3390d4bf42c1f48e69e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "specialGroup", value)

    @builtins.property
    @jsii.member(jsii_name="userByEmail")
    def user_by_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userByEmail"))

    @user_by_email.setter
    def user_by_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b1869a8af1ca29db991ac39e070f35f3cf8ed065d667a564ccaeb46ae354604)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userByEmail", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleBigqueryDatasetAccess, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleBigqueryDatasetAccess, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleBigqueryDatasetAccess, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__217f7098a5ade70f14d9df12b30e83894944d2a08282b741be44639a63892e77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryDataset.GoogleBigqueryDatasetAccessRoutine",
    jsii_struct_bases=[],
    name_mapping={
        "dataset_id": "datasetId",
        "project_id": "projectId",
        "routine_id": "routineId",
    },
)
class GoogleBigqueryDatasetAccessRoutine:
    def __init__(
        self,
        *,
        dataset_id: builtins.str,
        project_id: builtins.str,
        routine_id: builtins.str,
    ) -> None:
        '''
        :param dataset_id: The ID of the dataset containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#dataset_id GoogleBigqueryDataset#dataset_id}
        :param project_id: The ID of the project containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#project_id GoogleBigqueryDataset#project_id}
        :param routine_id: The ID of the routine. The ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_). The maximum length is 256 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#routine_id GoogleBigqueryDataset#routine_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70a49e663e5e5487a6cd6a37e2c76aa87a47f3cf2078359a4ae64734b5a4201a)
            check_type(argname="argument dataset_id", value=dataset_id, expected_type=type_hints["dataset_id"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument routine_id", value=routine_id, expected_type=type_hints["routine_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataset_id": dataset_id,
            "project_id": project_id,
            "routine_id": routine_id,
        }

    @builtins.property
    def dataset_id(self) -> builtins.str:
        '''The ID of the dataset containing this table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#dataset_id GoogleBigqueryDataset#dataset_id}
        '''
        result = self._values.get("dataset_id")
        assert result is not None, "Required property 'dataset_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''The ID of the project containing this table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#project_id GoogleBigqueryDataset#project_id}
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def routine_id(self) -> builtins.str:
        '''The ID of the routine.

        The ID must contain only letters (a-z,
        A-Z), numbers (0-9), or underscores (_). The maximum length
        is 256 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#routine_id GoogleBigqueryDataset#routine_id}
        '''
        result = self._values.get("routine_id")
        assert result is not None, "Required property 'routine_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryDatasetAccessRoutine(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryDatasetAccessRoutineOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryDataset.GoogleBigqueryDatasetAccessRoutineOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__35f59f19dfd4ed95b69a3fb290c3a10cc21d575f13624c237bf2687297d3ae9d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="datasetIdInput")
    def dataset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="routineIdInput")
    def routine_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "routineIdInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetId")
    def dataset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetId"))

    @dataset_id.setter
    def dataset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2472a09c4aca94c76f1d4d595ca08cfb4015fa4399dac7bd9ba07332b3fc862)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetId", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b50f714239c36141bc12cfc98323f6591af539d225abbb1f6c2ee8ae7ffe9a6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="routineId")
    def routine_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "routineId"))

    @routine_id.setter
    def routine_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cc395fa5fc592ee3f6ddbb5e1b4e4f7c62faccc5101ff4a145e99a437506aac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routineId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryDatasetAccessRoutine]:
        return typing.cast(typing.Optional[GoogleBigqueryDatasetAccessRoutine], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryDatasetAccessRoutine],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d63e91d897705da21bbefa67ee11de665054247b702a2e8d4c58ea4fe96ea51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryDataset.GoogleBigqueryDatasetAccessView",
    jsii_struct_bases=[],
    name_mapping={
        "dataset_id": "datasetId",
        "project_id": "projectId",
        "table_id": "tableId",
    },
)
class GoogleBigqueryDatasetAccessView:
    def __init__(
        self,
        *,
        dataset_id: builtins.str,
        project_id: builtins.str,
        table_id: builtins.str,
    ) -> None:
        '''
        :param dataset_id: The ID of the dataset containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#dataset_id GoogleBigqueryDataset#dataset_id}
        :param project_id: The ID of the project containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#project_id GoogleBigqueryDataset#project_id}
        :param table_id: The ID of the table. The ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_). The maximum length is 1,024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#table_id GoogleBigqueryDataset#table_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__592316e2ffc7a19d0a8acb8507260c0d1c329d78349b99977c564311ff68f42e)
            check_type(argname="argument dataset_id", value=dataset_id, expected_type=type_hints["dataset_id"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument table_id", value=table_id, expected_type=type_hints["table_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataset_id": dataset_id,
            "project_id": project_id,
            "table_id": table_id,
        }

    @builtins.property
    def dataset_id(self) -> builtins.str:
        '''The ID of the dataset containing this table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#dataset_id GoogleBigqueryDataset#dataset_id}
        '''
        result = self._values.get("dataset_id")
        assert result is not None, "Required property 'dataset_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''The ID of the project containing this table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#project_id GoogleBigqueryDataset#project_id}
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_id(self) -> builtins.str:
        '''The ID of the table.

        The ID must contain only letters (a-z,
        A-Z), numbers (0-9), or underscores (_). The maximum length
        is 1,024 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#table_id GoogleBigqueryDataset#table_id}
        '''
        result = self._values.get("table_id")
        assert result is not None, "Required property 'table_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryDatasetAccessView(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryDatasetAccessViewOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryDataset.GoogleBigqueryDatasetAccessViewOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b71ed2ad39adde649f4449fef33c596acf530be5eced712317b751170444185a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="datasetIdInput")
    def dataset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tableIdInput")
    def table_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableIdInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetId")
    def dataset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetId"))

    @dataset_id.setter
    def dataset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__695a82f06ebce8b31a14750f1b37aaa347f76d4bf05a7dfab9d68da7b4790e16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetId", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__058e82f2fa3c967883d6c90f7ca308cd366a63c7844912106262a9926c0c7991)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="tableId")
    def table_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableId"))

    @table_id.setter
    def table_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc88be9fe73a322a468168316e105f143c79fa1eca69f0f60d2ceeff2ac46a9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryDatasetAccessView]:
        return typing.cast(typing.Optional[GoogleBigqueryDatasetAccessView], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryDatasetAccessView],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e89960afcbcd83c125d8150ade0ff996a9e9ff33cde66355a18262fb7e56d9ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryDataset.GoogleBigqueryDatasetConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "dataset_id": "datasetId",
        "access": "access",
        "default_encryption_configuration": "defaultEncryptionConfiguration",
        "default_partition_expiration_ms": "defaultPartitionExpirationMs",
        "default_table_expiration_ms": "defaultTableExpirationMs",
        "delete_contents_on_destroy": "deleteContentsOnDestroy",
        "description": "description",
        "friendly_name": "friendlyName",
        "id": "id",
        "labels": "labels",
        "location": "location",
        "max_time_travel_hours": "maxTimeTravelHours",
        "project": "project",
        "timeouts": "timeouts",
    },
)
class GoogleBigqueryDatasetConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        dataset_id: builtins.str,
        access: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleBigqueryDatasetAccess, typing.Dict[builtins.str, typing.Any]]]]] = None,
        default_encryption_configuration: typing.Optional[typing.Union["GoogleBigqueryDatasetDefaultEncryptionConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        default_partition_expiration_ms: typing.Optional[jsii.Number] = None,
        default_table_expiration_ms: typing.Optional[jsii.Number] = None,
        delete_contents_on_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        friendly_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        location: typing.Optional[builtins.str] = None,
        max_time_travel_hours: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleBigqueryDatasetTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param dataset_id: A unique ID for this dataset, without the project name. The ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_). The maximum length is 1,024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#dataset_id GoogleBigqueryDataset#dataset_id}
        :param access: access block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#access GoogleBigqueryDataset#access}
        :param default_encryption_configuration: default_encryption_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#default_encryption_configuration GoogleBigqueryDataset#default_encryption_configuration}
        :param default_partition_expiration_ms: The default partition expiration for all partitioned tables in the dataset, in milliseconds. Once this property is set, all newly-created partitioned tables in the dataset will have an 'expirationMs' property in the 'timePartitioning' settings set to this value, and changing the value will only affect new tables, not existing ones. The storage in a partition will have an expiration time of its partition time plus this value. Setting this property overrides the use of 'defaultTableExpirationMs' for partitioned tables: only one of 'defaultTableExpirationMs' and 'defaultPartitionExpirationMs' will be used for any new partitioned table. If you provide an explicit 'timePartitioning.expirationMs' when creating or updating a partitioned table, that value takes precedence over the default partition expiration time indicated by this property. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#default_partition_expiration_ms GoogleBigqueryDataset#default_partition_expiration_ms}
        :param default_table_expiration_ms: The default lifetime of all tables in the dataset, in milliseconds. The minimum value is 3600000 milliseconds (one hour). Once this property is set, all newly-created tables in the dataset will have an 'expirationTime' property set to the creation time plus the value in this property, and changing the value will only affect new tables, not existing ones. When the 'expirationTime' for a given table is reached, that table will be deleted automatically. If a table's 'expirationTime' is modified or removed before the table expires, or if you provide an explicit 'expirationTime' when creating a table, that value takes precedence over the default expiration time indicated by this property. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#default_table_expiration_ms GoogleBigqueryDataset#default_table_expiration_ms}
        :param delete_contents_on_destroy: If set to 'true', delete all the tables in the dataset when destroying the resource; otherwise, destroying the resource will fail if tables are present. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#delete_contents_on_destroy GoogleBigqueryDataset#delete_contents_on_destroy}
        :param description: A user-friendly description of the dataset. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#description GoogleBigqueryDataset#description}
        :param friendly_name: A descriptive name for the dataset. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#friendly_name GoogleBigqueryDataset#friendly_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#id GoogleBigqueryDataset#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: The labels associated with this dataset. You can use these to organize and group your datasets. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#labels GoogleBigqueryDataset#labels}
        :param location: The geographic location where the dataset should reside. See `official docs <https://cloud.google.com/bigquery/docs/dataset-locations>`_. There are two types of locations, regional or multi-regional. A regional location is a specific geographic place, such as Tokyo, and a multi-regional location is a large geographic area, such as the United States, that contains at least two geographic places. The default value is multi-regional location 'US'. Changing this forces a new resource to be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#location GoogleBigqueryDataset#location}
        :param max_time_travel_hours: Defines the time travel window in hours. The value can be from 48 to 168 hours (2 to 7 days). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#max_time_travel_hours GoogleBigqueryDataset#max_time_travel_hours}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#project GoogleBigqueryDataset#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#timeouts GoogleBigqueryDataset#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(default_encryption_configuration, dict):
            default_encryption_configuration = GoogleBigqueryDatasetDefaultEncryptionConfiguration(**default_encryption_configuration)
        if isinstance(timeouts, dict):
            timeouts = GoogleBigqueryDatasetTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2246e8300e0dd33437569bdea98647baa6e1283e2a64a0ddb6d57bae172df0b9)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument dataset_id", value=dataset_id, expected_type=type_hints["dataset_id"])
            check_type(argname="argument access", value=access, expected_type=type_hints["access"])
            check_type(argname="argument default_encryption_configuration", value=default_encryption_configuration, expected_type=type_hints["default_encryption_configuration"])
            check_type(argname="argument default_partition_expiration_ms", value=default_partition_expiration_ms, expected_type=type_hints["default_partition_expiration_ms"])
            check_type(argname="argument default_table_expiration_ms", value=default_table_expiration_ms, expected_type=type_hints["default_table_expiration_ms"])
            check_type(argname="argument delete_contents_on_destroy", value=delete_contents_on_destroy, expected_type=type_hints["delete_contents_on_destroy"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument friendly_name", value=friendly_name, expected_type=type_hints["friendly_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument max_time_travel_hours", value=max_time_travel_hours, expected_type=type_hints["max_time_travel_hours"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataset_id": dataset_id,
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
        if access is not None:
            self._values["access"] = access
        if default_encryption_configuration is not None:
            self._values["default_encryption_configuration"] = default_encryption_configuration
        if default_partition_expiration_ms is not None:
            self._values["default_partition_expiration_ms"] = default_partition_expiration_ms
        if default_table_expiration_ms is not None:
            self._values["default_table_expiration_ms"] = default_table_expiration_ms
        if delete_contents_on_destroy is not None:
            self._values["delete_contents_on_destroy"] = delete_contents_on_destroy
        if description is not None:
            self._values["description"] = description
        if friendly_name is not None:
            self._values["friendly_name"] = friendly_name
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if location is not None:
            self._values["location"] = location
        if max_time_travel_hours is not None:
            self._values["max_time_travel_hours"] = max_time_travel_hours
        if project is not None:
            self._values["project"] = project
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
    def dataset_id(self) -> builtins.str:
        '''A unique ID for this dataset, without the project name.

        The ID
        must contain only letters (a-z, A-Z), numbers (0-9), or
        underscores (_). The maximum length is 1,024 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#dataset_id GoogleBigqueryDataset#dataset_id}
        '''
        result = self._values.get("dataset_id")
        assert result is not None, "Required property 'dataset_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleBigqueryDatasetAccess]]]:
        '''access block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#access GoogleBigqueryDataset#access}
        '''
        result = self._values.get("access")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleBigqueryDatasetAccess]]], result)

    @builtins.property
    def default_encryption_configuration(
        self,
    ) -> typing.Optional["GoogleBigqueryDatasetDefaultEncryptionConfiguration"]:
        '''default_encryption_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#default_encryption_configuration GoogleBigqueryDataset#default_encryption_configuration}
        '''
        result = self._values.get("default_encryption_configuration")
        return typing.cast(typing.Optional["GoogleBigqueryDatasetDefaultEncryptionConfiguration"], result)

    @builtins.property
    def default_partition_expiration_ms(self) -> typing.Optional[jsii.Number]:
        '''The default partition expiration for all partitioned tables in the dataset, in milliseconds.

        Once this property is set, all newly-created partitioned tables in
        the dataset will have an 'expirationMs' property in the 'timePartitioning'
        settings set to this value, and changing the value will only
        affect new tables, not existing ones. The storage in a partition will
        have an expiration time of its partition time plus this value.
        Setting this property overrides the use of 'defaultTableExpirationMs'
        for partitioned tables: only one of 'defaultTableExpirationMs' and
        'defaultPartitionExpirationMs' will be used for any new partitioned
        table. If you provide an explicit 'timePartitioning.expirationMs' when
        creating or updating a partitioned table, that value takes precedence
        over the default partition expiration time indicated by this property.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#default_partition_expiration_ms GoogleBigqueryDataset#default_partition_expiration_ms}
        '''
        result = self._values.get("default_partition_expiration_ms")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def default_table_expiration_ms(self) -> typing.Optional[jsii.Number]:
        '''The default lifetime of all tables in the dataset, in milliseconds. The minimum value is 3600000 milliseconds (one hour).

        Once this property is set, all newly-created tables in the dataset
        will have an 'expirationTime' property set to the creation time plus
        the value in this property, and changing the value will only affect
        new tables, not existing ones. When the 'expirationTime' for a given
        table is reached, that table will be deleted automatically.
        If a table's 'expirationTime' is modified or removed before the
        table expires, or if you provide an explicit 'expirationTime' when
        creating a table, that value takes precedence over the default
        expiration time indicated by this property.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#default_table_expiration_ms GoogleBigqueryDataset#default_table_expiration_ms}
        '''
        result = self._values.get("default_table_expiration_ms")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def delete_contents_on_destroy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If set to 'true', delete all the tables in the dataset when destroying the resource;

        otherwise,
        destroying the resource will fail if tables are present.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#delete_contents_on_destroy GoogleBigqueryDataset#delete_contents_on_destroy}
        '''
        result = self._values.get("delete_contents_on_destroy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A user-friendly description of the dataset.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#description GoogleBigqueryDataset#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def friendly_name(self) -> typing.Optional[builtins.str]:
        '''A descriptive name for the dataset.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#friendly_name GoogleBigqueryDataset#friendly_name}
        '''
        result = self._values.get("friendly_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#id GoogleBigqueryDataset#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The labels associated with this dataset. You can use these to organize and group your datasets.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#labels GoogleBigqueryDataset#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''The geographic location where the dataset should reside. See `official docs <https://cloud.google.com/bigquery/docs/dataset-locations>`_.

        There are two types of locations, regional or multi-regional. A regional
        location is a specific geographic place, such as Tokyo, and a multi-regional
        location is a large geographic area, such as the United States, that
        contains at least two geographic places.

        The default value is multi-regional location 'US'.
        Changing this forces a new resource to be created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#location GoogleBigqueryDataset#location}
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_time_travel_hours(self) -> typing.Optional[builtins.str]:
        '''Defines the time travel window in hours.

        The value can be from 48 to 168 hours (2 to 7 days).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#max_time_travel_hours GoogleBigqueryDataset#max_time_travel_hours}
        '''
        result = self._values.get("max_time_travel_hours")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#project GoogleBigqueryDataset#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleBigqueryDatasetTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#timeouts GoogleBigqueryDataset#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleBigqueryDatasetTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryDatasetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryDataset.GoogleBigqueryDatasetDefaultEncryptionConfiguration",
    jsii_struct_bases=[],
    name_mapping={"kms_key_name": "kmsKeyName"},
)
class GoogleBigqueryDatasetDefaultEncryptionConfiguration:
    def __init__(self, *, kms_key_name: builtins.str) -> None:
        '''
        :param kms_key_name: Describes the Cloud KMS encryption key that will be used to protect destination BigQuery table. The BigQuery Service Account associated with your project requires access to this encryption key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#kms_key_name GoogleBigqueryDataset#kms_key_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a4e25ef50cf914077bebc1d083852a51cd3fa7a213954d031f3524b89891f6a)
            check_type(argname="argument kms_key_name", value=kms_key_name, expected_type=type_hints["kms_key_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "kms_key_name": kms_key_name,
        }

    @builtins.property
    def kms_key_name(self) -> builtins.str:
        '''Describes the Cloud KMS encryption key that will be used to protect destination BigQuery table.

        The BigQuery Service Account associated with your project requires
        access to this encryption key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#kms_key_name GoogleBigqueryDataset#kms_key_name}
        '''
        result = self._values.get("kms_key_name")
        assert result is not None, "Required property 'kms_key_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryDatasetDefaultEncryptionConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryDatasetDefaultEncryptionConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryDataset.GoogleBigqueryDatasetDefaultEncryptionConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b376cc4dc242dde1fbc845be71c73b7da3cc30cdba749054a74b2670a24ce001)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="kmsKeyNameInput")
    def kms_key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyName")
    def kms_key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyName"))

    @kms_key_name.setter
    def kms_key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__653dfdd019b7495eb2e4d8ddf39d4701d0eb600d3eaf82d586d89813a1f76e8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBigqueryDatasetDefaultEncryptionConfiguration]:
        return typing.cast(typing.Optional[GoogleBigqueryDatasetDefaultEncryptionConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryDatasetDefaultEncryptionConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f092dae67262cc008cbe6e91e0b3137e9ddb7cff98846dedad79c219593f196e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryDataset.GoogleBigqueryDatasetTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleBigqueryDatasetTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#create GoogleBigqueryDataset#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#delete GoogleBigqueryDataset#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#update GoogleBigqueryDataset#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4a55aedb68beec1fd88c16fa1ff6b6cb0d996f505f1976020ea472b8e9ad660)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#create GoogleBigqueryDataset#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#delete GoogleBigqueryDataset#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset#update GoogleBigqueryDataset#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryDatasetTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryDatasetTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryDataset.GoogleBigqueryDatasetTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__006e1679dba925f9fbd88c3591389adf363f133d42faa4addc5ef757db6b96ec)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c3da33bb1108b1f95c661fa04964e34b851468a5641e634f8a4aeadd8b0e839c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efd609582957055c5a6dd7aec96f89c7a19f884667b675187baaa624e720c81c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dc95452da6ee583db056480a84deb75dfdb8ae272c1034be07734c5b942dee7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleBigqueryDatasetTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleBigqueryDatasetTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleBigqueryDatasetTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a24b81a496606ddfdfd0573d12492534098ac68addf4a5e5081e95e04dfc5b14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleBigqueryDataset",
    "GoogleBigqueryDatasetAccess",
    "GoogleBigqueryDatasetAccessDataset",
    "GoogleBigqueryDatasetAccessDatasetDataset",
    "GoogleBigqueryDatasetAccessDatasetDatasetOutputReference",
    "GoogleBigqueryDatasetAccessDatasetOutputReference",
    "GoogleBigqueryDatasetAccessList",
    "GoogleBigqueryDatasetAccessOutputReference",
    "GoogleBigqueryDatasetAccessRoutine",
    "GoogleBigqueryDatasetAccessRoutineOutputReference",
    "GoogleBigqueryDatasetAccessView",
    "GoogleBigqueryDatasetAccessViewOutputReference",
    "GoogleBigqueryDatasetConfig",
    "GoogleBigqueryDatasetDefaultEncryptionConfiguration",
    "GoogleBigqueryDatasetDefaultEncryptionConfigurationOutputReference",
    "GoogleBigqueryDatasetTimeouts",
    "GoogleBigqueryDatasetTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__01c9f131dddab1567761e838ffafa3f08e583d2ae9d88e87f7f5e3d1a8722d72(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    dataset_id: builtins.str,
    access: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleBigqueryDatasetAccess, typing.Dict[builtins.str, typing.Any]]]]] = None,
    default_encryption_configuration: typing.Optional[typing.Union[GoogleBigqueryDatasetDefaultEncryptionConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    default_partition_expiration_ms: typing.Optional[jsii.Number] = None,
    default_table_expiration_ms: typing.Optional[jsii.Number] = None,
    delete_contents_on_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    description: typing.Optional[builtins.str] = None,
    friendly_name: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    location: typing.Optional[builtins.str] = None,
    max_time_travel_hours: typing.Optional[builtins.str] = None,
    project: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[GoogleBigqueryDatasetTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__816e95fb5b7b6c2e50fe6a012597df445d867eccb174761d7c5eb78924097fa1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleBigqueryDatasetAccess, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13524e53781de2922306fba5e3fac43d7b843b110a2259cb05ef14e7d850d3b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c03835cfc643c099c3ffb9d36c37183db52067f27d6a6d3ea69506c4f1f70244(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25e1263daa5b22bed837072d8382c2800c7cc81b218a09e49a599ccb8faf8db3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2617e3ceee065f9500864d2ed3e7bc9897fc94142998bae2643cef868c062e2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10d7121d4a1ef6d7d465c1510e9a62930f392e261ea127da99d826419a3c007c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9278ef18ed8be870b9bce403159ef31b2a1e8e8071d41c7134c6272752804d3c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__183679536beb31ccf8ee0e4ab1caef257a05c690bd5d6b57c67575591c64eeae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66a02fe6cbe42ebd4d5e47eb2d564fa4732acd4ced63191c5a63447a5949eb10(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4156e636fde758e45ea75da7582c5b41d9558722cf41f23883079e14a1863a81(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41cac7c4273699a3a1b014c2f71d76842db766cff92cccded9b5dd2ad5a7022e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f05bf6adcbf676e11f8cb77f31a33f055acb96c0dc7cf66c7287f86fe56fa95a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__613d381cedcf41848d324a342642216ada4ff55e14f6fcb8d4baaf0f8c3c7b1f(
    *,
    dataset: typing.Optional[typing.Union[GoogleBigqueryDatasetAccessDataset, typing.Dict[builtins.str, typing.Any]]] = None,
    domain: typing.Optional[builtins.str] = None,
    group_by_email: typing.Optional[builtins.str] = None,
    role: typing.Optional[builtins.str] = None,
    routine: typing.Optional[typing.Union[GoogleBigqueryDatasetAccessRoutine, typing.Dict[builtins.str, typing.Any]]] = None,
    special_group: typing.Optional[builtins.str] = None,
    user_by_email: typing.Optional[builtins.str] = None,
    view: typing.Optional[typing.Union[GoogleBigqueryDatasetAccessView, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acb014f214110e09e964d9c0d9703f66cdf5e7867e68f75d66c883854b5411e8(
    *,
    dataset: typing.Union[GoogleBigqueryDatasetAccessDatasetDataset, typing.Dict[builtins.str, typing.Any]],
    target_types: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38d38cd45eea1eab2f5df1c064e9af56d85e0b894280af381bc213ad0969871b(
    *,
    dataset_id: builtins.str,
    project_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1997cdeaa5477a776314fd07ed596e7249a96bcb5eb7ead612387d67a3b3c63(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__684f48d1e8322e3f96d5d2ad4c5b6fba2c1512165fdc541548a57f55744f15ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b5bfb765c0f572d7b029a64dc14dd0dba1ee3be3a3daa904379be654c8fff1c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64fdc148017d4a0b1a9e18b24ca4b8e7f73a4e73713161ae78301ce97d2b7630(
    value: typing.Optional[GoogleBigqueryDatasetAccessDatasetDataset],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__858a6428d7847b9ef010c5c41d6c6e3561912ca0733bb97b02bc241fd34cb0ed(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91eff44f6aafb2ad15a81678d1ba4a17bc706974c237a9727d8945429b9772c3(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a0c2c90f636435a07d0aee8766d9e8cdb7f48b10142e88978e983ed91286937(
    value: typing.Optional[GoogleBigqueryDatasetAccessDataset],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f71a9317d9eaa1dbb6712be1937932c46eced2cffc5c3fac44c382512dea964(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4d8ab300b4079e9295b08d7ece1bef849090d079205aeaf563352837d056899(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__689acfb4346973bb9c290bd631ee9bc79c135dd53833c285262da3f5e8b6195b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__facbbf7aafabd1745f4a512c1a0cc58f80250e02e39288193145118eca2bb94b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d478cc27adaacc36fc9360c2ac532646482eda90bdbb3e52022e9ffed1b873a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9de38e1e0cf7b8f81cdbd42bd8ec60f1c4b6b3c01ee503f08fa4249e9b6dcb3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleBigqueryDatasetAccess]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5786e1b0d4ba8e7b2b0c8b3999d6efb9cbee526a543a84381996c96d69cadaa3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb1714425ad2b936ec5170d4731fbab3bd3fd5db4780471cdab3d48ba81e08ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b589f56ada34c40cff137af06bbfc285ece387bec23142553996da804a3e76a8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f1bcb453ae2f2772b5e907f47f4dfd40864c79a39e5ae7d01a15f41a2db02cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f71b6272bcbca378fe75b68d1236711e6c5e1807a5a3390d4bf42c1f48e69e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b1869a8af1ca29db991ac39e070f35f3cf8ed065d667a564ccaeb46ae354604(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__217f7098a5ade70f14d9df12b30e83894944d2a08282b741be44639a63892e77(
    value: typing.Optional[typing.Union[GoogleBigqueryDatasetAccess, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70a49e663e5e5487a6cd6a37e2c76aa87a47f3cf2078359a4ae64734b5a4201a(
    *,
    dataset_id: builtins.str,
    project_id: builtins.str,
    routine_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35f59f19dfd4ed95b69a3fb290c3a10cc21d575f13624c237bf2687297d3ae9d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2472a09c4aca94c76f1d4d595ca08cfb4015fa4399dac7bd9ba07332b3fc862(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b50f714239c36141bc12cfc98323f6591af539d225abbb1f6c2ee8ae7ffe9a6b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cc395fa5fc592ee3f6ddbb5e1b4e4f7c62faccc5101ff4a145e99a437506aac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d63e91d897705da21bbefa67ee11de665054247b702a2e8d4c58ea4fe96ea51(
    value: typing.Optional[GoogleBigqueryDatasetAccessRoutine],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__592316e2ffc7a19d0a8acb8507260c0d1c329d78349b99977c564311ff68f42e(
    *,
    dataset_id: builtins.str,
    project_id: builtins.str,
    table_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b71ed2ad39adde649f4449fef33c596acf530be5eced712317b751170444185a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__695a82f06ebce8b31a14750f1b37aaa347f76d4bf05a7dfab9d68da7b4790e16(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__058e82f2fa3c967883d6c90f7ca308cd366a63c7844912106262a9926c0c7991(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc88be9fe73a322a468168316e105f143c79fa1eca69f0f60d2ceeff2ac46a9c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e89960afcbcd83c125d8150ade0ff996a9e9ff33cde66355a18262fb7e56d9ae(
    value: typing.Optional[GoogleBigqueryDatasetAccessView],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2246e8300e0dd33437569bdea98647baa6e1283e2a64a0ddb6d57bae172df0b9(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    dataset_id: builtins.str,
    access: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleBigqueryDatasetAccess, typing.Dict[builtins.str, typing.Any]]]]] = None,
    default_encryption_configuration: typing.Optional[typing.Union[GoogleBigqueryDatasetDefaultEncryptionConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    default_partition_expiration_ms: typing.Optional[jsii.Number] = None,
    default_table_expiration_ms: typing.Optional[jsii.Number] = None,
    delete_contents_on_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    description: typing.Optional[builtins.str] = None,
    friendly_name: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    location: typing.Optional[builtins.str] = None,
    max_time_travel_hours: typing.Optional[builtins.str] = None,
    project: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[GoogleBigqueryDatasetTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a4e25ef50cf914077bebc1d083852a51cd3fa7a213954d031f3524b89891f6a(
    *,
    kms_key_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b376cc4dc242dde1fbc845be71c73b7da3cc30cdba749054a74b2670a24ce001(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__653dfdd019b7495eb2e4d8ddf39d4701d0eb600d3eaf82d586d89813a1f76e8e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f092dae67262cc008cbe6e91e0b3137e9ddb7cff98846dedad79c219593f196e(
    value: typing.Optional[GoogleBigqueryDatasetDefaultEncryptionConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4a55aedb68beec1fd88c16fa1ff6b6cb0d996f505f1976020ea472b8e9ad660(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__006e1679dba925f9fbd88c3591389adf363f133d42faa4addc5ef757db6b96ec(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3da33bb1108b1f95c661fa04964e34b851468a5641e634f8a4aeadd8b0e839c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efd609582957055c5a6dd7aec96f89c7a19f884667b675187baaa624e720c81c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dc95452da6ee583db056480a84deb75dfdb8ae272c1034be07734c5b942dee7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a24b81a496606ddfdfd0573d12492534098ac68addf4a5e5081e95e04dfc5b14(
    value: typing.Optional[typing.Union[GoogleBigqueryDatasetTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
