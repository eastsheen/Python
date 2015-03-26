#!/user/bin/env python
#coding=utf-8

'''
Created on 2014-11-3

@auther: Eastsheen

QQ:393857608

'''

import urlRequest
import io
import gzip
import json

class pushServices():
    """pushServices"""
    def __init__(self):
        """init"""
        self.request = urlRequest.url_request()
        self.url_pushMessageToUsers = None
    
    def pushMessageToUsers(self):
        data = [{'ClientTokenList':'32565957900000028824',
                 'MessageBody':{'Title':'titel',
                                'ExpiredTime':'2014-11-11T20:49:10',
                                'BusinessType':'1',
                                'Payload':{
                                'body':'body',
                                'sound':'default'}}}]
        print "data:%s" % repr(data)
        req = self.request.send_post_pushService(self.url_pushMessageToUsers, data)
        f = req.read().decode('utf-8')
        print "response:%s" % f
        
        
        