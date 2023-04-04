
from .views import *
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', main),
    path('login/', login, name='login'),
    path('api/', ajax_post_view, name='api')
]