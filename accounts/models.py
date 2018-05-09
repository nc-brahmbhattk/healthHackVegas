# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

"""
username : agowda
password : test1234
"""
class Drink(models.Model):
    """docstring forActivity."""
    flavor = models.IntegerField()
    size = models.IntegerField()
    protein = models.IntegerField(default=0)
    vitamin = models.IntegerField(default=0)
    probiotic = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
# Create your models here.
    def __str__(self):
        return str(self.date.date())

    def date_only(self):
        return self.date.date()
