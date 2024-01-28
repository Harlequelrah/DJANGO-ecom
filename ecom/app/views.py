from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import View




# Create your views here.
def base(request,*args,**kwargs):
   return  render(request,"base.html",{
      'home':"templates/app/home"
      })

def home(request,*args,**kwargs):
   return  render(request,"home.html",{})

from .models import Product
class CategoryView(View):
   def get(self,request,val):
      category_name=Product.get_category_name(val)
      product=Product.objects.filter(category=val)
      title=Product.objects.filter(category=val).values('title')
      return  render(request,"category.html",{
         'val':val,
         'category_name':category_name,
         'product':product,
         'title':title,
         })

