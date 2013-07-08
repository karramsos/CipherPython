#!/usr/bin/env python3
# Transposition Cipher Encryption
# Note that first you will need to download the pyperclip.py module and
# place this file in the same directory (that is, folder) as the caesarCipher.py file.

# http://inventwithpython.com/hacking (BSD Licensed)
# Sukhvinder Singh | karramsos@gmail.com | @karramsos

import pyperclip

def main():
    myMessage = 'Common sense is not so common.'
    myKey = 14
    
    ciphertext = encryptMessage(myKey, myMessage)
    
    # Print the encrypted string in ciphertext to the screen, with
    # a | (called "pipe" character) after it in case there are spaces at
    # the end of the encrypted message.
    print(ciphertext + '|')
    
    # Copy the encrypted string in ciphertext to the clipboard.
    pyperclip.copy(ciphertext)
    
def encryptMessage(key, message):
    # Each string in ciphertext represents a column in the grid.
    ciphertext = [''] * key
    
    # Lopp through each column in ciphertext.
    for col in range(key):
        pointer = col
        
        # Keep looping until pointer gets past the length of the message.
        while pointer < len(message):
            # Place the character at pointer in message at the end of the
            # current column in the ciphertext list.
            ciphertext[col] += message[pointer]
            
            # move poimnter over
            pointer += key 
    # Convert the ciphertext list into a single string value and return it.
    return ''.join(ciphertext)

# If transpositionEncrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()
            
            
    
