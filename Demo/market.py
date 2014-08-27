#!/user/bin/env python
#coding=utf-8

'''
Created on 2014-8-22

@auther: Eastsheen

email:yangdongxian@gmail.com

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
    def sendPost(self,marketUrl,fileSuc,fileFai,fileOth,fileError):
        ErrorCount = 0
        passCount = 0
        for read in marketUrl:     
            try:
                #time.sleep(0.5)
                code = urllib2.Request(url=read,headers=self.headlers)
                urlCode = urllib2.urlopen(code)
                urlread = urlCode.read()
                print 'getcode:%s' % urlCode.getcode()
                if urlCode.getcode() == 200:
                    codeUrl = str(urlCode.getcode()) + ',' + read
                    fileSuc.write(codeUrl)
                    passCount += 1
                elif urlCode.getcode() == 400 or urlCode.getcode() == 404 or urlCode.getcode() == 403:
                    codeUrl = str(urlCode.getcode()) + ',' + read
                    fileFai.write(codeUrl)
                elif str(urlCode.getcode()) == '404 Not Found':
                    print urlCode.getcode()
                else:
                    codeUrl = str(urlCode.getcode()) + ',' + read
                    fileOth.write(codeUrl)
            except Exception,e:
                ErrorCount += 1
                codeUrl = str(e)+','+read
                fileError.write(codeUrl)              
                #if e.getcode() == 403 or e.getcode() == 403:
                    #codeUrl = str(urlCode.getcode()) + ',' + read
                    #fileFai.write(codeUrl)
                #else:
                    #codeUrl = str(e)+','+read
                    #fileError.write(codeUrl)
        print 'ErrorCount:%s' % ErrorCount
        print 'PassCount:%s' % passCount

    #发送get请求
    def send_get(self,urls,fileSuc,fileFai):
        Passcount = 0
        ErrorCount = 0
        try:
            #设置模拟模式
            self.set_ios_mobile()
            while 1:
                readline = urls.readline()
                if not readline:
                    break
                else:
                    my_request = urllib2.Request(url=readline)
                    #用urlopen打开url,urlopen对象可以获取如下三个方法getcode()、geturl()、info()
                    mycode = urllib2.urlopen(my_request)
                    #url对象用read()方法读取response内容
                    myReadCode= mycode.read()
                    #print "code:%s" % mycode
                    print "getcodes:%s" % mycode.getcode()
                    print "geturl:%s" % mycode.geturl()
                    #print "info:%s" % mycode.info()
                    #print "getcontent:%s" % myReadCode
                    #write suc
                    log = str(mycode.getcode())+mycode.geturl()
                    fileSuc.write(log)
        except Exception,e:
            print e
            #fileFai.write(e)
    
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
        fileOth.close()
        urls.close()
                 
        
if __name__=='__main__':
    myRequest = url_request()
    urls = open('sourceUrl.txt','r')
    fileSuc = open('urlSuc.txt','w')
    fileFai = open('urlFai.txt','w')
    fileOth = open('urlOth.txt','w')
    fileTes = open('marketTes.txt','w')
    fileError = open('fileError.txt','w')
    urls.seek(0)
    #urls.readline()      
    #myMarket.sendPost(marketUrl,fileSuc,fileFai,fileOth,fileError)
    url = 'http://m.ctrip.com/market/AdMonitorService.aspx'
    myRequest.send_get(urls,fileSuc,fileFai)
    myRequest.closeFile()
    
    #da = sys.stdin.read()
    #print  'data %s' % da    
    
    

