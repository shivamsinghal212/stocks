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


def get_function_list():
    function_list = ['TIME_SERIES_DAILY','TIME_SERIES_WEEKLY','TIME_SERIES_MONTHLY']
    return function_list




def home(request):
    context = {

    }
    return render(request,'index.html', context)


def get_data(request):
    if request.method == 'POST' and 'Livedata' in request.POST:
        symbol = str(request.POST.get('get_symbol'))
        functions = str(request.POST.get('get_function'))
        key = 'LSFIEW3MWL734JUH'
        url = 'https://www.alphavantage.co/query?function='+functions+'&symbol='+symbol+'&apikey='+key
        if functions == 'TIME_SERIES_DAILY':
            var = 'Time Series (Daily)'
        elif functions == 'TIME_SERIES_WEEKLY':
            var = 'Weekly Time Series'
        else:
            var = 'Monthly Time Series'
        data = requests.get(url).json()[str(var)]
        transformed = [(v.update({'Time': k}) or v) for (k, v) in data.items()]
        transformed_list = []
        for x in transformed:
            x['open'] = x.pop('1. open')
            x['high'] = x.pop('2. high')
            x['low'] = x.pop('3. low')
            x['close'] = x.pop('4. close')
            x['volume'] = x.pop('5. volume')
            transformed_list.append(x)

        context = {
            'ticker_list': get_ticker_list(),
            'function_list': get_function_list(),
            'data': transformed_list,
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
    else:
        context = {
            'ticker_list': get_ticker_list(),
            'function_list': get_function_list(),
        }
        return render(request, "livedata.html", context)






