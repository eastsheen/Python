#!/user/bin/env python
#coding=utf-8

import threading
import datetime
import time

class ThreadClass(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self._run_num = num
    def run(self):
        global count,mutex
        threadname = threading.currentThread().getName()
        
        for x in xrange(0,int(self._run_num)):
            mutex.acquire()
            count += 1
            mutex.release()
            print 'name:%s x:%s count:%s \n' % (threadname,x,count)
            time.sleep(1)
            
            
if __name__=='__main__':
    global count,mutex
    threads = []
    num = 5
    count = 0
    
    mutex = threading.Lock()
    
    for x in xrange(0,num):
        threads.append(ThreadClass(num))
        
    for t in threads:
        t.start()
    
    #for t in threads:
        #t.join()