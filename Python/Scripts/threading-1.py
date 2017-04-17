# -*- coding: cp936 -*-
import threading
import time
import sys
globals_num = 0
##lock = threading.Lock()
def Func():
##    lock.acquire() # 获得锁
    global globals_num
    globals_num += 1
    globals_num += 1
    sys.stdout.write("%d\n" %globals_num)
##    lock.release() # 释放锁
    
for i in range(10):
    t = threading.Thread(target=Func)
    t.start()
