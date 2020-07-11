import socket 
import threading 
import json
from . import pdbadmin
import time
# import json
class data:
    def __init__(self,typep,reqstr,id=None):
        self.type=typep
        # if reqstr is not None:
        self.code=reqstr
        if(id is None):
            self.id=hash(reqstr+str(time.time()))%(10**5)
        else:
            self.id=id
        # self.query=query
    def json(self):
        if self.type =="query":
            data={"type":self.type,"query":self.code,"id":self.id}
        else :
            data={"type":self.type,"code":self.code,"id":self.id}
        return json.dumps(data)
    def encode(self):
        return self.json().encode()

class daemon:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.server_socket.bind(('127.0.0.1', 12345)) ## 서버의 IP와 포트를 연결 
        self.server_socket.listen(0)   ## 서버의 포트를 LISTENING 상태로 변경 
        self.recv_thread = threading.Thread(target=self.recv_data) 
        self.recv_thread.daemon=True
        self.recv_thread.start() 
    def __del__(self):
        self.server_socket.close()
    def recv_data(self):
        try:
            client_socket, addr = self.server_socket.accept()
            while True:  # binary
                data = client_socket.recv(65535)
                res = pdbadmin.contr(data)
                client_socket.send(res)
        finally:
            client_socket.close() 
        # while True:
        #     try:
        #         client_socket, addr = server_socket.accept()
        #         while True: #binary
        #             data = client_socket.recv(65535) 
        #             res=pdbadmin.contr(data)
        #             client_socket.send(res)
        #     finally:
        #         client_socket.close() 
d=daemon()


