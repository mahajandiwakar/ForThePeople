from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Poll(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=100)
    poll_name = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)

    class Meta:
        ordering = ('created',)