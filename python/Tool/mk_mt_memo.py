from datetime import datetime

today = datetime.today().strftime('%Y/%m/%d %H:%M')
today_for_filename = datetime.today().strftime('%Y%m%d')
mt_title = input('議事録のタイトル：')
place = input('開催場所：')
recorder = input('記録者：')
attendees = list()
while(1):
    attendee = input('出席者(Enterのみで終了)：')
    if attendee == '':
        break
    else:
        attendees.append(attendee)
attendees.append(recorder)
attendees = ', '.join(attendees)

memo_tmp = """■■■{0} 議事録■■■
[開催場所]{1}
[開催日時]{2} ～ :
[出席者]{3}(記)

【概要】
・
・
・

【To Doリスト】
・
・
・
以上
""".format(mt_title, place, today, attendees)

filename = today_for_filename + '_' + mt_title + '議事録.txt'

with open(filename, 'w') as f:
    f.write(memo_tmp)
