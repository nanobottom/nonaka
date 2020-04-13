# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""
import os
import platform
import zipfile
import time
import configparser
from datetime import date

# configparserの宣言とiniファイルの読み込み
config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

pc_name = platform.uname().node
name = config_ini.get('DEFAULT', 'name')
#target_dir = config_ini.get('DEFAULT', 'target_dir')
#target_dir2 = config_ini.get('DEFAULT', 'target_dir2')
target_dir = 'C:\\'
target_dir2 = 'D:\\'
"""
if not os.path.exists(target_dir):
    print('Warning:設定したtarget_dirは存在しません.')
    time.sleep(3)
    exit()
if not os.path.exists(target_dir2):
    print('Warning:設定したtarget_dir2は存在しません.')
    time.sleep(3)
    exit()
"""
today = date.today().strftime('%Y%m%d')
filename = today + '_' + name + '_' + pc_name + '_tree_CD.txt'

#cmd = 'tree {0} > {1}'.format(target_dir, os.path.join(cur_dirpath, filename))
print('Tree情報を取得しています.しばらくお待ちください...')
time_start = time.perf_counter()
cmd = 'tree {0} > {1}'.format(target_dir, filename)
os.system(cmd)
cmd = 'tree {0} >> {1}'.format(target_dir2, filename)
os.system(cmd)
time_end = time.perf_counter()
elapsed_time = time_end - time_start
print('Tree取得時間：{:.2f}秒'.format(elapsed_time))
zip_filename = filename.rsplit('.')[0] + '.zip'
if os.path.exists(zip_filename):
    print('Warning:{0}は既に存在しているため、上書きできません.'.format(zip_filename))
    time.sleep(3)
    os.remove(filename)
    exit()
else:
    with zipfile.ZipFile(zip_filename, 'w', compression=zipfile.ZIP_DEFLATED) as f:
        f.write(filename)
os.remove(filename)
print('{0}を出力しました.'.format(zip_filename))
time.sleep(3)
