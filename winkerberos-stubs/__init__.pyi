"""
Type stubs for winkerberos

A native Kerberos SSPI client implementation.
"""

from typing import Optional, Tuple, Union, Any

__version__: str

# Constants
AUTH_GSS_COMPLETE: int
AUTH_GSS_CONTINUE: int
GSS_C_AF_UNSPEC: int
GSS_C_CONF_FLAG: int
GSS_C_DELEG_FLAG: int
GSS_C_INTEG_FLAG: int
GSS_C_MUTUAL_FLAG: int
GSS_C_REPLAY_FLAG: int
GSS_C_SEQUENCE_FLAG: int
GSS_MECH_OID_KRB5: Any
GSS_MECH_OID_SPNEGO: Any

# Exception classes
class KrbError(Exception):
    """Base Kerberos error exception."""

    ...

class GSSError(KrbError):
    """GSS-API error exception."""

    ...

# Client functions
def authGSSClientInit(
    service: str,
    principal: Optional[str] = None,
    gssflags: int = GSS_C_MUTUAL_FLAG | GSS_C_SEQUENCE_FLAG,
    user: Optional[str] = None,
    domain: Optional[str] = None,
    password: Optional[Union[str, bytes]] = None,
    mech_oid: Any = GSS_MECH_OID_KRB5,
) -> Tuple[int, Any]:
    """
    Initializes a context for Kerberos SSPI client side authentication with
    the given service principal.

    Args:
        service: A string containing the service principal in RFC-2078 format
            (service@hostname) or SPN format (service/hostname or
            service/hostname@REALM).
        principal: An optional string containing the user principal name in
            the format user@realm. Can include password as user@realm:password.
        gssflags: An optional integer used to set GSS flags.
        user: (DEPRECATED) An optional string that contains the name of the
            user whose credentials should be used for authentication.
        domain: (DEPRECATED) An optional string that contains the domain or
            workgroup name for user.
        password: (DEPRECATED) An optional string that contains the password
            for user in domain.
        mech_oid: Optional GSS mech OID. Defaults to GSS_MECH_OID_KRB5.

    Returns:
        A tuple of (result, context) where result is AUTH_GSS_COMPLETE
        and context is an opaque value passed in subsequent function calls.
    """
    ...

def authGSSClientStep(context: Any, challenge: str, **kwargs: Any) -> int:
    """
    Executes a single Kerberos SSPI client step using the supplied server challenge.

    Args:
        context: The context object returned by authGSSClientInit.
        challenge: A string containing the base64 encoded server challenge.
            Ignored for the first step (pass the empty string).
        **kwargs: Optional keyword arguments including:
            channel_bindings: Optional SecPkgContext_Bindings structure
                returned by channelBindings().

    Returns:
        AUTH_GSS_CONTINUE or AUTH_GSS_COMPLETE
    """
    ...

def authGSSClientResponse(context: Any) -> str:
    """
    Get the response to the last successful client operation.

    Args:
        context: The context object returned by authGSSClientInit.

    Returns:
        A base64 encoded string to return to the server.
    """
    ...

def authGSSClientResponseConf(context: Any) -> int:
    """
    Determine whether confidentiality was enabled in the previously unwrapped
    buffer.

    Args:
        context: The context object returned by authGSSClientInit.

    Returns:
        1 if confidentiality was enabled in the previously unwrapped
        buffer, 0 otherwise.
    """
    ...

def authGSSClientUserName(context: Any) -> str:
    """
    Get the user name of the authenticated principal. Will only succeed after
    authentication is complete.

    Args:
        context: The context object returned by authGSSClientInit.

    Returns:
        A string containing the username.
    """
    ...

