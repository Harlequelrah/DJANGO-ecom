from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import View




# Create your views here.
def base(request,*args,**kwargs):
   return  render(request,"base.html",{
      # 'home':"home.html"
      })

def home(request,*args,**kwargs):
   return  render(request,"home.html",{})
def aboutus(request,*args,**kwargs):
   return  render(request,"aboutus.html",{})
def contactus(request,*args,**kwargs):
   return  render(request,"contactus.html",{})

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

class ProductDetail(View):
   def get(self,request,val):
      product=Product.objects.get(title=val)
      return render(request,'productdetail.html',{'val':val,'product':product})

# class ProductDetail(View):
#    def get(self,request,pk):
#       product=Product.objects.get(pk=pk)
#       return render(request,'productdetail.html',{'pk':pk,'product':product})
class CategoryTitle(View):

   def get(self, request, val):
      product=Product.objects.filter(title=val)
      #recuperer le title des produits de chaque valeur de category
      title=Product.objects.filter(category=product[0].category).values('title')
      return render(request, "category.html",{'val':val,'title':title})
