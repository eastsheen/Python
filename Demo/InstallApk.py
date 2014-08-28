#!/user/bin/env python
#coding=utf-8

'''
Created on 2014-8-28

@auther: Eastsheen

QQ:393857608

'''

import time
import os

from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By
from com.android.chimpchat.hierarchyviewer import HierarchyViewer

device = MonkeyRunner.waitForConnection()
easy_device = EasyMonkeyDevice(device)   

class Install_apk():
    def __init__(self):
        print 'construtor'     
    
    def installApk(self,readFile):
        print 'install...'
        #flist = readFile.readline()
        for f in readFile:
            print f
            device.installPackage(f)
            time.sleep(2)
    
    def startApk(self,packageName,Activity):
        print 'startApk...'
        device.startActivity(component=packageName+Activity)
        time.sleep(5)
    
    def removeApk(self,packageName):
        print 'removeApk...'
        device.removePackage(packageName)
        time.sleep(3)
    
    def shellInstall(self,readFile):
        print 'shellInstall...'
        print readFile
        for f in readFile:
            print f
            os.system('adb install -l %s' % f)
        
    def get_dirs_files_walk(self,filePath,fileinfo):
        for dirspath,dirsnames,filenames in os.walk(filePath):
            if os.path.isdir(dirspath):
                print 'dirspath:'+dirspath
            for dirs in dirsnames:
                print 'dirsnames:'+dirs
            for files in filenames:
                print 'filenames:'+files
                path = os.path.join(dirspath,files)
                fileinfo.write(path+'\n')
                
if __name__=="__main__":
    myInstall = Install_apk()
    cur_dir = os.getcwd()
    apkPath = cur_dir+r'\apk'
    fwrite = open('apkfile.txt','w')
    fread = open('apkfile.txt','r')

    packageName = "ctrip.android.view"
    Activity = "/.home.CtripSplashActivity"    
    file_path = r'E:\newwork\apk\Huawei_8061.apk'
    myInstall.get_dirs_files_walk(apkPath, fwrite)
    fread.seek(0)
    fread.readline()

    myInstall.installApk(fread)
    #myInstall.shellInstall(fread)
    myInstall.startApk(packageName, Activity)
    #myInstall.removeApk(packageName)