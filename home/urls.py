from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('logi',views.logi,name='logi'),
    path('logo',views.logo,name='logo'),
    path('order',views.ord,name='order'),
    path('cont',views.cont,name='cont')
]