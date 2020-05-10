# -*- coding: utf-8 -*-
"""
Created on Thu May  7 22:25:38 2020

@author: nanob
"""

from PIL import ImageGrab

# full screen
ImageGrab.grab().save("PIL_capture.png")

# 指定した領域内をクリッピング
#ImageGrab.grab(bbox=(100, 100, 200, 200)).save("PIL_capture_clip.png")