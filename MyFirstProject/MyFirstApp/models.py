from django.db import models

class MyFirstModel(models.Model):
    MyFirstField = models.CharField(max_length=10)
