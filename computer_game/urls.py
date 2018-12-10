"""computer_game URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('login/',views.login.as_view(),name='login'),
    path('register/',views.register.as_view(),name='register'),
    path('k1/', views.k1,name='k1'),
    path('center/', views.center,name='center'),
    re_path('doctor/p=(\d+)', views.doctor,name='doctor'),
    path('info/', views.info,name='info'),
    re_path('time/p=(\d+)', views.time,name='time'),
    path('wodepaihao/', views.wodepaihao,name='wodepaihao'),
    path('yuyuepaidui/', views.yuyuepaidui,name='yuyuepaidui'),
    path('footer/', views.footer,name='footer'),
    path('login_out/', views.login_out,name='login_out'),
]
