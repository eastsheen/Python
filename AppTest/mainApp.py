#!/user/bin/env python
#coding=utf-8

'''
Created on 2015-04-10

python 2.7 for window

@auther: Eastsheen

QQ:393857608

'''

import testAppChannelPackages
import os

########################################################################
class MainApp():
    """"""
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.testAppChannel = testAppChannelPackages.TestAppChannelPackages()

        
    def testAppChannelPackagesFunc(self):
        self.testAppChannel.testApp()
        
        
        
if __name__ == '__main__':
    myApp = MainApp()
    myApp.testAppChannelPackagesFunc()
    
        
    
    