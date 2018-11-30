#!/usr/bin/env python
import socket

#AF_INET for IPv4, SOCK_STREAM for TCP (as opposed to UDP).
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tell the socket what IP and port number to connect to (must be in two brackets because it needs a tuple).
clientsocket.connect(('arcade.fluxfingers.net', 1821))

def choose_operand(op):
    clientsocket.send(op+"\n")
    data = ""
    while len(data) < 37:
        data += clientsocket.recv(37-len(data))

def get_answer(num):
    clientsocket.send(hex(num)[2:]+"\n")
    data = ""
    while len(data) < 262:
        data += clientsocket.recv(262 - len(data))
    return data[16:92] + data[93:105]

data = ""
while len(data) < 242:
    data += clientsocket.recv(242)

print("got", len(data), "characters")
print(data)

ans = 0

r = 8*64 #64*8
for i in range(r):
    choose_operand("XOR")
    xtext = get_answer(2**i)
    choose_operand("ADD")
    atext = get_answer(2**i)
    #print(xtext)
    #print(atext)
    if xtext == atext:
        ans += 2**i
print(ans)

stringans = ""
while ans > 0:
    stringans = chr(ans%256) + stringans
    ans = ans // 256
print(stringans)

