from email import message
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from datetime import *
from home.models import Product
# from tempfile import templates

def home(request):
    messages.success(request, 'Sale is live now! Checkout our New Arrivals!')
    dateset = date(2022,6,16)
    print(dateset)
    items=Product.objects.filter(pub_date__gte=dateset)
    params = {"items": items}
    return render(request , 'index.html', params)

