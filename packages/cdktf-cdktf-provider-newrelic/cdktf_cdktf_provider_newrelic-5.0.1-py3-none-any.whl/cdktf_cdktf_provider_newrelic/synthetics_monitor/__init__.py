'''
# `newrelic_synthetics_monitor`

Refer to the Terraform Registory for docs: [`newrelic_synthetics_monitor`](https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor).
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


class SyntheticsMonitor(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.syntheticsMonitor.SyntheticsMonitor",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor newrelic_synthetics_monitor}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        status: builtins.str,
        type: builtins.str,
        account_id: typing.Optional[jsii.Number] = None,
        bypass_head_request: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        custom_header: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SyntheticsMonitorCustomHeader", typing.Dict[str, typing.Any]]]]] = None,
        enable_screenshot_on_failure_and_script: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        locations_private: typing.Optional[typing.Sequence[builtins.str]] = None,
        locations_public: typing.Optional[typing.Sequence[builtins.str]] = None,
        period: typing.Optional[builtins.str] = None,
        runtime_type: typing.Optional[builtins.str] = None,
        runtime_type_version: typing.Optional[builtins.str] = None,
        script_language: typing.Optional[builtins.str] = None,
        tag: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SyntheticsMonitorTag", typing.Dict[str, typing.Any]]]]] = None,
        treat_redirect_as_failure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        uri: typing.Optional[builtins.str] = None,
        validation_string: typing.Optional[builtins.str] = None,
        verify_ssl: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor newrelic_synthetics_monitor} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The title of this monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#name SyntheticsMonitor#name}
        :param status: The monitor status (i.e. ENABLED, MUTED, DISABLED). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#status SyntheticsMonitor#status}
        :param type: The monitor type. Valid values are SIMPLE AND BROWSER. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#type SyntheticsMonitor#type}
        :param account_id: ID of the newrelic account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#account_id SyntheticsMonitor#account_id}
        :param bypass_head_request: Bypass HEAD request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#bypass_head_request SyntheticsMonitor#bypass_head_request}
        :param custom_header: custom_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#custom_header SyntheticsMonitor#custom_header}
        :param enable_screenshot_on_failure_and_script: Capture a screenshot during job execution. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#enable_screenshot_on_failure_and_script SyntheticsMonitor#enable_screenshot_on_failure_and_script}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#id SyntheticsMonitor#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param locations_private: The locations in which this monitor should be run. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#locations_private SyntheticsMonitor#locations_private}
        :param locations_public: The locations in which this monitor should be run. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#locations_public SyntheticsMonitor#locations_public}
        :param period: The interval at which this monitor should run. Valid values are EVERY_MINUTE, EVERY_5_MINUTES, EVERY_10_MINUTES, EVERY_15_MINUTES, EVERY_30_MINUTES, EVERY_HOUR, EVERY_6_HOURS, EVERY_12_HOURS, or EVERY_DAY. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#period SyntheticsMonitor#period}
        :param runtime_type: The runtime type that the monitor will run. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#runtime_type SyntheticsMonitor#runtime_type}
        :param runtime_type_version: The specific version of the runtime type selected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#runtime_type_version SyntheticsMonitor#runtime_type_version}
        :param script_language: The programing language that should execute the script. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#script_language SyntheticsMonitor#script_language}
        :param tag: tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#tag SyntheticsMonitor#tag}
        :param treat_redirect_as_failure: Fail the monitor check if redirected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#treat_redirect_as_failure SyntheticsMonitor#treat_redirect_as_failure}
        :param uri: The URI for the monitor to hit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#uri SyntheticsMonitor#uri}
        :param validation_string: The string to validate against in the response. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#validation_string SyntheticsMonitor#validation_string}
        :param verify_ssl: Verify SSL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#verify_ssl SyntheticsMonitor#verify_ssl}
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
                status: builtins.str,
                type: builtins.str,
                account_id: typing.Optional[jsii.Number] = None,
                bypass_head_request: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                custom_header: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SyntheticsMonitorCustomHeader, typing.Dict[str, typing.Any]]]]] = None,
                enable_screenshot_on_failure_and_script: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                id: typing.Optional[builtins.str] = None,
                locations_private: typing.Optional[typing.Sequence[builtins.str]] = None,
                locations_public: typing.Optional[typing.Sequence[builtins.str]] = None,
                period: typing.Optional[builtins.str] = None,
                runtime_type: typing.Optional[builtins.str] = None,
                runtime_type_version: typing.Optional[builtins.str] = None,
                script_language: typing.Optional[builtins.str] = None,
                tag: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SyntheticsMonitorTag, typing.Dict[str, typing.Any]]]]] = None,
                treat_redirect_as_failure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                uri: typing.Optional[builtins.str] = None,
                validation_string: typing.Optional[builtins.str] = None,
                verify_ssl: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
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
        config = SyntheticsMonitorConfig(
            name=name,
            status=status,
            type=type,
            account_id=account_id,
            bypass_head_request=bypass_head_request,
            custom_header=custom_header,
            enable_screenshot_on_failure_and_script=enable_screenshot_on_failure_and_script,
            id=id,
            locations_private=locations_private,
            locations_public=locations_public,
            period=period,
            runtime_type=runtime_type,
            runtime_type_version=runtime_type_version,
            script_language=script_language,
            tag=tag,
            treat_redirect_as_failure=treat_redirect_as_failure,
            uri=uri,
            validation_string=validation_string,
            verify_ssl=verify_ssl,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCustomHeader")
    def put_custom_header(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SyntheticsMonitorCustomHeader", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SyntheticsMonitorCustomHeader, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomHeader", [value]))

    @jsii.member(jsii_name="putTag")
    def put_tag(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SyntheticsMonitorTag", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SyntheticsMonitorTag, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTag", [value]))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetBypassHeadRequest")
    def reset_bypass_head_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBypassHeadRequest", []))

    @jsii.member(jsii_name="resetCustomHeader")
    def reset_custom_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomHeader", []))

    @jsii.member(jsii_name="resetEnableScreenshotOnFailureAndScript")
    def reset_enable_screenshot_on_failure_and_script(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableScreenshotOnFailureAndScript", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLocationsPrivate")
    def reset_locations_private(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocationsPrivate", []))

    @jsii.member(jsii_name="resetLocationsPublic")
    def reset_locations_public(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocationsPublic", []))

    @jsii.member(jsii_name="resetPeriod")
    def reset_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeriod", []))

    @jsii.member(jsii_name="resetRuntimeType")
    def reset_runtime_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuntimeType", []))

    @jsii.member(jsii_name="resetRuntimeTypeVersion")
    def reset_runtime_type_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuntimeTypeVersion", []))

    @jsii.member(jsii_name="resetScriptLanguage")
    def reset_script_language(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScriptLanguage", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @jsii.member(jsii_name="resetTreatRedirectAsFailure")
    def reset_treat_redirect_as_failure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTreatRedirectAsFailure", []))

    @jsii.member(jsii_name="resetUri")
    def reset_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUri", []))

    @jsii.member(jsii_name="resetValidationString")
    def reset_validation_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidationString", []))

    @jsii.member(jsii_name="resetVerifySsl")
    def reset_verify_ssl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerifySsl", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="customHeader")
    def custom_header(self) -> "SyntheticsMonitorCustomHeaderList":
        return typing.cast("SyntheticsMonitorCustomHeaderList", jsii.get(self, "customHeader"))

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> "SyntheticsMonitorTagList":
        return typing.cast("SyntheticsMonitorTagList", jsii.get(self, "tag"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="bypassHeadRequestInput")
    def bypass_head_request_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "bypassHeadRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="customHeaderInput")
    def custom_header_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsMonitorCustomHeader"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsMonitorCustomHeader"]]], jsii.get(self, "customHeaderInput"))

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
    @jsii.member(jsii_name="locationsPrivateInput")
    def locations_private_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "locationsPrivateInput"))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsMonitorTag"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsMonitorTag"]]], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="treatRedirectAsFailureInput")
    def treat_redirect_as_failure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "treatRedirectAsFailureInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="validationStringInput")
    def validation_string_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "validationStringInput"))

    @builtins.property
    @jsii.member(jsii_name="verifySslInput")
    def verify_ssl_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "verifySslInput"))

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
    @jsii.member(jsii_name="bypassHeadRequest")
    def bypass_head_request(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "bypassHeadRequest"))

    @bypass_head_request.setter
    def bypass_head_request(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bypassHeadRequest", value)

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
    @jsii.member(jsii_name="locationsPrivate")
    def locations_private(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "locationsPrivate"))

    @locations_private.setter
    def locations_private(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locationsPrivate", value)

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
    @jsii.member(jsii_name="treatRedirectAsFailure")
    def treat_redirect_as_failure(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "treatRedirectAsFailure"))

    @treat_redirect_as_failure.setter
    def treat_redirect_as_failure(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "treatRedirectAsFailure", value)

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
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)

    @builtins.property
    @jsii.member(jsii_name="validationString")
    def validation_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "validationString"))

    @validation_string.setter
    def validation_string(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validationString", value)

    @builtins.property
    @jsii.member(jsii_name="verifySsl")
    def verify_ssl(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "verifySsl"))

    @verify_ssl.setter
    def verify_ssl(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verifySsl", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.syntheticsMonitor.SyntheticsMonitorConfig",
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
        "status": "status",
        "type": "type",
        "account_id": "accountId",
        "bypass_head_request": "bypassHeadRequest",
        "custom_header": "customHeader",
        "enable_screenshot_on_failure_and_script": "enableScreenshotOnFailureAndScript",
        "id": "id",
        "locations_private": "locationsPrivate",
        "locations_public": "locationsPublic",
        "period": "period",
        "runtime_type": "runtimeType",
        "runtime_type_version": "runtimeTypeVersion",
        "script_language": "scriptLanguage",
        "tag": "tag",
        "treat_redirect_as_failure": "treatRedirectAsFailure",
        "uri": "uri",
        "validation_string": "validationString",
        "verify_ssl": "verifySsl",
    },
)
class SyntheticsMonitorConfig(cdktf.TerraformMetaArguments):
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
        status: builtins.str,
        type: builtins.str,
        account_id: typing.Optional[jsii.Number] = None,
        bypass_head_request: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        custom_header: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SyntheticsMonitorCustomHeader", typing.Dict[str, typing.Any]]]]] = None,
        enable_screenshot_on_failure_and_script: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        locations_private: typing.Optional[typing.Sequence[builtins.str]] = None,
        locations_public: typing.Optional[typing.Sequence[builtins.str]] = None,
        period: typing.Optional[builtins.str] = None,
        runtime_type: typing.Optional[builtins.str] = None,
        runtime_type_version: typing.Optional[builtins.str] = None,
        script_language: typing.Optional[builtins.str] = None,
        tag: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SyntheticsMonitorTag", typing.Dict[str, typing.Any]]]]] = None,
        treat_redirect_as_failure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        uri: typing.Optional[builtins.str] = None,
        validation_string: typing.Optional[builtins.str] = None,
        verify_ssl: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The title of this monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#name SyntheticsMonitor#name}
        :param status: The monitor status (i.e. ENABLED, MUTED, DISABLED). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#status SyntheticsMonitor#status}
        :param type: The monitor type. Valid values are SIMPLE AND BROWSER. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#type SyntheticsMonitor#type}
        :param account_id: ID of the newrelic account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#account_id SyntheticsMonitor#account_id}
        :param bypass_head_request: Bypass HEAD request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#bypass_head_request SyntheticsMonitor#bypass_head_request}
        :param custom_header: custom_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#custom_header SyntheticsMonitor#custom_header}
        :param enable_screenshot_on_failure_and_script: Capture a screenshot during job execution. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#enable_screenshot_on_failure_and_script SyntheticsMonitor#enable_screenshot_on_failure_and_script}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#id SyntheticsMonitor#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param locations_private: The locations in which this monitor should be run. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#locations_private SyntheticsMonitor#locations_private}
        :param locations_public: The locations in which this monitor should be run. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#locations_public SyntheticsMonitor#locations_public}
        :param period: The interval at which this monitor should run. Valid values are EVERY_MINUTE, EVERY_5_MINUTES, EVERY_10_MINUTES, EVERY_15_MINUTES, EVERY_30_MINUTES, EVERY_HOUR, EVERY_6_HOURS, EVERY_12_HOURS, or EVERY_DAY. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#period SyntheticsMonitor#period}
        :param runtime_type: The runtime type that the monitor will run. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#runtime_type SyntheticsMonitor#runtime_type}
        :param runtime_type_version: The specific version of the runtime type selected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#runtime_type_version SyntheticsMonitor#runtime_type_version}
        :param script_language: The programing language that should execute the script. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#script_language SyntheticsMonitor#script_language}
        :param tag: tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#tag SyntheticsMonitor#tag}
        :param treat_redirect_as_failure: Fail the monitor check if redirected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#treat_redirect_as_failure SyntheticsMonitor#treat_redirect_as_failure}
        :param uri: The URI for the monitor to hit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#uri SyntheticsMonitor#uri}
        :param validation_string: The string to validate against in the response. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#validation_string SyntheticsMonitor#validation_string}
        :param verify_ssl: Verify SSL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#verify_ssl SyntheticsMonitor#verify_ssl}
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
                status: builtins.str,
                type: builtins.str,
                account_id: typing.Optional[jsii.Number] = None,
                bypass_head_request: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                custom_header: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SyntheticsMonitorCustomHeader, typing.Dict[str, typing.Any]]]]] = None,
                enable_screenshot_on_failure_and_script: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                id: typing.Optional[builtins.str] = None,
                locations_private: typing.Optional[typing.Sequence[builtins.str]] = None,
                locations_public: typing.Optional[typing.Sequence[builtins.str]] = None,
                period: typing.Optional[builtins.str] = None,
                runtime_type: typing.Optional[builtins.str] = None,
                runtime_type_version: typing.Optional[builtins.str] = None,
                script_language: typing.Optional[builtins.str] = None,
                tag: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SyntheticsMonitorTag, typing.Dict[str, typing.Any]]]]] = None,
                treat_redirect_as_failure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                uri: typing.Optional[builtins.str] = None,
                validation_string: typing.Optional[builtins.str] = None,
                verify_ssl: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
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
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument bypass_head_request", value=bypass_head_request, expected_type=type_hints["bypass_head_request"])
            check_type(argname="argument custom_header", value=custom_header, expected_type=type_hints["custom_header"])
            check_type(argname="argument enable_screenshot_on_failure_and_script", value=enable_screenshot_on_failure_and_script, expected_type=type_hints["enable_screenshot_on_failure_and_script"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument locations_private", value=locations_private, expected_type=type_hints["locations_private"])
            check_type(argname="argument locations_public", value=locations_public, expected_type=type_hints["locations_public"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument runtime_type", value=runtime_type, expected_type=type_hints["runtime_type"])
            check_type(argname="argument runtime_type_version", value=runtime_type_version, expected_type=type_hints["runtime_type_version"])
            check_type(argname="argument script_language", value=script_language, expected_type=type_hints["script_language"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
            check_type(argname="argument treat_redirect_as_failure", value=treat_redirect_as_failure, expected_type=type_hints["treat_redirect_as_failure"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
            check_type(argname="argument validation_string", value=validation_string, expected_type=type_hints["validation_string"])
            check_type(argname="argument verify_ssl", value=verify_ssl, expected_type=type_hints["verify_ssl"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
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
        if bypass_head_request is not None:
            self._values["bypass_head_request"] = bypass_head_request
        if custom_header is not None:
            self._values["custom_header"] = custom_header
        if enable_screenshot_on_failure_and_script is not None:
            self._values["enable_screenshot_on_failure_and_script"] = enable_screenshot_on_failure_and_script
        if id is not None:
            self._values["id"] = id
        if locations_private is not None:
            self._values["locations_private"] = locations_private
        if locations_public is not None:
            self._values["locations_public"] = locations_public
        if period is not None:
            self._values["period"] = period
        if runtime_type is not None:
            self._values["runtime_type"] = runtime_type
        if runtime_type_version is not None:
            self._values["runtime_type_version"] = runtime_type_version
        if script_language is not None:
            self._values["script_language"] = script_language
        if tag is not None:
            self._values["tag"] = tag
        if treat_redirect_as_failure is not None:
            self._values["treat_redirect_as_failure"] = treat_redirect_as_failure
        if uri is not None:
            self._values["uri"] = uri
        if validation_string is not None:
            self._values["validation_string"] = validation_string
        if verify_ssl is not None:
            self._values["verify_ssl"] = verify_ssl

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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#name SyntheticsMonitor#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def status(self) -> builtins.str:
        '''The monitor status (i.e. ENABLED, MUTED, DISABLED).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#status SyntheticsMonitor#status}
        '''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The monitor type. Valid values are SIMPLE AND BROWSER.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#type SyntheticsMonitor#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[jsii.Number]:
        '''ID of the newrelic account.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#account_id SyntheticsMonitor#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def bypass_head_request(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Bypass HEAD request.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#bypass_head_request SyntheticsMonitor#bypass_head_request}
        '''
        result = self._values.get("bypass_head_request")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def custom_header(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsMonitorCustomHeader"]]]:
        '''custom_header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#custom_header SyntheticsMonitor#custom_header}
        '''
        result = self._values.get("custom_header")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsMonitorCustomHeader"]]], result)

    @builtins.property
    def enable_screenshot_on_failure_and_script(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Capture a screenshot during job execution.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#enable_screenshot_on_failure_and_script SyntheticsMonitor#enable_screenshot_on_failure_and_script}
        '''
        result = self._values.get("enable_screenshot_on_failure_and_script")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#id SyntheticsMonitor#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def locations_private(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The locations in which this monitor should be run.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#locations_private SyntheticsMonitor#locations_private}
        '''
        result = self._values.get("locations_private")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def locations_public(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The locations in which this monitor should be run.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#locations_public SyntheticsMonitor#locations_public}
        '''
        result = self._values.get("locations_public")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def period(self) -> typing.Optional[builtins.str]:
        '''The interval at which this monitor should run.

        Valid values are EVERY_MINUTE, EVERY_5_MINUTES, EVERY_10_MINUTES, EVERY_15_MINUTES, EVERY_30_MINUTES, EVERY_HOUR, EVERY_6_HOURS, EVERY_12_HOURS, or EVERY_DAY.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#period SyntheticsMonitor#period}
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def runtime_type(self) -> typing.Optional[builtins.str]:
        '''The runtime type that the monitor will run.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#runtime_type SyntheticsMonitor#runtime_type}
        '''
        result = self._values.get("runtime_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def runtime_type_version(self) -> typing.Optional[builtins.str]:
        '''The specific version of the runtime type selected.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#runtime_type_version SyntheticsMonitor#runtime_type_version}
        '''
        result = self._values.get("runtime_type_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def script_language(self) -> typing.Optional[builtins.str]:
        '''The programing language that should execute the script.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#script_language SyntheticsMonitor#script_language}
        '''
        result = self._values.get("script_language")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsMonitorTag"]]]:
        '''tag block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#tag SyntheticsMonitor#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsMonitorTag"]]], result)

    @builtins.property
    def treat_redirect_as_failure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Fail the monitor check if redirected.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#treat_redirect_as_failure SyntheticsMonitor#treat_redirect_as_failure}
        '''
        result = self._values.get("treat_redirect_as_failure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def uri(self) -> typing.Optional[builtins.str]:
        '''The URI for the monitor to hit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#uri SyntheticsMonitor#uri}
        '''
        result = self._values.get("uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def validation_string(self) -> typing.Optional[builtins.str]:
        '''The string to validate against in the response.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#validation_string SyntheticsMonitor#validation_string}
        '''
        result = self._values.get("validation_string")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def verify_ssl(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Verify SSL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#verify_ssl SyntheticsMonitor#verify_ssl}
        '''
        result = self._values.get("verify_ssl")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsMonitorConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.syntheticsMonitor.SyntheticsMonitorCustomHeader",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class SyntheticsMonitorCustomHeader:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Header name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#name SyntheticsMonitor#name}
        :param value: Header value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#value SyntheticsMonitor#value}
        '''
        if __debug__:
            def stub(
                *,
                name: typing.Optional[builtins.str] = None,
                value: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Header name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#name SyntheticsMonitor#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Header value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#value SyntheticsMonitor#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsMonitorCustomHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsMonitorCustomHeaderList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.syntheticsMonitor.SyntheticsMonitorCustomHeaderList",
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
    def get(self, index: jsii.Number) -> "SyntheticsMonitorCustomHeaderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SyntheticsMonitorCustomHeaderOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsMonitorCustomHeader]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsMonitorCustomHeader]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsMonitorCustomHeader]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsMonitorCustomHeader]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SyntheticsMonitorCustomHeaderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.syntheticsMonitor.SyntheticsMonitorCustomHeaderOutputReference",
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

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

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
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SyntheticsMonitorCustomHeader, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SyntheticsMonitorCustomHeader, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SyntheticsMonitorCustomHeader, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[SyntheticsMonitorCustomHeader, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.syntheticsMonitor.SyntheticsMonitorTag",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class SyntheticsMonitorTag:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Name of the tag key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#key SyntheticsMonitor#key}
        :param values: Values associated with the tag key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#values SyntheticsMonitor#values}
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#key SyntheticsMonitor#key}
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Values associated with the tag key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#values SyntheticsMonitor#values}
        '''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsMonitorTag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsMonitorTagList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.syntheticsMonitor.SyntheticsMonitorTagList",
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
    def get(self, index: jsii.Number) -> "SyntheticsMonitorTagOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SyntheticsMonitorTagOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsMonitorTag]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsMonitorTag]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsMonitorTag]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsMonitorTag]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SyntheticsMonitorTagOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.syntheticsMonitor.SyntheticsMonitorTagOutputReference",
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
    ) -> typing.Optional[typing.Union[SyntheticsMonitorTag, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SyntheticsMonitorTag, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SyntheticsMonitorTag, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[SyntheticsMonitorTag, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SyntheticsMonitor",
    "SyntheticsMonitorConfig",
    "SyntheticsMonitorCustomHeader",
    "SyntheticsMonitorCustomHeaderList",
    "SyntheticsMonitorCustomHeaderOutputReference",
    "SyntheticsMonitorTag",
    "SyntheticsMonitorTagList",
    "SyntheticsMonitorTagOutputReference",
]

publication.publish()
