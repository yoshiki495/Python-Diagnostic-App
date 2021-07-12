"""config URL Configuration

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
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.start),
    path('accounts/', include('allauth.urls')),
    path('q1/', views.q1),
    path('q2/', views.q1),
    path('q3/', views.q1),
    path('q4/', views.q1),
    path('q5/', views.q1),
    path('q1_post/', views.q1_post, name='q1_post'),
    path('q2_post/', views.q2_post, name='q2_post'),
    path('q3_post/', views.q3_post, name='q3_post'),
    path('q4_post/', views.q4_post, name='q4_post'),
    path('q5_post/', views.q5_post, name='q5_post'),
    path('chart/', views.chart, name='chart')
]
