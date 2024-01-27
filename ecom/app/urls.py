from django.contrib import admin
from django.urls import path
# import views
from .views import *
urlpatterns = [
    path('base/',base,name='base'),
    path('home/',home,name='home'),

]
