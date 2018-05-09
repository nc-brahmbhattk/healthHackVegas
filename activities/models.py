# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

"""
username : agowda
password : test1234
"""
class Activity(models.Model):
    """docstring forActivity."""
    sleep = models.IntegerField()
    calories = models.IntegerField()
    steps = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

# Create your models here.
    def __str__(self):
        return str(self.date.date())

    def date_only(self):
        return self.date.date()
