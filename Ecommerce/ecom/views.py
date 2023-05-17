from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    item = Product.objects.all()
    return render(request, 'home.html', {'item': item})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
