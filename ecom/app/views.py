from django.shortcuts import render
from django.urls import reverse



# Create your views here.
def base(request,*args,**kwargs):
   return  render(request,"base.html",{
      'home':"templates/app/home"
      })

def home(request,*args,**kwargs):
   return  render(request,"home.html",{})

