#!/usr/bin/env python3
# The Caesar Cipher
# Note that first you will need to download the pyperclip.py module and
# place this file in the same directory (that is, folder) as the caesarCipher.py file.

# http://inventwithpython.com/hacking (BSD Licensed)
# Sukhvinder Singh | karramsos@gmail.com | @karramsos

import pyperclip

# the string to be encrypted/decrypted
message = 'GUVF VF ZL FRPERG ZRFFNTR.'

# the encryption/decryption key
key = 13

# tells the program to encrypt or decrypt
mode = 'decrypt' # set to 'encrypt' or 'decrypt'

# every possible symbol that can be encrypted
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# stores the encrypted/decrypted form of the message
translated = ''

# capitalize the string in message
message = message.upper()

# run the encryption/decryption code on each symbol in the message string
for symbol in message:
    if symbol in LETTERS:
        # get the encrypted/decrypted number for this symbol
        num = LETTERS.find(symbol) # get the numbor of the symbol
        if mode == 'encrypt':
            num += key
        elif mode == 'decrypt':
            num += key
        
        # handle the wrap-around if num is larger than the length of
        # LETTERS or less than 0
        if num >= len(LETTERS):
            num -= len(LETTERS)
        elif num < 0:
            num += len(LETTERS)
        
        # add encrypted /decrypted number's symbol at the end of translated
        translated = translated + LETTERS[num]
        
    else:
        # just add the symbol without encrypting/decrypting
        translated += symbol

# print the encrypted/decrypted string to the screen
print(translated)

# copy the encrypted/decrypted string to the clipboard
pyperclip.copy(translated)

    

