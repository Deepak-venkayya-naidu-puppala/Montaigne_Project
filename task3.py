import datetime as dt 

from datetime import timedelta 

date_input = input()

tmp = date_input.split('-')

delimiter = '-'

if len(tmp) == 1:
    tmp = date_input.split('/')
    delimiter = "/"
tmp = [int(i) for i in tmp]
date = dt.date(tmp[2], tmp[1], tmp[0])

after_adding_one_day = date + timedelta(days=1)

after_adding_one_day = after_adding_one_day.strftime('%d{}%m{}%Y'.format(delimiter, delimiter))

print(after_adding_one_day)