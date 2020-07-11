import queue
import socket 
import threading 

from subpdb import pdbwork


class worker:
    def __init__(self,code,hashid):
        self.code=code
        self.id=hashid
        self.pdb=pdbwork(code,hashid)       
    def query(self, qstr):
        self.pdb.input(qstr)
    def get(self):
        return self.pdb.getall()

    # def work(self):
        
        
# def get(strp):
#     workers.append(worker())
#     w=workers.get()
#     return w.wok(strp)