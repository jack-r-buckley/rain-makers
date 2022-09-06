import socket
import serverconfig as sc
from _thread import *
import sys



print("Initialising socket.")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Binding server")
try:
  s.bind((sc.Server_Config.SERVER.value, sc.Server_Config.PORT.value))
except socket.error as e:
  str(e)

s.listen(2)
print(f"server is listening on port {sc.Server_Config.PORT.value}")

def threaded_client(conn):
  conn.send(str.encode("Connected"))
  reply=""
  while True:
    try:
      data=conn.recv(2048)
      reply=data = data.decode("utf-8")
      if not data:
        print("Disconnected")
        break
      conn.sendall(str.encode(reply))
    except:
      break


while True:
  conn, addr = s.accept()
  print(f"{addr} connected")

  start_new_thread(threaded_client, (conn,))