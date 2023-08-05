from typing import Optional
from . import _chloryne
from .misc import AEAD_NONCE_SIZE, STREAM_NONCE_SIZE
import os

__all__ = ['AEADCipher', 'StreamCipher', 'DecryptionFailure']

class DecryptionFailure(Exception):
    'AEAD decryption failed, as the MAC is unmatched.'

class AEADCipher:
    'An AEAD cipher with MAC prepended to the message.'
    def __init__(self, secret: bytes, nonce: bytes=b''):
        self.secret = secret
        self.nonce = nonce
    def _ensurenonce(self) -> None:
        if self.nonce:
            if len(self.nonce) != AEAD_NONCE_SIZE:
                raise ValueError('invalid nonce size')
            return
        self.nonce = os.urandom(AEAD_NONCE_SIZE)
    def encrypt(self, data: bytes) -> bytes:
        'Encrypts given data with provided secret.'
        self._ensurenonce()
        return _chloryne.aead_encrypt(self.secret, self.nonce, data)
    def decrypt(self, data: bytes, raise_errors: bool=False) -> Optional[bytes]:
        'Decrypts given data with provided secret and nonce.'
        if not self.nonce:
            raise ValueError('decryption requires nonce')
        plain_text = _chloryne.aead_decrypt(self.secret, self.nonce, data)
        if not plain_text and raise_errors:
            raise DecryptionFailure
        return plain_text

class StreamCipher:
    'XSalsa20 stream cipher implementation.'
    def __init__(self, secret: bytes, nonce: bytes=b''):
        self.secret = secret
        self.nonce = nonce
    def _ensurenonce(self) -> None:
        if self.nonce:
            if len(self.nonce) != STREAM_NONCE_SIZE:
                raise ValueError('invalid nonce size')
            return
        self.nonce = os.urandom(STREAM_NONCE_SIZE)
    def encrypt(self, data: bytes) -> bytes:
        'Encrypts given data with provided secret.'
        self._ensurenonce()
        return _chloryne.stream_encrypt(self.secret, self.nonce, self.data)
    def decrypt(self, data: bytes) -> bytes:
        'Decrypts given data with provided secret and nonce.'
        if not self.nonce:
            raise ValueError('decryption requires nonce')
        self._ensurenonce()
        return _chloryne.stream_decrypt(self.secret, self.nonce, data)