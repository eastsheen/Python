#!/user/bin/env python
#coding=utf-8

import urllib
import whyspider
import urllib2
import sys
import cookielib
import time
#mySpider = whyspider.WhySpider()


class Market:
    def __init__(self):
        """Constructor"""
        self.cookie_jar = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        self.headlers = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 4 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19'}
             
    def sendPost(self,marketUrl,fileSuc,fileFai,fileOth,fileError):
        ErrorCount = 0
        passCount = 0
        for read in marketUrl:
            #my_request = urllib2.Request(url=get_url,headers=self.headlers)
            #reCode = urllib2.urlopen(my_request)
            #print '%s' % reCode.getcode()          
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

    def TestUrlOpen(self,fileTes):
        f = urllib2.urlopen('http://python.org')
        print f.read(100)
        fileTes.write(f.read())
    
    def TestUrlRequest(self,fileTes):
        request = urllib2.Request(url="http://www.baidu.com/",data='python')
        f = urllib2.urlopen(request)
        #print f.read()
        fileTes.write(f.read())
        
    def TestUrlAuth():
        auth_handler = urllib2.HTTPBasicAuthHandler()
        auth_handler.add_password(uri='https://accounts.ctrip.com/H5Login/#login',user='wwwwww',passwd='good08')
        opener = urllib2.build_opener(auth_handler)
        urllib2.install_opener(opener)
        urllib2.urlopen('https://accounts.ctrip.com/H5Login/#login')
    
    def closeFile(self):
        fileSuc.close()
        fileFai.close()
        fileOth.close()
        marketUrl.close()
        
    def send_get(self,get_url):
        try:
            my_request = urllib2.Request(url=get_url,headers=self.headlers)
            reCode = urllib2.urlopen(my_request)
            print '%s' % reCode.getcode()
            #reUrl = self.opener.open(my_request)
            #print reUrl.read()
            #print reUrl.getCode()
        except Exception,e:
            print "Exception:",e
            
        
if __name__=='__main__':
    myMarket = Market()
    marketUrl = open('newMarketUrl.txt','r')
    fileSuc = open('marketSuc.txt','w')
    fileFai = open('marketFai.txt','w')
    fileOth = open('marketOth.txt','w')
    fileTes = open('marketTes.txt','w')
    fileError = open('fileError.txt','w')
    marketUrl.seek(0)
    marketUrl.readline()      
    myMarket.sendPost(marketUrl,fileSuc,fileFai,fileOth,fileError)
    #import urllib2
    #r = urllib2.urlopen('http://m.ctrip.com')
    #print '%s %s %s' % (r.getcode(),r.geturl(),r.info())
    #print 'code:%s' % r.getcode()
    #print 'url:%s' % r.geturl()
    #print 'info:%s' % r.info()
    #myMarket.TestUrlOpen(fileTes)
    #myMarket.TestUrlRequest(fileTes)
    #url = 'http://m.ctrip.com/market/libs.js'
    #myMarket.send_get(url)
    
    myMarket.closeFile()
    
    #da = sys.stdin.read()
    #print  'data %s' % da    
    
    

