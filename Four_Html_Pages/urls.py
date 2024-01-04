"""
URL configuration for Four_Html_Pages project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Html_Pages_App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('templates1/',templates1,name='templates1'),
    path('templates2/',templates2,name='templates2'),
    path('templates3/',templates3,name='templates3'),
    path('templates4/',templates4,name='templates4'),
    
]
