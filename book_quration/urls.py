"""book_quration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url, include
from blog.views import *

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    url(r'^category_02_women/', category_02_women, name='category_02_women'),
    url(r'^category_01_economics/', category_01_economics, name='category_01_economics'),
    url(r'^category_03_art/', category_03_art, name='category_03_art'),
    url(r'^category_04_humanities/', category_04_humanities, name='category_04_humanities'),
    url(r'^category_05_science/', category_05_science, name='category_05_science'),

]
