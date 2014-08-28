#!/user/bin/env python
#coding=utf-8

'''
Created on 2014-8-22

@auther: Eastsheen

QQ:393857608

'''

import urllib
import urllib2
import sys
import cookielib
import time

class url_request():
    #初始化opener headlers,默认headlers为android Nexus 4
    def __init__(self):
        """Constructor"""
        self.cookie_jar = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        self.headlers = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 4 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19'}
     
    #发送post请求     
    def sendPost(self,urls,fileSuc,fileFai):
        ErrorCount = 0
        passCount = 0
        for read in urls:     
            try:
                code = urllib2.Request(url=read,headers=self.headlers)
                urlCode = urllib2.urlopen(code)
                urlread = urlCode.read()
                print 'getcode:%s' % urlCode.getcode()
                if urlCode.getcode() == 200:
                    codeUrl = str(urlCode.getcode()) + ',' + read
                    fileSuc.write(codeUrl)
                    passCount += 1
            except Exception,e:
                ErrorCount += 1
                codeUrl = str(e)+','+read
                fileFai.write(codeUrl)
        print 'ErrorCount:%d PassCount:%s' % (ErrorCount,passCount)

    #发送get请求
    def send_get(self,urls,fileSuc,fileFai):
        Passcount = 0
        Failcount = 0
        #设置模拟模式
        self.set_ios_mobile()
        #while循环从txt文件读取内容，判断not readline跳出while
        while 1:
            try:
                readline = urls.readline()
                if not readline:
                    break
                else:
                    my_request = urllib2.Request(url=readline)
                    #用urlopen打开url,urlopen对象可以获取如下三个方法getcode()、geturl()、info()
                    mycode = urllib2.urlopen(my_request)
                    #url对象用read()方法读取response内容
                    myReadCode= mycode.read()
                    #输入getcode()/geturl()/info()/read()相关信息
                    #print "getcode:%s geturl:%s info:%s read:%s" % (mycode.getcode(),mycode.geturl(),mycode.info(),myReadCode)
                    if mycode.getcode() == 200:
                        log = str(mycode.getcode()) + ',' + mycode.geturl()
                        fileSuc.write(log+'\n')
                        Passcount += 1
            except Exception,e:
                log = str(e) + ',' + readline +'\n'
                #print log
                fileFai.write(log)
                Failcount += 1
        print "Passcount:%d Failcount:%d" % (Passcount,Failcount)
            
    
    #模拟android Nexus 4 手机
    def set_android_mobile(self):
        user_agent= "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 4 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
        self.headlers = {"User-Agent",user_agent}
    
    #模拟ios 5 手机
    def set_ios_mobile(self):
        user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X; en-us) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53"
        self.headlers = {"User-Agent",user_agent}
     
    #模拟computer
    def set_computer(self):
        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"
        self.headlers = {"User-Agent",user_agent}
    
    #关闭file      
    def closeFile(self):
        fileSuc.close()
        fileFai.close()
        urls.close()
                 
        
if __name__=='__main__':
    myRequest = url_request()
    urls = open('sourceUrl.txt','r')
    fileSuc = open('urlSuc.txt','w')
    fileFai = open('urlFai.txt','w')
    urls.seek(0)
    #post
    myRequest.sendPost(urls,fileSuc,fileFai)
    #get
    #myRequest.send_get(urls,fileSuc,fileFai)
    myRequest.closeFile()
    
    

