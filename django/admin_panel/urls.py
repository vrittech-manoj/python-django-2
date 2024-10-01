from . import views
from django.urls import path

urlpatterns = [
    path('dashboard/', views.index,name="admin_dashboard"),
    path('product/', views.product,name="admin_product"),
    path('account/', views.account,name="admin_account"),
    path('login/', views.admin_login,name="admin_login"),
    path('add-product/', views.AddProduct,name="product_add"),


]