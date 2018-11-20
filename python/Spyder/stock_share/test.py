# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 07:26:16 2018

@author: 亮
"""
import time, datetime

def execute_timer():
    _stop = True
    while(_stop):
        print(datetime.datetime.now().strftime("%H:%M"))
        time.sleep(1)
        
        if datetime.datetime.now().strftime("%H:%M") == "08:04":
            _stop = False
            
execute_timer()