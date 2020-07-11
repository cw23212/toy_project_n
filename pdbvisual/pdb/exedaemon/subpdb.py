import subprocess
import os
import threading 
import queue
base=os.getcwd()+"\\var"
class pdbwork:
    def __init__(self,fname,code):
        self.filepath=base+fname
        self.file=file(self.filepath,code)
        self.sub=_start(self.filepath)
        self.que=queue.Queue()
        self.thr=_getpullthread(self.sub,self.que)
    def __del__(self):
        os.remove(self.filepath)
    def getall(self):
        li=[]
        while not self.que.empty():
            li.append(self.que.get())
        return li
    def input(self,message):
        self.sub.stdin.write(f"{message.strip()}\n".encode("utf-8"))
        self.sub.stdin.flush()
def _start(executable_file):
    return subprocess.Popen(
        "python -m pdb "+executable_file,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=1
    )
def _getpullthread(subp,que):
    recv_thread = threading.Thread(target=_pullthread,args=(que,subp)) 
    recv_thread.daemon=True
    recv_thread.start()
    return recv_thread
def _pullthread(que,subp):
    while True:
        line = subp.stdout.readline()
        que.put(line)

def file(filepath,code):
    f=open(filepath,"w")
    f.write(code)