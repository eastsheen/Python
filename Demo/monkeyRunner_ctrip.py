#!\usr\bin\env python
#coding=UTF-8

import os,sys
import codecs
import time
import thread
import threading
import xml.dom.minidom as minidom

from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By
from com.android.chimpchat.hierarchyviewer import HierarchyViewer
from xml.dom.minidom import Node


device = MonkeyRunner.waitForConnection()
easy_device = EasyMonkeyDevice(device)


class ctrip():
    def initDevice(self):
        device = MonkeyRunner.waitForConnection()
        if not device:
            print "Please connect a device"
        else:
            print "device connect success222"
        #easy_device = EsayMonkeyDevice(device)
        
    def installApk(self,path):
        print "  install..."
        print "path:"+path
        install = device.installPackage(path)
        time.sleep(2)
        if(install == True):
            print 'install success'
        else:
            print "fail"
            intstall
    
    def removeApk(self,packageName):
        remove = device.removePackage(packageName)
        if(remove == True):
            print "remove:" + packageName + " success"
        else:
            print "remove" + packageName + "fail"
            remove
    
    def startApk(self,packageName,startActivity):
        print "starting..."
        startProparm = device.startActivity(component=packageName+startActivity)
        if(startProparm==True):
            startProparm
        else:
            print "start apk success"
        time.sleep(3)
    
    def testSuite(self,fileName):
        time.sleep(5)
        myparserXml = parserXml(fileName)
        #easyUp = easy_device.touch(By.id('%s' % myparserXml.getparser('index','home_index_hotel'),MonkeyDevice.DOWN_AND_UP)
        easyUp = easy_device.touch(By.id('id/home_index_hotel'),MonkeyDevice.DOWN_AND_UP)
        time.sleep(3)
        easyUp = easy_device.touch(By.id('id/price_star_infobar'),MonkeyDevice.DOWN_AND_UP)
        time.sleep(3)
        easyUp = easy_device.touch(By.id('id/filter_select_ok_button'),MonkeyDevice.DOWN_AND_UP)
        time.sleep(3)
        #print easyUp
    
    def hotelSuite(self):
        time.sleep(5)
        print 'writeLog ......'
        #self.theadWriteLog()
        #self.writeLog()
        print 'run TestCase ...... '
        #首页酒店
        self.touchFunc('id/home_index_hotel',4)
        #self.writeLog()
        #touchFunc('id/check_in_city_infobar',3)
        self.touchFunc('id/search_button',5)
        self.touchFunc('id/hotel_name', 5)
        self.touchFunc('id/room_item_book', 3)
        #self.touchFunc('id/hotel_order_checkin_person', 3)
        #self.touchFunc('id/button_person_list_select', 3)
        self.touchFunc('id/submit', 3)
        self.touchFunc('@4353bea8', 3)
        time.sleep(4)
    
    def touchFunc(self,idName,sleepTime):
        time.sleep(sleepTime)
        easy_device.touch(By.id('%s' % idName),MonkeyDevice.DOWN_AND_UP)
        
    def writeLog(self):
        #os.system('adb logcat -s ctrip *:E > d:/log.txt')
        #os.system('adb logcat ActivityManager:I ctrip.android.view:D *:W > d:/log.txt')
        data = self.getSystemTime()
        fileName = data+'.txt'
        print fileName
        #os.system('adb logcat ctrip.android.view:D *:W > d:/%s' % fileName)
        #os.system('adb logcat ctrip.android.view:D *:W > d:/%s' % fileName)
        try:
            os.system('adb logcat -s ActivityManager:I ctrip.android.view:W dalvikvm > d:/log/%s' % fileName)
        except:
            print 'adb error'
        #adb logcat | find /N /I "ctrip.android.view"
        #os.system('adb logcat | find /N /I "ctrip.android.view" > d:/%s' % fileName)
      
    def getSystemTime(self):
        yearMD = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        hourMS = time.strftime('%H-%M-%S',time.localtime(time.time()))
        yearhour =  yearMD+'-'+hourMS
        return yearhour
       
    def deviceInfo(self):
        high = device.getProperty('display.height')
        width = device.getProperty('display.width')
        print 'high:'+ str(high)
        print 'width:'+ str(width)
        
    def theadWriteLog(self):
        try:
            thread.start_new_thread(writeLog, ('threadName',5,))
        except:
            print 'thread error'
        while 1:
            pass
        
    def killApp(self):
        os.system('adb shell ')

