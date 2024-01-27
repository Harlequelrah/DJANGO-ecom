from django.shortcuts import render

# Create your views here.
def base(request,*args,**kwargs):
   return  render(request,"base.html",{})

def home(request,*args,**kwargs):
   return  render(request,"home.html",{})

