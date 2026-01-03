from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('auth/', views.AuthView.as_view(), name='auth'),
    path('admin_register/', views.admin_register_view, name='admin_register'),
]