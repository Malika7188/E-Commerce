from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.orders.models import Order


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'accounts/order_history.html', {'orders': orders})