from django.db.models import Count
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from shop.models import Client, Order


def all_clients(request: HttpRequest) -> render:
    clients_with_order_counts = Client.objects.annotate(order_count=Count("orders"))
    return render(
        request, "shop/index.html", context={"clients": clients_with_order_counts}
    )


def orders_by_client(request: HttpRequest, client_pk: int) -> render:
    client = get_object_or_404(Client, pk=client_pk)
    orders = client.orders.all()
    all_goods_by_client = set()
    for order in orders:
        all_goods_by_client.update(order.goods.all())
    goods = sorted(list(all_goods_by_client), key=lambda good: good.pk, reverse=True)
    context = {
        "client": client,
        "orders": orders,
        "goods": goods,
    }
    return render(request, "shop/orders_by_client.html", context=context)


def order_full(request: HttpRequest, order_pk: int) -> render:
    order = get_object_or_404(Order, pk=order_pk)
    goods = order.goods.all()
    context = {
        "order": order,
        "goods": goods,
    }
    return render(request, "shop/order_full.html", context=context)
