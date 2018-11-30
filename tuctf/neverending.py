#!/usr/bin/env python
import socket

csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
csock.connect(('18.223.156.26', 12345))

morse_alphabet = [('.-', 'A'), ('-...', 'B'), ('-.-.', 'C'),
        ('-..', 'D'), ('.', 'E'), ('..-.', 'F'), ('--.', 'G'), ('....', 'H'),
        ('..', 'I'), ('.---', 'J'), ('-.-', 'K'), ('.-..', 'L'), ('--', 'M'),
        ('-.', 'N'), ('---', 'O'), ('.--.', 'P'), ('--.-', 'Q'),
        ('.-.', 'R'), ('...', 'S'), ('-', 'T'), ('..-', 'U'),
        ('...-', 'V'), ('.--', 'W'), ('-..-', 'X'), ('-.--', 'Y'), ('--..', 'Z')]

def flipper(s):
    return ''.join(['-' if m == '.' else '.' for m in s])

m2a = {}
a2m = {}
fm2a = {}
for (m, a) in morse_alphabet:
    m2a[m] = a
    a2m[a] = m
    fm2a[flipper(m)] = a

def decrypt(s):
    return ''.join([m2a[x] for x in s])

def encrypt(s):
    return [a2m[x] for x in s]

print('starting!')

data = ""
while len(data) < 104:
    data += csock.recv(104 - len(data))
#print(data)

csock.send('e\n')
data = ""
while len(data) < 18:
    data += csock.recv(18 - len(data))
#print(data)

def do_stage(f):
    data = ""
    while '\n' not in data:
        data += csock.recv(10)
    #print(data)
    lets = data.split()[1:]
    #print(lets)
    ans = f(lets)
    #print('answer: %s' % ans)
    csock.send(ans + '\n')

    data = ''
    while '\n\n' not in data:
        data += csock.recv(1)
    #print(data)

def do_decryption():
    data = ""
    while '\n' not in data:
        data += csock.recv(10)
    #print(data)
    lets = data.split()[1:]
    #print(lets)
    ans = decrypt(lets)
    #print('answer: %s' % ans)
    csock.send(ans + '\n')

    data = ''
    while '\n\n' not in data:
        data += csock.recv(1)
    #print(data)

for i in range(50):
    do_stage(lambda x: decrypt(x))
print("finished level 0")
print(csock.recv(100))

# level two!!!

print("beginning level 2!")

def rot13(s):
    lets = [chr(ord(c) + (13 if c < 'N' else - 13)) for c in s]
    return ''.join(lets)

def part1():
    data = ""
    while '\n' not in data:
        data += csock.recv(10)
        #print(data)
    lets = data.split()[1:]
#    print(lets)
    ans = rot13(decrypt(lets))
    print(ans)
    csock.send(ans + '\n')
    data = ''
    while '\n\n' not in data:
        data += csock.recv(1)
#    print(data)

csock.send('abcdefghijklmnopqrstuvwxyz\n')
data = ''
while '\n\n' not in data:
    data += csock.recv(1)
print(data)
print('got to first decryption')
for i in range(50):
#    print('part %d' % i)
    do_stage(lambda x: rot13(decrypt(x)))
print(csock.recv(100))
csock.send('abcdefghijklmnopqrstuvwxyz\n')

print('level 2!!!!!!')

def flipper_translate(m):
    return ''.join(fm2a[x] for x in m)

data = ''
while '\n\n' not in data:
    data += csock.recv(1)
for i in range(50):
    do_stage(flipper_translate)
print(csock.recv(200))
csock.send('abcdefghijklmnopqrstuvwxyz\n')

def level3(s):
    scrambled = 'ADGJMPSVYBEHKNQTWZCFILORUX'
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join([alpha[scrambled.find(x)] for x in s])

print('level 3!')
data = ''
while '\n\n' not in data:
    data += csock.recv(1)
print(data)
#for i in range(1):
#    do_stage(lambda x: level3(decrypt(x)))
#print(csock.recv(100))
#csock.send('abcdefghijklmnopqrstuvwxyz\n')
#print(csock.recv(300))

def yay():
    data = ""
    while '\n' not in data:
        data += csock.recv(10)
        #print(data)
    print(data)
    lets = data.split()[1:]
    print(lets)
    ans = level3(decrypt(lets))
    print(ans)
    csock.send(ans + '\n')
    data = ''
    while '\n\n' not in data:
        data += csock.recv(1)
    print(data)
for i in range(5):
    yay()
print(csock.recv(100))

