from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Stock(models.Model):
    ticker = models.CharField(max_length=10)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ticker
