from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField('Name', max_length=50)
    short_name = models.CharField('Short Name', max_length=20, unique=True)
    canceled = models.BooleanField('Canceled', default=False)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
    
    def __str__(self):
        return self.name
