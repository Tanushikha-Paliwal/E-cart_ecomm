from django.shortcuts import render
from . models import *
from django.views import View
from django.db.models import Q

# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get (self , request):
     topwears = Product.objects.filter(category = 'TW')
     bottomwears = Product.objects.filter(category = 'BW')
     mobiles = Product.objects.filter(category = 'M')
     laptops = Product.objects.filter(category = 'L')
     return render(request , "app/home.html" , {"topwears":topwears , "bottomwears":bottomwears ,
                        "mobiles":mobiles ,  "laptops":laptops })
    

class ProductDetailView(View):
 def get(self , request , pk):
    product = Product.objects.get(pk = pk)
    item_already_in_cart = False
    if request.user.is_authenticated:
     item_already_in_cart = Cart.objects.filter(Q(product = product.id) & Q(user = request.user)).exists()
     return render(request , "app/productdetail.html" , {"product":product ,
                                                          "item_already_in_cart":item_already_in_cart})
    else:
      return render(request , "app/productdetail.html" , {"product":product ,
                                                          "item_already_in_cart":item_already_in_cart})
     

# def product_detail(request):
#  return render(request, 'app/productdetail.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
