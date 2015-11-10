# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, url
from main.views import *

urlpatterns = patterns("main.views",

    url("^home", "main_home", name="main_home"),

)
