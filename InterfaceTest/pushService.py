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

class pushServices():
    """pushServices"""
    def __init__(self):
        """init"""
        self.request = urlRequest.url_request()
        self.url_pushMessageToUsers = 'http://ws.push.mobile.uat.qa.nt.ctripcorp.com/CPNPSOA/json/PushMessageToClients'
    
    def pushMessageToUsers(self):
        ClientTokenList = ['32565957900000028824']
        parameters = {"ClientTokenList":['32565957900000028824'],
                      "MessageBody":{"Title":"python1","Payload":"{\"body\":\"python1\",\"ext\":{\"sound\":\"default\",\"url\":\"ctrip://wireless/hotel_inland_list\"}}","ExpiredTime":"2014-11-07 20:49:10","BusinessType":512}}
        #parameters = {
        #'userIDList' : '18900001111',
        #'MessageBody' : '',
        #'Title' : '推送标题',
        #'body' : '消息概述消息概述',
        #'sound' : 'default',
        #'url' : 'ctrip://wireless/hotel_inland_list',
        #'ExpiredTime' : '2014-11-7T20:10:00',
        #'BusinessType' : '1'}
        #parameters = {
        #"userIDList" : "18900001111",
        #"MessageBody" : {
            #"Title" : "title",
            #"Payload" : {
                #"body" : "new",
                #"ext" : {
                    #"sound" : "default",
                    #"url" : "ctrip://wireless/hotel_inland_list"
                    #}},
            #"ExpiredTime" : "2014-11-7T20:10:00",
            #"BusinessType" : "1"}}
        req = self.request.send_post_pushService(self.url_pushMessageToUsers, parameters)
        f = req.read().decode('utf-8')
        print "response:%s" % f
        
        
        