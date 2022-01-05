from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import HTTP_HEADER_ENCODING
from rest_framework.parsers import JSONParser
from order.models import Shop, Menu, Order, Orderfood
from order.serializers import ShopSerializer, MenuSerializer

@csrf_exempt
def order_list(request, shop):
    if request.method == "GET":     
        order_list = Order.objects.filter(shop=shop)
        return render(request, 'boss/order_list.html', {'order_list':order_list})
    else:
        return HttpResponse(status=404)


@csrf_exempt
def time_input(request):
    if request.method == "POST":
        order_itme = Order.objects.filter(pk=request.POST["order_id"])
        shop = order_itme.shop.id
        order_itme.estimate_time = int(request.POST["estimate_time"])
        order_itme.save()
        return render(request, 'boss/success.html', {"shop":int(shop)})
    else:
        return HttpResponse(status=404)