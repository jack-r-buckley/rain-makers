import socket
import serverconfig as sc

class Network:
  def __init__(self):
    self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server = sc.Server_Config.SERVER.value
    self.port = sc.Server_Config.PORT.value
    self.addr = (self.server, self.port)
    self.id = self.connect()
    print(self.id)

  def connect(self):
    try:
      self.client.connect(self.addr)
      return self.client.recv(2048).decode()
    except:
      pass

n = Network()