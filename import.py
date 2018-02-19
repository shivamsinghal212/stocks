import csv,sys,os
project_dir = r'C:\Users\singishi\PycharmProjects\Stocks\Stocks'
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django
django.setup()

from stocksapp.models import HistStocks

data = csv.reader(open(r'C:\Users\singishi\Downloads\prices763fefc.csv'))

for row in data:
    if row[0] != 'date':
        histdata = HistStocks()
        histdata.date = row[0]
        histdata.symbol = row[1]
        histdata.open = row[2]
        histdata.close = row[3]
        histdata.low = row[4]
        histdata.high = row[5]
        histdata.volume = row[6]

        histdata.save()


