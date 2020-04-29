from django.db import models


class Wine(models.Model):
    country = models.CharField(max_length=50)
    description = models.TextField()
    designation = models.CharField(max_length=50)
    points = models.IntegerField()
    price = models.FloatField(null=True)
    province = models.CharField(max_length=50)
    region_1 = models.CharField(max_length=50)
    region_2 = models.CharField(max_length=50)
    taster_name = models.CharField(max_length=50)
    taster_twitter_handle = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    variety = models.CharField(max_length=50)
    winery = models.CharField(max_length=50)
