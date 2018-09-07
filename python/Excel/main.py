import openpyxl, datetime, locale, calendar, jholiday, os
from openpyxl import load_workbook
from openpyxl.styles import Border, Side, PatternFill, Alignment
from openpyxl.utils import get_column_letter
current_year = 2018
current_month = 4
fin_month_interval = 1
white_row_num = 30
main_column_num = 7
filename = '作業進捗表.xlsx'

current_dir = os.path.dirname(os.path.abspath(__file__))
xlsx_path = os.path.join(current_dir, filename)
try:
    if os.path.exists(xlsx_path) == False:
        raise SystemError('Missing "{0}" file at {1}. Make new file.'.format(filename, current_dir))
except SystemError as e:
    print("SystemError : {}".format(e))
    work_book = openpyxl.Workbook()
else:
    work_book = load_workbook(filename)
sheet_name = str(current_year) + '年' + str(current_month) + '月'
work_sheet = work_book.create_sheet(sheet_name)

class EditCell:
    def __init__(self, work_sheet, column, row, value, cell_color):
        self.ws = work_sheet
        self.column = column
        self.row = row
        self.value = value
        self.cell_color = cell_color
        self.border_color = 'FF000000'

    # セルの枠線の設定
    def set_border(self):
        return Border(left   = Side(border_style = 'thin', color = self.border_color),
                      right  = Side(border_style = 'thin', color = self.border_color),
                      top    = Side(border_style = 'thin', color = self.border_color),
                      bottom = Side(border_style = 'thin', color = self.border_color)
                      )

    # 値、セルの塗りつぶし、セルの幅、中央揃え、枠線を設定する
    def edit(self):
        current_ws = self.ws.cell(row = self.row, column = self.column)
        if self.value != '':
            current_ws.value = self.value
        current_ws.fill = PatternFill(fill_type = 'solid', fgColor = self.cell_color) # セルの塗りつぶし
        current_ws.border = self.set_border()
        current_ws.alignment = Alignment(horizontal = 'center', vertical = 'bottom')
    
    def edit_hight_width(self, column_width = 8.11, row_height = 13.2):
        self.ws.column_dimensions[get_column_letter(self.column)].width = column_width
        self.ws.row_dimensions[self.row].height = row_height

# 土日祝日を判定して土曜日なら青,祝日か日曜日なら赤を、それ以外ならcolorを返す関数
def is_sat_sun_holiday(date, color):
    blue = 'FF0000FF'
    red = 'FFFF0000'
    day_of_the_week_index = int(date.strftime('%w'))
    if jholiday.holiday_name(date.year, date.month, date.day) is not None:
        return red
    else:
        if day_of_the_week_index == 6:
            return blue
        elif day_of_the_week_index == 0:
            return red
        else:
            return color

# 項目(A1)のセル編集
work_sheet.merge_cells("A1:A3")
a1 = EditCell(work_sheet, 1, 1, '項目', 'FFAAD8E6')
a1.edit()
a1.edit_hight_width(column_width = 30)
a2 = EditCell(work_sheet, 1, 2, '', 'FFAAD8E6')
a2.edit()
a3 = EditCell(work_sheet, 1, 3, '', 'FFAAD8E6')
a3.edit()

# 予定(B1)のセル編集
work_sheet.merge_cells("B1:C2")
b1 = EditCell(work_sheet, 2, 1, '予定', 'FFAAD8E6')
b1.edit()
c2 = EditCell(work_sheet, 3, 2, '', 'FFAAD8E6')
c2.edit()

# 実績(D1)のセル編集
work_sheet.merge_cells("D1:E2")
d1 = EditCell(work_sheet, 4, 1, '実績', 'FFAAD8E6')
d1.edit()

#開始(B3)のセル編集
b3 = EditCell(work_sheet, 2, 3, '開始', 'FFAAD8E6')
b3.edit()

#終了(C3)のセル編集
c3 = EditCell(work_sheet, 3, 3, '終了', 'FFAAD8E6')
c3.edit()

