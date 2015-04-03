#!/user/bin/env python
#coding=utf-8

'''
Created on 2014-12-15

@auther: Eastsheen

QQ:393857608

python version 2.7

'''

global testCasePass
global testCaseFail
testCasePass = 0
testCaseFail = 0

class TestCaseTotal():
    """"""
    def __init__(self):
        """"""
        
    def addTestCasePass(self,number):
        global testCasePass
        testCasePass = testCasePass + number
        
    def addTestCaseFail(self,number):
        global testCaseFail
        testCaseFail = testCaseFail + number
    
    def getTestCasePassTotal(self):
        global testCasePass
        return testCasePass
    
    def getTestCaseFailTotal(self):
        global testCaseFail
        return testCaseFail
    def getTestCaseTotal(self):
        global testCaseFail
        global testCasePass
        return testCasePass + testCaseFail