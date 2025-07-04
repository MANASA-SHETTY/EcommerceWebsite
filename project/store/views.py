from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, CartItem, Order, OrderItem
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')


@login_required
def cart_view(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in items)
    return render(request, 'store/cart.html', {'items': items, 'total': total})

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('cart')


@login_required
def checkout(request):
    items = CartItem.objects.filter(user=request.user)
    if request.method == 'POST':
        order = Order.objects.create(user=request.user, is_paid=True)
        for item in items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
        items.delete()
        return redirect('orders')
    total = sum(item.total_price() for item in items)
    return render(request, 'store/checkout.html', {'items': items, 'total': total})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'store/orders.html', {'orders': orders})



