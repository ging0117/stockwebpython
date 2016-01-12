#from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Stock(models.Model):
    symbol=models.CharField(max_length=10)
    qty=models.IntegerField()
    purchaser=models.ForeignKey(User, related_name='stocks')

    def __unicode__(self):
        return self.symbol
