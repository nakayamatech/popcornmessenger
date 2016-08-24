#!/usr/bin/python

import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))

s.listen(5)
while True:
  c, addr = s.accept()
  print 'Got connection from', addr
  c.send(raw_input('Let\'s start the bitchin\'\!'))
  print c.recv(100)
  c.close()
