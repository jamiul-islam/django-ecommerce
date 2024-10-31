from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Count, ExpressionWrapper, DecimalField
from store.models import Product, OrderItem, Customer, Order
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem
from django.db import transaction


def say_hello(request):
    # try:
    #     product = Product.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     pass

    # query_set = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    # query_set = Product.objects.filter(inventory = F('unit_price'))
    # query_set = Product.objects.only('id', 'title')
    # query_set = Product.objects.defer('description')
    # query_set = Product.objects.select_related('collection').all()
    # query_set = Product.objects.prefetch_related('promotions').select_related('collections').all()
    # query_set = Customer.objects.annotate(new_id = F('id') + 1)
    # query_set = Customer.objects.annotate(
    #     orders_count = Count('order')
    # )

    # discounted_price = ExpressionWrapper(F('unit_price') * F('inventory'), output_field=DecimalField())
    # query_set = Product.objects.annotate(discounted_price = discounted_price)

    # with transaction.atomic():
    #     order = Order()
    #     order.customer_id = 1
    #     order.save()

    #     item = OrderItem()
    #     item.order = order
    #     item.product_id = 1
    #     item.quantity = 1
    #     item.unit_price = 10
    #     item.save()

    return render(request, 'hello.html', {'name': 'Jami', 'product': list(query_set)})
