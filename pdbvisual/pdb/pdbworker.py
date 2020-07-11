import os
from os import remove
from time import time
from .subpdb import subpdb

import os

class worker: # file, subprocess 관리
    def __init__(self,code):
        self.base=os.getcwd()+"\\var\\"
        self.id=str(hash(code+str(time()))%(10**5))
        self.filepath=self.base+str(self.id)
        self.file=fileadmin(self.filepath,code)
        self.sub=subpdb(self.filepath)
        self.time_s=time()
    # def __del__(self):
    # def query(self,query):
    #     self.time_s=time()
    #     self.sub.send(query)
    def query(self,query):
        self.time_s=time()
        reslist =self.sub.query(query)
        return reslist[0]
    def time(self):
        return (time()-self.time_s)
class fileadmin:
    def __init__(self,filepath,code):
        self.f=self.file(filepath,code)
        self.filepath=filepath
    def __del__(self):
        os.remove(self.filepath)
    def file(self,filepath,code):
        f=open(filepath,"w")
        f.write(code)
        f.close()
        return f
    def path(self):
        return self.filepath
    def fdel(self):
        os.remove(self.filepath)