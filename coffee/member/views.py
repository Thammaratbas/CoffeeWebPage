from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"Home.html")

def coffee(request):
    return render(request,"Coffee.html")

def maker(request):
    return render(request,"maker.html")