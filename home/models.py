from django.db import models

# Create your models here.

class Test(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title