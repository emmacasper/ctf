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
    clientsocket.send(num+"\n")
    data = ""
    while len(data) < 262:
        data += clientsocket.recv(262 - len(data))
    return data[16:92] + data[93:105]

data = ""
while len(data) < 242:
    data += clientsocket.recv(242)

#print("got", len(data), "characters")
#print(data)

ans = ""

for j in range(64, 62, -1): #64
    k = 63
    charans = 0
    for i in range(8):
        num = hex(2**i)[2:] + '0'*(j*2)
        choose_operand("XOR")
        print("exp is:", num)
        xtext = get_answer(num)
        choose_operand("ADD")
        atext = get_answer(num)
        #print(xtext)
        #print(atext)
        if xtext != atext:
            #print("not equal: bit  is 1")
            charans += 2**i
        #print(charans)
    ans = chr(charans) + ans
    print("got char:", chr(charans))
print(ans)

