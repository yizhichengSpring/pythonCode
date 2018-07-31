from django.db import models

# Create your models here.
from django.db import models
class Person(models.Model):
    """
     编写person模型类
    """
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)

class CreateUpdate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

class Meta:
    abstract = True


class Person(CreateUpdate):
    """
     编写person模型类
    """
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)


class Order(CreateUpdate):
    order_id = models.CharField(max_length=30,db_index=True)
    order_desc = models.CharField(max_length=120)