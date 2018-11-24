from django.db import models

# Create your models here.
class Data(models.Model):
    url = models.CharField(max_length = 200)
    thumbnail = models.CharField(max_length = 200)
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    date = models.CharField(max_length = 200)
    topic = models.CharField(max_length = 200)
    sentiment_value = models.IntegerField(default = 0)