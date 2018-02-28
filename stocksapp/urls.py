from django.urls import path
from stocksapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('intradaydata/',views.get_intra_day_data, name='getintradaylivedata'),
    path('livedata/',views.get_data, name='getlivedata'),
    path('adjlivedata/',views.get_adj_data, name='getadjlivedata'),
    path('gethistdata/',views.get_data, name='gethistdata'),
]
