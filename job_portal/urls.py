"""job_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from core.views import core
from registrationapp.views import signup
from registrationapp.views import login
from info.views import info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core, name='core'),
    path('signup/', signup, name='signup'),
    path('signup/login/', login, name='login'),
    path('info/', info, name='info'),
]
