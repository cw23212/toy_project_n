import socket
import json
class client:
    def __init__(self):
        self.client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(("127.0.0.1", 12345))
        # super().__init__()
    def __del__(self):
        self.client_socket.close()
    def send(self,data):
        self.client_socket.sendall(data.encode())
        data = self.client_socket.recv(65535)
        return data.decode("utf-8")
    def connect(self,port):
        self.client_socket.connect(("127.0.0.1", port))
    def idsconnect(self):
        self.client_socket.sendall("exit".encode())
c=client()
def query(query):
    global c
    return c.send(query)