"""
URL configuration for application project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_day/', views.add_day, name='add_day'),
    path('add_day_submit/', views.add_day_submit, name='add_day_submit'),
    path('info_day/', views.info_day, name='info_day'),
    path('info_day_submit/', views.info_day_submit, name='info_day_submit'),
    path('info_activity/', views.info_activity, name='info_activity'),
    path('info_activity_submit/', views.info_activity_submit, name='info_activity_submit')

]
