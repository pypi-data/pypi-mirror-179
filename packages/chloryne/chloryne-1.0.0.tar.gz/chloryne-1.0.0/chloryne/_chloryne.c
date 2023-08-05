#include <sodium.h>
#include <Python.h>

#define INV_ARGS \
    PyErr_SetString(PyExc_TypeError, "invalid arguments"); \
    return NULL

PyObject *InitSodium(PyObject *self, PyObject *args) {
    return Py_BuildValue("i", sodium_init());
}

PyObject *GenerateKey(PyObject *self, PyObject *args) {
    unsigned char pk[crypto_sign_ed25519_PUBLICKEYBYTES];
    unsigned char sk[crypto_sign_ed25519_SECRETKEYBYTES];
    crypto_sign_ed25519_keypair(pk, sk);
    PyObject *sk_bytes = PyBytes_FromStringAndSize((char*)sk, crypto_sign_ed25519_SECRETKEYBYTES);
    PyObject *pk_bytes = PyBytes_FromStringAndSize((char*)pk, crypto_sign_ed25519_PUBLICKEYBYTES);
    return PyTuple_Pack(2, sk_bytes, pk_bytes);
}

PyObject *PublicSignKey(PyObject *self, PyObject *args) {
    PyObject *sk_bytes;
    if (!PyArg_ParseTuple(args, "O", &sk_bytes)) {
        INV_ARGS;
    }
    unsigned char *sk = (unsigned char*)PyBytes_AsString(sk_bytes);
    unsigned char pk[crypto_sign_ed25519_PUBLICKEYBYTES];
    crypto_sign_ed25519_sk_to_pk(pk, sk);
    return PyBytes_FromStringAndSize((char*)pk, crypto_sign_ed25519_PUBLICKEYBYTES);
}

PyObject *PublicXKey(PyObject *self, PyObject *args) {
    PyObject *sk_bytes;
    if (!PyArg_ParseTuple(args, "O", &sk_bytes)) {
        INV_ARGS;
    }
    unsigned char *sk = (unsigned char*)PyBytes_AsString(sk_bytes);
    unsigned char pk[crypto_scalarmult_curve25519_BYTES];
    crypto_scalarmult_curve25519_base(pk, sk);
    return PyBytes_FromStringAndSize((char*)pk, crypto_scalarmult_curve25519_BYTES);
}

PyObject *ConvertPrivateKey(PyObject *self, PyObject *args) {
    PyObject *sk_bytes;
    if (!PyArg_ParseTuple(args, "O", &sk_bytes)) {
        INV_ARGS;
    }
    unsigned char *sk = (unsigned char*)PyBytes_AsString(sk_bytes);
    unsigned char sk_c2[crypto_scalarmult_curve25519_BYTES];
    crypto_sign_ed25519_sk_to_curve25519(sk_c2, sk);
    return PyBytes_FromStringAndSize((char*)sk_c2, crypto_scalarmult_curve25519_BYTES);
}

PyObject *ConvertPublicKey(PyObject *self, PyObject *args) {
    PyObject *pk_bytes;
    if (!PyArg_ParseTuple(args, "O", &pk_bytes)) {
        INV_ARGS;
    }
    unsigned char *pk = (unsigned char*)PyBytes_AsString(pk_bytes);
    unsigned char pk_c2[crypto_scalarmult_curve25519_BYTES];
    if (crypto_sign_ed25519_pk_to_curve25519(pk_c2, pk) != 0) {
        PyErr_SetString(PyExc_ValueError, "failed to convert");
    }
    return PyBytes_FromStringAndSize((char*)pk_c2, crypto_scalarmult_curve25519_BYTES);
}

PyObject *Sign(PyObject *self, PyObject *args) {
    PyObject *sk_bytes;
    PyObject *msg_bytes;
    if (!PyArg_ParseTuple(args, "OO", &sk_bytes, &msg_bytes)) {
        INV_ARGS;
    }
    unsigned char *sk = (unsigned char*)PyBytes_AsString(sk_bytes);
    long len;
    char *msg;
    PyBytes_AsStringAndSize(msg_bytes, &msg, &len);
    unsigned char sig[crypto_sign_ed25519_BYTES];
    crypto_sign_ed25519_detached(sig, NULL, (unsigned char*)msg, len, sk);
    return PyBytes_FromStringAndSize((char*)sig, crypto_sign_ed25519_BYTES);
}

