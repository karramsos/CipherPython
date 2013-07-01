#!/usr/bin/env python3
# Reverse Chiper
# http://inventwithpython.com/hacking (BSD Licensed)
# Sukhvinder Singh | karramsos@gmail.com | @karramsos

message = input('Enter message:')
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    print(i, message[i], translated)
    i = i - 1

print(translated)

message1 = input('Enter message2:')
translated1 = ''

i = len(message1) - 1
while i >= 0:
    translated1 = translated1 + message1[i]
    print(i, message1[i], translated1)
    i = i - 1

print(translated1)

