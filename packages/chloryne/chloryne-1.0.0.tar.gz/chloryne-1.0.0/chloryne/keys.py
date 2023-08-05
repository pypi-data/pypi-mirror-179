from typing import Tuple
from . import _chloryne
from .misc import CONTEXT

__all__ = ['PrivateKey', 'PublicKey', 'generate_key_pair', 'generate_key']

class PrivateKey:
    'Secret key of chloryne. Involves both ed-25519 and curve-25519.'
    def __init__(self, sk: bytes):
        self._edsk = sk
        self._xsk = _chloryne.convert_private_key(sk)
    @property
    def publicKey(self) -> 'PublicKey':
        'Gets the public key of this private key.'
        return PublicKey(_chloryne.public_sign_key(self._edsk))
    def exportKey(self, x25519: bool=False) -> bytes:
        'Exports raw private key.'
        return self._xsk if x25519 else self._edsk
    def compute(self, pub_key: 'PublicKey', raw: bool=False) -> bytes:
        'Computes shared secret with public key.'
        raw_secret = _chloryne.compute_secret(self._xsk, pub_key._xpk)
        if raw:
            return raw_secret
        return _chloryne.derive_key_plain(raw_secret, CONTEXT)
    def sign(self, data: bytes) -> bytes:
        'Signs given data with ed-25519 key.'
        return _chloryne.sign(self._edsk, data)

class PublicKey:
    'Public key of chloryne. Involves both ed-25519 and curve-25519.'
    def __init__(self, pk: bytes):
        self._edpk = pk
        self._xpk = _chloryne.convert_public_key(pk)
    def exportKey(self, x25519: bool=False) -> bytes:
        'Exports raw public key.'
        return self._xpk if x25519 else self._edpk
    def verify(self, data: bytes, signature: bytes) -> bool:
        'Verifes given signature against specific data.'
        return _chloryne.verify(self._edpk, data, signature)

def generate_key_pair() -> Tuple[PrivateKey, PublicKey]:
    'Generates a pair of private and public keys.'
    sk, pk = _chloryne.generate_key()
    return PrivateKey(sk), PublicKey(pk)

def generate_key() -> PrivateKey:
    'Generates private key only.'
    sk = _chloryne.generate_key()[0]
    return PrivateKey(sk)