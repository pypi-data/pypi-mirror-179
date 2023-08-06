'''
# `aws_dx_gateway_association`

Refer to the Terraform Registory for docs: [`aws_dx_gateway_association`](https://www.terraform.io/docs/providers/aws/r/dx_gateway_association).
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


class DxGatewayAssociation(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dxGatewayAssociation.DxGatewayAssociation",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association aws_dx_gateway_association}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        dx_gateway_id: builtins.str,
        allowed_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        associated_gateway_id: typing.Optional[builtins.str] = None,
        associated_gateway_owner_account_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        proposal_id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DxGatewayAssociationTimeouts", typing.Dict[str, typing.Any]]] = None,
        vpn_gateway_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association aws_dx_gateway_association} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param dx_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#dx_gateway_id DxGatewayAssociation#dx_gateway_id}.
        :param allowed_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#allowed_prefixes DxGatewayAssociation#allowed_prefixes}.
        :param associated_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#associated_gateway_id DxGatewayAssociation#associated_gateway_id}.
        :param associated_gateway_owner_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#associated_gateway_owner_account_id DxGatewayAssociation#associated_gateway_owner_account_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#id DxGatewayAssociation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param proposal_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#proposal_id DxGatewayAssociation#proposal_id}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#timeouts DxGatewayAssociation#timeouts}
        :param vpn_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#vpn_gateway_id DxGatewayAssociation#vpn_gateway_id}.
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
                dx_gateway_id: builtins.str,
                allowed_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
                associated_gateway_id: typing.Optional[builtins.str] = None,
                associated_gateway_owner_account_id: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                proposal_id: typing.Optional[builtins.str] = None,
                timeouts: typing.Optional[typing.Union[DxGatewayAssociationTimeouts, typing.Dict[str, typing.Any]]] = None,
                vpn_gateway_id: typing.Optional[builtins.str] = None,
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
        config = DxGatewayAssociationConfig(
            dx_gateway_id=dx_gateway_id,
            allowed_prefixes=allowed_prefixes,
            associated_gateway_id=associated_gateway_id,
            associated_gateway_owner_account_id=associated_gateway_owner_account_id,
            id=id,
            proposal_id=proposal_id,
            timeouts=timeouts,
            vpn_gateway_id=vpn_gateway_id,
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#create DxGatewayAssociation#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#delete DxGatewayAssociation#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#update DxGatewayAssociation#update}.
        '''
        value = DxGatewayAssociationTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAllowedPrefixes")
    def reset_allowed_prefixes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedPrefixes", []))

    @jsii.member(jsii_name="resetAssociatedGatewayId")
    def reset_associated_gateway_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssociatedGatewayId", []))

    @jsii.member(jsii_name="resetAssociatedGatewayOwnerAccountId")
    def reset_associated_gateway_owner_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssociatedGatewayOwnerAccountId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProposalId")
    def reset_proposal_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProposalId", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVpnGatewayId")
    def reset_vpn_gateway_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpnGatewayId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="associatedGatewayType")
    def associated_gateway_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "associatedGatewayType"))

    @builtins.property
    @jsii.member(jsii_name="dxGatewayAssociationId")
    def dx_gateway_association_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dxGatewayAssociationId"))

    @builtins.property
    @jsii.member(jsii_name="dxGatewayOwnerAccountId")
    def dx_gateway_owner_account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dxGatewayOwnerAccountId"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DxGatewayAssociationTimeoutsOutputReference":
        return typing.cast("DxGatewayAssociationTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="allowedPrefixesInput")
    def allowed_prefixes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedPrefixesInput"))

    @builtins.property
    @jsii.member(jsii_name="associatedGatewayIdInput")
    def associated_gateway_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "associatedGatewayIdInput"))

    @builtins.property
    @jsii.member(jsii_name="associatedGatewayOwnerAccountIdInput")
    def associated_gateway_owner_account_id_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "associatedGatewayOwnerAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="dxGatewayIdInput")
    def dx_gateway_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dxGatewayIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="proposalIdInput")
    def proposal_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "proposalIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DxGatewayAssociationTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DxGatewayAssociationTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="vpnGatewayIdInput")
    def vpn_gateway_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpnGatewayIdInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedPrefixes")
    def allowed_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedPrefixes"))

    @allowed_prefixes.setter
    def allowed_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedPrefixes", value)

    @builtins.property
    @jsii.member(jsii_name="associatedGatewayId")
    def associated_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "associatedGatewayId"))

    @associated_gateway_id.setter
    def associated_gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associatedGatewayId", value)

    @builtins.property
    @jsii.member(jsii_name="associatedGatewayOwnerAccountId")
    def associated_gateway_owner_account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "associatedGatewayOwnerAccountId"))

    @associated_gateway_owner_account_id.setter
    def associated_gateway_owner_account_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associatedGatewayOwnerAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="dxGatewayId")
    def dx_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dxGatewayId"))

    @dx_gateway_id.setter
    def dx_gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dxGatewayId", value)

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
    @jsii.member(jsii_name="proposalId")
    def proposal_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "proposalId"))

    @proposal_id.setter
    def proposal_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proposalId", value)

    @builtins.property
    @jsii.member(jsii_name="vpnGatewayId")
    def vpn_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpnGatewayId"))

    @vpn_gateway_id.setter
    def vpn_gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpnGatewayId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dxGatewayAssociation.DxGatewayAssociationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "dx_gateway_id": "dxGatewayId",
        "allowed_prefixes": "allowedPrefixes",
        "associated_gateway_id": "associatedGatewayId",
        "associated_gateway_owner_account_id": "associatedGatewayOwnerAccountId",
        "id": "id",
        "proposal_id": "proposalId",
        "timeouts": "timeouts",
        "vpn_gateway_id": "vpnGatewayId",
    },
)
class DxGatewayAssociationConfig(cdktf.TerraformMetaArguments):
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
        dx_gateway_id: builtins.str,
        allowed_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        associated_gateway_id: typing.Optional[builtins.str] = None,
        associated_gateway_owner_account_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        proposal_id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DxGatewayAssociationTimeouts", typing.Dict[str, typing.Any]]] = None,
        vpn_gateway_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param dx_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#dx_gateway_id DxGatewayAssociation#dx_gateway_id}.
        :param allowed_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#allowed_prefixes DxGatewayAssociation#allowed_prefixes}.
        :param associated_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#associated_gateway_id DxGatewayAssociation#associated_gateway_id}.
        :param associated_gateway_owner_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#associated_gateway_owner_account_id DxGatewayAssociation#associated_gateway_owner_account_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#id DxGatewayAssociation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param proposal_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#proposal_id DxGatewayAssociation#proposal_id}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#timeouts DxGatewayAssociation#timeouts}
        :param vpn_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#vpn_gateway_id DxGatewayAssociation#vpn_gateway_id}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = DxGatewayAssociationTimeouts(**timeouts)
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
                dx_gateway_id: builtins.str,
                allowed_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
                associated_gateway_id: typing.Optional[builtins.str] = None,
                associated_gateway_owner_account_id: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                proposal_id: typing.Optional[builtins.str] = None,
                timeouts: typing.Optional[typing.Union[DxGatewayAssociationTimeouts, typing.Dict[str, typing.Any]]] = None,
                vpn_gateway_id: typing.Optional[builtins.str] = None,
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
            check_type(argname="argument dx_gateway_id", value=dx_gateway_id, expected_type=type_hints["dx_gateway_id"])
            check_type(argname="argument allowed_prefixes", value=allowed_prefixes, expected_type=type_hints["allowed_prefixes"])
            check_type(argname="argument associated_gateway_id", value=associated_gateway_id, expected_type=type_hints["associated_gateway_id"])
            check_type(argname="argument associated_gateway_owner_account_id", value=associated_gateway_owner_account_id, expected_type=type_hints["associated_gateway_owner_account_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument proposal_id", value=proposal_id, expected_type=type_hints["proposal_id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument vpn_gateway_id", value=vpn_gateway_id, expected_type=type_hints["vpn_gateway_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "dx_gateway_id": dx_gateway_id,
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
        if allowed_prefixes is not None:
            self._values["allowed_prefixes"] = allowed_prefixes
        if associated_gateway_id is not None:
            self._values["associated_gateway_id"] = associated_gateway_id
        if associated_gateway_owner_account_id is not None:
            self._values["associated_gateway_owner_account_id"] = associated_gateway_owner_account_id
        if id is not None:
            self._values["id"] = id
        if proposal_id is not None:
            self._values["proposal_id"] = proposal_id
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if vpn_gateway_id is not None:
            self._values["vpn_gateway_id"] = vpn_gateway_id

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
    def dx_gateway_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#dx_gateway_id DxGatewayAssociation#dx_gateway_id}.'''
        result = self._values.get("dx_gateway_id")
        assert result is not None, "Required property 'dx_gateway_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#allowed_prefixes DxGatewayAssociation#allowed_prefixes}.'''
        result = self._values.get("allowed_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def associated_gateway_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#associated_gateway_id DxGatewayAssociation#associated_gateway_id}.'''
        result = self._values.get("associated_gateway_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def associated_gateway_owner_account_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#associated_gateway_owner_account_id DxGatewayAssociation#associated_gateway_owner_account_id}.'''
        result = self._values.get("associated_gateway_owner_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#id DxGatewayAssociation#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def proposal_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#proposal_id DxGatewayAssociation#proposal_id}.'''
        result = self._values.get("proposal_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DxGatewayAssociationTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#timeouts DxGatewayAssociation#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DxGatewayAssociationTimeouts"], result)

    @builtins.property
    def vpn_gateway_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#vpn_gateway_id DxGatewayAssociation#vpn_gateway_id}.'''
        result = self._values.get("vpn_gateway_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DxGatewayAssociationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dxGatewayAssociation.DxGatewayAssociationTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class DxGatewayAssociationTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#create DxGatewayAssociation#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#delete DxGatewayAssociation#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#update DxGatewayAssociation#update}.
        '''
        if __debug__:
            def stub(
                *,
                create: typing.Optional[builtins.str] = None,
                delete: typing.Optional[builtins.str] = None,
                update: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#create DxGatewayAssociation#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#delete DxGatewayAssociation#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_gateway_association#update DxGatewayAssociation#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DxGatewayAssociationTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DxGatewayAssociationTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dxGatewayAssociation.DxGatewayAssociationTimeoutsOutputReference",
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
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DxGatewayAssociationTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DxGatewayAssociationTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DxGatewayAssociationTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[DxGatewayAssociationTimeouts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DxGatewayAssociation",
    "DxGatewayAssociationConfig",
    "DxGatewayAssociationTimeouts",
    "DxGatewayAssociationTimeoutsOutputReference",
]

publication.publish()
