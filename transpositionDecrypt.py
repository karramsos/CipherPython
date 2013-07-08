#!/usr/bin/env python3
# Transposition Cipher Decryption
# Note that first you will need to download the pyperclip.py module and
# place this file in the same directory (that is, folder) as the caesarCipher.py file.

# http://inventwithpython.com/hacking (BSD Licensed)
# Sukhvinder Singh | karramsos@gmail.com | @karramsos

import math, pyperclip

def main():
    myMessage = 'Csno .mnmootn  ssoe ncsoem mio'
    myKey = 14
    
    plaintext = decryptMessage(myKey, myMessage)
    
    # Print with a | (called "pipe" character) after it in case
    # there are spaces at the end if the decrypted message.
    print(plaintext + '|')
    
    pyperclip.copy(plaintext)
    
def decryptMessage(key, message):
    # The transposition decrypt function will simmulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list
    # of strings. First, we need to calculate a few values.
    
    # The number of "columns" in our transposition grid:
    numOfColumns = math.ceil(len(message)/key)
    # The number of "rows" in our grid will need:
    numOfRows = key
    # The number of "shaded boxes" in the last "column" of the grid:
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    
    # Each string in a plaintext represents a column in the grid.
    plaintext = [''] * numOfColumns
    
    # The col and row variables point to where in the grid the next
    # character in the encrypted message will go.
    col = 0
    row = 0
    
    for symbol in message:
        plaintext[col] += symbol
        col += 1 # point to the next column
        
        # If there are no more columns OR we're at a shaded box, go back to
        # the first column and the next row
        if(col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1
    
    return ''.join(plaintext)

# If transpositionDecrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()
        
            
    



