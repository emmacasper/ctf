#!/usr/bin/python

import socket

csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
csock.connect(('18.218.238.95', 12345))

data = ''
while len(data) < 106:
    data += csock.recv(106 - len(data))
print(data)

print('****')

def padleft(s):
    return (31 - len(s)) * '^' + s

def make_guess(s):
    data = ''
    while len(data) < 24:
        data += csock.recv(24 - len(data))
    csock.send(s + '\n')
    #print(data)
    data = ''
    while len(data) < 28:
        data += csock.recv(28 - len(data))
    #print(data)
    data = ''
    while len(data) < 128:
        data += csock.recv(128 - len(data))
    #print(data)
    return data[:64]


def guess_letter(rest):
    r = '^' * (31 - len(rest))
    goal = make_guess(r)
    print("goal: %s" % goal)
    print("rest: %s" % rest)
    r += rest
    for i in range(32,127):
        #if make_guess(rest + chr(i)) == goal:
        guess = make_guess(r + chr(i))
        #print("guessing %s: %s" % (rest + chr(i) ,guess))
        if guess == goal:
            #print(chr(i))
            print('got answer on %dth roundL %s' %(i, chr(i)))
            return chr(i)
    print("aaaaaaaaaaaa")
    print(rest)

#print(guess_letter(padleft('')))

#flag = "TUCTF{"
flag = 'TUCTF{'
while len(flag) < 31:
    let = guess_letter(flag)
    print("%s, %s" %(flag, let))
    flag += let
print(flag)