#開始(D3)のセル編集
d3 = EditCell(work_sheet, 4, 3, '開始', 'FFAAD8E6')
d3.edit()

#終了(E3)のセル編集
work_sheet.merge_cells("D1:E2")
e3 = EditCell(work_sheet, 5, 3, '終了', 'FFAAD8E6')
e3.edit()

#工数(F1)のセル編集
work_sheet.merge_cells("F1:F3")
f1 = EditCell(work_sheet, 6, 1, '工数', 'FFAAD8E6')
f1.edit()
f2 = EditCell(work_sheet, 6, 2, '', 'FFAAD8E6')
f2.edit()
f3 = EditCell(work_sheet, 6, 3, '', 'FFAAD8E6')
f3.edit()

#状態(G1)のセル編集
work_sheet.merge_cells("G1:G3")
g1 = EditCell(work_sheet, 7, 1, '状態', 'FFAAD8E6')
g1.edit()
g2 = EditCell(work_sheet, 7, 2, '', 'FFAAD8E6')
g2.edit()
g3 = EditCell(work_sheet, 7, 3, '', 'FFAAD8E6')
g3.edit()

#白枠（4行目以降）の編集
for i_row in range(4,white_row_num + 4):
    for i_column in range(1,main_column_num + 1):
        white = EditCell(work_sheet, i_column, i_row, '', 'FFF8F8FF')
        white.edit()
# 列の固定
work_sheet.freeze_panes = 'H1'

date = datetime.datetime(current_year, current_month, 1)
column_count = main_column_num + 1
for i_month in range(current_month, current_month + fin_month_interval):
    move_up_year = i_month // 12
    if move_up_year > 0 and i_month % 12 != 0:
        i_month -= move_up_year * 12
        print(i_month)
    (_, last_day) = calendar.monthrange(current_year + move_up_year, i_month)

    for i_day in range(1,last_day + 1):
        # 年月日を取得する
        year = date.year
        month = date.month
        day = date.day

        # 日付の文字列からその日付の曜日を取得する
        locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
        day_of_the_week = date.strftime('%a')
        day_of_the_week_index = int(date.strftime('%w'))
        
        # 日付セルの編集
        if i_day == 1:
            if i_month == 1:
                month_title = str(year) + '年' + str(month) + '月'
                work_sheet.merge_cells(get_column_letter(column_count) + '1:' + get_column_letter(column_count + 2) + '1')

            else:
                month_title = str(month) + '月'
            i1= EditCell(work_sheet, column_count, 1, month_title, 'FFFF8C00')
        else:
            i1= EditCell(work_sheet, column_count, 1, '', 'FFFF8C00')
        i1.border_color = 'FFFF8C00'
        i1.edit()
        i1.edit_hight_width(column_width = 4)
        yellow = 'FFFFD700'
        ans_color = is_sat_sun_holiday(date, yellow)
        i2= EditCell(work_sheet, column_count, 2, str(day), ans_color)
        i2.edit()
        i3 = EditCell(work_sheet, column_count, 3, day_of_the_week, ans_color)
        i3.edit()
        #白枠（4行目以降）の編集
        for i_row in range(4,white_row_num + 4):
            white = 'FFF8F8FF'
            ans_color = is_sat_sun_holiday(date, white)
            white_cell = EditCell(work_sheet, column_count, i_row, '', ans_color)
            white_cell.edit()
        print('Processing : {0}年{1}月{2}日({3})'.format(year, month, day, day_of_the_week))
        date = date + datetime.timedelta(days = 1)
        column_count += 1
    current_month += 1
# 工数の数式を代入する
for i_row in range(4,white_row_num + 4):
    numerical_formula ='=SUM(H'+str(i_row)+':'+get_column_letter(column_count - 1)+str(i_row)+')'
    work_sheet.cell(row = i_row, column = 6).value = numerical_formula

# ファイル保存
work_book.save(filename)
print('Finish!')
