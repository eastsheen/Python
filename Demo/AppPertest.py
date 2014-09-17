#!/user/bin/env python
#coding=utf-8

'''
Created on 2014-9-12

python 2.7 for window

@auther: Eastsheen

QQ:393857608

'''
import os
import re
import time
import sys

class appPerTest:
    
    def __init__(self):
        """ init """
    def connectionDevice(self):
        try:
            devices = os.popen('adb devices').read()
            device = re.findall('device', devices)
            if device.__len__() < 2:
                print 'not connection device !!'
                print 'wait for 5s'
                time.sleep(5)
                print 'exit app'
                sys.exit(1)
            else:
                print 'connection success !!'
        except Exception,e:
            print e
        except IOError,i:
            print i
    
    def startApp(self,packageName):
        try:
            startout = os.popen('adb shell am start -W -n %s' % packageName).read()
            print startout
        except Exception,e:
            print '没有连接手机'
            print e
    
    def uninstallApp(self,packageName):
        try:
            os.popen("adb uninstall %s" + packageName)
        except Exception,e:
            print e
    
    #获取android packageName列表
    def getCurrentPackages(self):
        try:
            for package in os.popen('adb shell pm list packages','r').readlines():
                reList = re.sub('package:','',package)
                list.append(reList)
                reList = reList.replace('\n','')
                result = re.search('ctrip.android.view', reList)
                print "result:%s" % result
                print reList
                packages.write(reList)
        except Exception,e:
            print e
    
    #获取apk占用内存
    def getDumpsysMeminfo(self,adbShellMem,searchWord,fileMeminfo):
        try:
            for line in os.popen('%s' % adbShellMem).readlines():
                #print '%s' % line
                if re.search('%s' % searchWord, line):
                    print 'Meminfo:%s' % line
                    result = re.findall('[0-9]{1,9} ', line)
                    Headsize = result[-2]
                    HeadAlloc = result[-1]
                    size = 'headSize:%s ' % Headsize
                    alloc = 'headAlloc:%s' % HeadAlloc
                    log = str(self.getCurrentTime()) + str(' ') + size + alloc
                    print log
                    fileMeminfo.write(log)
                    
        except Exception,e:
            print e
        except IOError,e:
            print e
    
    #获取apk占用 cpu
    def getDumpsysCpuinfo(self,adbShellCpu,searchWord,fileCpuinfo):
        try:
            time.sleep(2)
            for line in os.popen('%s' % adbShellCpu).readlines():
                #print line
                if re.search('%s' % searchWord,line):
                    print 'Cpuinfo:%s' % line
                    result = re.findall('[/.0-9]{1,9}%', line)
                    if result:
                        cpu = 'cpu:%s ' % result[0]
                        userCpu = 'userCpu:%s' % result[1]
                        log = str(self.getCurrentTime()) +' '+ cpu + userCpu
                        print log
                        fileCpuinfo.write(log)
        except  Exception,e:
            print e
    
    #getCurrentTime
    def getCurrentTime(self):
        try:
            currentTime = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
            #print currentTime
        except Exception,e:
            print e
        return currentTime
    
    def readTxt(self,fileName):
        try:
            print fileName
            readContent = open('%s' % fileName,'r')
            writeMeminfo = open('Meminfo.txt','w')
            readContent.seek(0)
            while 1:
                line = readContent.readline()
                if not line:
                    break
                else:
                    print line
                    if(re.search('TOTAL', line)):
                        print 'total:' + line
                        #content = re.sub(' ', '.', line)
                        result = re.findall('[0-9]{1,9} ', line)
                        #print 'start:'+ str(result.start(0))
                        #print 'end:' + str(result.end(0))
                        print 'result:%s' % result
                        print 'Head Size:%s' % result[-3]
                        print 'Heap allo:%s' % result[-2]
                        for number in result:
                            print 'size:%s \n' % (number)
                        
        except IOError,e:
            print e


if __name__=="__main__":
    myApp = appPerTest()
    myApp.connectionDevice()
    packageName='ctrip.android.view'
    startActivity = '/.home.CtripSplashActivity'
    packNameStartActivity = packageName + startActivity
    myApp.startApp(packNameStartActivity)
    
    fileMeminfo = open('meminfo.txt','w')
    fileCpuinfo = open('cpuinfo.txt','w')
    #myApp.getDumpinfo()
    filePath = r'D:\meminfo3.txt'
    print filePath
    #myApp.readTxt(filePath)
    meminfo = 'adb shell dumpsys meminfo ctrip.android.view'
    cpufinfo = 'adb shell dumpsys cpuinfo'
    myApp.getDumpsysMeminfo(meminfo,'TOTAL',fileMeminfo)
    myApp.getDumpsysCpuinfo(cpufinfo,'ctrip.android.view',fileCpuinfo)
    #print myApp.getCurrentTime()