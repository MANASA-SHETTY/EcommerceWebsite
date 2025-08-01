from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name='home'),
    path('product/<int:pk>/',views.product_detail, name='product_detail'),
    path('cart/', views.cart_view, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.order_history, name='orders'),
]

