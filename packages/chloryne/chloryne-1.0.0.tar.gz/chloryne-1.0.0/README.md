# Chloryne - libsodium wrapper

Another libsodium wrapper, with its own scheme.

## Installation

Chloryne is available via PyPI:
```
$ pip install chloryne
```

Installation requires the presence of `libsodium`.

## Usage

Use the up-level interface `Chloride` for a full cryptographic scheme.

Key generation:
```py
from chloryne import Chloride
# lib sodium will be initialized automatically

server = Chloride()
client = Chloride()
```

Key export / import:
```py
server.importKey(client.exportKey())
client.importKey(server.exportKey())
```

Compute a blake2b-derived shared secret:
```py
assert server.compute() == client.compute()
```

> NOTE: If you want a raw secret use `server.privateKey.compute(client.publicKey, raw=True)` and vice versa.

Signature (`Ed25519`):
```py
sig = server.sign(b'data')
assert client.verify(b'data', sig)
```

> NOTE: Signing messages only does not require peer key.

Encryption (`Curve25519XSalsa20Poly1305`):
```py
ct = server.encrypt(b'data')
assert client.decrypt(ct) == b'data'
```

> NOTE: Decrypting messages only does not require peer key.

Unsafe MAC (fixed key):
```py
mac = server.unsafeMAC()
mac.update(b'data')
digest = mac.finalize()
mac = client.unsafeMAC()
mac.update(b'data')
assert mac.verify(digest)
```

Safe MAC (ephemeral keys)
```py
eph, mac = server.safeMAC()
mac.update(b'data')
digest = mac.finalize()
mac = client.safeMAC(eph)
mac.update(b'data')
assert mac.verify(digest)
```

> NOTE: Verifying MACs only does not require peer key.

Incremental signing:
```py
from chloride.signers import Signer

signer = Signer()
signer.update(b'data')
sig = signer.sign(server.privateKey)
signer = Signer()
signer.update(b'data')
assert signer.verify(client.peerPublicKey, sig)
```

Password hashing:
```py
from chloride.password import Password
import os

# password-based KDF
salt = os.urandom(32) # must be 32-bytes
Password.derive(b'password', salt)

# password storage
strhash = Password.stringify(b'password')
assert Password.verify(b'password', strhash)
```

Stream Cipher (`XChaCha20`):
```py
from chloride.ciphers import StreamCipher
import os

key = os.urandom(32)
sc = StreamCipher(key)
ct = sc.encrypt(b'data') + sc.nonce
# other side...
ct, nonce = ct[:-24], ct[-24:]
sc = StreamCipher(key, nonce)
assert sc.decrypt(ct) == b'data'
```

> NOTE: `nonce` is `b''` before calling `encrypt` if not provided via constructor.

Store a chloride:
```py
sk = server.privateKey.exportKey()
# sk is a bytes object that can be stored anywhere
server = Chloride(sk)
```