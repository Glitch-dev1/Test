from django.db import models

# Create your models here.
class usertype(models.Model,user):
    is_staff  = models.BooleanField(default=False)
    is_client = models.BoleanField()
    