# -*- coding: cp936 -*-
import threading
import time
import sys
globals_num = 0
##lock = threading.Lock()
def Func():
##    lock.acquire() # �����
    global globals_num
    globals_num += 1
    globals_num += 1
    sys.stdout.write("%d\n" %globals_num)
##    lock.release() # �ͷ���
    
for i in range(10):
    t = threading.Thread(target=Func)
    t.start()
