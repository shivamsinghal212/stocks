from django.shortcuts import render
from .models import HistStocks
import requests
# Create your views here.


def get_ticker_list():
    ticker_list = []
    ticker = HistStocks.objects.values('symbol').distinct()
    for i in ticker:
        for k,v in i.items():
            if k == 'symbol':
                ticker_list.append(v)
                ticker_list.sort()
    return ticker_list


def home(request):
    context = {
        'ticker_list': get_ticker_list()
    }
    return render(request,'index.html', context)


def get_data(request):
    if request.method == 'POST' and 'Livedata' in request.POST:
        symbol = str(request.POST.get('get_symbol'))
        key = 'LSFIEW3MWL734JUH'
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+symbol+'&interval=1min&apikey='+key
        data = requests.get(url).json()
        l = list(data.values())[1]
        time = []
        values = []
        for k, v in l.items():
            time.append(k)
            values.append(v)
        open = []
        high = []
        low = []
        close = []
        volume = []
        d = {'time': '', 'open': '', 'high': '', 'low': '', 'close': '', 'volume': ''}
        for i in values:
            for k, v in i.items():
                if k == '1. open':
                    open.append(v)
                elif k == '2. high':
                    open.append(v)
                elif k == '3. low':
                    open.append(v)
                elif k == '4. close':
                    open.append(v)
                elif k == '5. volume':
                    open.append(v)
        d['time'] = time
        d['open'] = open
        d['high'] = high
        d['low'] = low
        d['close'] = close
        d['volume'] = volume

        context = {
            'data': d,
        }
        return render(request,"livedata.html",context)
    elif request.method == 'POST' and 'Histdata' in request.POST:
        symbol = str(request.POST.get('get_symbol'))
        start_date = request.POST.get('startdate')
        end_date = request.POST.get('enddate')
        data = HistStocks.objects.filter(symbol=symbol, date__range=(start_date, end_date)).values()
        context = {
            'data': data
        }
        return render(request,"histdata.html",context)






