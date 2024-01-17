# README
#
# Author: Landon Moon
# ID: 1001906270

import socket
from time import *
import sys
import time
# functions ===================================================================

# main ========================================================================

#argument handling
n = len(sys.argv)
ip = '127.0.0.1'
port = 8080
filename = 'index.html'
if n>1: ip=sys.argv[1]
if n>2: port=int(sys.argv[2])
if n>3: filename=sys.argv[3]

# connect to local host
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', port))

#displaying 4 connection parameters
print("Connection Parameters:")
print("  Family: %s" %s.family)
print("  Type: %s" %s.type)
print("  Protocol: %s" %s.proto)
print("  Timeout: %s" %s.timeout)

# send a GET request
if filename=='/':
  filename='index.html'
s.send(("GET /"+filename+" HTTP/1.1\r\n\r\n").encode())
print("Request: \"GET /"+filename+" HTTP/1.1\"")
sendTime = time.time()*1000

# retrieve headers and file. Also get time
response = s.recv(1024).decode('utf-8')
recieveTime = time.time()*1000
headers = response.split("\r\n")
HTMLcode = headers[0].split(" ")[1]

# output OK/FNF
print("Response: \""+headers[0]+"\"")
print("RTT: %dms" %(recieveTime-sendTime))

# if OK, save file
if HTMLcode=='200':
  file = open(filename, "w")
  print("saving to file...")
  file.write(headers[2])
  print("Complete.")
