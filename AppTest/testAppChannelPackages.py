#!/user/bin/env python
#coding=utf-8

'''
Created on 2015-04-10

python 2.7 for window

@auther: Eastsheen

QQ:393857608

'''

import os
import re
import sys
import time

########################################################################
"""
大概思路：
1、用adb shell 连接设备
2、遍历指定路径下apk包，存放list里
3、adb shell install依次安装apk包
4、安装成功启动app，进行随意monkey测试，截图保存
5、卸装app，循环执行list的apk
"""
class TestAppChannelPackages():
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.packageNameList = []
        self.apkNameList = []
        self.packageName = 'ctrip.android.view'
        self.startPackageName = 'ctrip.android.view/.home.CtripSplashActivity'
        self.currentPath = os.getcwd() + '\\' + 'packages'
        
    """
    执行测试
    """
    def testApp(self):
        self.connectionDevice()
        self.get_dirs_files_walk(self.currentPath)
        if self.packageNameList:
            for i in range(0,len(self.packageNameList)):
                print 'install',self.apkNameList[i]
                self.InstallApp(self.packageNameList[i])
                self.startApp(self.startPackageName)
                self.testMonkey(self.packageName)
                self.uninstallApp(self.packageName)
        else:
            print 'packageNameList is null'
    
    """
    用adb devices命令检测有没有连接设备
    """
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
    
    """
    遍历目录下文件夹、文件
    """    
    def get_dirs_files_walk(self,filePath):
        for dirspath,dirsnames,filenames in os.walk(filePath):
            if os.path.isdir(dirspath):
                #print 'dirspath:'+dirspath
                pass
            for dirs in dirsnames:
                #print 'dirsnames:'+dirs
                pass
            for files in filenames:
                #print 'filenames:'+files
                path = os.path.join(dirspath,files)
                #print  'path',path
                self.packageNameList.append(path)
                self.apkNameList.append(files)
            
    """
    安装APP
    """
    def InstallApp(self,apkPath):
        searchResult = self.checkAppExist(self.packageName)
        if searchResult:
            #print 'search match',searchResult.group()
            self.uninstallApp(self.packageName)
            os.system('adb install -l %s' % apkPath) 
        else:
            #print 'search no match'
            os.system('adb install -l %s' % apkPath) 
    
    """
    启动APP
    """   
    def startApp(self,packageName):
        try:
            if self.checkAppExist(self.packageName):
                startout = os.popen('adb shell am start -W -n %s' % packageName).read()
                print startout
                time.sleep(5)
                self.killApp(self.packageName)
                startout = os.popen('adb shell am start -W -n %s' % packageName).read()
                print startout                
            else:
                self.InstallApp(self.currentPath)
        except Exception,e:
            print '没有连接手机'
            print e
    
    """
    卸装APP
    """
    def uninstallApp(self,packageName):
        try:
            out = os.popen("adb uninstall %s" % packageName).read()
            print out
        except Exception,e:
            print e  
       
    """
    检测app是否安装
    """
    def checkAppExist(self,packageName):
        try:
            out = os.popen('adb shell pm list package %s' % packageName).read()
            searchResult = re.search('%s' % ('.'+self.packageName+'.'),out) 
            print out
            return searchResult
        except Exception,e:
            print e  
    
    """
    kill App
    @packageName:apk包名
    """
    def killApp(self,packageName):
        try:
            out = os.popen('adb shell am force-stop %s' % packageName).read()
            print out
        except Exception,e:
            print e        
    
    """
    Monkey Test
    adb shell monkey -p ctrip.android.view  --throttle 500 -s 600 -v -v -v 100 > C:\monkeylog.txt
    @packageName:apk包名
    @ -throttle: 在事件之间插入固定延迟
    @ -p ctrip.android.view
    @ -v -v -v 100（3个-v代表最详细的日志级别）（数字100： 表示测试事件数）
    @ -s 600（如果用相同的seed值再次运行monkey，它将生成相同的事件序列。
    @ > C:\ 重定向输出
    """
    def testMonkey(self,packageName):
        try:
            out = os.popen("adb shell monkey -p %s --throttle 500 -s 600 -v -v -v 100 > C:\monkeylog.txt" % (packageName))
            print out
            time.sleep(10)
        except Exception,e:
            print e 
            
    """
    通过adb shell screencap命令截图，保存在手机sdcard/上
    通过adb pull cdcard/screenPicture C:/picture/ 保存电脑上
    """
    def screenHotPicture(self,pictureName):
        try:
            out = os.popen("adb shell screencap -p /cdcard/screenPicture/%s" % (pictureName))
            print out
            out = os.popen("adb pull /cdcard/screenPicture/%s C:\picture\ " % (pictureName))
            print out            
        except Exception,e:
            print e         
        
        
        
        
    
    