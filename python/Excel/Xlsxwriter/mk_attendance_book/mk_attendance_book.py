import xlsxwriter
import csv
import os
import numpy as np
# エクセルの列のアルファベットを数値から変換するメソッド
from openpyxl.utils import get_column_letter
from editcell import EditCell
target_filename = '出席簿.xlsx'
csv_filename = 'name.csv'

# 名前のリスト(CSV)を読み込む
names = list()
with open(csv_filename, 'r') as csv_file:
    f = csv.reader(csv_file)
    for i in f:
        names.append(i)
names = list(np.array(names).flatten()) # numpyのflattenを使用して平滑化

# 現在のディレクトリに対象のExcelファイルを作成する
# 既に同じ名前のファイルが存在する場合はエラーとなる
current_dir = os.path.dirname(os.path.abspath(__file__))
target_file_path = os.path.join(current_dir, target_filename)
try:
    if os.path.exists(target_file_path) == True:
        raise SystemError('{}の"{}"が上書きされる恐れがあります。'.format(current_dir, target_filename))
except SystemError as e:
    print("SystemError : {}".format(e))
    exit()
else:
    wb = xlsxwriter.Workbook(target_filename)
sheet_name = '出席簿'
ws = wb.add_worksheet(sheet_name)

# 名前のセル
a1 = EditCell(wb, ws, 1, 1, '名前')
a1.edit_font(bold = True)
a1.edit_border_round()
a1.edit_height_width(width = 20)
a1.edit_fill(fgColor = 'yellow')
a1.edit_alignment()

# 出欠のセル
b1 = EditCell(wb, ws, 2, 1, '出欠')
b1.edit_font(bold = True)
b1.edit_border_round()
b1.edit_height_width(width = 5)
b1.edit_fill(fgColor = 'yellow')
b1.edit_alignment()

for i, row in enumerate(range(2, 2 + len(names))):
    # CSVファイルからリスト化された名前を書き込む
    name_cell = EditCell(wb, ws, 1, row, names[i])
    name_cell.edit_border_round()
    name_cell.edit_alignment()
    # 出欠のプルダウンメニューを書き込む
    attendance_cell = EditCell(wb, ws, 2, row)
    attendance_cell.edit_alignment()
    attendance_cell.edit_border_round()
    attendance_cell.regulate_input_str(['○', '△', '☓'])

wb.close()
