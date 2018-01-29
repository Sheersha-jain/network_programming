#SERVER CODE
"""
This code opens the web server at port 62. 
In a second screen, open a client with Telnet. If we use 
the same machine for the client and server :

$ telnet 127.0.0.1 62.

If we use another machine as client, we need to type the according 
IP address of that machine which can be find using ifconfig.

Everything we write from the client will arrive at the server.
The server sends the received messages back.
"""


#!/usr/bin/env python
 
import socket
 
TCP_IP = '127.0.0.1'
TCP_PORT = 62
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
 
conn, addr = s.accept()
print 'Connection address:', addr
while 1:
     data = conn.recv(BUFFER_SIZE)
     if not data: break
     print "received data:", data
     conn.send(data)  # echo
conn.close()
