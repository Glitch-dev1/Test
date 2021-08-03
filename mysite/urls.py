"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from
    other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import register_request, logout_req, home_page, login_request
from products.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('Blog.urls')),
    path('product/', include('products.urls')),
    path('', home_page, name = 'home'),
    path('register/', register_request, name= "register"),
    path('login/', login_request, name= "login"),
    path('logout/', logout_req, name= "logout"),
]