from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.core import serializers

from .models import Orders

"""用户信息"""


def get_user_orders(request, user_id):
    """获取用户所有订单信息
    user_id： wx user id
    """
    data = {}
    orders = Orders.objects.filter(user=user_id)
    data["result"] = "success"
    data["data"] = serializers.serialize("json",orders)
    return JsonResponse(data)
