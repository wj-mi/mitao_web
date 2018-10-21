import datetime

from django.db import models
from django.utils import timezone



# Create your models here.


# ------------product ----------------
# class Tag(models.Model):
#     """product tag"""
#     tag_id = models.IntegerField("unique tag id")
#     intro = models.CharField("tag 描述")


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


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
