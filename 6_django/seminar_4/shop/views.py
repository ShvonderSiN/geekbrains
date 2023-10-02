from django.db.models import Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import Client, Order, Good
from .forms import EditGoodForm

import logging

logger = logging.getLogger(__name__)


def all_clients(request: HttpRequest) -> HttpResponse:
    clients_with_order_counts = Client.objects.annotate(order_count=Count("orders"))
    return render(
        request, "shop/index.html", context={"clients": clients_with_order_counts}
    )


def orders_by_client(request: HttpRequest, client_pk: int) -> HttpResponse:
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


def order_full(request: HttpRequest, order_pk: int) -> HttpResponse:
    order = get_object_or_404(Order, pk=order_pk)
    goods = order.goods.all()
    context = {
        "order": order,
        "goods": goods,
    }
    return render(request, "shop/order_full.html", context=context)


def good_full(request: HttpRequest, good_pk: int) -> HttpResponse:
    good = get_object_or_404(Good, pk=good_pk)
    context = {
        "good": good,
    }
    return render(request, "shop/good_full.html", context=context)


def edit_good(request: HttpRequest, good_pk: int) -> HttpResponse:
    good = get_object_or_404(Good, pk=good_pk)
    if request.method == "POST":
        form = EditGoodForm(request.POST, request.FILES)
        if form.is_valid():
            good.title = request.POST["title"]
            good.description = request.POST["description"]
            good.price = request.POST["price"]
            good.quantity = request.POST["quantity"]
            if "image" in request.FILES:
                good.image = request.FILES["image"]
            good.save()
            logger.info(f"Good {good.title} edited")
            return redirect("good_full", good_pk=good.pk)
    else:
        form = EditGoodForm(
            initial={
                "title": good.title,
                "description": good.description,
                "price": good.price,
                "quantity": good.quantity,
            },
        )
    context = {
        "form": form,
        "good": good,
    }
    return render(request, "shop/edit_good.html", context=context)
