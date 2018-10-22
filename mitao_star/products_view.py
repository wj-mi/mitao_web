# -*- coding:utf-8 -*-

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.views.generic import ListView
from django.core import serializers
from django.views import View


from .models import Products, Orders


class ProductsListView(View):

    def get(self, request):
        products = Products.objects.all()
        data = {}

        print("product len: {}".format(len(products)))
        print(products)
        products = serializers.serialize("json", products)
        data["product"] = products
        response = JsonResponse(data)
        return response



class ProductView(View):

    def get(self, request, p_id):
        product = Products.objects.filter(product_id=p_id)
        if not product:
            print("Product not found, Check id: {}".format(p_id))
        # product.create_time = product.create_time.strftime('%a, %d %b %Y %H:%M:%S GMT')
        data = {}
        data["result"] = "success"
        data["data"] = serializers.serialize("json", product)
        return JsonResponse(data)

# -------- 订单------
class OrderView(View):

    def get(self, request, order_id):
        data = {}
        order = Orders.objects.filter(order_id=order_id)
        if not order:
            data["result"] = "falt"
            print("order not found")
            data["data"] = "Check you order_id:"
        else:
            data["result"] = "success"
            data["data"] = serializers.serialize("json", order)
        return JsonResponse(data)

    def post(self, request, order_id):
        """create new order
        order_id from front
        """
        pass

    def put(self, request, order_id):
        pass



