import threading
from queue import Queue
# from model.image_model import execute
from model import sql
path_queue=Queue()
def thread_queu():
    global path_queue
    while True:
        get_path=path_queue.get()
        # img_res=execute.image_getNum(get_path['path'],get_path['location'])
        img_res="{'person':6,'place':'hakgwan_food','complexity':'High','time':'2020-07-02-03-21'}"
        # res=sql.update(get_path['location'],img_res['person'],img_res)
        res=sql.update(get_path['location'],1,img_res)
        print(img_res)
queue_thread = threading.Thread(target=thread_queu) 
queue_thread.daemon=True
queue_thread.start() 
def input_queue(img_path,location):
    global path_queue
    d_q={"path":img_path,"location":location}
    path_queue.put(d_q)
