from django.urls import path
from . import views

app_name = 'sstest'
urlpatterns = [
    path('main/', views.main, name='main'),
    path('qSet/', views.qSet, name='qSet'),
    path('result/', views.result, name='result'),
    path('result1/', views.result1, name='result'),
    path('result2/', views.result2, name='result'),
    path('result3/', views.result3, name='result'),
    path('result4/', views.result4, name='result'),
 
    
]