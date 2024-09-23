from django.urls import path
from . import views

urlpatterns = [
    path('products/',views.allprod,name='getproducts'),
    path('product-details/<int:id>/',views.productDetail,name='productdetail'),
]