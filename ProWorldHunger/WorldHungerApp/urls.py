from django.urls import path
from django.conf.urls import include
from WorldHungerApp import views

urlpatterns = [
    path('', views.index, name='index'),
]
