import threading
import time
def sample():
    for i in range(10):
        obj2=threading.Thread(target=example)  
        obj2.start()
def example():
    for j in range(10):
        print(j ,"hello python code", time.ctime())