PyObject *Verify(PyObject *self, PyObject *args) {
    PyObject *pk_bytes;
    PyObject *msg_bytes;
    PyObject *sig_bytes;
    if (!PyArg_ParseTuple(args, "OOO", &pk_bytes, &msg_bytes, &sig_bytes)) {
        INV_ARGS;
    }
    unsigned char *pk = (unsigned char*)PyBytes_AsString(pk_bytes);
    unsigned char *sig = (unsigned char*)PyBytes_AsString(sig_bytes);
    long msg_len;
    char *msg;
    PyBytes_AsStringAndSize(msg_bytes, &msg, &msg_len);
    if (crypto_sign_ed25519_verify_detached((unsigned char*)sig, (unsigned char*)msg, msg_len, pk) != 0) {
        Py_RETURN_FALSE;
    }
    Py_RETURN_TRUE;
}

PyObject *NewSignContext(PyObject *self, PyObject *args) {
    crypto_sign_ed25519ph_state state;
    crypto_sign_ed25519ph_init(&state);
    return PyCapsule_New(&state, NULL, NULL);
}

PyObject *UpdateSignContext(PyObject *self, PyObject *args) {
    PyObject *context_cap;
    PyObject *msg_bytes;
    if (!PyArg_ParseTuple(args, "O", &context_cap, &msg_bytes)) {
        INV_ARGS;
    }
    long len;
    char *msg;
    PyBytes_AsStringAndSize(msg_bytes, &msg, &len);
    crypto_sign_ed25519ph_state* state = 
        (crypto_sign_ed25519ph_state*)PyCapsule_GetPointer(context_cap, NULL);
    crypto_sign_ed25519ph_update(state, (unsigned char*)msg, len);
    Py_RETURN_NONE;
}

PyObject *SignSignContext(PyObject *self, PyObject *args) {
    PyObject *context_cap;
    PyObject *sk_bytes;
    if (!PyArg_ParseTuple(args, "OO", &context_cap, &sk_bytes)) {
        INV_ARGS;
    }
    crypto_sign_ed25519ph_state *state = PyCapsule_GetPointer(context_cap, NULL);
    unsigned char *sk = (unsigned char*)PyBytes_AsString(sk_bytes);
    unsigned char sig[crypto_sign_ed25519_BYTES];
    crypto_sign_ed25519ph_final_create(state, sig, NULL, sk);
    return PyBytes_FromStringAndSize((char*)sig, crypto_sign_ed25519_BYTES);
}

PyObject *VerifySignContext(PyObject *self, PyObject *args) {
    PyObject *context_cap;
    PyObject *pk_bytes;
    PyObject *sig_bytes;
    if (!PyArg_ParseTuple(args, "OOO", &context_cap, &pk_bytes, &sig_bytes)) {
        INV_ARGS;
    }
    crypto_sign_ed25519ph_state *state = PyCapsule_GetPointer(context_cap, NULL);
    unsigned char *pk = (unsigned char*)PyBytes_AsString(pk_bytes);
    unsigned char *sig = (unsigned char*)PyBytes_AsString(sig_bytes);
    if (crypto_sign_ed25519ph_final_verify(state, sig, pk) != 0) {
        Py_RETURN_FALSE;
    }
    Py_RETURN_TRUE;
}

PyObject *ComputeSecret(PyObject *self, PyObject *args) {
    PyObject *sk_bytes;
    PyObject *pk_bytes;
    if (!PyArg_ParseTuple(args, "OO", &sk_bytes, &pk_bytes)) {
        INV_ARGS;
    }
    unsigned char *sk = (unsigned char*)PyBytes_AsString(sk_bytes);
    unsigned char *pk = (unsigned char*)PyBytes_AsString(pk_bytes);
    unsigned char ss[crypto_scalarmult_curve25519_BYTES];
    if (crypto_scalarmult_curve25519(ss, sk, pk) != 0) {
        PyErr_SetString(PyExc_ValueError, "failed to compute secret");
        return NULL;
    }
    return PyBytes_FromStringAndSize((char*)ss, crypto_scalarmult_curve25519_BYTES);
}