#挂起10秒
#MonkeyRunner.sleep(20)

#打印出logcat日志
#print logcat

#用shell执行monkey命令，随机点击2000次，有点类似压力或暴力测试
#device.shell('monkey -v -p ctrip.android.view 100')

#用shell命令，将logcat保存在sdcard/yang.text文件
##device.shell('logcat > sdcard/yang.txt')

#用adb命令，将logcat保存在电脑上D盘根目录下
##os.system('adb logcat > d:/yang.txt')

#拖拽后截屏功能，并把图片保存在电脑指定目录下
##for i in range(1,6):
##    #device.drag((1000,500),(50,500),1,5)
##    device.drag((50,500),(1000,500,1,4))
##    draghot = device.takeSnapshot()
##    draghot.writeToFile('D:/test/draghot'+str(i)+'.png','png')
##    MonkeyRunner.sleep(1)
##    device.touch(500,600,'DONW_AND_UP')
##    touchhot = device.takeSnapshot()
##    touchhot.writeToFile('D:/test/touch'+str(i)+'.png','png')
##    print i
##device.drag((800,300),(0,300),1,4)

class ThreadClass(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self._run_num = num
        
    def run(self):
        global mutex
        threadName = threading.currentThread().getName()
        print 'run...'
        for x in xrange(0,int(self._run_num)):
            mutex.acquire()
            my = ctrip()
            my.writeLog()
            print x,self._run_num
            #os.system('adb logcat *:E > d:/log.txt')
            print 'end'
            mutex.release()
            time.sleep(3)
    def startThread(self):
        global mutex
        threads = []
        mutex = threading.Lock()
        
        threads.append(ThreadClass(self._run_num))
        for t in threads:
            t.start()
        
class parserXml():
    def __init__(self,xmlName):
        self._xmlName = xmlName
    def getparser(self,tag,desid):
        print 'start parse xml'
        dom1 = minidom.parse(self._xmlName)
        root = dom1.documentElement
        nodelist = root.getElementsByTagName(tag)
        for node in nodelist:
            if (node.getAttribute('id') == desid):
                textlist = node.getElementsByTagName('text')
                for text in textlist:
                    for child in text.childNodes:
                        if child.nodeType == Node.TEXT_NODE:
                            return child.data    


if __name__=="__main__":
    myctrip = ctrip()
    cur_dir_file = r'E:\myPython\myCtrip.xml'
    myparserXml = parserXml(cur_dir_file)
    path = r"D:\apk\ctrip_542_9013.apk"
    name = "ctrip_542_9013.apk"
    packageName = "ctrip.android.view"
    startActivity = "/.home.CtripSplashActivity"
    #filepathName = r'E:\android\sdk\tools\myCtrip.xml'
    cur_dir = os.getcwd()
    #initDevice()
    #installApk(path)
    myctrip.startApk(packageName,startActivity)
    #myctrip.deviceInfo()
    #print cur_dir_file
    #data = myparserXml.getparser('index','home_index_hotel')
    #print data
    #myctrip.testSuite(cur_dir_file)
    #removeApk(packageName)
    global mutex
    num = 5
    threads = []
    mutex = threading.Lock()
    for i in xrange(0,num):
        threads.append(ThreadClass(num))
    for t in threads:
        t.start()
    #myThread = ThreadClass(6)
    #myThread.startThread()
    myctrip.hotelSuite()
