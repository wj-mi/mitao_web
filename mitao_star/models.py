import datetime
import uuid

from django.db import models
from django.utils import timezone



# Create your models here.


# ------------product ----------------

class Products(models.Model):
    """product info"""
    product_id = models.CharField("unique product id", unique=True, max_length=40)
    name = models.CharField('Product name', max_length=200)
    introduct = models.CharField("breaf introduct", max_length=300)
    price = models.FloatField("商品价格")
    head_image = models.ImageField('图片', upload_to="productHeads")
    create_time = models.DateTimeField("创建时间")
    last_update_time = models.DateTimeField("上次更新时间", auto_now=True)
    #
    tags = models.IntegerField("tag", default=0)

    def __str__(self):
        return "Product id {}, name: {}".format(self.product_id, self.name)


class Orders(models.Model):
    """订单"""
    order_id = models.CharField("unique order id", unique=True, default=uuid.uuid4().hex, max_length=40)
    products = models.ManyToManyField(Products)
    user = models.CharField(help_text=" 微信用户ID", max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=0, help_text=" 状态0 待支付，1：服务中 2：待评价 3：已完成 -1：删除 ")
    is_delete = models.BooleanField(default=False, help_text="False:未关闭，正常订单")

    class Meta:
        db_table = "Orders"     # db table name