PyObject *DeriveKeyPlain(PyObject *self, PyObject *args) {
    PyObject *ss_bytes;
    PyObject *context_bytes;
    if (!PyArg_ParseTuple(args, "OO", &ss_bytes, &context_bytes)) {
        INV_ARGS;
    }
    unsigned char *ss = (unsigned char*)PyBytes_AsString(ss_bytes);
    unsigned char *context = (unsigned char*)PyBytes_AsString(context_bytes);
    unsigned char derived[crypto_generichash_blake2b_BYTES];
    crypto_generichash_blake2b_salt_personal(
        derived, crypto_generichash_blake2b_BYTES, 
        ss, crypto_scalarmult_curve25519_BYTES,
        NULL, 0, NULL, context);
    return PyBytes_FromStringAndSize((char*)derived, crypto_generichash_blake2b_BYTES);
}

PyObject *DeriveKeySalted(PyObject *self, PyObject *args) {
    PyObject *ss_bytes;
    PyObject *salt_bytes;
    PyObject *context_bytes;
    if (!PyArg_ParseTuple(args, "OOO", &ss_bytes, &salt_bytes, &context_bytes)) {
        INV_ARGS;
    }
    unsigned char *ss = (unsigned char*)PyBytes_AsString(ss_bytes);
    unsigned char *salt = (unsigned char*)PyBytes_AsString(salt_bytes);
    unsigned char *context = (unsigned char*)PyBytes_AsString(context_bytes);
    unsigned char derived[crypto_generichash_blake2b_BYTES];
    crypto_generichash_blake2b_salt_personal(
        derived, crypto_generichash_blake2b_BYTES, 
        ss, crypto_scalarmult_curve25519_BYTES, 
        NULL, 0, salt, context);
    return PyBytes_FromStringAndSize((char*)derived, crypto_generichash_blake2b_BYTES);
}

PyObject *NewMACContext(PyObject *self, PyObject *args) {
    PyObject *secret_bytes;
    if (!PyArg_ParseTuple(args, "O", &secret_bytes)) {
        INV_ARGS;
    }
    unsigned char* secret = (unsigned char*)PyBytes_AsString(secret_bytes);
    crypto_generichash_blake2b_state state;
    crypto_generichash_blake2b_init(
        &state, (unsigned char*)secret, 
        crypto_generichash_blake2b_KEYBYTES, crypto_generichash_blake2b_BYTES);
    return PyCapsule_New(&state, NULL, NULL);
}

PyObject *UpdateMACContext(PyObject *self, PyObject *args) {
    PyObject *context_cap;
    PyObject *msg_bytes;
    if (!PyArg_ParseTuple(args, "OO", &context_cap, &msg_bytes)) {
        INV_ARGS;
    }
    crypto_generichash_blake2b_state *state = PyCapsule_GetPointer(context_cap, NULL);
    long len;
    char* msg;
    PyBytes_AsStringAndSize(msg_bytes, &msg, &len);
    crypto_generichash_blake2b_update(state, (unsigned char*)msg, len);
    Py_RETURN_NONE;
}

PyObject *FinalMACContext(PyObject *self, PyObject *args) {
    PyObject *context_cap;
    if (!PyArg_ParseTuple(args, "O", &context_cap)) {
        INV_ARGS;
    }
    crypto_generichash_blake2b_state *state = PyCapsule_GetPointer(context_cap, NULL);
    unsigned char mac[crypto_generichash_blake2b_BYTES];
    crypto_generichash_blake2b_final(state, mac, crypto_generichash_blake2b_BYTES);
    return PyBytes_FromStringAndSize((char*)mac, crypto_generichash_blake2b_BYTES);
}

PyObject *AEADEncrypt(PyObject *self, PyObject *args) {
    PyObject *secret_bytes;
    PyObject *nonce_bytes;
    PyObject *msg_bytes;
    if (!PyArg_ParseTuple(args, "OOO", &secret_bytes, &nonce_bytes, &msg_bytes)) {
        INV_ARGS;
    }
    unsigned char *secret = (unsigned char*)PyBytes_AsString(secret_bytes);
    unsigned char *nonce = (unsigned char*)PyBytes_AsString(nonce_bytes);
    long len;
    char *msg;
    PyBytes_AsStringAndSize(msg_bytes, &msg, &len);
    unsigned char *ciphertext = malloc(len+crypto_secretbox_xchacha20poly1305_MACBYTES);
    crypto_secretbox_xchacha20poly1305_easy(ciphertext, (unsigned char*)msg, len, nonce, secret);
    return PyBytes_FromStringAndSize((char*)ciphertext, len+crypto_secretbox_xchacha20poly1305_MACBYTES);
}

