from django.shortcuts import render

# Create your views here.

def products(request):
    data = {'title':"Daraz Ecom | product page dynamic title"}
    return render(request,"product.html",data)
