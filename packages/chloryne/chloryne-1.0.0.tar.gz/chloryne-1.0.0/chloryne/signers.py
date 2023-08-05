from . import _chloryne
from .keys import PrivateKey, PublicKey

__all__ = ['Signer']

class Signer:
    def __init__(self):
        self._context = _chloryne.new_sign_context()
    def update(self, data: bytes) -> None:
        'Updates the signer with given data.'
        _chloryne.update_sign_context(self._context, data)
    def sign(self, sk: PrivateKey) -> bytes:
        'Signs the context with given key.'
        return _chloryne.sign_sign_context(self._context, sk._edsk)
    def verify(self, pk: PublicKey, signature: bytes) -> bool:
        'Verifies the signature against this context.'
        return _chloryne.verify_sign_context(self._context, pk._edpk, signature)