PyObject *AEADDecrypt(PyObject *self, PyObject *args) {
    PyObject *secret_bytes;
    PyObject *nonce_bytes;
    PyObject *ciphertext_bytes;
    if (!PyArg_ParseTuple(args, "OOO", &secret_bytes, &nonce_bytes, &ciphertext_bytes)) {
        INV_ARGS;
    }
    unsigned char *secret = (unsigned char*)PyBytes_AsString(secret_bytes);
    unsigned char *nonce = (unsigned char*)PyBytes_AsString(nonce_bytes);
    long len;
    char *ciphertext;
    PyBytes_AsStringAndSize(ciphertext_bytes, &ciphertext, &len);
    unsigned char *msg = malloc(len-crypto_secretbox_xchacha20poly1305_MACBYTES);
    if (crypto_secretbox_xchacha20poly1305_open_easy(msg, (unsigned char*)ciphertext, len, nonce, secret) != 0) {
        Py_RETURN_NONE;
    }
    return PyBytes_FromStringAndSize((char*)msg, len-crypto_secretbox_xchacha20poly1305_MACBYTES);
}

PyObject *StreamEncrypt(PyObject *self, PyObject *args) {
    PyObject *secret_bytes;
    PyObject *nonce_bytes;
    PyObject *msg_bytes;
    if (!PyArg_ParseTuple(args, "OOO", &secret_bytes, &nonce_bytes, &msg_bytes)) {
        INV_ARGS;
    }
    unsigned char *secret = (unsigned char*)PyBytes_AsString(secret_bytes);
    unsigned char *nonce = (unsigned char*)PyBytes_AsString(nonce_bytes);
    long len;
    char *msg;
    PyBytes_AsStringAndSize(msg_bytes, &msg, &len);
    unsigned char *ciphertext = malloc(len);
    crypto_stream_xsalsa20_xor(ciphertext, (unsigned char*)msg, len, nonce, secret);
    return PyBytes_FromStringAndSize((char*)ciphertext, len);
}

PyObject *StreamDecrypt(PyObject *self, PyObject *args) {
    PyObject *secret_bytes;
    PyObject *nonce_bytes;
    PyObject *ciphertext_bytes;
    if (!PyArg_ParseTuple(args, "OOO", &secret_bytes, &nonce_bytes, &ciphertext_bytes)) {
        INV_ARGS;
    }
    unsigned char *secret = (unsigned char*)PyBytes_AsString(secret_bytes);
    unsigned char *nonce = (unsigned char*)PyBytes_AsString(nonce_bytes);
    long len;
    char *ciphertext;
    PyBytes_AsStringAndSize(ciphertext_bytes, &ciphertext, &len);
    unsigned char *msg = malloc(len);
    crypto_stream_xsalsa20_xor(msg, (unsigned char*)ciphertext, len, nonce, secret);
    return PyBytes_FromStringAndSize((char*)msg, len);
}

PyObject *DerivePassword(PyObject *self, PyObject *args) {
    PyObject *passwd_bytes;
    PyObject *salt_bytes;
    int keylen;
    if (!PyArg_ParseTuple(args, "OOi", &passwd_bytes, &salt_bytes, &keylen)) {
        INV_ARGS;
    }
    unsigned char *salt = (unsigned char*)PyBytes_AsString(salt_bytes);
    long len;
    char *passwd;
    PyBytes_AsStringAndSize(passwd_bytes, &passwd, &len);
    unsigned char* key = malloc(keylen);
    if (crypto_pwhash_scryptsalsa208sha256(key, keylen, passwd, len, salt, 
        crypto_pwhash_scryptsalsa208sha256_OPSLIMIT_INTERACTIVE,
        crypto_pwhash_scryptsalsa208sha256_MEMLIMIT_INTERACTIVE) != 0) {
        PyErr_SetString(PyExc_ValueError, "failed to derive");
        return NULL;
    }
    return PyBytes_FromStringAndSize((char*)key, keylen);
}

