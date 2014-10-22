#!/user/bin/env python
#coding=utf-8

'''
Created on 2014-9-12

python 2.7 for window

@auther: Eastsheen

QQ:393857608

'''

import threading
import datetime
import time
import AppPertest

class ThreadClass(threading.Thread):
    """启动线程时时获取Memery Cpu 信息"""
    def __init__(self,num):
        threading.Thread.__init__(self)
        global mutex
        mutex = threading.Lock()
        self._run_num = num
        self.myApp = AppPertest.appPerTest()
        self.fileOjbect = self.myApp.getfileOjbect('meminfo.txt', 'w')
        self.meminfo = 'adb shell dumpsys meminfo ctrip.android.view'
    def run(self):
        threadname = threading.currentThread().getName()
        self.count = 0
        
        for x in xrange(0,int(self._run_num)):
            mutex.acquire()
            self.count += 1
            self.myApp.getDumpsysMeminfo(self.meminfo, 'TOTAL', self.fileOjbect)
            mutex.release()
            print 'name:%s x:%s count:%s \n' % (threadname,x,self.count)
            time.sleep(1)
            
            
#if __name__=='__main__':
    #global count,mutex
    #threads = []
    #num = 5
    #count = 0
    
    #mutex = threading.Lock()
    
    #for x in xrange(0,num):
        #threads.append(ThreadClass(num))
        
    #for t in threads:
        #t.start()
    
    #for t in threads:
        #t.join()