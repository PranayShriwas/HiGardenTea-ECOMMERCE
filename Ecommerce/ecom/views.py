from django.shortcuts import render, redirect
from .models import *
from django.http.response import HttpResponse
from django.contrib import messages
# Create your views here.


def home(request):
    item = Product.objects.all()
    return render(request, 'home.html', {'item': item})


def about(request):
    return render(request, 'about.html')


def contact(request):
    per = Person.objects.all()
    return render(request, 'contact.html', {'per': per})


def infor(request):
    if request.method == 'POST':
        nm = request.POST['name']
        em = request.POST['email']
        su = request.POST['subject']
        me = request.POST['message']
        Person.objects.create(name=nm, email=em, subject=su, message=me)
        messages.success(
            request, "Your feedback has been received, you will get a response soon.")
        return redirect('/contact/')
