# product_app/urls.py
from django.urls import path
from .views import product_list
from django.urls import path
from .views import *

urlpatterns = [
    path('', product_list, name='product_list'),
    path('productsubcatlist/<int:product_id>/', product_subcat_list, name='product_subcat_list'),
    path('add-product-subcat/<int:product_id>/', add_product_subcat, name='add_product_subcat'),
    path('edit-product-subcat/<int:product_id>/<int:subcat_id>/', edit_product_subcat, name='edit_product_subcat'),
    path('delete-product-subcat/<int:product_id>/<int:subcat_id>/', delete_product_subcat,name='delete_product_subcat'),
    path('search/', search_products, name='search_products'),
    path('product_detail/<int:product_id>/', product_detail, name='product_detail'),
]

