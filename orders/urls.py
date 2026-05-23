from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('my_orders/', views.my_orders, name='my_orders'),
    path('create/<int:excursion_id>/', views.order_create, name='order_create'),
    path('cancel/<int:order_id>/', views.cancel_order, name='cancel_order'),
    path('dashboard/', views.user_orders, name='user_orders'),
]
