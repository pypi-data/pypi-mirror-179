from hmac import compare_digest
from . import _chloryne
from .misc import pad

__all__ = ['MAC']

class MAC:
    'MAC (Message Authentication Code) context.'
    def __init__(self, secret: bytes):
        secret = pad(secret, 32)
        self._context = _chloryne.new_mac_context(secret)
    def update(self, data: bytes) -> None:
        'Updates the MAC context with given data.'
        _chloryne.update_mac_context(self._context, data)
    def finalize(self) -> bytes:
        'Finalizes the MAC context.'
        return _chloryne.final_mac_context(self._context)
    def verify(self, digest: bytes) -> bool:
        'Verifies the MAC context against given digest.'
        return compare_digest(self.finalize(), digest)