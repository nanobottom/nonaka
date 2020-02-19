import datetime
youbi = ('月', '火', '水', '木', '金', '土', '日')
today = datetime.date.today()
today_youbi ='(' +  youbi[today.weekday()] + ')'
today = today.strftime("%Y/%m/%d")
today = today + today_youbi
print(today)
