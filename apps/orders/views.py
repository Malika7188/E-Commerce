from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.cart.cart import Cart
from .models import OrderItem, Order
from .forms import OrderCreateForm


@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_amount = cart.get_total_price()
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                       product=item['product'],
                                       price=item['price'],
                                       quantity=item['quantity'])
            # clear the cart
            cart.clear()
            messages.success(request, 'Your order has been placed successfully!')
            return redirect('orders:order_detail', order_id=order.id)
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order/detail.html', {'order': order})