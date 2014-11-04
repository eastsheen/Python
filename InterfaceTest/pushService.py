#!/user/bin/env python
#coding=utf-8

'''
Created on 2014-11-3

@auther: Eastsheen

QQ:393857608

'''

import urlRequest

class pushServices():
    """pushServices"""
    def __init__(self):
        """init"""
        self.request = urlRequest.url_request()
        self.url_pushMessageToUsers = 'http://ws.push.mobile.uat.qa.nt.ctripcorp.com/CPNPSOA/json/PushMessageToUsers'
    
    def pushMessageToUsers(self):
        parameters = {
        'userIDList' : '18900001111',
        'MessageBody' : {
            'Title' : '推送标题',
            'Payload' : {
                'body' : '消息概述消息概述',
                'ext' : {
                    'sound' : 'default',
                    'url' : 'ctrip://wireless/hotel_inland_list'
                    }},
            'ExpiredTime' : '2014-11-3T20:10:00',
            'BusinessType' : '1'}}
        req = self.request.send_post_pushService(self.url_pushMessageToUsers, parameters)
        print str(req.code)
        print str(req.msg)
        
        
        