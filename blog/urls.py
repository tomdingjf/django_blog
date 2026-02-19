# -*- coding: utf-8 -*-
# @Time: 2026/2/19 22:26
# @Author: Ding

from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index,name='index'),
]
