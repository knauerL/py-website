"""superlists URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from lists import views

urlpatterns = [
    url(r'^$', views.home_page, name="home"),
    #url(r'^(filename).html', views.page_page, name="page"),
    #url(r'^name.html', views.name_page, name="name"),
    url(r'^cat.html', views.cat_page, name="cat"),
    url(r'^dog.html', views.dog_page, name="dog"),
    url(r'^right.html', views.right_page, name="right"),
    url(r'^left.html', views.left_page, name="left"),
    url(r'^win.html', views.win_page, name="win"),
    url(r'^lose.html', views.lose_page, name="lose"),
]
