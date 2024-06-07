from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    # path('', product_list, name='product-list'),
    path('', ProductList.as_view(), name='product-list'),

    # path('product/<int:pk>/', product_detail, name='product-detail'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product-detail'),

    path('product/create/', product_create, name='product-create'),
    # Shopping Cart URLs
    path('cart/', cart_detail, name='cart-detail'),
    path('cart/add/<int:pk>/', cart_add, name='cart-add'),
    path('cart/remove/<int:pk>/', cart_remove, name='cart-remove'),
    path('cart/update/<int:pk>/', cart_update, name='cart-update'),
]