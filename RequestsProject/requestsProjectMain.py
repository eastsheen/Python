#!/user/bin/env python
#coding=utf-8

'''
Created on 2015-04-02

@auther: Eastsheen

QQ:393857608

python version 2.7

requests version 2.4.3

'''

import requests
import json
import time,datetime
import writelogging
import testCaseTotal
import getCurrentTime


global isWriteLog
isWriteLog = True

global isWriteSqlite
isWriteSqlite = True

global isShowLog
isShowLog = True

########################################################################
class RequestsProjectMain():
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        #
        self.mywriteLog = writelogging.WriteLogging()
        self.mytotalTestCase = testCaseTotal.TestCaseTotal()
        self.mygetCurrentTime = getCurrentTime.getCurrentTime()
        self.log_file_name = self.mygetCurrentTime.getCurrentTimeYearMonthDay()+'.txt'
        self.url_get = 'http://httpbin.org/get'
        self.url_post = 'http://httpbin.org/post'
   
        
    '''
    send post requests 发送requests请求方法
    url--请求url地址
    data--post请求data
    headers--默认为None,选填参数
    timeout--默认30秒，选填参数
    '''
    def send_requests(self,url,data,headers=None,timeout=30):
        #校验url data
        if url == '' or data == '' or not url or not data:
            print 'url or data is None'
            return
        r = requests.post(url,data=data,headers=headers,timeout=timeout)
        return r      
    
    '''
    send get requests 
    '''
    def send_get_requests(self):
        testCaseName = 'send_get_requests'
        payload = json.dumps({'name':'eastsheen','work':'test'})
        r = self.send_requests(self.url_get,payload)
        if r == None:
            print 'send_requests_response is None'
            return
        else:
            #requests请求所消耗的时间
            elapsed = r.elapsed
            #print 'elapse',r.elapsed
            #requests请求返回响应状态码
            #print 'status_code',r.status_code
            #如requests正常响应，
            #print 'headers',r.headers
            #如响应类型application/json，使用r.json()方法把这个返回的数据解析为python对象
            #print 'json',r.json().keys()
            #输入返回的内容
            #print r.text
            #校验response数据及写日志、统计case
            self.response(testCaseName, payload, r,elapsed,'test')            
    
    '''
    send post reqeusts
    '''   
    def send_post_requests(self):
        testCaseName = 'send_post_requests'
        #post请求中data数据，传递一个字典，json.dumps()
        payload = json.dumps({'name':'tester','age':20,'address':'shanghai'})
        #定制请求头
        header = {'content-type':'application/json'}
        #发送一个post请求，必填url、data,headers、timeout选填
        r = self.send_requests(self.url_post, payload,header,15)
        #校验requests返回对象
        if r == None:
            print 'send_requests_response is None'
            return            
        else:
            #requests请求所消耗的时间
            elapsed = r.elapsed
            #print 'elapse',r.elapsed
            #requests请求返回响应状态码
            #print 'status_code',r.status_code
            #如requests正常响应，
            #print 'headers',r.headers
            #如响应类型application/json，使用r.json()方法把这个返回的数据解析为python对象
            #print 'json',r.json().keys() 
            #输入返回的内容
            #print r.text
            #校验response数据及写日志、统计case
            self.response(testCaseName, payload, r,elapsed,'test')


    """
    response 
    校验response数据及写日志、统计case
    """
    def response(self,testCaseName,request,response,elapsed,description=None):
        #print 'req:',request
        #print 'res',response.text
        res = response.text
        #commit_data =  response.json()
        if response.status_code == 200 or response.status_code == 405:
            log_req = self.mygetCurrentTime.getCurrentTime() + ' Request:' + request +  '\n'
            log_res = self.mygetCurrentTime.getCurrentTime() + ' Response:' + res + '\n'
            log = (log_req + log_res)
            testResult = testCaseName  + ' --Pass' + '\n'
            self.mytotalTestCase.addTestCasePass(1)
            if isShowLog == True:
                print testResult
            if isWriteLog == True:
                self.mywriteLog.writelog(self.log_file_name, 'a+', testResult+log)
            
        elif response.status_code == 404 or response.status_code == 500 or response.status_code == 400:
            log_req = self.mygetCurrentTime.getCurrentTime() + ' Request:' + Request + '\n'
            log_res = self.mygetCurrentTime.getCurrentTime() + ' Response:' + res + '\n'
            log = (log_req + log_res)
            testResult = testCaseName + ' --Fail' + '\n'
            self.mytotalTestCase.addTestCaseFail(1)
            if isShowLog == True:
                print testResult
                print log
            if isWriteLog == True:
                self.mywriteLog.writelog(self.log_file_name, 'a+', testResult+log)
        else:
            print 'other'   
      
    
    '''
    testcaseTotal
    '''
    def testCaseTotalRequests(self):
        print 'testCase Total:%s \n' % self.mytotalTestCase.getTestCaseTotal()
        print 'testCasePass:%s \n' % self.mytotalTestCase.getTestCasePassTotal()
        print 'testCaseFail:%s \n' % self.mytotalTestCase.getTestCaseFailTotal()    
            
        
if __name__=='__main__':
    myRequests = RequestsProjectMain()
    #print requests.__version__
    myRequests.send_get_requests()
    myRequests.send_post_requests()
    
    myRequests.testCaseTotalRequests()