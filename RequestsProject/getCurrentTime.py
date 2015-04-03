#!/user/bin/env python
#coding=utf-8

'''
Created on 2014-11-20

@auther: Eastsheen

QQ:393857608

python version 2.7

'''
import time
import datetime

class getCurrentTime():
    def __init__(self):
        """
        """
        
    """
    getCurrentTime add day 
    return %Y-%m-%d %H:%M:%S
    """
    def getCurrentTimeAddDay(self,numberDay):
        nowtime = time.localtime(time.time())
        tm_mday = nowtime.tm_mday
        tm_mon = nowtime.tm_mon
        tm_year = nowtime.tm_year 
        dayNumber = numberDay
        if (nowtime.tm_year % 4 == 0 and nowtime.tm_year % 100 != 0) or (nowtime.tm_year % 400 == 0):
            if nowtime.tm_mon == 2:
                if nowtime.tm_mday < 29:
                    tm_mday = tm_mday + dayNumber
                else:
                    tm_mday = dayNumber
                    tm_mon = nowtime.tm_mon + 1
            elif nowtime.tm_mon == 12 and nowtime.tm_mday == 31:
                tm_year = nowtime.tm_year + 1
                tm_mon = 1
                tm_mday = 1
            elif (nowtime.tm_mon % 2) == 0 and nowtime.tm_mday != 12 and nowtime.tm_mon != 2:
                if nowtime.tm_mday < 31:
                    tm_mday = nowtime.tm_mday + dayNumber
                else:
                    tm_mday = dayNumber
                    tm_mon = nowtime.tm_mon + 1
            elif (nowtime.tm_mon % 2) == 1 and nowtime.tm_mday != 12 and nowtime.tm_mon != 2:
                if nowtime.tm_mday < 30:
                    tm_mday = nowtime.tm_mday + dayNumber
                else:
                    tm_mday = dayNumber
                    tm_mon = nowtime.tm_mon + 1
        else:
            if nowtime.tm_mon == 2:
                if nowtime.tm_mday < 28:
                    tm_mday = tm_mday + dayNumber
                else:
                    tm_mday = dayNumber
                    tm_mon = nowtime.tm_mon + 1
            elif nowtime.tm_mon == 12 and nowtime.tm_mday == 31:
                tm_year = nowtime.tm_year + 1
                tm_mon = 1
                tm_mday = 1        
            elif (nowtime.tm_mon % 2) == 0 and nowtime.tm_mday != 31 and nowtime.tm_mon != 2:
                if nowtime.tm_mday < 31:
                    tm_mday = nowtime.tm_mday + dayNumber
                else:
                    tm_mday = dayNumber
                    tm_mon = nowtime.tm_mon + 1
            elif (nowtime.tm_mon % 2) == 1 and nowtime.tm_mday != 31 and nowtime.tm_mon != 2:
                if nowtime.tm_mday < 30:
                    tm_mday = nowtime.tm_mday + dayNumber
                else:
                    tm_mday = dayNumber
                    tm_mon = nowtime.tm_mon + 1
            
        currenttime =  ('%s-%s-%s %s:%s:%s') % (tm_year,tm_mon,tm_mday,nowtime.tm_hour,nowtime.tm_min,nowtime.tm_sec)
        return currenttime     
    
    """
    getCureentTime
    return fromat time %Y-%m-%d %H:%M:%S
    """
    def getCurrentTime(self):
        try:
            currentTime = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
            #print currentTime
        except Exception,e:
            print e
        return currentTime
    
    """
    getCureentTime
    return fromat time %Y-%m-%d %H:%M:%S
    """
    def getCurrentTimeMicrosecond(self):
        try:
            currentTime = datetime.datetime.now().microsecond
            #print currentTime
        except Exception,e:
            print e
        return currentTime
    
    def getCurrentTimeAddMinute(self,minute):
        now = datetime.datetime.today()
        minu = datetime.timedelta(minutes=minute)
        addMinute = now+minu
        return addMinute
    
    def getCurrentTimeAddDay(self,dayNumber):
        now = datetime.datetime.now()
        d = datetime.timedelta(days = dayNumber)
        addDay = now + d
        return addDay
    
    def getCurrentTimeYearMonthDay(self):
        try:
            currentTime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
            #print currentTime
        except Exception,e:
            print e
        return currentTime        
    
    def getCurrentTimeNow(self):
        return datetime.datetime.now()    
