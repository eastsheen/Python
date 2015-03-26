#!/user/bin/env python
#coding=utf-8

'''
Created on 2014-11-13

@auther: Eastsheen

QQ:393857608

'''
import urlRequest
import json
import datetime,time
import io

class watchService():
    """init"""
    def __init__(self):
        print "watchService start"
        self.request = urlRequest.url_request()
        self.url_Flight = None
        self.url_Car = None
        self.url_TravelAgenda = None
        self.fileCount = open('TravelAgendaInfo.txt','w')
        
    def FlightCheckInInfoRequest(self):
        """
        Platform:请求来自设备平台(1:Android Watch)
        UID:用户UID
        FlightNO：航班号
        FlightDate:飞机启飞日期
        """
        param = {'Platform':'1',
                 'UID':'M00053146',
                 'FlightNO':'GS6459',
                 'FlightDate':'2014-11-13 20:49:10'}
        #print "%s" % json.dumps(param)
        req = self.request.send_post_pushService(self.url_Flight, param)
        f = req.read().decode('utf-8')
        print "code:%s ,msg:%s" % (req.code,req.msg)
        print "response:%s" % f
        
    def ShowCarInInfo(self):
        """
        Platform:请求来自设备平台(1:Android Watch)
        UID:用户UID
        """
        param = {
            'Platform':'1',
            'UID':'test111111'
        }
        req = self.request.send_post_pushService(self.url_Car, param)
        f = req.read().decode('utf-8')
        print "code:%s ,msg:%s" % (req.code,req.msg)
        print "response:%s" % f
        
        
    def TravelAgendaInfo(self):
        """
        Platform:请求来自设备平台(1:Android Watch)
        UID:用户UID
        """
        userIDList = ['2336885156']
        print 'userlist:%s' % userIDList[0]

        for i in range(0,len(userIDList)-1):
            #print userIDList[i]
            param = json.dumps({'Platform':'1','UID':'%s'}) % userIDList[i]
            #param1 = json.dumps({'Platform':'1','UID':'18800001111'},sort_keys=True)
            load = json.loads(param)           
            #print 'json:%s' % load
            startTime = datetime.datetime.utcnow()
            req = self.request.send_post_pushService(self.url_TravelAgenda, load)
            f = req.read().decode('utf-8')
            endTime = datetime.datetime.utcnow()
            t = (endTime - startTime)
            log = str(self.getCurrentTime()) + ' ' + 'userid:' + str(userIDList[i]) + 'elapsed time:' + str(t) + '\n' + f + '\n'
            print log
            try:
                self.fileCount.write(log)
            except IOError,e:
                print e        
        #print "time:%s" % t
        #print "code:%s ,msg:%s" % (req.code,req.msg)
        #print "response:%s" % f    
        
    #getCurrentTime
    def getCurrentTime(self):
        try:
            currentTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            #print currentTime
        except Exception,e:
            print e
        return currentTime    
        
        