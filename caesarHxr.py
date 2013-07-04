#!/usr/bin/env python3
# Caesar Cipher Hacker
# Note that first you will need to download the pyperclip.py module and
# place this file in the same directory (that is, folder) as the caesarCipher.py file.

# http://inventwithpython.com/hacking (BSD Licensed)
# Sukhvinder Singh | karramsos@gmail.com | @karramsos

message = 'auv!-v!-z\'-!rp r"-zr!!ntr;'
LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

# loop through every possible key
for key in range(len(LETTERS)):
    # It is important to set translated to the blank string so that the
    # previous iteration's value for translated is cleared.
    translated = ''
    
    
    # The rest of the program is the same as the origional Caesar program:
    # run the encryption/decryption code on each symbol in the message
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol) # get the number of the symbol
            num = num - key
            
            # handle the wrap-around if num is 26 or larger or less than 0
            if num < 0:
                num = num + len(LETTERS)
            
            # add number's symbol at the end of translated
            translated = translated + LETTERS[num]
            
        else:
            # just add the symbol without encrypting/derypting
            translated = translated + symbol
    
    # display the current key being tested, along with its decryption
    print('Key #%s: %s' %(key, translated))
                