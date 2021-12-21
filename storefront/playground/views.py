from django.core import exceptions
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F
from django.db.models.aggregates import Count, Max, Min, Avg
from store.models import OrderItem, Product, Customer, Order


def say_hello(request):

    #https://docs.djangoproject.com/en/4.0/ref/models/querysets/
    #Django database functions
    result = Product.objects.aggregate(count= Count('id'))
    return render(request, 'hello.html', {'name': 'Mosh','result': result})
