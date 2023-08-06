from python_jose_TPM.backends.base import Key
from python_jose_TPM.constants import ALGORITHMS
from python_jose_TPM.exceptions import JWKError

try:
    from python_jose_TPM.backends import RSAKey  # noqa: F401
except ImportError:
    pass

try:
    from python_jose_TPM.backends import ECKey  # noqa: F401
except ImportError:
    pass

try:
    from python_jose_TPM.backends import AESKey  # noqa: F401
except ImportError:
    pass

try:
    from python_jose_TPM.backends import DIRKey  # noqa: F401
except ImportError:
    pass

try:
    from python_jose_TPM.backends import HMACKey  # noqa: F401
except ImportError:
    pass


def get_key(algorithm):
    if algorithm in ALGORITHMS.KEYS:
        return ALGORITHMS.KEYS[algorithm]
    elif algorithm in ALGORITHMS.HMAC:  # noqa: F811
        return HMACKey
    elif algorithm in ALGORITHMS.RSA:
        from python_jose_TPM.backends import RSAKey  # noqa: F811

        return RSAKey
    elif algorithm in ALGORITHMS.EC:
        from python_jose_TPM.backends import ECKey  # noqa: F811

        return ECKey
    elif algorithm in ALGORITHMS.AES:
        from python_jose_TPM.backends import AESKey  # noqa: F811

        return AESKey
    elif algorithm == ALGORITHMS.DIR:
        from python_jose_TPM.backends import DIRKey  # noqa: F811

        return DIRKey
    return None


def register_key(algorithm, key_class):
    if not issubclass(key_class, Key):
        raise TypeError("Key class is not a subclass of jwk.Key")
    ALGORITHMS.KEYS[algorithm] = key_class
    ALGORITHMS.SUPPORTED.add(algorithm)
    return True


def construct(key_data, algorithm=None):
    """
    Construct a Key object for the given algorithm with the given
    key_data.
    """

    # Allow for pulling the algorithm off of the passed in jwk.
    if not algorithm and isinstance(key_data, dict):
        algorithm = key_data.get("alg", None)

    if not algorithm:
        raise JWKError("Unable to find an algorithm for key: %s" % key_data)

    key_class = get_key(algorithm)
    if not key_class:
        raise JWKError("Unable to find an algorithm for key: %s" % key_data)
    return key_class(key_data, algorithm)
