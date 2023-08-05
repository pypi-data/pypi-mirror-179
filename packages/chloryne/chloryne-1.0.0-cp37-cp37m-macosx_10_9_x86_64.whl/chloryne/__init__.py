from typing import Optional, Tuple
from . import _chloryne
from .ciphers import AEADCipher
from .keys import PrivateKey, PublicKey, generate_key_pair
from .mac import MAC
from .misc import CONTEXT
import os

__all__ = ['Chloride']

if _chloryne.init_sodium():
    raise RuntimeError('libsodium initialization error')

class Chloride:
    'A crypto scheme containing all functionalities in submodules.'
    def __init__(self, sk: bytes=b''):
        if sk:
            self.privateKey = PrivateKey(sk)
            self.publicKey = self.privateKey.publicKey
        else:
            self.privateKey, self.publicKey = generate_key_pair()
        self.peerPublicKey = None
    def exportKey(self) -> bytes:
        'Exports public key as bytes.'
        return self.publicKey.exportKey()
    def importKey(self, blob: bytes) -> None:
        'Imports peer public key from bytes.'
        self.peerPublicKey = PublicKey(blob)
    def compute(self) -> bytes:
        'Computes a shared secret with peer.'
        self._ensurePublicKey('compute')
        return self.privateKey.compute(self.peerPublicKey)
    def _ensurePublicKey(self, op: str) -> None:
        if not self.peerPublicKey:
            raise ValueError(f'{op} requires peer public key')
    def sign(self, data: bytes) -> bytes:
        'Signs given data with local private key.'
        return self.privateKey.sign(data)
    def verify(self, data: bytes, signature: bytes) -> bool:
        'Verifies given data with remote public key.'
        self._ensurePublicKey('verify')
        return self.peerPublicKey.verify(data, signature)
    def encrypt(self, data: bytes) -> bytes:
        'Encrypts given data with remote public key.'
        self._ensurePublicKey('encrypt')
        esk, epk = generate_key_pair()
        salt = os.urandom(16)
        secret = esk.compute(self.peerPublicKey, raw=True)
        secret = _chloryne.derive_key_salted(secret, salt, CONTEXT)
        cipher = AEADCipher(secret)
        ciphertext = cipher.encrypt(data)
        return epk.exportKey() + salt + cipher.nonce + ciphertext
    def decrypt(self, data: bytes, raise_errors: bool=False) -> Optional[bytes]:
        'Decrypts given data with local private key.'
        epk = PublicKey(data[:32])
        salt = data[32:48]
        nonce = data[48:72]
        secret = self.privateKey.compute(epk, raw=True)
        secret = _chloryne.derive_key_salted(secret, salt, CONTEXT)
        cipher = AEADCipher(secret, nonce)
        return cipher.decrypt(data[72:], raise_errors)
    def unsafeMAC(self) -> MAC:
        'Creates a MAC context with fixed shared secret.'
        self._ensurePublicKey('unsafeMAC')
        return MAC(self.privateKey.compute(self.peerPublicKey))
    def safeMAC(self, ephemeral_pk: bytes=b'') -> Tuple[bytes, MAC]:
        'Creates a MAC context with ephemeral keys.'
        if ephemeral_pk:
            secret = self.privateKey.compute(PublicKey(ephemeral_pk))
            return ephemeral_pk, MAC(secret)
        else:
            self._ensurePublicKey('safeMAC without ephemeral key')
            esk, epk = generate_key_pair()
            secret = esk.compute(self.peerPublicKey)
            return epk.exportKey(), MAC(secret)