PyObject *StorePassword(PyObject *self, PyObject *args) {
    PyObject *passwd_bytes;
    if (!PyArg_ParseTuple(args, "O", &passwd_bytes)) {
        INV_ARGS;
    }
    long len;
    char *passwd;
    PyBytes_AsStringAndSize(passwd_bytes, &passwd, &len);
    char hash[crypto_pwhash_argon2id_STRBYTES];
    if (crypto_pwhash_argon2id_str(hash, passwd, len,
        crypto_pwhash_argon2id_OPSLIMIT_INTERACTIVE,
        crypto_pwhash_argon2id_MEMLIMIT_INTERACTIVE) != 0) {
        PyErr_SetString(PyExc_ValueError, "failed to derive");
        return NULL;
    }
    return PyUnicode_FromString(hash);
}

PyObject *VerifyPassword(PyObject *self, PyObject *args) {
    PyObject *passwd_bytes;
    char* hash_str;
    if (!PyArg_ParseTuple(args, "Os", &passwd_bytes, &hash_str)) {
        INV_ARGS;
    }
    long passwd_len;
    char *passwd;
    PyBytes_AsStringAndSize(passwd_bytes, &passwd, &passwd_len);
    if (crypto_pwhash_argon2id_str_verify(hash_str, passwd, passwd_len) != 0) {
        Py_RETURN_FALSE;
    }
    Py_RETURN_TRUE;
}

PyObject *FixedHash(PyObject *self, PyObject *args) {
    PyObject *msg_bytes;
    if (!PyArg_ParseTuple(args, "O", &msg_bytes)) {
        INV_ARGS;
    }
    long len;
    char *msg;
    PyBytes_AsStringAndSize(msg_bytes, &msg, &len);
    unsigned char hash[crypto_generichash_blake2b_BYTES];
    crypto_generichash_blake2b(hash, crypto_generichash_blake2b_BYTES, (unsigned char*)msg, len, NULL, 0);
    return PyBytes_FromStringAndSize((char*)hash, crypto_generichash_blake2b_BYTES);
}

PyMethodDef ChloryneMethods[] = {
    { "init_sodium", InitSodium, METH_NOARGS, NULL },
    { "generate_key", GenerateKey, METH_NOARGS, NULL },
    { "public_sign_key", PublicSignKey, METH_VARARGS, NULL },
    { "public_x_key", PublicXKey, METH_VARARGS, NULL },
    { "convert_private_key", ConvertPrivateKey, METH_VARARGS, NULL },
    { "convert_public_key", ConvertPublicKey, METH_VARARGS, NULL },
    { "sign", Sign, METH_VARARGS, NULL },
    { "verify", Verify, METH_VARARGS, NULL },
    { "new_sign_context", NewSignContext, METH_NOARGS, NULL },
    { "update_sign_context", UpdateSignContext, METH_VARARGS, NULL },
    { "sign_sign_context", SignSignContext, METH_VARARGS, NULL },
    { "verify_sign_context", VerifySignContext, METH_VARARGS, NULL },
    { "compute_secret", ComputeSecret, METH_VARARGS, NULL },
    { "derive_key_plain", DeriveKeyPlain, METH_VARARGS, NULL },
    { "derive_key_salted", DeriveKeySalted, METH_VARARGS, NULL },
    { "new_mac_context", NewMACContext, METH_VARARGS, NULL },
    { "update_mac_context", UpdateMACContext, METH_VARARGS, NULL },
    { "final_mac_context", FinalMACContext, METH_VARARGS, NULL },
    { "aead_encrypt", AEADEncrypt, METH_VARARGS, NULL },
    { "aead_decrypt", AEADDecrypt, METH_VARARGS, NULL },
    { "stream_encrypt", StreamEncrypt, METH_VARARGS, NULL },
    { "stream_decrypt", StreamDecrypt, METH_VARARGS, NULL },
    { "derive_password", DerivePassword, METH_VARARGS, NULL },
    { "store_password", StorePassword, METH_VARARGS, NULL },
    { "verify_password", VerifyPassword, METH_VARARGS, NULL },
    { "fixed_hash", FixedHash, METH_VARARGS, NULL },
    { NULL, NULL, 0, NULL }
};

PyModuleDef ChloryneModule = {
    PyModuleDef_HEAD_INIT,
    "_chloryne",
    NULL,
    -1,
    ChloryneMethods
};

PyMODINIT_FUNC PyInit__chloryne() {
    return PyModule_Create(&ChloryneModule);
}