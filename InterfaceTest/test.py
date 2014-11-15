#!/user/bin/env python
#coding=utf-8
import json

userIDList = ['2336885156']


for i in range(0,len(userIDList)-1):
    param = json.dumps({'user:':'id','phone':'%s'}) % userIDList[i]
    print param

