from django.urls import path
from .views import all_clients, orders_by_client, order_full

urlpatterns = [
    path('', all_clients, name='all_clients'),
    path('client/<int:client_pk>', orders_by_client, name='orders_by_client'),
    path('order/<int:order_pk>', order_full, name='order_full'),
]
