#!/usr/bin/env python3
# Affine Key Test
# This program proves that the keyspace of the affine cipher is limited
# to len(SYMBOLS) ^ 2.
# Note that first you will need to download the pyperclip.py module and
# place this file in the same directory (that is, folder) as the caesarCipher.py file.

# http://inventwithpython.com/hacking (BSD Licensed)
# Sukhvinder Singh | karramsos@gmail.com | @karramsos

import affineCipher, cryptomath

message = 'Make things as simple as possible, but not simpler.'
for keyA in range(2,100):
    key = keyA * len(affineCipher.SYMBOLS) + 1
    
    if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) == 1:
        print(keyA, affineCipher.encryptMessage(key, message))
