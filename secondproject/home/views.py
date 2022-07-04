from unicodedata import category
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Contact, Order, orderupdate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from datetime import *
import json
# Create your views here.
def home(request):
    messages.success(request, 'Sale is live now! Checkout our New Arrivals!')
    dateset = date(2022,6,16)
    items=Product.objects.filter(pub_date__gte=dateset)
    params = {"items": items}
    return render(request , 'index.html', params)


def shop(request):
    allprods = []
    catprods = Product.objects.values('Category')
    cats = {item['Category'] for item in catprods}
    for cat in cats:
        prod= Product.objects.filter(Category=cat)
        allprods.append([prod, range(1,5)])
    params = {'allproducts': allprods}
    
    # params = ['products': prod, 'range': range(1,5)]
    return render( request, "shop.html", params)

def contact(request):
    if request.method == "POST":
        name =request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        state = request.POST.get('state')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        text = request.POST.get('text')
        contact = Contact(name=name, email=email, phone=phone, address=address, state=state, city=city, pincode=pincode, textarea=text)
        contact.save()
        messages.success(request, "Your query has been successfully submitted we will reach out to you shortly!")
    
    return render(request, "contact.html")


def handlesignup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get("phone")
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1!=pass2:
            messages.error(request, "Passwords Do not match")
            return redirect("http://127.0.0.1:8000")
        
        if username.isalnum()!= True:
            messages.error(request, "Username can only contain letters and numbers")
            return redirect("http://127.0.0.1:8000")

        

        myuser = User.objects.create_user(username=username, email=email, password=pass1)
        myuser.first_name= fname
        myuser.last_name = lname
        myuser.phone = phone
        myuser.save()
        messages.success(request, "Congratulations! You have been Signed up with us")
        return redirect('http://127.0.0.1:8000')
    else:
        return HttpResponse('404-not found')

def handlelogin(request):
    if request.method == "POST":
        loginusername = request.POST.get('loginusername')
        password = request.POST.get('loginpass')

        user = authenticate(request ,username=loginusername, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in successful')
        
        else:
             messages.error(request, 'Check your credentials!')
        
        return redirect("http://127.0.0.1:8000")
    else:
        return HttpResponse('404-not found')

def handlelogout(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("http://127.0.0.1:8000")


def checkout(request):
    if request.method == "POST":
        jsonitems = request.POST.get("jsonitems")
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zipcode = request.POST.get("zipcode")

        orders = Order(jsonitems=jsonitems, name=name, email=email, phone=phone, address=address, city=city, state=state, zipcode=zipcode)
        orders.save()
        thank = True
        order_id= orders.order_id
        return render(request , 'checkout.html', {"thank": thank, "id": order_id})
    else:
        return render(request , 'checkout.html')



def fashprods(request):
    allprods = Product.objects.filter(Category = "Fashion")
    params = {"allprods": allprods}
    return render(request , 'fashion.html', params)


def elecprods(request):
    return render(request , 'electronics.html')


def statprods(request):
    allprods = Product.objects.filter(Category = "Stationary")
    params = {"allprods": allprods}
    return render(request , 'stationary.html', params)

def search(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if len(query) == 0:
            messages.error(request, "Your search was empty")
    

        if len(query) > 40:
            allprods = []
            messages.error(request, 'Your query exceeds the word limit of 40 words try again')
        else:
            allprodsname = Product.objects.filter(product_name__icontains = query)
            allprodcat = Product.objects.filter(Category__icontains = query)
            allproddesc = Product.objects.filter(description__icontains = query)
            allprods = allprodsname.union(allproddesc , allprodcat)

        # if allprods.count() == 0:
        #     messages.error(request, 'Your query exceeds the word limit of 40 words try again')
        # if allprods == Product.object.none():
        #     messages.error(request, "No results found")
    params = {"allprods": allprods , "query": query}
    return render(request, 'search.html' , params)

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get("orderid")
        email = request.POST.get("email")

        try:
            orderver = Order.objects.filter(order_id=orderId, email=email)
            if len(orderver)>0:
                update = orderupdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({"text": item.update_desc, "time":item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                messages.error(request, "There is no matching id and email of this sort. Please try again with correct entries")
                return redirect ("/tracker/")
        except Exception as e:
            return HttpResponse(f"exception{e}")

            
            
    return render(request, "tracker.html")
