from django.db import models

# Create your models here.

class Bookinfo(models.Model):
    title=models.CharField(max_length=250)
    year=models.IntegerField(null=True)
    summary=models.TextField()
