'''
# `newrelic_workflow`

Refer to the Terraform Registory for docs: [`newrelic_workflow`](https://www.terraform.io/docs/providers/newrelic/r/workflow).
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


class Workflow(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.workflow.Workflow",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/newrelic/r/workflow newrelic_workflow}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        destination: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkflowDestination", typing.Dict[str, typing.Any]]]],
        issues_filter: typing.Union["WorkflowIssuesFilter", typing.Dict[str, typing.Any]],
        muting_rules_handling: builtins.str,
        name: builtins.str,
        account_id: typing.Optional[jsii.Number] = None,
        destinations_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enrichments: typing.Optional[typing.Union["WorkflowEnrichments", typing.Dict[str, typing.Any]]] = None,
        enrichments_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/newrelic/r/workflow newrelic_workflow} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param destination: destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#destination Workflow#destination}
        :param issues_filter: issues_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#issues_filter Workflow#issues_filter}
        :param muting_rules_handling: The type of the muting rule handling. One of: (NOTIFY_ALL_ISSUES, DONT_NOTIFY_FULLY_MUTED_ISSUES, DONT_NOTIFY_FULLY_OR_PARTIALLY_MUTED_ISSUES). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#muting_rules_handling Workflow#muting_rules_handling}
        :param name: (Required) The name of the workflow. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#name Workflow#name}
        :param account_id: The account id of the workflow. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#account_id Workflow#account_id}
        :param destinations_enabled: Indicates whether the destinations are enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#destinations_enabled Workflow#destinations_enabled}
        :param enabled: Indicates whether the workflow is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#enabled Workflow#enabled}
        :param enrichments: enrichments block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#enrichments Workflow#enrichments}
        :param enrichments_enabled: Indicates whether the enrichments are enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#enrichments_enabled Workflow#enrichments_enabled}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#id Workflow#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
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
                destination: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[WorkflowDestination, typing.Dict[str, typing.Any]]]],
                issues_filter: typing.Union[WorkflowIssuesFilter, typing.Dict[str, typing.Any]],
                muting_rules_handling: builtins.str,
                name: builtins.str,
                account_id: typing.Optional[jsii.Number] = None,
                destinations_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                enrichments: typing.Optional[typing.Union[WorkflowEnrichments, typing.Dict[str, typing.Any]]] = None,
                enrichments_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                id: typing.Optional[builtins.str] = None,
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
        config = WorkflowConfig(
            destination=destination,
            issues_filter=issues_filter,
            muting_rules_handling=muting_rules_handling,
            name=name,
            account_id=account_id,
            destinations_enabled=destinations_enabled,
            enabled=enabled,
            enrichments=enrichments,
            enrichments_enabled=enrichments_enabled,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDestination")
    def put_destination(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkflowDestination", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[WorkflowDestination, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDestination", [value]))

    @jsii.member(jsii_name="putEnrichments")
    def put_enrichments(
        self,
        *,
        nrql: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkflowEnrichmentsNrql", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param nrql: nrql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#nrql Workflow#nrql}
        '''
        value = WorkflowEnrichments(nrql=nrql)

        return typing.cast(None, jsii.invoke(self, "putEnrichments", [value]))

    @jsii.member(jsii_name="putIssuesFilter")
    def put_issues_filter(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        predicate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkflowIssuesFilterPredicate", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: (Required) Filter's name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#name Workflow#name}
        :param type: (Required) The type of the filter. One of: (FILTER, VIEW). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#type Workflow#type}
        :param predicate: predicate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#predicate Workflow#predicate}
        '''
        value = WorkflowIssuesFilter(name=name, type=type, predicate=predicate)

        return typing.cast(None, jsii.invoke(self, "putIssuesFilter", [value]))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetDestinationsEnabled")
    def reset_destinations_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationsEnabled", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetEnrichments")
    def reset_enrichments(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnrichments", []))

    @jsii.member(jsii_name="resetEnrichmentsEnabled")
    def reset_enrichments_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnrichmentsEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> "WorkflowDestinationList":
        return typing.cast("WorkflowDestinationList", jsii.get(self, "destination"))

    @builtins.property
    @jsii.member(jsii_name="enrichments")
    def enrichments(self) -> "WorkflowEnrichmentsOutputReference":
        return typing.cast("WorkflowEnrichmentsOutputReference", jsii.get(self, "enrichments"))

    @builtins.property
    @jsii.member(jsii_name="issuesFilter")
    def issues_filter(self) -> "WorkflowIssuesFilterOutputReference":
        return typing.cast("WorkflowIssuesFilterOutputReference", jsii.get(self, "issuesFilter"))

    @builtins.property
    @jsii.member(jsii_name="lastRun")
    def last_run(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastRun"))

    @builtins.property
    @jsii.member(jsii_name="workflowId")
    def workflow_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workflowId"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkflowDestination"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkflowDestination"]]], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationsEnabledInput")
    def destinations_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "destinationsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="enrichmentsEnabledInput")
    def enrichments_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enrichmentsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="enrichmentsInput")
    def enrichments_input(self) -> typing.Optional["WorkflowEnrichments"]:
        return typing.cast(typing.Optional["WorkflowEnrichments"], jsii.get(self, "enrichmentsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="issuesFilterInput")
    def issues_filter_input(self) -> typing.Optional["WorkflowIssuesFilter"]:
        return typing.cast(typing.Optional["WorkflowIssuesFilter"], jsii.get(self, "issuesFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="mutingRulesHandlingInput")
    def muting_rules_handling_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mutingRulesHandlingInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

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
    @jsii.member(jsii_name="destinationsEnabled")
    def destinations_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "destinationsEnabled"))

    @destinations_enabled.setter
    def destinations_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationsEnabled", value)

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
    @jsii.member(jsii_name="enrichmentsEnabled")
    def enrichments_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enrichmentsEnabled"))

    @enrichments_enabled.setter
    def enrichments_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enrichmentsEnabled", value)

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
    @jsii.member(jsii_name="mutingRulesHandling")
    def muting_rules_handling(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mutingRulesHandling"))

    @muting_rules_handling.setter
    def muting_rules_handling(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mutingRulesHandling", value)

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


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.workflow.WorkflowConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "destination": "destination",
        "issues_filter": "issuesFilter",
        "muting_rules_handling": "mutingRulesHandling",
        "name": "name",
        "account_id": "accountId",
        "destinations_enabled": "destinationsEnabled",
        "enabled": "enabled",
        "enrichments": "enrichments",
        "enrichments_enabled": "enrichmentsEnabled",
        "id": "id",
    },
)
class WorkflowConfig(cdktf.TerraformMetaArguments):
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
        destination: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkflowDestination", typing.Dict[str, typing.Any]]]],
        issues_filter: typing.Union["WorkflowIssuesFilter", typing.Dict[str, typing.Any]],
        muting_rules_handling: builtins.str,
        name: builtins.str,
        account_id: typing.Optional[jsii.Number] = None,
        destinations_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enrichments: typing.Optional[typing.Union["WorkflowEnrichments", typing.Dict[str, typing.Any]]] = None,
        enrichments_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param destination: destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#destination Workflow#destination}
        :param issues_filter: issues_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#issues_filter Workflow#issues_filter}
        :param muting_rules_handling: The type of the muting rule handling. One of: (NOTIFY_ALL_ISSUES, DONT_NOTIFY_FULLY_MUTED_ISSUES, DONT_NOTIFY_FULLY_OR_PARTIALLY_MUTED_ISSUES). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#muting_rules_handling Workflow#muting_rules_handling}
        :param name: (Required) The name of the workflow. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#name Workflow#name}
        :param account_id: The account id of the workflow. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#account_id Workflow#account_id}
        :param destinations_enabled: Indicates whether the destinations are enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#destinations_enabled Workflow#destinations_enabled}
        :param enabled: Indicates whether the workflow is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#enabled Workflow#enabled}
        :param enrichments: enrichments block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#enrichments Workflow#enrichments}
        :param enrichments_enabled: Indicates whether the enrichments are enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#enrichments_enabled Workflow#enrichments_enabled}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#id Workflow#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(issues_filter, dict):
            issues_filter = WorkflowIssuesFilter(**issues_filter)
        if isinstance(enrichments, dict):
            enrichments = WorkflowEnrichments(**enrichments)
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
                destination: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[WorkflowDestination, typing.Dict[str, typing.Any]]]],
                issues_filter: typing.Union[WorkflowIssuesFilter, typing.Dict[str, typing.Any]],
                muting_rules_handling: builtins.str,
                name: builtins.str,
                account_id: typing.Optional[jsii.Number] = None,
                destinations_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                enrichments: typing.Optional[typing.Union[WorkflowEnrichments, typing.Dict[str, typing.Any]]] = None,
                enrichments_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                id: typing.Optional[builtins.str] = None,
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
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument issues_filter", value=issues_filter, expected_type=type_hints["issues_filter"])
            check_type(argname="argument muting_rules_handling", value=muting_rules_handling, expected_type=type_hints["muting_rules_handling"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument destinations_enabled", value=destinations_enabled, expected_type=type_hints["destinations_enabled"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument enrichments", value=enrichments, expected_type=type_hints["enrichments"])
            check_type(argname="argument enrichments_enabled", value=enrichments_enabled, expected_type=type_hints["enrichments_enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "destination": destination,
            "issues_filter": issues_filter,
            "muting_rules_handling": muting_rules_handling,
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
        if destinations_enabled is not None:
            self._values["destinations_enabled"] = destinations_enabled
        if enabled is not None:
            self._values["enabled"] = enabled
        if enrichments is not None:
            self._values["enrichments"] = enrichments
        if enrichments_enabled is not None:
            self._values["enrichments_enabled"] = enrichments_enabled
        if id is not None:
            self._values["id"] = id

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
    def destination(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["WorkflowDestination"]]:
        '''destination block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#destination Workflow#destination}
        '''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["WorkflowDestination"]], result)

    @builtins.property
    def issues_filter(self) -> "WorkflowIssuesFilter":
        '''issues_filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#issues_filter Workflow#issues_filter}
        '''
        result = self._values.get("issues_filter")
        assert result is not None, "Required property 'issues_filter' is missing"
        return typing.cast("WorkflowIssuesFilter", result)

    @builtins.property
    def muting_rules_handling(self) -> builtins.str:
        '''The type of the muting rule handling. One of: (NOTIFY_ALL_ISSUES, DONT_NOTIFY_FULLY_MUTED_ISSUES, DONT_NOTIFY_FULLY_OR_PARTIALLY_MUTED_ISSUES).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#muting_rules_handling Workflow#muting_rules_handling}
        '''
        result = self._values.get("muting_rules_handling")
        assert result is not None, "Required property 'muting_rules_handling' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''(Required) The name of the workflow.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#name Workflow#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[jsii.Number]:
        '''The account id of the workflow.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#account_id Workflow#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def destinations_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates whether the destinations are enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#destinations_enabled Workflow#destinations_enabled}
        '''
        result = self._values.get("destinations_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates whether the workflow is enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#enabled Workflow#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enrichments(self) -> typing.Optional["WorkflowEnrichments"]:
        '''enrichments block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#enrichments Workflow#enrichments}
        '''
        result = self._values.get("enrichments")
        return typing.cast(typing.Optional["WorkflowEnrichments"], result)

    @builtins.property
    def enrichments_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates whether the enrichments are enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#enrichments_enabled Workflow#enrichments_enabled}
        '''
        result = self._values.get("enrichments_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#id Workflow#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkflowConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.workflow.WorkflowDestination",
    jsii_struct_bases=[],
    name_mapping={"channel_id": "channelId"},
)
class WorkflowDestination:
    def __init__(self, *, channel_id: builtins.str) -> None:
        '''
        :param channel_id: (Required) Destination's channel id. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#channel_id Workflow#channel_id}
        '''
        if __debug__:
            def stub(*, channel_id: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument channel_id", value=channel_id, expected_type=type_hints["channel_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "channel_id": channel_id,
        }

    @builtins.property
    def channel_id(self) -> builtins.str:
        '''(Required) Destination's channel id.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#channel_id Workflow#channel_id}
        '''
        result = self._values.get("channel_id")
        assert result is not None, "Required property 'channel_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkflowDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WorkflowDestinationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.workflow.WorkflowDestinationList",
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
    def get(self, index: jsii.Number) -> "WorkflowDestinationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WorkflowDestinationOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkflowDestination]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkflowDestination]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkflowDestination]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkflowDestination]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WorkflowDestinationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.workflow.WorkflowDestinationOutputReference",
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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="channelIdInput")
    def channel_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "channelIdInput"))

    @builtins.property
    @jsii.member(jsii_name="channelId")
    def channel_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "channelId"))

    @channel_id.setter
    def channel_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WorkflowDestination, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WorkflowDestination, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WorkflowDestination, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[WorkflowDestination, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.workflow.WorkflowEnrichments",
    jsii_struct_bases=[],
    name_mapping={"nrql": "nrql"},
)
class WorkflowEnrichments:
    def __init__(
        self,
        *,
        nrql: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkflowEnrichmentsNrql", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param nrql: nrql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#nrql Workflow#nrql}
        '''
        if __debug__:
            def stub(
                *,
                nrql: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[WorkflowEnrichmentsNrql, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument nrql", value=nrql, expected_type=type_hints["nrql"])
        self._values: typing.Dict[str, typing.Any] = {
            "nrql": nrql,
        }

    @builtins.property
    def nrql(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["WorkflowEnrichmentsNrql"]]:
        '''nrql block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#nrql Workflow#nrql}
        '''
        result = self._values.get("nrql")
        assert result is not None, "Required property 'nrql' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["WorkflowEnrichmentsNrql"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkflowEnrichments(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.workflow.WorkflowEnrichmentsNrql",
    jsii_struct_bases=[],
    name_mapping={"configuration": "configuration", "name": "name"},
)
class WorkflowEnrichmentsNrql:
    def __init__(
        self,
        *,
        configuration: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkflowEnrichmentsNrqlConfiguration", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
    ) -> None:
        '''
        :param configuration: configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#configuration Workflow#configuration}
        :param name: (Required) Enrichment's name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#name Workflow#name}
        '''
        if __debug__:
            def stub(
                *,
                configuration: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[WorkflowEnrichmentsNrqlConfiguration, typing.Dict[str, typing.Any]]]],
                name: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "configuration": configuration,
            "name": name,
        }

    @builtins.property
    def configuration(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["WorkflowEnrichmentsNrqlConfiguration"]]:
        '''configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#configuration Workflow#configuration}
        '''
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["WorkflowEnrichmentsNrqlConfiguration"]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''(Required) Enrichment's name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#name Workflow#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkflowEnrichmentsNrql(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.workflow.WorkflowEnrichmentsNrqlConfiguration",
    jsii_struct_bases=[],
    name_mapping={"query": "query"},
)
class WorkflowEnrichmentsNrqlConfiguration:
    def __init__(self, *, query: builtins.str) -> None:
        '''
        :param query: enrichment's NRQL query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#query Workflow#query}
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
        '''enrichment's NRQL query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#query Workflow#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkflowEnrichmentsNrqlConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WorkflowEnrichmentsNrqlConfigurationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.workflow.WorkflowEnrichmentsNrqlConfigurationList",
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
    ) -> "WorkflowEnrichmentsNrqlConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WorkflowEnrichmentsNrqlConfigurationOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkflowEnrichmentsNrqlConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkflowEnrichmentsNrqlConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkflowEnrichmentsNrqlConfiguration]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkflowEnrichmentsNrqlConfiguration]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WorkflowEnrichmentsNrqlConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.workflow.WorkflowEnrichmentsNrqlConfigurationOutputReference",
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
    ) -> typing.Optional[typing.Union[WorkflowEnrichmentsNrqlConfiguration, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WorkflowEnrichmentsNrqlConfiguration, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WorkflowEnrichmentsNrqlConfiguration, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[WorkflowEnrichmentsNrqlConfiguration, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WorkflowEnrichmentsNrqlList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.workflow.WorkflowEnrichmentsNrqlList",
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
    def get(self, index: jsii.Number) -> "WorkflowEnrichmentsNrqlOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WorkflowEnrichmentsNrqlOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkflowEnrichmentsNrql]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkflowEnrichmentsNrql]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkflowEnrichmentsNrql]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkflowEnrichmentsNrql]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WorkflowEnrichmentsNrqlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.workflow.WorkflowEnrichmentsNrqlOutputReference",
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

    @jsii.member(jsii_name="putConfiguration")
    def put_configuration(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[WorkflowEnrichmentsNrqlConfiguration, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[WorkflowEnrichmentsNrqlConfiguration, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConfiguration", [value]))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "accountId"))

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(self) -> WorkflowEnrichmentsNrqlConfigurationList:
        return typing.cast(WorkflowEnrichmentsNrqlConfigurationList, jsii.get(self, "configuration"))

    @builtins.property
    @jsii.member(jsii_name="enrichmentId")
    def enrichment_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enrichmentId"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="configurationInput")
    def configuration_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkflowEnrichmentsNrqlConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkflowEnrichmentsNrqlConfiguration]]], jsii.get(self, "configurationInput"))

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
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WorkflowEnrichmentsNrql, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WorkflowEnrichmentsNrql, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WorkflowEnrichmentsNrql, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[WorkflowEnrichmentsNrql, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WorkflowEnrichmentsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.workflow.WorkflowEnrichmentsOutputReference",
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

    @jsii.member(jsii_name="putNrql")
    def put_nrql(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[WorkflowEnrichmentsNrql, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[WorkflowEnrichmentsNrql, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNrql", [value]))

    @builtins.property
    @jsii.member(jsii_name="nrql")
    def nrql(self) -> WorkflowEnrichmentsNrqlList:
        return typing.cast(WorkflowEnrichmentsNrqlList, jsii.get(self, "nrql"))

    @builtins.property
    @jsii.member(jsii_name="nrqlInput")
    def nrql_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkflowEnrichmentsNrql]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkflowEnrichmentsNrql]]], jsii.get(self, "nrqlInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WorkflowEnrichments]:
        return typing.cast(typing.Optional[WorkflowEnrichments], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[WorkflowEnrichments]) -> None:
        if __debug__:
            def stub(value: typing.Optional[WorkflowEnrichments]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.workflow.WorkflowIssuesFilter",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type", "predicate": "predicate"},
)
class WorkflowIssuesFilter:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        predicate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkflowIssuesFilterPredicate", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: (Required) Filter's name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#name Workflow#name}
        :param type: (Required) The type of the filter. One of: (FILTER, VIEW). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#type Workflow#type}
        :param predicate: predicate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#predicate Workflow#predicate}
        '''
        if __debug__:
            def stub(
                *,
                name: builtins.str,
                type: builtins.str,
                predicate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[WorkflowIssuesFilterPredicate, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument predicate", value=predicate, expected_type=type_hints["predicate"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "type": type,
        }
        if predicate is not None:
            self._values["predicate"] = predicate

    @builtins.property
    def name(self) -> builtins.str:
        '''(Required) Filter's name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#name Workflow#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''(Required) The type of the filter. One of: (FILTER, VIEW).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#type Workflow#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def predicate(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkflowIssuesFilterPredicate"]]]:
        '''predicate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#predicate Workflow#predicate}
        '''
        result = self._values.get("predicate")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkflowIssuesFilterPredicate"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkflowIssuesFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WorkflowIssuesFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.workflow.WorkflowIssuesFilterOutputReference",
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

    @jsii.member(jsii_name="putPredicate")
    def put_predicate(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkflowIssuesFilterPredicate", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[WorkflowIssuesFilterPredicate, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPredicate", [value]))

    @jsii.member(jsii_name="resetPredicate")
    def reset_predicate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPredicate", []))

    @builtins.property
    @jsii.member(jsii_name="filterId")
    def filter_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filterId"))

    @builtins.property
    @jsii.member(jsii_name="predicate")
    def predicate(self) -> "WorkflowIssuesFilterPredicateList":
        return typing.cast("WorkflowIssuesFilterPredicateList", jsii.get(self, "predicate"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="predicateInput")
    def predicate_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkflowIssuesFilterPredicate"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkflowIssuesFilterPredicate"]]], jsii.get(self, "predicateInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

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
    def internal_value(self) -> typing.Optional[WorkflowIssuesFilter]:
        return typing.cast(typing.Optional[WorkflowIssuesFilter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[WorkflowIssuesFilter]) -> None:
        if __debug__:
            def stub(value: typing.Optional[WorkflowIssuesFilter]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.workflow.WorkflowIssuesFilterPredicate",
    jsii_struct_bases=[],
    name_mapping={
        "attribute": "attribute",
        "operator": "operator",
        "values": "values",
    },
)
class WorkflowIssuesFilterPredicate:
    def __init__(
        self,
        *,
        attribute: builtins.str,
        operator: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param attribute: (Required) predicate's attribute. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#attribute Workflow#attribute}
        :param operator: The type of the operator. One of: (CONTAINS, DOES_NOT_CONTAIN, DOES_NOT_EQUAL, DOES_NOT_EXACTLY_MATCH, ENDS_WITH, EQUAL, EXACTLY_MATCHES, GREATER_OR_EQUAL, GREATER_THAN, IS, IS_NOT, LESS_OR_EQUAL, LESS_THAN, STARTS_WITH). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#operator Workflow#operator}
        :param values: List of predicate values. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#values Workflow#values}
        '''
        if __debug__:
            def stub(
                *,
                attribute: builtins.str,
                operator: builtins.str,
                values: typing.Sequence[builtins.str],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument attribute", value=attribute, expected_type=type_hints["attribute"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "attribute": attribute,
            "operator": operator,
            "values": values,
        }

    @builtins.property
    def attribute(self) -> builtins.str:
        '''(Required) predicate's attribute.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#attribute Workflow#attribute}
        '''
        result = self._values.get("attribute")
        assert result is not None, "Required property 'attribute' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''The type of the operator.

        One of: (CONTAINS, DOES_NOT_CONTAIN, DOES_NOT_EQUAL, DOES_NOT_EXACTLY_MATCH, ENDS_WITH, EQUAL, EXACTLY_MATCHES, GREATER_OR_EQUAL, GREATER_THAN, IS, IS_NOT, LESS_OR_EQUAL, LESS_THAN, STARTS_WITH).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#operator Workflow#operator}
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''List of predicate values.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/workflow#values Workflow#values}
        '''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkflowIssuesFilterPredicate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WorkflowIssuesFilterPredicateList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.workflow.WorkflowIssuesFilterPredicateList",
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
    def get(self, index: jsii.Number) -> "WorkflowIssuesFilterPredicateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WorkflowIssuesFilterPredicateOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkflowIssuesFilterPredicate]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkflowIssuesFilterPredicate]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkflowIssuesFilterPredicate]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkflowIssuesFilterPredicate]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WorkflowIssuesFilterPredicateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.workflow.WorkflowIssuesFilterPredicateOutputReference",
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
    @jsii.member(jsii_name="attributeInput")
    def attribute_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attributeInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="attribute")
    def attribute(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attribute"))

    @attribute.setter
    def attribute(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attribute", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WorkflowIssuesFilterPredicate, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WorkflowIssuesFilterPredicate, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WorkflowIssuesFilterPredicate, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[WorkflowIssuesFilterPredicate, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Workflow",
    "WorkflowConfig",
    "WorkflowDestination",
    "WorkflowDestinationList",
    "WorkflowDestinationOutputReference",
    "WorkflowEnrichments",
    "WorkflowEnrichmentsNrql",
    "WorkflowEnrichmentsNrqlConfiguration",
    "WorkflowEnrichmentsNrqlConfigurationList",
    "WorkflowEnrichmentsNrqlConfigurationOutputReference",
    "WorkflowEnrichmentsNrqlList",
    "WorkflowEnrichmentsNrqlOutputReference",
    "WorkflowEnrichmentsOutputReference",
    "WorkflowIssuesFilter",
    "WorkflowIssuesFilterOutputReference",
    "WorkflowIssuesFilterPredicate",
    "WorkflowIssuesFilterPredicateList",
    "WorkflowIssuesFilterPredicateOutputReference",
]

publication.publish()
