#!/user/bin/env python
#coding=utf-8

'''
Created on 2014-12-2

@auther: Eastsheen

QQ:393857608

python version 2.7

'''
import io
import sys
import os

class WriteLogging():
    """
    """
    def __init__(self):
        """ """
        
    def writeData(self,dirName,fileName,wr,content):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        try:
            logpath = os.getcwd()+'\\'+ dirName+'\\'+fileName
            self.check_dir_file_isexist(os.getcwd(), dirName, fileName)
            if len(fileName) > 0 and len(wr) > 0:
                openfile = open(logpath,wr)
                openfile.write(content)
            else:
                print 'no fileName or no wr'
        except IOError,e:
            print e
    
    def writelog(self,fileName,wr,log):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        try:
            logpath = os.getcwd()+r'\log\\'+fileName
            self.check_dir_file_isexist(os.getcwd(), 'log', fileName)
            if len(fileName) > 0 and len(wr) > 0:
                openfile = open(logpath,wr)
                openfile.write(log)
            else:
                print 'no fileName or no wr'
        except IOError,e:
            print e
            
    def create_dirname(self,dirpath,mkfile):
        #cur_dir = os.getcwd()
        for dirspath,dirnames,filenames in os.walk(dirpath):
            if os.path.isdir(dirspath):
                print 'dirspath:' + dirspath
            for dir in dirnames:
                newdir = os.path.join(dirpath,mkfile)
                if os.path.isdir(newdir):
                    print '%s is exist' % newdir
                    return newdir
                else:
                    os.mkdir(newdir)
                    return newdir
                
    def check_dir_file_isexist(self,dirpath,dirname,filename):
        for dirspath,dirnames,filenames in os.walk(dirpath):
            #if os.path.isdir(dirspath):
                #print 'dirspath:' + dirspath
            for dir in dirnames:
                newdirpath = os.path.join(dirpath,dirname)
                if os.path.isdir(newdirpath):
                    #print '%s is exist' % newdirpath
                    if dir == dirname:
                        newpath = os.path.join(newdirpath,filename)
                        if os.path.isfile(newpath):
                            #print '%s is exist' % newpath
                            return newpath
                        else:
                            #os.mkdir(newpath)
                            try:
                                open(newpath,'w')
                                print 'create file'
                            except IOError,i:
                                print i
                            return False                    
                else:
                    os.mkdir(newdirpath)
                    return False
                
    """
    read txt file
    """   
    def readFileContext(self,dirName,fileName,mList):
        try:
            cur_dir = os.getcwd()
            filepath = self.check_dir_file_isexist(cur_dir, dirName, fileName)
            if filepath == False:
                print 'file is on exist'
                return False
            read = open(filepath,'r')
            while mList:
                mList.pop()
            while 1:
                user = read.readline()
                if not user:
                    break
                elif len(user) > 1:
                    user = user.replace('\n','')
                    mList.append(user)
        except IOError,i:
            print i    


                
                
                
                        
                    
        
        
        