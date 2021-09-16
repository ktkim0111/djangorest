"""MyApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    # rest_framework가 제공하는 auth
    path('api-auth/', include('rest_framework.urls')),
    # rest_auth가 제공하는 auth
    path('rest-auth/', include('rest_auth.urls')),
    # rest_auth가 제공하는 registration
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('first-app/', include('firstApp.api.urls')),
    path('cars-app/', include('cars.api.urls'))
]
