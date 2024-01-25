from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=30)
    cuisine_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name