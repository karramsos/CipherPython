#!/usr/bin/env python3
# Transposition Cipher Encrypt/Decrypt File
# Note that first you will need to download the pyperclip.py module and
# place this file in the same directory (that is, folder) as the caesarCipher.py file.

# http://inventwithpython.com/hacking (BSD Licensed)
# Sukhvinder Singh | karramsos@gmail.com | @karramsos

import time, os, sys, transpositionEncrypt, transpositionDecrypt

def main():
    inputFilename = 'frankenstein.txt'
    # BE CAREFUL! If a file with the outputFilename name already exists,
    # this program will overwrite that file.
    outputFilename = 'frankenstein.encrypted.txt'
    myKey = 10
    myMode = 'encrypt' # set to 'encrypt' or 'decrypt'
    
    # If the input file does not exist, thrn the program terminates early.
    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quitting...' %(inputFilename))
        sys.exit()
    
    # If the output file already exists, give the user a chance to quit.
    print('This will overwrite the file %s. (C)ontinue or(Q)uit?'%(outputFilename))
    response = input('>')
    if not response.lower().startswith('c'):
        sys.exit()
    
    # Read in the message from the input file
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()
    
    print('%sing...' % (myMode.title()))
    
    # Measure how long thr encryption/decryption takes.
    startTime = time.time()
    if myMode == 'encrypt':
        translated = transpositionEncrypt.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = transpositionDecryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion time:%s seconds' %(myMode.title(), totalTime))
    
    # Write out the translated message to the output file.
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()
    
    print('Done %sing %s(%s characters).' % (myMode, inputFilename, len(content)))
    print('%sed file is %s.'%(myMode.title(),outputFilename))
    
# If transpositionCipherFile.py is run (instead of imported as a module)
# call the main() function

if __name__ == '__main__':
    main()
