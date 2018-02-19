from django.urls import path
from stocksapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('getlivedata/',views.get_data, name='getlivedata'),
    path('gethistdata/',views.get_data, name='gethistdata'),
]
