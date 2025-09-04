from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('orders/', views.order_history, name='order_history'),
]