#!/usr/bin/python

import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1235))

mySocket.listen(5)

try:
    while True:
        print 'Esperando conexiones'
        (recvSocket, address) = mySocket.accept()
        print 'HTTP request received:'
        direccion_aleat = random.randint(0, 10000000)
        print recvSocket.recv(1024)
        recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                        "<html><body><h1>Hello World!" +
                        "</h1></body></html>" +
                        '<a href=' + str(direccion_aleat) +
                        '>Dame otra </a>' +
                        "\r\n")
        recvSocket.close()
except KeyboardInterrupt:
    print "Closing binded socket"
    mySocket.close()
