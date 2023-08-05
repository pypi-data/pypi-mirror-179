from io import StringIO as _StringIO

CONTEXT = b"_ChloryneDerive_"
AEAD_NONCE_SIZE = 24
STREAM_NONCE_SIZE = 24

def hexdump(b: bytes) -> str:
    'Simulates the hexdump shell command.'
    result = _StringIO()
    for i in range(0, len(b), 8):
        result.write(oct(i))
        result.write('\t')
        result.write(' '.join([hex(j)[2:].zfill(2) for j in b[i:i+8]]))
        result.write('\n')
    return result.getvalue()[:-1]

def pad(b: bytes, size: int, padder: bytes=b'\0') -> bytes:
    'Pads given bytes to target size.'
    while len(b) < size:
        b += padder
    return b