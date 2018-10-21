# -*- coding:utf-8 -*-

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.views.generic import ListView
from django.core import serializers
from django.views import View


from .models import Products


class ProductsView(View):

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

    def get(self, p_id):
        product = Products.objects.filter(product_id=p_id)
        if not product:
            print("Product not found, Check id: {}".format(p_id))
        product.create_time = product.create_time.strftime('%a, %d %b %Y %H:%M:%S GMT')
        response = HttpResponse(product)
        return response


