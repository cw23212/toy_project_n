import threading
import time
from .data import data
from .pdbworker import worker
li=[]


def contr(data):
    global li
    if data.type=="code":
        p=worker(data.code)
        li.append(p)
        return p.id
    elif data.type=="query":
        p=find(data.id)
        return p.query(data.query)
        
def find(id):
    global li
    for i in li:
        if i.id==id:
            return i


def check():
    global li
    time.sleep(1000)
    for i in li:
        if i.time()>10:
            r= li.index(i).pop()
            del r
check_thread = threading.Thread(target=check) 
check_thread.daemon=True
# check_thread.start() 
