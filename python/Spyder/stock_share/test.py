# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 23:03:56 2018

@author: 亮
"""

import pandas as pd

def main():
    # データフレームの初期化
    df = pd.DataFrame({'A': [1, 11, 111],
                   'B': pd.Series([2, 22, 222]),
                   'C': pd.Series({0: 3, 1: 33, 2: 333})})

    # データフレームをExcelファイルに書き込む 
    df.to_excel("test.xlsx")

if __name__ == '__main__':
    main()