
from django.urls import path

from . import views


urlpatterns = [
    path('get-products/', views.products,name="wproducts"),

]