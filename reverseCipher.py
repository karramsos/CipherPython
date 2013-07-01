# Reverse Chiper
# http://inventwithpython.com/hacking (BSD Licensed)
# Sukhvinder Singh | karramsos@gmail.com | @karramsos

message = '.daed era meht fo owt fi ,terces a peek nac eerhT'
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)

message1 = 'Three can keep a secret, if two of them are dead.'
translated1 = ''

i = len(message1) - 1
while i >= 0:
    translated1 = translated1 + message1[i]
    i = i - 1

print(translated1)
