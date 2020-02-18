#!/usr/bin/env python3
# script: encrypt data
# author: Trader1 <hello@trader.co>
# notes: 

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA512
import base64

import os
os.system('clear')

# public key
public_key = """-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAkYVtN8avbzVYar1zwQkC
VbHgdCz11SEz88Qix4J3s/pavnQnObIIxfynYwrk1Zp0eUfAfoPqwO6EaAS2ijo8
/qrivQiOrEGc7fvM+h7k0xrIelu8hiGEr74Tj5uSVikLVCrDp9ztJXv3Kmc955b6
eLi08eM9xVvphoFqyCOX9d22d2hQV0CfRilvAO/CU2+aqapcGft2M740HZjbluEZ
B1Z5zKsDwccRtbL//ECBZkl+jK13YsyarYE20AJt4irSNSJb/JLXmP48xpYls95B
gPK1n04rttFh8WHOQA0Ep0p7CEZG6SRGiI6AKNOvuz8mLZmx24F0lxmDYkjaeVM6
SyUnqoNKnT5/mnXaAxn3+DtZADrC+BX89EmCK8YkYikKWvZ26ohG1jg/mGTKalo5
oOrPmbDu6Q+RCsfDktPOYaPjBO/cO48NCrnevaNnQXcUcPqgXsLVvfhZWj944bVR
RwtaqjYyw5ay7XIxYmFDKXX8UKxcWSFTbBtgmcV+rYE7GjepAQOgDk/wCjvDQZ64
DV40sdg9d2hNmXkb2/SbxiZLjJH8f1obmJMLLaoE0YaN2vrQJWFV2uIz5YPwxHeU
yqAfJwoV4QWHv8d6VgayQY+eWEGQirLTQEBuXpVlH++Sua/2+4K5WdhMDgKmbW0A
M+EcAGPQWXgg6SgRfNtmRrsCAwEAAQ==
-----END PUBLIC KEY-----"""

# get user data
print('~~~ Encrypt your keys for Trader1 ~~~')
raw_apikey = raw_input('Enter your APIKEY: ').encode()
raw_secret = raw_input('Enter your SECRET: ').encode()

# crypt
encrypt_public_key = RSA.importKey(public_key)
cipher = PKCS1_OAEP.new(encrypt_public_key, hashAlgo=SHA512)

enc_apikey_encoded = base64.b64encode(cipher.encrypt(raw_apikey)).decode("ASCII")
enc_secret_encoded = base64.b64encode(cipher.encrypt(raw_secret)).decode("ASCII")

os.system('clear')
print('~~~ Your encrypted keys for Trader1 ~~~\n')

print('Your APIKEY:\n')
print(enc_apikey_encoded)

print('\n\nYour SECRET:\n')
print(enc_secret_encoded)

print('\nCopy the encrypted credentials to https://app.trader1.co when adding the Exchange.\n')
