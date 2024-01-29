from django.contrib import admin
from django.urls import path


# import views
from ecom import settings
from .views import *
urlpatterns = [
    path('base/',base,name='base'),
    path('home/',home,name='home'),
    path('aboutus/',aboutus,name='aboutus'),
    path('contactus/',contactus,name='contactus'),
    path('category/<slug:val>',CategoryView.as_view(), name='category'),
    path('proddetail/<slug:val>',ProductDetail.as_view(),name='proddetail'),
    path('category-title/<val>', CategoryTitle.as_view(), name='category-title'),
]


