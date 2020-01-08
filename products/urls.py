from django.contrib import admin
from django.urls import path

from products.views import product_detail_view, product_create_view, product_detail_view_with_id, all_product_detail_view

app_name = "products"
urlpatterns = [
    # path('product/', product_detail_view,),
    path('<int:id>', product_detail_view_with_id, name="product-detail-id"),
    path('', all_product_detail_view, name="product-list"),
    path('create', product_create_view, name="create-product")
]
