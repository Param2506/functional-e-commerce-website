from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("" , views.home, name="home"),
    path("shop/", views.shop, name="shop"),
    path("contact/", views.contact, name="contact"),
    path("signup/", views.handlesignup, name="handlesignup"),
    path("login/", views.handlelogin, name="handlelogin"),
    path("checkout/", views.checkout, name="checkout"),
    path("fashion/", views.fashprods, name="fashionproducts"),
    path("stationary/", views.statprods, name="stationaryproducts"),
    path("electronics/", views.elecprods, name="electronicsproducts"),
    path("search/", views.search, name="search"),
    path("logout/", views.handlelogout, name="handlelogout"),
    path("tracker/", views.tracker, name="tracker"),
]