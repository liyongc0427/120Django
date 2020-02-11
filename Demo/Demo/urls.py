"""Demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about),
    path('index/', index),
    path('data/', data),
    path('indexhtml/',indexhtml),
    re_path("retest/(\d)/",retest),
    # re_path('textdemo/(\w*)/(\w*)/',textdemo),
    re_path('textdemo/(?P<year>\d{4})/(?P<city>\w*)/',textdemo),
    re_path("text/(?P<num1>\d{4})/(?P<num2>\w*)/",text),
]
