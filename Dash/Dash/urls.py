"""Dash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, re_path, path
#from dashboard.views import mi_vista


urlpatterns = [
    re_path(r'^dashboard/', include('dashboard.urls', namespace='dashboard')),
    #(r'^admin/', admin.site.url),
    path('admin/', admin.site.urls),
    #path('dashboard/', include('dashboard.urls')),
    #path('index', include('dashboard.urls'))
    #path('dashboard/', mi_vista.as_view()),

]
