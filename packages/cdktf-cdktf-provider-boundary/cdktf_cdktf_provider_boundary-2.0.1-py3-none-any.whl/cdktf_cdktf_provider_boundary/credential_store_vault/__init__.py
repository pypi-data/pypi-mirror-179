'''
# `boundary_credential_store_vault`

Refer to the Terraform Registory for docs: [`boundary_credential_store_vault`](https://www.terraform.io/docs/providers/boundary/r/credential_store_vault).
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


class CredentialStoreVault(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-boundary.credentialStoreVault.CredentialStoreVault",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault boundary_credential_store_vault}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        address: builtins.str,
        scope_id: builtins.str,
        token: builtins.str,
        ca_cert: typing.Optional[builtins.str] = None,
        client_certificate: typing.Optional[builtins.str] = None,
        client_certificate_key: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        tls_server_name: typing.Optional[builtins.str] = None,
        tls_skip_verify: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault boundary_credential_store_vault} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param address: The address to Vault server. This should be a complete URL such as 'https://127.0.0.1:8200'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#address CredentialStoreVault#address}
        :param scope_id: The scope for this credential store. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#scope_id CredentialStoreVault#scope_id}
        :param token: A token used for accessing Vault. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#token CredentialStoreVault#token}
        :param ca_cert: A PEM-encoded CA certificate to verify the Vault server's TLS certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#ca_cert CredentialStoreVault#ca_cert}
        :param client_certificate: A PEM-encoded client certificate to use for TLS authentication to the Vault server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#client_certificate CredentialStoreVault#client_certificate}
        :param client_certificate_key: A PEM-encoded private key matching the client certificate from 'client_certificate'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#client_certificate_key CredentialStoreVault#client_certificate_key}
        :param description: The Vault credential store description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#description CredentialStoreVault#description}
        :param name: The Vault credential store name. Defaults to the resource name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#name CredentialStoreVault#name}
        :param namespace: The namespace within Vault to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#namespace CredentialStoreVault#namespace}
        :param tls_server_name: Name to use as the SNI host when connecting to Vault via TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#tls_server_name CredentialStoreVault#tls_server_name}
        :param tls_skip_verify: Whether or not to skip TLS verification. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#tls_skip_verify CredentialStoreVault#tls_skip_verify}
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
                id: builtins.str,
                *,
                address: builtins.str,
                scope_id: builtins.str,
                token: builtins.str,
                ca_cert: typing.Optional[builtins.str] = None,
                client_certificate: typing.Optional[builtins.str] = None,
                client_certificate_key: typing.Optional[builtins.str] = None,
                description: typing.Optional[builtins.str] = None,
                name: typing.Optional[builtins.str] = None,
                namespace: typing.Optional[builtins.str] = None,
                tls_server_name: typing.Optional[builtins.str] = None,
                tls_skip_verify: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
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
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = CredentialStoreVaultConfig(
            address=address,
            scope_id=scope_id,
            token=token,
            ca_cert=ca_cert,
            client_certificate=client_certificate,
            client_certificate_key=client_certificate_key,
            description=description,
            name=name,
            namespace=namespace,
            tls_server_name=tls_server_name,
            tls_skip_verify=tls_skip_verify,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetCaCert")
    def reset_ca_cert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaCert", []))

    @jsii.member(jsii_name="resetClientCertificate")
    def reset_client_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCertificate", []))

    @jsii.member(jsii_name="resetClientCertificateKey")
    def reset_client_certificate_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCertificateKey", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetTlsServerName")
    def reset_tls_server_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsServerName", []))

    @jsii.member(jsii_name="resetTlsSkipVerify")
    def reset_tls_skip_verify(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsSkipVerify", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificateKeyHmac")
    def client_certificate_key_hmac(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientCertificateKeyHmac"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="tokenHmac")
    def token_hmac(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenHmac"))

    @builtins.property
    @jsii.member(jsii_name="addressInput")
    def address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressInput"))

    @builtins.property
    @jsii.member(jsii_name="caCertInput")
    def ca_cert_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caCertInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificateInput")
    def client_certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificateKeyInput")
    def client_certificate_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertificateKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeIdInput")
    def scope_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsServerNameInput")
    def tls_server_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsServerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsSkipVerifyInput")
    def tls_skip_verify_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tlsSkipVerifyInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="address")
    def address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "address"))

    @address.setter
    def address(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "address", value)

    @builtins.property
    @jsii.member(jsii_name="caCert")
    def ca_cert(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caCert"))

    @ca_cert.setter
    def ca_cert(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caCert", value)

    @builtins.property
    @jsii.member(jsii_name="clientCertificate")
    def client_certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientCertificate"))

    @client_certificate.setter
    def client_certificate(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="clientCertificateKey")
    def client_certificate_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientCertificateKey"))

    @client_certificate_key.setter
    def client_certificate_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCertificateKey", value)

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
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="scopeId")
    def scope_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scopeId"))

    @scope_id.setter
    def scope_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scopeId", value)

    @builtins.property
    @jsii.member(jsii_name="tlsServerName")
    def tls_server_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsServerName"))

    @tls_server_name.setter
    def tls_server_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsServerName", value)

    @builtins.property
    @jsii.member(jsii_name="tlsSkipVerify")
    def tls_skip_verify(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tlsSkipVerify"))

    @tls_skip_verify.setter
    def tls_skip_verify(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsSkipVerify", value)

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "token"))

    @token.setter
    def token(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-boundary.credentialStoreVault.CredentialStoreVaultConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "address": "address",
        "scope_id": "scopeId",
        "token": "token",
        "ca_cert": "caCert",
        "client_certificate": "clientCertificate",
        "client_certificate_key": "clientCertificateKey",
        "description": "description",
        "name": "name",
        "namespace": "namespace",
        "tls_server_name": "tlsServerName",
        "tls_skip_verify": "tlsSkipVerify",
    },
)
class CredentialStoreVaultConfig(cdktf.TerraformMetaArguments):
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
        address: builtins.str,
        scope_id: builtins.str,
        token: builtins.str,
        ca_cert: typing.Optional[builtins.str] = None,
        client_certificate: typing.Optional[builtins.str] = None,
        client_certificate_key: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        tls_server_name: typing.Optional[builtins.str] = None,
        tls_skip_verify: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param address: The address to Vault server. This should be a complete URL such as 'https://127.0.0.1:8200'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#address CredentialStoreVault#address}
        :param scope_id: The scope for this credential store. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#scope_id CredentialStoreVault#scope_id}
        :param token: A token used for accessing Vault. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#token CredentialStoreVault#token}
        :param ca_cert: A PEM-encoded CA certificate to verify the Vault server's TLS certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#ca_cert CredentialStoreVault#ca_cert}
        :param client_certificate: A PEM-encoded client certificate to use for TLS authentication to the Vault server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#client_certificate CredentialStoreVault#client_certificate}
        :param client_certificate_key: A PEM-encoded private key matching the client certificate from 'client_certificate'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#client_certificate_key CredentialStoreVault#client_certificate_key}
        :param description: The Vault credential store description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#description CredentialStoreVault#description}
        :param name: The Vault credential store name. Defaults to the resource name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#name CredentialStoreVault#name}
        :param namespace: The namespace within Vault to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#namespace CredentialStoreVault#namespace}
        :param tls_server_name: Name to use as the SNI host when connecting to Vault via TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#tls_server_name CredentialStoreVault#tls_server_name}
        :param tls_skip_verify: Whether or not to skip TLS verification. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#tls_skip_verify CredentialStoreVault#tls_skip_verify}
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
                address: builtins.str,
                scope_id: builtins.str,
                token: builtins.str,
                ca_cert: typing.Optional[builtins.str] = None,
                client_certificate: typing.Optional[builtins.str] = None,
                client_certificate_key: typing.Optional[builtins.str] = None,
                description: typing.Optional[builtins.str] = None,
                name: typing.Optional[builtins.str] = None,
                namespace: typing.Optional[builtins.str] = None,
                tls_server_name: typing.Optional[builtins.str] = None,
                tls_skip_verify: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
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
            check_type(argname="argument address", value=address, expected_type=type_hints["address"])
            check_type(argname="argument scope_id", value=scope_id, expected_type=type_hints["scope_id"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
            check_type(argname="argument ca_cert", value=ca_cert, expected_type=type_hints["ca_cert"])
            check_type(argname="argument client_certificate", value=client_certificate, expected_type=type_hints["client_certificate"])
            check_type(argname="argument client_certificate_key", value=client_certificate_key, expected_type=type_hints["client_certificate_key"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument tls_server_name", value=tls_server_name, expected_type=type_hints["tls_server_name"])
            check_type(argname="argument tls_skip_verify", value=tls_skip_verify, expected_type=type_hints["tls_skip_verify"])
        self._values: typing.Dict[str, typing.Any] = {
            "address": address,
            "scope_id": scope_id,
            "token": token,
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
        if ca_cert is not None:
            self._values["ca_cert"] = ca_cert
        if client_certificate is not None:
            self._values["client_certificate"] = client_certificate
        if client_certificate_key is not None:
            self._values["client_certificate_key"] = client_certificate_key
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace
        if tls_server_name is not None:
            self._values["tls_server_name"] = tls_server_name
        if tls_skip_verify is not None:
            self._values["tls_skip_verify"] = tls_skip_verify

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
    def address(self) -> builtins.str:
        '''The address to Vault server. This should be a complete URL such as 'https://127.0.0.1:8200'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#address CredentialStoreVault#address}
        '''
        result = self._values.get("address")
        assert result is not None, "Required property 'address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scope_id(self) -> builtins.str:
        '''The scope for this credential store.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#scope_id CredentialStoreVault#scope_id}
        '''
        result = self._values.get("scope_id")
        assert result is not None, "Required property 'scope_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def token(self) -> builtins.str:
        '''A token used for accessing Vault.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#token CredentialStoreVault#token}
        '''
        result = self._values.get("token")
        assert result is not None, "Required property 'token' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ca_cert(self) -> typing.Optional[builtins.str]:
        '''A PEM-encoded CA certificate to verify the Vault server's TLS certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#ca_cert CredentialStoreVault#ca_cert}
        '''
        result = self._values.get("ca_cert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_certificate(self) -> typing.Optional[builtins.str]:
        '''A PEM-encoded client certificate to use for TLS authentication to the Vault server.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#client_certificate CredentialStoreVault#client_certificate}
        '''
        result = self._values.get("client_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_certificate_key(self) -> typing.Optional[builtins.str]:
        '''A PEM-encoded private key matching the client certificate from 'client_certificate'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#client_certificate_key CredentialStoreVault#client_certificate_key}
        '''
        result = self._values.get("client_certificate_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The Vault credential store description.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#description CredentialStoreVault#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The Vault credential store name. Defaults to the resource name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#name CredentialStoreVault#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace within Vault to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#namespace CredentialStoreVault#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_server_name(self) -> typing.Optional[builtins.str]:
        '''Name to use as the SNI host when connecting to Vault via TLS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#tls_server_name CredentialStoreVault#tls_server_name}
        '''
        result = self._values.get("tls_server_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_skip_verify(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether or not to skip TLS verification.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_store_vault#tls_skip_verify CredentialStoreVault#tls_skip_verify}
        '''
        result = self._values.get("tls_skip_verify")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CredentialStoreVaultConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CredentialStoreVault",
    "CredentialStoreVaultConfig",
]

publication.publish()
