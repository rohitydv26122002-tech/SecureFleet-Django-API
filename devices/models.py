from django.db import models

# Create your models here.

class Device(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default="offline")
    last_seen = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name