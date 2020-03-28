"""avalon URL Configuration

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
from django.urls import path
from main import views as main_views

urlpatterns = [
    path('', main_views.init),
    path('create/',main_views.create),
    path('update/',main_views.update),
    path('join/',main_views.join),
    path('leave/',main_views.leave),
    path('start/',main_views.start),
    path('delete/',main_views.delete),
    path('vote/<int:choice>/',main_views.vote),
]
