from django.contrib import admin
from django.urls import path


# import views
from ecom import settings
from .views import *
urlpatterns = [
    path('base/',base,name='base'),
    path('home/',home,name='home'),
    path('category/<slug:val>',CategoryView.as_view(), name='category'),
]


