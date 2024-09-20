from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    data = {'title':"Daraz Ecom | Index page dynamic title",'page_heading':"Home Page"}
    return render(request,"index.html",data)
    # return HttpResponse("<html><body><marquee><h1 style='color:red;'>this is contact</h1></marquee> </body></html>")

def about(request):
    return HttpResponse("<html><body><marquee><h1 style='color:red;'>this is about</h1></marquee> </body></html>")
