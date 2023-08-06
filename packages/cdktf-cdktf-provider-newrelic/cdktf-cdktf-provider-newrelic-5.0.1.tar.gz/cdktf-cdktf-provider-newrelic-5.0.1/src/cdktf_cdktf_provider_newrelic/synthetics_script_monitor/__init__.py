'''
# `newrelic_synthetics_script_monitor`

Refer to the Terraform Registory for docs: [`newrelic_synthetics_script_monitor`](https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor).
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


class SyntheticsScriptMonitor(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.syntheticsScriptMonitor.SyntheticsScriptMonitor",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor newrelic_synthetics_script_monitor}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        period: builtins.str,
        status: builtins.str,
        type: builtins.str,
        account_id: typing.Optional[jsii.Number] = None,
        enable_screenshot_on_failure_and_script: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        location_private: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SyntheticsScriptMonitorLocationPrivate", typing.Dict[str, typing.Any]]]]] = None,
        locations_public: typing.Optional[typing.Sequence[builtins.str]] = None,
        runtime_type: typing.Optional[builtins.str] = None,
        runtime_type_version: typing.Optional[builtins.str] = None,
        script: typing.Optional[builtins.str] = None,
        script_language: typing.Optional[builtins.str] = None,
        tag: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SyntheticsScriptMonitorTag", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor newrelic_synthetics_script_monitor} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The title of this monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#name SyntheticsScriptMonitor#name}
        :param period: The interval at which this monitor should run. Valid values are EVERY_MINUTE, EVERY_5_MINUTES, EVERY_10_MINUTES, EVERY_15_MINUTES, EVERY_30_MINUTES, EVERY_HOUR, EVERY_6_HOURS, EVERY_12_HOURS, or EVERY_DAY. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#period SyntheticsScriptMonitor#period}
        :param status: The monitor status (i.e. ENABLED, MUTED, DISABLED). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#status SyntheticsScriptMonitor#status}
        :param type: The monitor type. Valid values are SCRIPT_BROWSER, and SCRIPT_API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#type SyntheticsScriptMonitor#type}
        :param account_id: ID of the newrelic account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#account_id SyntheticsScriptMonitor#account_id}
        :param enable_screenshot_on_failure_and_script: Capture a screenshot during job execution. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#enable_screenshot_on_failure_and_script SyntheticsScriptMonitor#enable_screenshot_on_failure_and_script}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#id SyntheticsScriptMonitor#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param location_private: location_private block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#location_private SyntheticsScriptMonitor#location_private}
        :param locations_public: The public location(s) that the monitor will run jobs from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#locations_public SyntheticsScriptMonitor#locations_public}
        :param runtime_type: The runtime type that the monitor will run. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#runtime_type SyntheticsScriptMonitor#runtime_type}
        :param runtime_type_version: The specific semver version of the runtime type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#runtime_type_version SyntheticsScriptMonitor#runtime_type_version}
        :param script: The script that the monitor runs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#script SyntheticsScriptMonitor#script}
        :param script_language: The programing language that should execute the script. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#script_language SyntheticsScriptMonitor#script_language}
        :param tag: tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#tag SyntheticsScriptMonitor#tag}
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
                period: builtins.str,
                status: builtins.str,
                type: builtins.str,
                account_id: typing.Optional[jsii.Number] = None,
                enable_screenshot_on_failure_and_script: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                id: typing.Optional[builtins.str] = None,
                location_private: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SyntheticsScriptMonitorLocationPrivate, typing.Dict[str, typing.Any]]]]] = None,
                locations_public: typing.Optional[typing.Sequence[builtins.str]] = None,
                runtime_type: typing.Optional[builtins.str] = None,
                runtime_type_version: typing.Optional[builtins.str] = None,
                script: typing.Optional[builtins.str] = None,
                script_language: typing.Optional[builtins.str] = None,
                tag: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SyntheticsScriptMonitorTag, typing.Dict[str, typing.Any]]]]] = None,
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
        config = SyntheticsScriptMonitorConfig(
            name=name,
            period=period,
            status=status,
            type=type,
            account_id=account_id,
            enable_screenshot_on_failure_and_script=enable_screenshot_on_failure_and_script,
            id=id,
            location_private=location_private,
            locations_public=locations_public,
            runtime_type=runtime_type,
            runtime_type_version=runtime_type_version,
            script=script,
            script_language=script_language,
            tag=tag,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putLocationPrivate")
    def put_location_private(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SyntheticsScriptMonitorLocationPrivate", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SyntheticsScriptMonitorLocationPrivate, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLocationPrivate", [value]))

    @jsii.member(jsii_name="putTag")
    def put_tag(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SyntheticsScriptMonitorTag", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SyntheticsScriptMonitorTag, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTag", [value]))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetEnableScreenshotOnFailureAndScript")
    def reset_enable_screenshot_on_failure_and_script(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableScreenshotOnFailureAndScript", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLocationPrivate")
    def reset_location_private(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocationPrivate", []))

    @jsii.member(jsii_name="resetLocationsPublic")
    def reset_locations_public(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocationsPublic", []))

    @jsii.member(jsii_name="resetRuntimeType")
    def reset_runtime_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuntimeType", []))

    @jsii.member(jsii_name="resetRuntimeTypeVersion")
    def reset_runtime_type_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuntimeTypeVersion", []))

    @jsii.member(jsii_name="resetScript")
    def reset_script(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScript", []))

    @jsii.member(jsii_name="resetScriptLanguage")
    def reset_script_language(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScriptLanguage", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="guid")
    def guid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "guid"))

    @builtins.property
    @jsii.member(jsii_name="locationPrivate")
    def location_private(self) -> "SyntheticsScriptMonitorLocationPrivateList":
        return typing.cast("SyntheticsScriptMonitorLocationPrivateList", jsii.get(self, "locationPrivate"))

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> "SyntheticsScriptMonitorTagList":
        return typing.cast("SyntheticsScriptMonitorTagList", jsii.get(self, "tag"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="enableScreenshotOnFailureAndScriptInput")
    def enable_screenshot_on_failure_and_script_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableScreenshotOnFailureAndScriptInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationPrivateInput")
    def location_private_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsScriptMonitorLocationPrivate"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsScriptMonitorLocationPrivate"]]], jsii.get(self, "locationPrivateInput"))

    @builtins.property
    @jsii.member(jsii_name="locationsPublicInput")
    def locations_public_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "locationsPublicInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="periodInput")
    def period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "periodInput"))

    @builtins.property
    @jsii.member(jsii_name="runtimeTypeInput")
    def runtime_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runtimeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="runtimeTypeVersionInput")
    def runtime_type_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runtimeTypeVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="scriptInput")
    def script_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scriptInput"))

    @builtins.property
    @jsii.member(jsii_name="scriptLanguageInput")
    def script_language_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scriptLanguageInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsScriptMonitorTag"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsScriptMonitorTag"]]], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

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
    @jsii.member(jsii_name="enableScreenshotOnFailureAndScript")
    def enable_screenshot_on_failure_and_script(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableScreenshotOnFailureAndScript"))

    @enable_screenshot_on_failure_and_script.setter
    def enable_screenshot_on_failure_and_script(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableScreenshotOnFailureAndScript", value)

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
    @jsii.member(jsii_name="locationsPublic")
    def locations_public(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "locationsPublic"))

    @locations_public.setter
    def locations_public(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locationsPublic", value)

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
    @jsii.member(jsii_name="period")
    def period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "period"))

    @period.setter
    def period(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "period", value)

    @builtins.property
    @jsii.member(jsii_name="runtimeType")
    def runtime_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runtimeType"))

    @runtime_type.setter
    def runtime_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtimeType", value)

    @builtins.property
    @jsii.member(jsii_name="runtimeTypeVersion")
    def runtime_type_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runtimeTypeVersion"))

    @runtime_type_version.setter
    def runtime_type_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtimeTypeVersion", value)

    @builtins.property
    @jsii.member(jsii_name="script")
    def script(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "script"))

    @script.setter
    def script(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "script", value)

    @builtins.property
    @jsii.member(jsii_name="scriptLanguage")
    def script_language(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scriptLanguage"))

    @script_language.setter
    def script_language(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scriptLanguage", value)

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


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.syntheticsScriptMonitor.SyntheticsScriptMonitorConfig",
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
        "period": "period",
        "status": "status",
        "type": "type",
        "account_id": "accountId",
        "enable_screenshot_on_failure_and_script": "enableScreenshotOnFailureAndScript",
        "id": "id",
        "location_private": "locationPrivate",
        "locations_public": "locationsPublic",
        "runtime_type": "runtimeType",
        "runtime_type_version": "runtimeTypeVersion",
        "script": "script",
        "script_language": "scriptLanguage",
        "tag": "tag",
    },
)
class SyntheticsScriptMonitorConfig(cdktf.TerraformMetaArguments):
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
        period: builtins.str,
        status: builtins.str,
        type: builtins.str,
        account_id: typing.Optional[jsii.Number] = None,
        enable_screenshot_on_failure_and_script: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        location_private: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SyntheticsScriptMonitorLocationPrivate", typing.Dict[str, typing.Any]]]]] = None,
        locations_public: typing.Optional[typing.Sequence[builtins.str]] = None,
        runtime_type: typing.Optional[builtins.str] = None,
        runtime_type_version: typing.Optional[builtins.str] = None,
        script: typing.Optional[builtins.str] = None,
        script_language: typing.Optional[builtins.str] = None,
        tag: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SyntheticsScriptMonitorTag", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The title of this monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#name SyntheticsScriptMonitor#name}
        :param period: The interval at which this monitor should run. Valid values are EVERY_MINUTE, EVERY_5_MINUTES, EVERY_10_MINUTES, EVERY_15_MINUTES, EVERY_30_MINUTES, EVERY_HOUR, EVERY_6_HOURS, EVERY_12_HOURS, or EVERY_DAY. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#period SyntheticsScriptMonitor#period}
        :param status: The monitor status (i.e. ENABLED, MUTED, DISABLED). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#status SyntheticsScriptMonitor#status}
        :param type: The monitor type. Valid values are SCRIPT_BROWSER, and SCRIPT_API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#type SyntheticsScriptMonitor#type}
        :param account_id: ID of the newrelic account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#account_id SyntheticsScriptMonitor#account_id}
        :param enable_screenshot_on_failure_and_script: Capture a screenshot during job execution. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#enable_screenshot_on_failure_and_script SyntheticsScriptMonitor#enable_screenshot_on_failure_and_script}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#id SyntheticsScriptMonitor#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param location_private: location_private block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#location_private SyntheticsScriptMonitor#location_private}
        :param locations_public: The public location(s) that the monitor will run jobs from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#locations_public SyntheticsScriptMonitor#locations_public}
        :param runtime_type: The runtime type that the monitor will run. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#runtime_type SyntheticsScriptMonitor#runtime_type}
        :param runtime_type_version: The specific semver version of the runtime type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#runtime_type_version SyntheticsScriptMonitor#runtime_type_version}
        :param script: The script that the monitor runs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#script SyntheticsScriptMonitor#script}
        :param script_language: The programing language that should execute the script. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#script_language SyntheticsScriptMonitor#script_language}
        :param tag: tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#tag SyntheticsScriptMonitor#tag}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
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
                period: builtins.str,
                status: builtins.str,
                type: builtins.str,
                account_id: typing.Optional[jsii.Number] = None,
                enable_screenshot_on_failure_and_script: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                id: typing.Optional[builtins.str] = None,
                location_private: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SyntheticsScriptMonitorLocationPrivate, typing.Dict[str, typing.Any]]]]] = None,
                locations_public: typing.Optional[typing.Sequence[builtins.str]] = None,
                runtime_type: typing.Optional[builtins.str] = None,
                runtime_type_version: typing.Optional[builtins.str] = None,
                script: typing.Optional[builtins.str] = None,
                script_language: typing.Optional[builtins.str] = None,
                tag: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SyntheticsScriptMonitorTag, typing.Dict[str, typing.Any]]]]] = None,
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
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument enable_screenshot_on_failure_and_script", value=enable_screenshot_on_failure_and_script, expected_type=type_hints["enable_screenshot_on_failure_and_script"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument location_private", value=location_private, expected_type=type_hints["location_private"])
            check_type(argname="argument locations_public", value=locations_public, expected_type=type_hints["locations_public"])
            check_type(argname="argument runtime_type", value=runtime_type, expected_type=type_hints["runtime_type"])
            check_type(argname="argument runtime_type_version", value=runtime_type_version, expected_type=type_hints["runtime_type_version"])
            check_type(argname="argument script", value=script, expected_type=type_hints["script"])
            check_type(argname="argument script_language", value=script_language, expected_type=type_hints["script_language"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "period": period,
            "status": status,
            "type": type,
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
        if enable_screenshot_on_failure_and_script is not None:
            self._values["enable_screenshot_on_failure_and_script"] = enable_screenshot_on_failure_and_script
        if id is not None:
            self._values["id"] = id
        if location_private is not None:
            self._values["location_private"] = location_private
        if locations_public is not None:
            self._values["locations_public"] = locations_public
        if runtime_type is not None:
            self._values["runtime_type"] = runtime_type
        if runtime_type_version is not None:
            self._values["runtime_type_version"] = runtime_type_version
        if script is not None:
            self._values["script"] = script
        if script_language is not None:
            self._values["script_language"] = script_language
        if tag is not None:
            self._values["tag"] = tag

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
        '''The title of this monitor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#name SyntheticsScriptMonitor#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def period(self) -> builtins.str:
        '''The interval at which this monitor should run.

        Valid values are EVERY_MINUTE, EVERY_5_MINUTES, EVERY_10_MINUTES, EVERY_15_MINUTES, EVERY_30_MINUTES, EVERY_HOUR, EVERY_6_HOURS, EVERY_12_HOURS, or EVERY_DAY.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#period SyntheticsScriptMonitor#period}
        '''
        result = self._values.get("period")
        assert result is not None, "Required property 'period' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def status(self) -> builtins.str:
        '''The monitor status (i.e. ENABLED, MUTED, DISABLED).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#status SyntheticsScriptMonitor#status}
        '''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The monitor type. Valid values are SCRIPT_BROWSER, and SCRIPT_API.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#type SyntheticsScriptMonitor#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[jsii.Number]:
        '''ID of the newrelic account.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#account_id SyntheticsScriptMonitor#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enable_screenshot_on_failure_and_script(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Capture a screenshot during job execution.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#enable_screenshot_on_failure_and_script SyntheticsScriptMonitor#enable_screenshot_on_failure_and_script}
        '''
        result = self._values.get("enable_screenshot_on_failure_and_script")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#id SyntheticsScriptMonitor#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location_private(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsScriptMonitorLocationPrivate"]]]:
        '''location_private block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#location_private SyntheticsScriptMonitor#location_private}
        '''
        result = self._values.get("location_private")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsScriptMonitorLocationPrivate"]]], result)

    @builtins.property
    def locations_public(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The public location(s) that the monitor will run jobs from.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#locations_public SyntheticsScriptMonitor#locations_public}
        '''
        result = self._values.get("locations_public")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def runtime_type(self) -> typing.Optional[builtins.str]:
        '''The runtime type that the monitor will run.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#runtime_type SyntheticsScriptMonitor#runtime_type}
        '''
        result = self._values.get("runtime_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def runtime_type_version(self) -> typing.Optional[builtins.str]:
        '''The specific semver version of the runtime type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#runtime_type_version SyntheticsScriptMonitor#runtime_type_version}
        '''
        result = self._values.get("runtime_type_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def script(self) -> typing.Optional[builtins.str]:
        '''The script that the monitor runs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#script SyntheticsScriptMonitor#script}
        '''
        result = self._values.get("script")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def script_language(self) -> typing.Optional[builtins.str]:
        '''The programing language that should execute the script.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#script_language SyntheticsScriptMonitor#script_language}
        '''
        result = self._values.get("script_language")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsScriptMonitorTag"]]]:
        '''tag block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#tag SyntheticsScriptMonitor#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsScriptMonitorTag"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsScriptMonitorConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.syntheticsScriptMonitor.SyntheticsScriptMonitorLocationPrivate",
    jsii_struct_bases=[],
    name_mapping={"guid": "guid", "vse_password": "vsePassword"},
)
class SyntheticsScriptMonitorLocationPrivate:
    def __init__(
        self,
        *,
        guid: builtins.str,
        vse_password: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param guid: The unique identifier for the Synthetics private location in New Relic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#guid SyntheticsScriptMonitor#guid}
        :param vse_password: The location's Verified Script Execution password (Only necessary if Verified Script Execution is enabled for the location). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#vse_password SyntheticsScriptMonitor#vse_password}
        '''
        if __debug__:
            def stub(
                *,
                guid: builtins.str,
                vse_password: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument guid", value=guid, expected_type=type_hints["guid"])
            check_type(argname="argument vse_password", value=vse_password, expected_type=type_hints["vse_password"])
        self._values: typing.Dict[str, typing.Any] = {
            "guid": guid,
        }
        if vse_password is not None:
            self._values["vse_password"] = vse_password

    @builtins.property
    def guid(self) -> builtins.str:
        '''The unique identifier for the Synthetics private location in New Relic.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#guid SyntheticsScriptMonitor#guid}
        '''
        result = self._values.get("guid")
        assert result is not None, "Required property 'guid' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vse_password(self) -> typing.Optional[builtins.str]:
        '''The location's Verified Script Execution password (Only necessary if Verified Script Execution is enabled for the location).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#vse_password SyntheticsScriptMonitor#vse_password}
        '''
        result = self._values.get("vse_password")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsScriptMonitorLocationPrivate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsScriptMonitorLocationPrivateList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.syntheticsScriptMonitor.SyntheticsScriptMonitorLocationPrivateList",
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
    ) -> "SyntheticsScriptMonitorLocationPrivateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SyntheticsScriptMonitorLocationPrivateOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsScriptMonitorLocationPrivate]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsScriptMonitorLocationPrivate]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsScriptMonitorLocationPrivate]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsScriptMonitorLocationPrivate]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SyntheticsScriptMonitorLocationPrivateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.syntheticsScriptMonitor.SyntheticsScriptMonitorLocationPrivateOutputReference",
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

    @jsii.member(jsii_name="resetVsePassword")
    def reset_vse_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVsePassword", []))

    @builtins.property
    @jsii.member(jsii_name="guidInput")
    def guid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "guidInput"))

    @builtins.property
    @jsii.member(jsii_name="vsePasswordInput")
    def vse_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vsePasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="guid")
    def guid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "guid"))

    @guid.setter
    def guid(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "guid", value)

    @builtins.property
    @jsii.member(jsii_name="vsePassword")
    def vse_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vsePassword"))

    @vse_password.setter
    def vse_password(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vsePassword", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SyntheticsScriptMonitorLocationPrivate, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SyntheticsScriptMonitorLocationPrivate, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SyntheticsScriptMonitorLocationPrivate, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[SyntheticsScriptMonitorLocationPrivate, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.syntheticsScriptMonitor.SyntheticsScriptMonitorTag",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class SyntheticsScriptMonitorTag:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Name of the tag key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#key SyntheticsScriptMonitor#key}
        :param values: Values associated with the tag key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#values SyntheticsScriptMonitor#values}
        '''
        if __debug__:
            def stub(
                *,
                key: builtins.str,
                values: typing.Sequence[builtins.str],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Name of the tag key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#key SyntheticsScriptMonitor#key}
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Values associated with the tag key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_script_monitor#values SyntheticsScriptMonitor#values}
        '''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsScriptMonitorTag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsScriptMonitorTagList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.syntheticsScriptMonitor.SyntheticsScriptMonitorTagList",
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
    def get(self, index: jsii.Number) -> "SyntheticsScriptMonitorTagOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SyntheticsScriptMonitorTagOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsScriptMonitorTag]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsScriptMonitorTag]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsScriptMonitorTag]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsScriptMonitorTag]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SyntheticsScriptMonitorTagOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.syntheticsScriptMonitor.SyntheticsScriptMonitorTagOutputReference",
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
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

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
    ) -> typing.Optional[typing.Union[SyntheticsScriptMonitorTag, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SyntheticsScriptMonitorTag, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SyntheticsScriptMonitorTag, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[SyntheticsScriptMonitorTag, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SyntheticsScriptMonitor",
    "SyntheticsScriptMonitorConfig",
    "SyntheticsScriptMonitorLocationPrivate",
    "SyntheticsScriptMonitorLocationPrivateList",
    "SyntheticsScriptMonitorLocationPrivateOutputReference",
    "SyntheticsScriptMonitorTag",
    "SyntheticsScriptMonitorTagList",
    "SyntheticsScriptMonitorTagOutputReference",
]

publication.publish()
