from django.db import models


# Create your models here.

class Block(models.Model):
    block_id = models.IntegerField(primary_key=True)
    lat = models.FloatField()
    lng = models.FloatField()
    quad = models.IntegerField()
    tag = models.CharField(max_length=100)
