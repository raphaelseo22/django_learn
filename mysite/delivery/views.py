from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import HTTP_HEADER_ENCODING
from rest_framework.parsers import JSONParser
from order.models import Shop, Menu, Order, Orderfood
from order.serializers import ShopSerializer, MenuSerializer

@csrf_exempt
def order_list(request):
    if request.method == "GET":     
        order_list = Order.objects.all()
        return render(request, 'delivery/order_list.html', {'order_list':order_list})

    elif request.method == "POST":
        order_itme = Order.objects.filter(pk=request.POST["order_id"])
        order_itme.deliver_finish = 1
        order_itme.save()
        return render(request, 'delivery/success.html')
    else:
        return HttpResponse(status=404)