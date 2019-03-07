import json
import pickle
import time
import rsa
import hashlib
import Crypto.Cipher.AES as aes
from Crypto.Util.Padding import pad, unpad


class Crypt:
    # Works
    def get_hash(self, btext):
        if str(type(btext)) == "<class 'str'>":
            btext = btext.encode()
        hash = hashlib.sha256(btext).hexdigest()
        return hash

    # Works
    def aes_encode(self, btext, key):
        if str(type(btext)) == "<class 'str'>":
            btext = btext.encode()

        if str(type(key)) == "<class 'str'>":
            key = key.encode()

        btext = pad(btext, 32)
        key = pad(key, 32)

        obj = aes.new(key, 1)
        cipher_text = obj.encrypt(btext)
        return cipher_text

    # Works
    def aes_decode(self, cipher_text, key):
        if str(type(cipher_text)) == "<class 'str'>":
            cipher_text = cipher_text.encode()

        if str(type(key)) == "<class 'str'>":
            key = key.encode()

        key = pad(key, 32)

        obj = aes.new(key, 1)
        btext = obj.decrypt(cipher_text)
        btext = unpad(btext, 32)
        return btext



