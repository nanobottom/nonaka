# -*- coding: utf-8 -*-
"""
Created on Fri May  8 23:35:04 2020

@author: nanob
"""

import pyautogui
import time
print('中断するにはCtrl-Cを押してください。')

try:
    while True:
        time.sleep(1)
        x, y = pyautogui.position()
        position_str = 'X:' + str(x).rjust(4) + ' Y:' + str(y).rjust(4)
        pixel_color = pyautogui.screenshot().getpixel((x, y))
        position_str += ' RGB: (' + str(pixel_color[0]).rjust(3)
        position_str += ', ' + str(pixel_color[1]).rjust(3)
        position_str += ', ' + str(pixel_color[2]).rjust(3) + ')'
        print(position_str)
        #print('\b' * len(position_str), end='', flush=True)
except KeyboardInterrupt:
    print('\n終了。')