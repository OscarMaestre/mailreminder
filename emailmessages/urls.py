from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^crear_recordatorio/', views.create_reminder, name='create_reminder'),
]
