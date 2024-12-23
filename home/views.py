from django.shortcuts import render
from django.http import HttpResponse

from .models import Setting


# Create your views here.

def index(request):
    setting = Setting.objects.get()
    context = {'setting':setting}
    return render(request,'index.html',context)

def about(request):
    settings = Setting.objects.get()
    context = {'setting': settings}
    return render(request,'about.html',context)

def contact(request):
    setting = Setting.objects.get()
    context = {'setting': setting}
    return render(request,'contact.html',context)
