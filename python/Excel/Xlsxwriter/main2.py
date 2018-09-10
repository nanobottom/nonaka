import os, xlsxwriter
from editcell import EditCell

sheet_name = '2019年春期'
filename = '応用情報過去問答案.xlsx'
question_num = 80
answer_num = 5

current_dir = os.path.dirname(os.path.abspath(__file__))
xlsx_path = os.path.join(current_dir, filename)
try:
    if os.path.exists(xlsx_path) == True:
        raise SystemError('{}の"{}"が上書きされる恐れがあります。'.format(current_dir, filename))
except SystemError as e:
    print("SystemError : {}".format(e))
    exit()
else:
    wb = xlsxwriter.Workbook(filename)
ws = wb.add_worksheet(sheet_name)

for i_question in range(1, question_num + 1):
    i1 = EditCell(wb, ws, i_question, 1, '第' + str(i_question) + '問')
    i1.edit_font(bold = True)
    i1.edit_border_left()
    i1.edit_border_top()
    i1.edit_border_right()
    i1.edit_height_width(width = 6)
    i1.edit_fill(fgColor = 'green')
    i1.edit_alignment()
    for i_ans in range(1, answer_num + 1):
        status_cell = EditCell(wb, ws,i_question, i_ans + 1)
        status_cell.edit_fill(fgColor = 'white')
        status_cell.edit_alignment()
        status_cell.edit_border_round()
        status_cell.regulate_input_str(['○', '×'])

wb.close()
