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

class appPerTest:
    
    def __init__(self):
        """ init """
    def connectionDevice(self):
        try:
            #out = os.popen('adb shell wait-for-device')
            deviceOut = os.popen('adb devices').read()
            print deviceOut
        except Exception,e:
            print e
        except IOError,i:
            print i
    
    def startApp(self,packageName):
        try:
            startout = os.popen('adb shell am start -W -n %s' % packageName).read()
            print startout
        except Exception,e:
            print e
    
    def uninstallApp(self,packageName):
        try:
            os.popen("adb uninstall %s" + packageName)
        except Exception,e:
            print e
    
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
    
    def getDumpinfo(self):
        try:
            os.popen('adb shell dumpsys meminfo ctrip.android.view')
        except Exception,e:
            print e


if __name__=="__main__":
    myApp = appPerTest()
    myApp.connectionDevice()
    packageName='ctrip.android.view/.home.CtripSplashActivity'
    myApp.startApp(packageName)