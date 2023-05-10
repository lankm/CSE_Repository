# README
#
# Author: Landon Moon
# ID: 1001906270

import os
import socket
import threading
import sys
# functions ===================================================================

# connection thread
def handle_connection(conn):
  # parse headers
  request = conn.recv(1024).decode('utf-8')
  headers = request.split("\r\n")
  page = headers[0].split(" ")[1]

  # output to terminal
  print("Request: \""+headers[0]+"\"")
  # output to log file
  log.write(request.replace("\r\n","\n"))
  log.flush()

  #determining requested webpage
  if page=="/":
    page = "/index.html"
  try:
    # try to open the file.
    page = open("sample_pages"+page, "r")

    # if file exitst, send OK and send file
    # file is read as binary so no encoding is needed
    conn.send(("HTTP/1.1 200 OK\r\n\r\n").encode() + page.read().encode())
    print("Response: \"HTTP/1.1 200 OK\"\n")
  # if the file can not be open
  except FileNotFoundError:
    conn.send(("HTTP/1.1 404 Not Found\r\n").encode())
    print("Response: \"HTTP/1.1 404 Not Found\"\n")

  # Close the socket after request has been handled
  conn.close()

# thread made for listening for new connections
def listening_thread():
  conn, addr = serverSocket.accept()

  # make new listening_thread
  Lthread = threading.Thread(target=listening_thread, args=())
  Lthread.start()

  #listing connection parameters
  print("Connection Parameters:")
  print("  Family: %s" %serverSocket.family)
  print("  Type: %s" %serverSocket.type)
  print("  Protocol: %s" %serverSocket.proto)
  print("  Timeout: %s" %serverSocket.timeout)

  # send connection to new thread
  Cthread = threading.Thread(target=handle_connection, args=(conn,))
  Cthread.start()
# thread made to exit server from server side
def admin_thread():
  while True:
    # get input
    u_in = input("Enter 'exit' to stop the server.\n\n")
    if u_in=="exit":
      log.close()
      os._exit(1)
# main ========================================================================

#argument handling
n = len(sys.argv)
port = 8080 
if n>1: port=int(sys.argv[1])

# serverSocket setup
try:
  serverSocket = socket.socket()

  # Binding
  serverSocket.bind(('', port))
  print("Socket bound to %d" %port)

  # Listening
  serverSocket.listen()
  print("Server listening...")
except socket.error:
  print("Error creating the socket. Exiting.")
  exit()

# opening log file
log = open("server_log.txt", "a")

# make a thread to be able to exit server
Athread = threading.Thread(target=admin_thread, args=())
Athread.start()

# start listening. This starts recursive multithreading
listening_thread()
