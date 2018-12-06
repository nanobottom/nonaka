# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 21:50:33 2018

@author: 亮
"""
import os
import pandas as pd

from stock_share import StockShare

class PlotCandleFromTradeHistory:
    """
    損益管理表のEXCELデータを取り出し、
    成功例と失敗例の株価データをプロットして保存する
    """
    def __init__(self, filename, sheet_name):
        self.filename = filename
        self.sheetname = sheet_name
        self.df_data = None
        
    def read_excel(self):
        """EXCELに記載されている取引履歴からpandasでデータを読み込む"""
        self.df_data = pd.read_excel(filename, sheet_name=sheet_name)
    
    def plot_success_trade(self):
        df = self.df_data
        # 損益率が5%以上のデータのみを取り出す
        df_success = df[df['05.損益率'] > 5]
        
        # 成功例のディレクトリに画像を保存する
        script_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)))
        success_dir = os.path.join(script_dir, "5kabu", "success")
        os.chdir(success_dir)
        
        for code, selling_date in zip(df_success["01.コード"], df_success["08.売却日"]):
            ss = StockShare(code, selling_date)
            ss.get_candle_data()
            if ss.is_exist_code == True:
                ss.plt(True)

    def plot_failure_trade(self):
        df = self.df_data
        # 損益率が-3%以下のデータのみを取り出す
        df_failure = df[df['05.損益率'] < -3]
        
        # 成功例のディレクトリに画像を保存する
        script_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)))
        failure_dir = os.path.join(script_dir, "5kabu", "failure")
        os.chdir(failure_dir)
        
        for code, selling_date in zip(df_failure["01.コード"], df_failure["08.売却日"]):
            ss = StockShare(code, selling_date)
            ss.get_candle_data()
            if ss.is_exist_code == True:
                ss.plt(True)
            
if __name__ == "__main__":
    filename = "損益管理表5日株.xlsx"
    sheet_name = "2014年"
    plot_candle = PlotCandleFromTradeHistory(filename, sheet_name)
    plot_candle.read_excel()
    plot_candle.plot_success_trade()
    plot_candle.plot_failure_trade()
    #print(plot_candle.df_data)