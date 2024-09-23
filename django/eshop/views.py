from django.shortcuts import render
from product.models import Banner,Product

def index(request):
    banner = Banner.objects.all()
    products = Product.objects.all()
    data = {
        'banners':banner,
        'products':products,
    }
    return render(request,"index.html",data)