def authGSSClientWrap(
    context: Any, data: str, user: Optional[str] = None, protect: int = 0
) -> int:
    """
    Execute the client side EncryptMessage (GSSAPI Wrap) operation.

    Args:
        context: The context object returned by authGSSClientInit.
        data: If user is not None, this should be the result of calling
            authGSSClientResponse after authGSSClientUnwrap.
            If user is None, this should be a base64 encoded authorization
            message as specified in Section 3.1 of RFC-4752.
        user: An optional string containing the user principal to authorize.
        protect: If 0 (the default), then just provide integrity protection.
            If 1, then provide confidentiality as well (requires passing
            GSS_C_CONF_FLAG to gssflags in authGSSClientInit).

    Returns:
        AUTH_GSS_COMPLETE
    """
    ...

def authGSSClientUnwrap(context: Any, challenge: str) -> int:
    """
    Execute the client side DecryptMessage (GSSAPI Unwrap) operation.

    Args:
        context: The context object returned by authGSSClientInit.
        challenge: A string containing the base64 encoded server challenge.

    Returns:
        AUTH_GSS_COMPLETE
    """
    ...

def authGSSClientClean(context: Any) -> int:
    """
    Destroys the client context. This function is provided for API
    compatibility with pykerberos but does nothing. The context object
    destroys itself when it is reclaimed.

    Args:
        context: The context object returned by authGSSClientInit.

    Returns:
        AUTH_GSS_COMPLETE
    """
    ...

# Server functions
def authGSSServerInit(service: str) -> Tuple[int, Any]:
    """
    Initializes a context for Kerberos SSPI server side authentication with
    the given service principal.

    Args:
        service: A string containing the service principal in RFC-2078 format
            (service@hostname) or SPN format (service/hostname or
            service/hostname@REALM).

    Returns:
        A tuple of (result, context) where result is AUTH_GSS_COMPLETE
        and context is an opaque value passed in subsequent function calls.
    """
    ...

def authGSSServerStep(context: Any, challenge: str) -> int:
    """
    Executes a single Kerberos SSPI server step using the supplied client data.

    Args:
        context: The context object returned by authGSSServerInit.
        challenge: A string containing the base64 encoded client data.

    Returns:
        AUTH_GSS_CONTINUE or AUTH_GSS_COMPLETE
    """
    ...

def authGSSServerResponse(context: Any) -> str:
    """
    Get the response to the last successful server operation.

    Args:
        context: The context object returned by authGSSServerInit.

    Returns:
        A base64 encoded string to be sent to the client.
    """
    ...

def authGSSServerUserName(context: Any) -> str:
    """
    Get the user name of the principal trying to authenticate to the server.
    Will only succeed after authGSSServerStep returns a complete or
    continue response.

    Args:
        context: The context object returned by authGSSServerInit.

    Returns:
        A string containing the username.
    """
    ...

def authGSSServerClean(context: Any) -> int:
    """
    Destroys the server context. This function is provided for API
    compatibility with pykerberos but does nothing. The context object
    destroys itself when it is reclaimed.

    Args:
        context: The context object returned by authGSSServerInit.

    Returns:
        AUTH_GSS_COMPLETE
    """
    ...

# Channel bindings function
def channelBindings(
    initiator_addrtype: int = GSS_C_AF_UNSPEC,
    initiator_address: Optional[bytes] = None,
    acceptor_addrtype: int = GSS_C_AF_UNSPEC,
    acceptor_address: Optional[bytes] = None,
    application_data: Optional[bytes] = None,
) -> Any:
    """
    Builds a SecPkgContext_Bindings struct and returns an opaque pointer to
    it. The return value can be passed to authGSSClientStep using the
    channel_bindings keyword argument.

    Args:
        initiator_addrtype: Optional int specifying the initiator address type.
            Defaults to GSS_C_AF_UNSPEC.
        initiator_address: Optional byte string containing the initiator address.
        acceptor_addrtype: Optional int specifying the acceptor address type.
            Defaults to GSS_C_AF_UNSPEC.
        acceptor_address: Optional byte string containing the acceptor address.
        application_data: Optional byte string containing the application data.
            An example of this would be 'tls-server-end-point:{cert-hash}' where
            {cert-hash} is the hash of the server's certificate.

    Returns:
        An opaque value to be passed to the channel_bindings parameter of
        authGSSClientStep
    """
    ...
