from django.shortcuts import render
from product.models import Product
# Create your views here.

def allprod(request):
    all_products = Product.objects.all()
    data = {
        'products': all_products
    }
    return render(request,"products.html",data)

def productDetail(request,id):

    single_product = Product.objects.filter(id=id).first()
    data = {
        'product':single_product,
    }
    return render(request,"single_product.html",data)