#!/usr/bin/env python3
# Excercise 10A
# Note that first you will need to download the pyperclip.py module and
# place this file in the same directory (that is, folder) as the caesarCipher.py file.

# http://inventwithpython.com/hacking (BSD Licensed)
# Sukhvinder Singh | karramsos@gmail.com | @karramsos


    # If you ran this program and it printed the number 7, what would it print the next time you run it?

import random
random.seed(9)
print(random.randint(1, 10))

    # What does this program print out?

spam = [1, 2, 3]
eggs = spam
ham = eggs
ham[0] = 99
print(ham == spam)


    # What does this program print out?

import copy
spam = [1, 2, 3]
eggs = copy.deepcopy(spam)
ham = copy.deepcopy(eggs)
ham[0] = 99
print(ham == spam)


