import jholiday
import datetime
import calendar

def count_workdays(start, end):
    """
    指定した開始日から終了日の平日（就業日）をカウントする
    start, end:'yyyy/mm/dd'の文字列形式
    """
    start_date = datetime.datetime.strptime(start, '%Y/%m/%d')
    end_date = datetime.datetime.strptime(end, '%Y/%m/%d')
    one_day = datetime.timedelta(days=1)
    count = 0
    while start_date != end_date+one_day:
        print(start_date.strftime('%Y/%m/%d'), end='')
        if start_date.weekday() not in\
            (calendar.SATURDAY, calendar.SUNDAY)\
            and jholiday.holiday_name(start_date.year,\
            start_date.month, start_date.day) is None:
            count += 1
            print('')
        else:
            print('(休)')
        

        start_date += one_day
    return count

if __name__ == '__main__':
    start = '2020/4/1'
    end = '2020/4/30'
    print('就業日：{}日'.format(count_workdays(start, end)))


#if jholiday.holiday_name(date.year, date.month, date.day) is not None:


