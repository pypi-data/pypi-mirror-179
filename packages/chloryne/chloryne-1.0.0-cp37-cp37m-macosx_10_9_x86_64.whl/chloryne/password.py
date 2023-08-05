from . import _chloryne
from .misc import pad

__all__ = ['Password']

class Password:
    'Functions for password hashing.'
    @staticmethod
    def derive(passwd: bytes, salt: bytes, keylen: int=32) -> bytes:
        'Derives a key from given password.'
        salt = pad(salt, 32)
        return _chloryne.derive_password(passwd, salt, keylen)
    @staticmethod
    def stringify(passwd: bytes) -> str:
        'Hashes the password as a self-described string.'
        return _chloryne.store_password(passwd)
    @staticmethod
    def verify(passwd: bytes, hash_str: str) -> bool:
        'Verifies the password against the hash.'
        return _chloryne.verify_password(passwd, hash_str)