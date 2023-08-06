'''
# `newrelic_workload`

Refer to the Terraform Registory for docs: [`newrelic_workload`](https://www.terraform.io/docs/providers/newrelic/r/workload).
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


class Workload(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.workload.Workload",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/newrelic/r/workload newrelic_workload}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        account_id: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        entity_guids: typing.Optional[typing.Sequence[builtins.str]] = None,
        entity_search_query: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkloadEntitySearchQuery", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        scope_account_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        status_config_automatic: typing.Optional[typing.Union["WorkloadStatusConfigAutomatic", typing.Dict[str, typing.Any]]] = None,
        status_config_static: typing.Optional[typing.Union["WorkloadStatusConfigStatic", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/newrelic/r/workload newrelic_workload} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The workload's name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#name Workload#name}
        :param account_id: The New Relic account ID where you want to create the workload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#account_id Workload#account_id}
        :param description: Relevant information about the workload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#description Workload#description}
        :param entity_guids: A list of entity GUIDs manually assigned to this workload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#entity_guids Workload#entity_guids}
        :param entity_search_query: entity_search_query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#entity_search_query Workload#entity_search_query}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#id Workload#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param scope_account_ids: A list of account IDs that will be used to get entities from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#scope_account_ids Workload#scope_account_ids}
        :param status_config_automatic: status_config_automatic block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#status_config_automatic Workload#status_config_automatic}
        :param status_config_static: status_config_static block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#status_config_static Workload#status_config_static}
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
                name: builtins.str,
                account_id: typing.Optional[jsii.Number] = None,
                description: typing.Optional[builtins.str] = None,
                entity_guids: typing.Optional[typing.Sequence[builtins.str]] = None,
                entity_search_query: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[WorkloadEntitySearchQuery, typing.Dict[str, typing.Any]]]]] = None,
                id: typing.Optional[builtins.str] = None,
                scope_account_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
                status_config_automatic: typing.Optional[typing.Union[WorkloadStatusConfigAutomatic, typing.Dict[str, typing.Any]]] = None,
                status_config_static: typing.Optional[typing.Union[WorkloadStatusConfigStatic, typing.Dict[str, typing.Any]]] = None,
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
        config = WorkloadConfig(
            name=name,
            account_id=account_id,
            description=description,
            entity_guids=entity_guids,
            entity_search_query=entity_search_query,
            id=id,
            scope_account_ids=scope_account_ids,
            status_config_automatic=status_config_automatic,
            status_config_static=status_config_static,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putEntitySearchQuery")
    def put_entity_search_query(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkloadEntitySearchQuery", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[WorkloadEntitySearchQuery, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEntitySearchQuery", [value]))

    @jsii.member(jsii_name="putStatusConfigAutomatic")
    def put_status_config_automatic(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        remaining_entities_rule: typing.Optional[typing.Union["WorkloadStatusConfigAutomaticRemainingEntitiesRule", typing.Dict[str, typing.Any]]] = None,
        rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkloadStatusConfigAutomaticRule", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Whether the automatic status configuration is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#enabled Workload#enabled}
        :param remaining_entities_rule: remaining_entities_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#remaining_entities_rule Workload#remaining_entities_rule}
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#rule Workload#rule}
        '''
        value = WorkloadStatusConfigAutomatic(
            enabled=enabled, remaining_entities_rule=remaining_entities_rule, rule=rule
        )

        return typing.cast(None, jsii.invoke(self, "putStatusConfigAutomatic", [value]))

    @jsii.member(jsii_name="putStatusConfigStatic")
    def put_status_config_static(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        status: builtins.str,
        description: typing.Optional[builtins.str] = None,
        summary: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Whether the static status configuration is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#enabled Workload#enabled}
        :param status: The status of the workload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#status Workload#status}
        :param description: A description that provides additional details about the status of the workload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#description Workload#description}
        :param summary: A short description of the status of the workload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#summary Workload#summary}
        '''
        value = WorkloadStatusConfigStatic(
            enabled=enabled, status=status, description=description, summary=summary
        )

        return typing.cast(None, jsii.invoke(self, "putStatusConfigStatic", [value]))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEntityGuids")
    def reset_entity_guids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEntityGuids", []))

    @jsii.member(jsii_name="resetEntitySearchQuery")
    def reset_entity_search_query(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEntitySearchQuery", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetScopeAccountIds")
    def reset_scope_account_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScopeAccountIds", []))

    @jsii.member(jsii_name="resetStatusConfigAutomatic")
    def reset_status_config_automatic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatusConfigAutomatic", []))

    @jsii.member(jsii_name="resetStatusConfigStatic")
    def reset_status_config_static(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatusConfigStatic", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="compositeEntitySearchQuery")
    def composite_entity_search_query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compositeEntitySearchQuery"))

    @builtins.property
    @jsii.member(jsii_name="entitySearchQuery")
    def entity_search_query(self) -> "WorkloadEntitySearchQueryList":
        return typing.cast("WorkloadEntitySearchQueryList", jsii.get(self, "entitySearchQuery"))

    @builtins.property
    @jsii.member(jsii_name="guid")
    def guid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "guid"))

    @builtins.property
    @jsii.member(jsii_name="permalink")
    def permalink(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "permalink"))

    @builtins.property
    @jsii.member(jsii_name="statusConfigAutomatic")
    def status_config_automatic(self) -> "WorkloadStatusConfigAutomaticOutputReference":
        return typing.cast("WorkloadStatusConfigAutomaticOutputReference", jsii.get(self, "statusConfigAutomatic"))

    @builtins.property
    @jsii.member(jsii_name="statusConfigStatic")
    def status_config_static(self) -> "WorkloadStatusConfigStaticOutputReference":
        return typing.cast("WorkloadStatusConfigStaticOutputReference", jsii.get(self, "statusConfigStatic"))

    @builtins.property
    @jsii.member(jsii_name="workloadId")
    def workload_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "workloadId"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="entityGuidsInput")
    def entity_guids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "entityGuidsInput"))

    @builtins.property
    @jsii.member(jsii_name="entitySearchQueryInput")
    def entity_search_query_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkloadEntitySearchQuery"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkloadEntitySearchQuery"]]], jsii.get(self, "entitySearchQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeAccountIdsInput")
    def scope_account_ids_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "scopeAccountIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="statusConfigAutomaticInput")
    def status_config_automatic_input(
        self,
    ) -> typing.Optional["WorkloadStatusConfigAutomatic"]:
        return typing.cast(typing.Optional["WorkloadStatusConfigAutomatic"], jsii.get(self, "statusConfigAutomaticInput"))

    @builtins.property
    @jsii.member(jsii_name="statusConfigStaticInput")
    def status_config_static_input(
        self,
    ) -> typing.Optional["WorkloadStatusConfigStatic"]:
        return typing.cast(typing.Optional["WorkloadStatusConfigStatic"], jsii.get(self, "statusConfigStaticInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

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
    @jsii.member(jsii_name="entityGuids")
    def entity_guids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "entityGuids"))

    @entity_guids.setter
    def entity_guids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entityGuids", value)

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
    @jsii.member(jsii_name="scopeAccountIds")
    def scope_account_ids(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "scopeAccountIds"))

    @scope_account_ids.setter
    def scope_account_ids(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            def stub(value: typing.List[jsii.Number]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scopeAccountIds", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.workload.WorkloadConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "account_id": "accountId",
        "description": "description",
        "entity_guids": "entityGuids",
        "entity_search_query": "entitySearchQuery",
        "id": "id",
        "scope_account_ids": "scopeAccountIds",
        "status_config_automatic": "statusConfigAutomatic",
        "status_config_static": "statusConfigStatic",
    },
)
class WorkloadConfig(cdktf.TerraformMetaArguments):
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
        name: builtins.str,
        account_id: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        entity_guids: typing.Optional[typing.Sequence[builtins.str]] = None,
        entity_search_query: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkloadEntitySearchQuery", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        scope_account_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        status_config_automatic: typing.Optional[typing.Union["WorkloadStatusConfigAutomatic", typing.Dict[str, typing.Any]]] = None,
        status_config_static: typing.Optional[typing.Union["WorkloadStatusConfigStatic", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The workload's name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#name Workload#name}
        :param account_id: The New Relic account ID where you want to create the workload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#account_id Workload#account_id}
        :param description: Relevant information about the workload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#description Workload#description}
        :param entity_guids: A list of entity GUIDs manually assigned to this workload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#entity_guids Workload#entity_guids}
        :param entity_search_query: entity_search_query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#entity_search_query Workload#entity_search_query}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#id Workload#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param scope_account_ids: A list of account IDs that will be used to get entities from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#scope_account_ids Workload#scope_account_ids}
        :param status_config_automatic: status_config_automatic block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#status_config_automatic Workload#status_config_automatic}
        :param status_config_static: status_config_static block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#status_config_static Workload#status_config_static}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(status_config_automatic, dict):
            status_config_automatic = WorkloadStatusConfigAutomatic(**status_config_automatic)
        if isinstance(status_config_static, dict):
            status_config_static = WorkloadStatusConfigStatic(**status_config_static)
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
                name: builtins.str,
                account_id: typing.Optional[jsii.Number] = None,
                description: typing.Optional[builtins.str] = None,
                entity_guids: typing.Optional[typing.Sequence[builtins.str]] = None,
                entity_search_query: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[WorkloadEntitySearchQuery, typing.Dict[str, typing.Any]]]]] = None,
                id: typing.Optional[builtins.str] = None,
                scope_account_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
                status_config_automatic: typing.Optional[typing.Union[WorkloadStatusConfigAutomatic, typing.Dict[str, typing.Any]]] = None,
                status_config_static: typing.Optional[typing.Union[WorkloadStatusConfigStatic, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument entity_guids", value=entity_guids, expected_type=type_hints["entity_guids"])
            check_type(argname="argument entity_search_query", value=entity_search_query, expected_type=type_hints["entity_search_query"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument scope_account_ids", value=scope_account_ids, expected_type=type_hints["scope_account_ids"])
            check_type(argname="argument status_config_automatic", value=status_config_automatic, expected_type=type_hints["status_config_automatic"])
            check_type(argname="argument status_config_static", value=status_config_static, expected_type=type_hints["status_config_static"])
        self._values: typing.Dict[str, typing.Any] = {
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
        if account_id is not None:
            self._values["account_id"] = account_id
        if description is not None:
            self._values["description"] = description
        if entity_guids is not None:
            self._values["entity_guids"] = entity_guids
        if entity_search_query is not None:
            self._values["entity_search_query"] = entity_search_query
        if id is not None:
            self._values["id"] = id
        if scope_account_ids is not None:
            self._values["scope_account_ids"] = scope_account_ids
        if status_config_automatic is not None:
            self._values["status_config_automatic"] = status_config_automatic
        if status_config_static is not None:
            self._values["status_config_static"] = status_config_static

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
    def name(self) -> builtins.str:
        '''The workload's name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#name Workload#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[jsii.Number]:
        '''The New Relic account ID where you want to create the workload.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#account_id Workload#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Relevant information about the workload.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#description Workload#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def entity_guids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of entity GUIDs manually assigned to this workload.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#entity_guids Workload#entity_guids}
        '''
        result = self._values.get("entity_guids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def entity_search_query(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkloadEntitySearchQuery"]]]:
        '''entity_search_query block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#entity_search_query Workload#entity_search_query}
        '''
        result = self._values.get("entity_search_query")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkloadEntitySearchQuery"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#id Workload#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scope_account_ids(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''A list of account IDs that will be used to get entities from.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#scope_account_ids Workload#scope_account_ids}
        '''
        result = self._values.get("scope_account_ids")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def status_config_automatic(
        self,
    ) -> typing.Optional["WorkloadStatusConfigAutomatic"]:
        '''status_config_automatic block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#status_config_automatic Workload#status_config_automatic}
        '''
        result = self._values.get("status_config_automatic")
        return typing.cast(typing.Optional["WorkloadStatusConfigAutomatic"], result)

    @builtins.property
    def status_config_static(self) -> typing.Optional["WorkloadStatusConfigStatic"]:
        '''status_config_static block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#status_config_static Workload#status_config_static}
        '''
        result = self._values.get("status_config_static")
        return typing.cast(typing.Optional["WorkloadStatusConfigStatic"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.workload.WorkloadEntitySearchQuery",
    jsii_struct_bases=[],
    name_mapping={"query": "query"},
)
class WorkloadEntitySearchQuery:
    def __init__(self, *, query: builtins.str) -> None:
        '''
        :param query: The query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#query Workload#query}
        '''
        if __debug__:
            def stub(*, query: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
        self._values: typing.Dict[str, typing.Any] = {
            "query": query,
        }

    @builtins.property
    def query(self) -> builtins.str:
        '''The query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#query Workload#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadEntitySearchQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WorkloadEntitySearchQueryList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.workload.WorkloadEntitySearchQueryList",
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
    def get(self, index: jsii.Number) -> "WorkloadEntitySearchQueryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WorkloadEntitySearchQueryOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkloadEntitySearchQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkloadEntitySearchQuery]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkloadEntitySearchQuery]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkloadEntitySearchQuery]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WorkloadEntitySearchQueryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.workload.WorkloadEntitySearchQueryOutputReference",
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
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WorkloadEntitySearchQuery, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WorkloadEntitySearchQuery, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WorkloadEntitySearchQuery, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[WorkloadEntitySearchQuery, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.workload.WorkloadStatusConfigAutomatic",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "remaining_entities_rule": "remainingEntitiesRule",
        "rule": "rule",
    },
)
class WorkloadStatusConfigAutomatic:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        remaining_entities_rule: typing.Optional[typing.Union["WorkloadStatusConfigAutomaticRemainingEntitiesRule", typing.Dict[str, typing.Any]]] = None,
        rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkloadStatusConfigAutomaticRule", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Whether the automatic status configuration is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#enabled Workload#enabled}
        :param remaining_entities_rule: remaining_entities_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#remaining_entities_rule Workload#remaining_entities_rule}
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#rule Workload#rule}
        '''
        if isinstance(remaining_entities_rule, dict):
            remaining_entities_rule = WorkloadStatusConfigAutomaticRemainingEntitiesRule(**remaining_entities_rule)
        if __debug__:
            def stub(
                *,
                enabled: typing.Union[builtins.bool, cdktf.IResolvable],
                remaining_entities_rule: typing.Optional[typing.Union[WorkloadStatusConfigAutomaticRemainingEntitiesRule, typing.Dict[str, typing.Any]]] = None,
                rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[WorkloadStatusConfigAutomaticRule, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument remaining_entities_rule", value=remaining_entities_rule, expected_type=type_hints["remaining_entities_rule"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }
        if remaining_entities_rule is not None:
            self._values["remaining_entities_rule"] = remaining_entities_rule
        if rule is not None:
            self._values["rule"] = rule

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Whether the automatic status configuration is enabled or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#enabled Workload#enabled}
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def remaining_entities_rule(
        self,
    ) -> typing.Optional["WorkloadStatusConfigAutomaticRemainingEntitiesRule"]:
        '''remaining_entities_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#remaining_entities_rule Workload#remaining_entities_rule}
        '''
        result = self._values.get("remaining_entities_rule")
        return typing.cast(typing.Optional["WorkloadStatusConfigAutomaticRemainingEntitiesRule"], result)

    @builtins.property
    def rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkloadStatusConfigAutomaticRule"]]]:
        '''rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#rule Workload#rule}
        '''
        result = self._values.get("rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkloadStatusConfigAutomaticRule"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadStatusConfigAutomatic(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WorkloadStatusConfigAutomaticOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.workload.WorkloadStatusConfigAutomaticOutputReference",
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

    @jsii.member(jsii_name="putRemainingEntitiesRule")
    def put_remaining_entities_rule(
        self,
        *,
        remaining_entities_rule_rollup: typing.Union["WorkloadStatusConfigAutomaticRemainingEntitiesRuleRemainingEntitiesRuleRollup", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param remaining_entities_rule_rollup: remaining_entities_rule_rollup block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#remaining_entities_rule_rollup Workload#remaining_entities_rule_rollup}
        '''
        value = WorkloadStatusConfigAutomaticRemainingEntitiesRule(
            remaining_entities_rule_rollup=remaining_entities_rule_rollup
        )

        return typing.cast(None, jsii.invoke(self, "putRemainingEntitiesRule", [value]))

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkloadStatusConfigAutomaticRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[WorkloadStatusConfigAutomaticRule, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRule", [value]))

    @jsii.member(jsii_name="resetRemainingEntitiesRule")
    def reset_remaining_entities_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemainingEntitiesRule", []))

    @jsii.member(jsii_name="resetRule")
    def reset_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRule", []))

    @builtins.property
    @jsii.member(jsii_name="remainingEntitiesRule")
    def remaining_entities_rule(
        self,
    ) -> "WorkloadStatusConfigAutomaticRemainingEntitiesRuleOutputReference":
        return typing.cast("WorkloadStatusConfigAutomaticRemainingEntitiesRuleOutputReference", jsii.get(self, "remainingEntitiesRule"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> "WorkloadStatusConfigAutomaticRuleList":
        return typing.cast("WorkloadStatusConfigAutomaticRuleList", jsii.get(self, "rule"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="remainingEntitiesRuleInput")
    def remaining_entities_rule_input(
        self,
    ) -> typing.Optional["WorkloadStatusConfigAutomaticRemainingEntitiesRule"]:
        return typing.cast(typing.Optional["WorkloadStatusConfigAutomaticRemainingEntitiesRule"], jsii.get(self, "remainingEntitiesRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkloadStatusConfigAutomaticRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkloadStatusConfigAutomaticRule"]]], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WorkloadStatusConfigAutomatic]:
        return typing.cast(typing.Optional[WorkloadStatusConfigAutomatic], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WorkloadStatusConfigAutomatic],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[WorkloadStatusConfigAutomatic]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.workload.WorkloadStatusConfigAutomaticRemainingEntitiesRule",
    jsii_struct_bases=[],
    name_mapping={"remaining_entities_rule_rollup": "remainingEntitiesRuleRollup"},
)
class WorkloadStatusConfigAutomaticRemainingEntitiesRule:
    def __init__(
        self,
        *,
        remaining_entities_rule_rollup: typing.Union["WorkloadStatusConfigAutomaticRemainingEntitiesRuleRemainingEntitiesRuleRollup", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param remaining_entities_rule_rollup: remaining_entities_rule_rollup block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#remaining_entities_rule_rollup Workload#remaining_entities_rule_rollup}
        '''
        if isinstance(remaining_entities_rule_rollup, dict):
            remaining_entities_rule_rollup = WorkloadStatusConfigAutomaticRemainingEntitiesRuleRemainingEntitiesRuleRollup(**remaining_entities_rule_rollup)
        if __debug__:
            def stub(
                *,
                remaining_entities_rule_rollup: typing.Union[WorkloadStatusConfigAutomaticRemainingEntitiesRuleRemainingEntitiesRuleRollup, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument remaining_entities_rule_rollup", value=remaining_entities_rule_rollup, expected_type=type_hints["remaining_entities_rule_rollup"])
        self._values: typing.Dict[str, typing.Any] = {
            "remaining_entities_rule_rollup": remaining_entities_rule_rollup,
        }

    @builtins.property
    def remaining_entities_rule_rollup(
        self,
    ) -> "WorkloadStatusConfigAutomaticRemainingEntitiesRuleRemainingEntitiesRuleRollup":
        '''remaining_entities_rule_rollup block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#remaining_entities_rule_rollup Workload#remaining_entities_rule_rollup}
        '''
        result = self._values.get("remaining_entities_rule_rollup")
        assert result is not None, "Required property 'remaining_entities_rule_rollup' is missing"
        return typing.cast("WorkloadStatusConfigAutomaticRemainingEntitiesRuleRemainingEntitiesRuleRollup", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadStatusConfigAutomaticRemainingEntitiesRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WorkloadStatusConfigAutomaticRemainingEntitiesRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.workload.WorkloadStatusConfigAutomaticRemainingEntitiesRuleOutputReference",
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

    @jsii.member(jsii_name="putRemainingEntitiesRuleRollup")
    def put_remaining_entities_rule_rollup(
        self,
        *,
        group_by: builtins.str,
        strategy: builtins.str,
        threshold_type: typing.Optional[builtins.str] = None,
        threshold_value: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param group_by: The grouping to be applied to the remaining entities. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#group_by Workload#group_by}
        :param strategy: The rollup strategy that is applied to a group of entities. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#strategy Workload#strategy}
        :param threshold_type: Type of threshold defined for the rule. This is an optional field that only applies when strategy is WORST_STATUS_WINS. Use a threshold to roll up the worst status only after a certain amount of entities are not operational. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#threshold_type Workload#threshold_type}
        :param threshold_value: Threshold value defined for the rule. This optional field is used in combination with thresholdType. If the threshold type is null, the threshold value will be ignored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#threshold_value Workload#threshold_value}
        '''
        value = WorkloadStatusConfigAutomaticRemainingEntitiesRuleRemainingEntitiesRuleRollup(
            group_by=group_by,
            strategy=strategy,
            threshold_type=threshold_type,
            threshold_value=threshold_value,
        )

        return typing.cast(None, jsii.invoke(self, "putRemainingEntitiesRuleRollup", [value]))

    @builtins.property
    @jsii.member(jsii_name="remainingEntitiesRuleRollup")
    def remaining_entities_rule_rollup(
        self,
    ) -> "WorkloadStatusConfigAutomaticRemainingEntitiesRuleRemainingEntitiesRuleRollupOutputReference":
        return typing.cast("WorkloadStatusConfigAutomaticRemainingEntitiesRuleRemainingEntitiesRuleRollupOutputReference", jsii.get(self, "remainingEntitiesRuleRollup"))

    @builtins.property
    @jsii.member(jsii_name="remainingEntitiesRuleRollupInput")
    def remaining_entities_rule_rollup_input(
        self,
    ) -> typing.Optional["WorkloadStatusConfigAutomaticRemainingEntitiesRuleRemainingEntitiesRuleRollup"]:
        return typing.cast(typing.Optional["WorkloadStatusConfigAutomaticRemainingEntitiesRuleRemainingEntitiesRuleRollup"], jsii.get(self, "remainingEntitiesRuleRollupInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WorkloadStatusConfigAutomaticRemainingEntitiesRule]:
        return typing.cast(typing.Optional[WorkloadStatusConfigAutomaticRemainingEntitiesRule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WorkloadStatusConfigAutomaticRemainingEntitiesRule],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[WorkloadStatusConfigAutomaticRemainingEntitiesRule],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.workload.WorkloadStatusConfigAutomaticRemainingEntitiesRuleRemainingEntitiesRuleRollup",
    jsii_struct_bases=[],
    name_mapping={
        "group_by": "groupBy",
        "strategy": "strategy",
        "threshold_type": "thresholdType",
        "threshold_value": "thresholdValue",
    },
)
class WorkloadStatusConfigAutomaticRemainingEntitiesRuleRemainingEntitiesRuleRollup:
    def __init__(
        self,
        *,
        group_by: builtins.str,
        strategy: builtins.str,
        threshold_type: typing.Optional[builtins.str] = None,
        threshold_value: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param group_by: The grouping to be applied to the remaining entities. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#group_by Workload#group_by}
        :param strategy: The rollup strategy that is applied to a group of entities. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#strategy Workload#strategy}
        :param threshold_type: Type of threshold defined for the rule. This is an optional field that only applies when strategy is WORST_STATUS_WINS. Use a threshold to roll up the worst status only after a certain amount of entities are not operational. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#threshold_type Workload#threshold_type}
        :param threshold_value: Threshold value defined for the rule. This optional field is used in combination with thresholdType. If the threshold type is null, the threshold value will be ignored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#threshold_value Workload#threshold_value}
        '''
        if __debug__:
            def stub(
                *,
                group_by: builtins.str,
                strategy: builtins.str,
                threshold_type: typing.Optional[builtins.str] = None,
                threshold_value: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument group_by", value=group_by, expected_type=type_hints["group_by"])
            check_type(argname="argument strategy", value=strategy, expected_type=type_hints["strategy"])
            check_type(argname="argument threshold_type", value=threshold_type, expected_type=type_hints["threshold_type"])
            check_type(argname="argument threshold_value", value=threshold_value, expected_type=type_hints["threshold_value"])
        self._values: typing.Dict[str, typing.Any] = {
            "group_by": group_by,
            "strategy": strategy,
        }
        if threshold_type is not None:
            self._values["threshold_type"] = threshold_type
        if threshold_value is not None:
            self._values["threshold_value"] = threshold_value

    @builtins.property
    def group_by(self) -> builtins.str:
        '''The grouping to be applied to the remaining entities.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#group_by Workload#group_by}
        '''
        result = self._values.get("group_by")
        assert result is not None, "Required property 'group_by' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def strategy(self) -> builtins.str:
        '''The rollup strategy that is applied to a group of entities.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#strategy Workload#strategy}
        '''
        result = self._values.get("strategy")
        assert result is not None, "Required property 'strategy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def threshold_type(self) -> typing.Optional[builtins.str]:
        '''Type of threshold defined for the rule.

        This is an optional field that only applies when strategy is WORST_STATUS_WINS. Use a threshold to roll up the worst status only after a certain amount of entities are not operational.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#threshold_type Workload#threshold_type}
        '''
        result = self._values.get("threshold_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def threshold_value(self) -> typing.Optional[jsii.Number]:
        '''Threshold value defined for the rule.

        This optional field is used in combination with thresholdType. If the threshold type is null, the threshold value will be ignored.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#threshold_value Workload#threshold_value}
        '''
        result = self._values.get("threshold_value")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadStatusConfigAutomaticRemainingEntitiesRuleRemainingEntitiesRuleRollup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WorkloadStatusConfigAutomaticRemainingEntitiesRuleRemainingEntitiesRuleRollupOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.workload.WorkloadStatusConfigAutomaticRemainingEntitiesRuleRemainingEntitiesRuleRollupOutputReference",
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

    @jsii.member(jsii_name="resetThresholdType")
    def reset_threshold_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThresholdType", []))

    @jsii.member(jsii_name="resetThresholdValue")
    def reset_threshold_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThresholdValue", []))

    @builtins.property
    @jsii.member(jsii_name="groupByInput")
    def group_by_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupByInput"))

    @builtins.property
    @jsii.member(jsii_name="strategyInput")
    def strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "strategyInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdTypeInput")
    def threshold_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thresholdTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdValueInput")
    def threshold_value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdValueInput"))

    @builtins.property
    @jsii.member(jsii_name="groupBy")
    def group_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupBy"))

    @group_by.setter
    def group_by(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupBy", value)

    @builtins.property
    @jsii.member(jsii_name="strategy")
    def strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "strategy"))

    @strategy.setter
    def strategy(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "strategy", value)

    @builtins.property
    @jsii.member(jsii_name="thresholdType")
    def threshold_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thresholdType"))

    @threshold_type.setter
    def threshold_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thresholdType", value)

    @builtins.property
    @jsii.member(jsii_name="thresholdValue")
    def threshold_value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "thresholdValue"))

    @threshold_value.setter
    def threshold_value(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thresholdValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WorkloadStatusConfigAutomaticRemainingEntitiesRuleRemainingEntitiesRuleRollup]:
        return typing.cast(typing.Optional[WorkloadStatusConfigAutomaticRemainingEntitiesRuleRemainingEntitiesRuleRollup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WorkloadStatusConfigAutomaticRemainingEntitiesRuleRemainingEntitiesRuleRollup],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[WorkloadStatusConfigAutomaticRemainingEntitiesRuleRemainingEntitiesRuleRollup],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.workload.WorkloadStatusConfigAutomaticRule",
    jsii_struct_bases=[],
    name_mapping={
        "rollup": "rollup",
        "entity_guids": "entityGuids",
        "nrql_query": "nrqlQuery",
    },
)
class WorkloadStatusConfigAutomaticRule:
    def __init__(
        self,
        *,
        rollup: typing.Union["WorkloadStatusConfigAutomaticRuleRollup", typing.Dict[str, typing.Any]],
        entity_guids: typing.Optional[typing.Sequence[builtins.str]] = None,
        nrql_query: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkloadStatusConfigAutomaticRuleNrqlQuery", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rollup: rollup block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#rollup Workload#rollup}
        :param entity_guids: A list of entity GUIDs composing the rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#entity_guids Workload#entity_guids}
        :param nrql_query: nrql_query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#nrql_query Workload#nrql_query}
        '''
        if isinstance(rollup, dict):
            rollup = WorkloadStatusConfigAutomaticRuleRollup(**rollup)
        if __debug__:
            def stub(
                *,
                rollup: typing.Union[WorkloadStatusConfigAutomaticRuleRollup, typing.Dict[str, typing.Any]],
                entity_guids: typing.Optional[typing.Sequence[builtins.str]] = None,
                nrql_query: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[WorkloadStatusConfigAutomaticRuleNrqlQuery, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument rollup", value=rollup, expected_type=type_hints["rollup"])
            check_type(argname="argument entity_guids", value=entity_guids, expected_type=type_hints["entity_guids"])
            check_type(argname="argument nrql_query", value=nrql_query, expected_type=type_hints["nrql_query"])
        self._values: typing.Dict[str, typing.Any] = {
            "rollup": rollup,
        }
        if entity_guids is not None:
            self._values["entity_guids"] = entity_guids
        if nrql_query is not None:
            self._values["nrql_query"] = nrql_query

    @builtins.property
    def rollup(self) -> "WorkloadStatusConfigAutomaticRuleRollup":
        '''rollup block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#rollup Workload#rollup}
        '''
        result = self._values.get("rollup")
        assert result is not None, "Required property 'rollup' is missing"
        return typing.cast("WorkloadStatusConfigAutomaticRuleRollup", result)

    @builtins.property
    def entity_guids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of entity GUIDs composing the rule.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#entity_guids Workload#entity_guids}
        '''
        result = self._values.get("entity_guids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def nrql_query(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkloadStatusConfigAutomaticRuleNrqlQuery"]]]:
        '''nrql_query block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#nrql_query Workload#nrql_query}
        '''
        result = self._values.get("nrql_query")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkloadStatusConfigAutomaticRuleNrqlQuery"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadStatusConfigAutomaticRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WorkloadStatusConfigAutomaticRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.workload.WorkloadStatusConfigAutomaticRuleList",
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
    ) -> "WorkloadStatusConfigAutomaticRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WorkloadStatusConfigAutomaticRuleOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkloadStatusConfigAutomaticRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkloadStatusConfigAutomaticRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkloadStatusConfigAutomaticRule]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkloadStatusConfigAutomaticRule]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.workload.WorkloadStatusConfigAutomaticRuleNrqlQuery",
    jsii_struct_bases=[],
    name_mapping={"query": "query"},
)
class WorkloadStatusConfigAutomaticRuleNrqlQuery:
    def __init__(self, *, query: builtins.str) -> None:
        '''
        :param query: The entity search query that is used to perform the search of a group of entities. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#query Workload#query}
        '''
        if __debug__:
            def stub(*, query: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
        self._values: typing.Dict[str, typing.Any] = {
            "query": query,
        }

    @builtins.property
    def query(self) -> builtins.str:
        '''The entity search query that is used to perform the search of a group of entities.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#query Workload#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadStatusConfigAutomaticRuleNrqlQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WorkloadStatusConfigAutomaticRuleNrqlQueryList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.workload.WorkloadStatusConfigAutomaticRuleNrqlQueryList",
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
    ) -> "WorkloadStatusConfigAutomaticRuleNrqlQueryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WorkloadStatusConfigAutomaticRuleNrqlQueryOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkloadStatusConfigAutomaticRuleNrqlQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkloadStatusConfigAutomaticRuleNrqlQuery]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkloadStatusConfigAutomaticRuleNrqlQuery]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkloadStatusConfigAutomaticRuleNrqlQuery]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WorkloadStatusConfigAutomaticRuleNrqlQueryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.workload.WorkloadStatusConfigAutomaticRuleNrqlQueryOutputReference",
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
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WorkloadStatusConfigAutomaticRuleNrqlQuery, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WorkloadStatusConfigAutomaticRuleNrqlQuery, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WorkloadStatusConfigAutomaticRuleNrqlQuery, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[WorkloadStatusConfigAutomaticRuleNrqlQuery, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WorkloadStatusConfigAutomaticRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.workload.WorkloadStatusConfigAutomaticRuleOutputReference",
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

    @jsii.member(jsii_name="putNrqlQuery")
    def put_nrql_query(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[WorkloadStatusConfigAutomaticRuleNrqlQuery, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[WorkloadStatusConfigAutomaticRuleNrqlQuery, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNrqlQuery", [value]))

    @jsii.member(jsii_name="putRollup")
    def put_rollup(
        self,
        *,
        strategy: builtins.str,
        threshold_type: typing.Optional[builtins.str] = None,
        threshold_value: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param strategy: The rollup strategy that is applied to a group of entities. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#strategy Workload#strategy}
        :param threshold_type: Type of threshold defined for the rule. This is an optional field that only applies when strategy is WORST_STATUS_WINS. Use a threshold to roll up the worst status only after a certain amount of entities are not operational. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#threshold_type Workload#threshold_type}
        :param threshold_value: Threshold value defined for the rule. This optional field is used in combination with thresholdType. If the threshold type is null, the threshold value will be ignored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#threshold_value Workload#threshold_value}
        '''
        value = WorkloadStatusConfigAutomaticRuleRollup(
            strategy=strategy,
            threshold_type=threshold_type,
            threshold_value=threshold_value,
        )

        return typing.cast(None, jsii.invoke(self, "putRollup", [value]))

    @jsii.member(jsii_name="resetEntityGuids")
    def reset_entity_guids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEntityGuids", []))

    @jsii.member(jsii_name="resetNrqlQuery")
    def reset_nrql_query(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNrqlQuery", []))

    @builtins.property
    @jsii.member(jsii_name="nrqlQuery")
    def nrql_query(self) -> WorkloadStatusConfigAutomaticRuleNrqlQueryList:
        return typing.cast(WorkloadStatusConfigAutomaticRuleNrqlQueryList, jsii.get(self, "nrqlQuery"))

    @builtins.property
    @jsii.member(jsii_name="rollup")
    def rollup(self) -> "WorkloadStatusConfigAutomaticRuleRollupOutputReference":
        return typing.cast("WorkloadStatusConfigAutomaticRuleRollupOutputReference", jsii.get(self, "rollup"))

    @builtins.property
    @jsii.member(jsii_name="entityGuidsInput")
    def entity_guids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "entityGuidsInput"))

    @builtins.property
    @jsii.member(jsii_name="nrqlQueryInput")
    def nrql_query_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkloadStatusConfigAutomaticRuleNrqlQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkloadStatusConfigAutomaticRuleNrqlQuery]]], jsii.get(self, "nrqlQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="rollupInput")
    def rollup_input(
        self,
    ) -> typing.Optional["WorkloadStatusConfigAutomaticRuleRollup"]:
        return typing.cast(typing.Optional["WorkloadStatusConfigAutomaticRuleRollup"], jsii.get(self, "rollupInput"))

    @builtins.property
    @jsii.member(jsii_name="entityGuids")
    def entity_guids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "entityGuids"))

    @entity_guids.setter
    def entity_guids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entityGuids", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WorkloadStatusConfigAutomaticRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WorkloadStatusConfigAutomaticRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WorkloadStatusConfigAutomaticRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[WorkloadStatusConfigAutomaticRule, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.workload.WorkloadStatusConfigAutomaticRuleRollup",
    jsii_struct_bases=[],
    name_mapping={
        "strategy": "strategy",
        "threshold_type": "thresholdType",
        "threshold_value": "thresholdValue",
    },
)
class WorkloadStatusConfigAutomaticRuleRollup:
    def __init__(
        self,
        *,
        strategy: builtins.str,
        threshold_type: typing.Optional[builtins.str] = None,
        threshold_value: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param strategy: The rollup strategy that is applied to a group of entities. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#strategy Workload#strategy}
        :param threshold_type: Type of threshold defined for the rule. This is an optional field that only applies when strategy is WORST_STATUS_WINS. Use a threshold to roll up the worst status only after a certain amount of entities are not operational. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#threshold_type Workload#threshold_type}
        :param threshold_value: Threshold value defined for the rule. This optional field is used in combination with thresholdType. If the threshold type is null, the threshold value will be ignored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#threshold_value Workload#threshold_value}
        '''
        if __debug__:
            def stub(
                *,
                strategy: builtins.str,
                threshold_type: typing.Optional[builtins.str] = None,
                threshold_value: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument strategy", value=strategy, expected_type=type_hints["strategy"])
            check_type(argname="argument threshold_type", value=threshold_type, expected_type=type_hints["threshold_type"])
            check_type(argname="argument threshold_value", value=threshold_value, expected_type=type_hints["threshold_value"])
        self._values: typing.Dict[str, typing.Any] = {
            "strategy": strategy,
        }
        if threshold_type is not None:
            self._values["threshold_type"] = threshold_type
        if threshold_value is not None:
            self._values["threshold_value"] = threshold_value

    @builtins.property
    def strategy(self) -> builtins.str:
        '''The rollup strategy that is applied to a group of entities.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#strategy Workload#strategy}
        '''
        result = self._values.get("strategy")
        assert result is not None, "Required property 'strategy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def threshold_type(self) -> typing.Optional[builtins.str]:
        '''Type of threshold defined for the rule.

        This is an optional field that only applies when strategy is WORST_STATUS_WINS. Use a threshold to roll up the worst status only after a certain amount of entities are not operational.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#threshold_type Workload#threshold_type}
        '''
        result = self._values.get("threshold_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def threshold_value(self) -> typing.Optional[jsii.Number]:
        '''Threshold value defined for the rule.

        This optional field is used in combination with thresholdType. If the threshold type is null, the threshold value will be ignored.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#threshold_value Workload#threshold_value}
        '''
        result = self._values.get("threshold_value")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadStatusConfigAutomaticRuleRollup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WorkloadStatusConfigAutomaticRuleRollupOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.workload.WorkloadStatusConfigAutomaticRuleRollupOutputReference",
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

    @jsii.member(jsii_name="resetThresholdType")
    def reset_threshold_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThresholdType", []))

    @jsii.member(jsii_name="resetThresholdValue")
    def reset_threshold_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThresholdValue", []))

    @builtins.property
    @jsii.member(jsii_name="strategyInput")
    def strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "strategyInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdTypeInput")
    def threshold_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thresholdTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdValueInput")
    def threshold_value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdValueInput"))

    @builtins.property
    @jsii.member(jsii_name="strategy")
    def strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "strategy"))

    @strategy.setter
    def strategy(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "strategy", value)

    @builtins.property
    @jsii.member(jsii_name="thresholdType")
    def threshold_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thresholdType"))

    @threshold_type.setter
    def threshold_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thresholdType", value)

    @builtins.property
    @jsii.member(jsii_name="thresholdValue")
    def threshold_value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "thresholdValue"))

    @threshold_value.setter
    def threshold_value(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thresholdValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WorkloadStatusConfigAutomaticRuleRollup]:
        return typing.cast(typing.Optional[WorkloadStatusConfigAutomaticRuleRollup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WorkloadStatusConfigAutomaticRuleRollup],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[WorkloadStatusConfigAutomaticRuleRollup],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.workload.WorkloadStatusConfigStatic",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "status": "status",
        "description": "description",
        "summary": "summary",
    },
)
class WorkloadStatusConfigStatic:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        status: builtins.str,
        description: typing.Optional[builtins.str] = None,
        summary: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Whether the static status configuration is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#enabled Workload#enabled}
        :param status: The status of the workload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#status Workload#status}
        :param description: A description that provides additional details about the status of the workload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#description Workload#description}
        :param summary: A short description of the status of the workload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#summary Workload#summary}
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Union[builtins.bool, cdktf.IResolvable],
                status: builtins.str,
                description: typing.Optional[builtins.str] = None,
                summary: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument summary", value=summary, expected_type=type_hints["summary"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
            "status": status,
        }
        if description is not None:
            self._values["description"] = description
        if summary is not None:
            self._values["summary"] = summary

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Whether the static status configuration is enabled or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#enabled Workload#enabled}
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def status(self) -> builtins.str:
        '''The status of the workload.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#status Workload#status}
        '''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description that provides additional details about the status of the workload.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#description Workload#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def summary(self) -> typing.Optional[builtins.str]:
        '''A short description of the status of the workload.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workload#summary Workload#summary}
        '''
        result = self._values.get("summary")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadStatusConfigStatic(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WorkloadStatusConfigStaticOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.workload.WorkloadStatusConfigStaticOutputReference",
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

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetSummary")
    def reset_summary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSummary", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="summaryInput")
    def summary_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "summaryInput"))

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
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="summary")
    def summary(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "summary"))

    @summary.setter
    def summary(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "summary", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WorkloadStatusConfigStatic]:
        return typing.cast(typing.Optional[WorkloadStatusConfigStatic], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WorkloadStatusConfigStatic],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[WorkloadStatusConfigStatic]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Workload",
    "WorkloadConfig",
    "WorkloadEntitySearchQuery",
    "WorkloadEntitySearchQueryList",
    "WorkloadEntitySearchQueryOutputReference",
    "WorkloadStatusConfigAutomatic",
    "WorkloadStatusConfigAutomaticOutputReference",
    "WorkloadStatusConfigAutomaticRemainingEntitiesRule",
    "WorkloadStatusConfigAutomaticRemainingEntitiesRuleOutputReference",
    "WorkloadStatusConfigAutomaticRemainingEntitiesRuleRemainingEntitiesRuleRollup",
    "WorkloadStatusConfigAutomaticRemainingEntitiesRuleRemainingEntitiesRuleRollupOutputReference",
    "WorkloadStatusConfigAutomaticRule",
    "WorkloadStatusConfigAutomaticRuleList",
    "WorkloadStatusConfigAutomaticRuleNrqlQuery",
    "WorkloadStatusConfigAutomaticRuleNrqlQueryList",
    "WorkloadStatusConfigAutomaticRuleNrqlQueryOutputReference",
    "WorkloadStatusConfigAutomaticRuleOutputReference",
    "WorkloadStatusConfigAutomaticRuleRollup",
    "WorkloadStatusConfigAutomaticRuleRollupOutputReference",
    "WorkloadStatusConfigStatic",
    "WorkloadStatusConfigStaticOutputReference",
]

publication.publish()
