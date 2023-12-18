import logging
import datetime
import argparse
from datetime import datetime
from collections import namedtuple
logging.basicConfig(filename="log1.log", encoding="utf8", level=logging.INFO) 
logger = logging.getLogger("log") 

MONTHS = {
'января': 1,
'февраля': 2,
'марта': 3,
'апреля': 4,
'мая': 5,
'июня': 6,
'июля': 7,
'августа': 8,
'сентября': 9,
'октября': 10,
'ноября': 11,
'декабря': 12
}
WEEKDAYS = {
'понедельник': 0,
'вторник': 1,
'среда': 2,
'четверг': 3,
'пятница': 4,
'суббота': 5,
'воскресенье': 6
}

DATE = namedtuple("DATE", "day month year") 

def get_date(text):  
    num_week, week_day, month = text.split()
    try: 
        if 5 > int(num_week.split("-") [0]) > 0:
            num_week = int(num_week.split("-") [0]) 
        else:
            return "\nнеправильно введен номер дня недели"
    except:
        return "\nнеправильно введен номер дня недели"
    
    if week_day in WEEKDAYS:
        week_day = WEEKDAYS[week_day]
    else:    
        return "\nнеправильно введено название дня недели"
    if month not in MONTHS:  
        return "\nнеправильно введено название месяца"
    year=datetime.today().year
    x = datetime(year, MONTHS[month], 1).weekday()
    count_week = 0
    for day in range(1, 31+1):
        d = DATE(year=year , month=MONTHS[month], day=day) 
        if x == week_day:
            count_week +=1
        x = x - 6 if x == 6 else x + 1
        if count_week == num_week:
            logger.info(DATE(d.day, d.month, d.year)) 
            return d
    return "в этом месяце нет столько дней недели" 

parser = argparse.ArgumentParser(usage='Не введены значения аргументами')
parser.add_argument(dest='num_week', type=str)
parser.add_argument(dest='week_day', type=str)
parser.add_argument(dest='month', type=str)
args = parser.parse_args()
print(get_date(args.num_week + " " + args.week_day + " " + args.month))
print(get_date(input("введите текст вида: '1-й четверг ноября' -> ")))