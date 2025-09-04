from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.orders.models import Order
from .models import Payment


@login_required
def payment_process(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    if request.method == 'POST':
        # Here you would integrate with Stellar SDK
        # For now, we'll simulate a successful payment
        payment = Payment.objects.create(
            order=order,
            stellar_transaction_id=f"stellar_tx_{order.id}",
            amount=order.total_amount,
            status='completed'
        )
        order.status = 'paid'
        order.stellar_transaction_id = payment.stellar_transaction_id
        order.save()
        
        messages.success(request, 'Payment processed successfully!')
        return redirect('payments:payment_done')
    
    return render(request, 'payments/process.html', {'order': order})


def payment_done(request):
    return render(request, 'payments/done.html')


def payment_canceled(request):
    return render(request, 'payments/canceled.html')