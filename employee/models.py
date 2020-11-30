from django.db import models
#importar tabla department
from department.models import Department
from ckeditor.fields import RichTextField

# Create your models here.
class Skills(models.Model):
    skill = models.CharField('Skill', max_length=50)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
    
    def __str__(self):
        return self.skill

class Employee(models.Model):
    JOB_CHOICES = [
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    ]

    first_name = models.CharField('Names', max_length=100)
    last_name = models.CharField('Last Name', max_length=100)
    full_name = models.CharField('Complete Name', max_length=120, blank=True)
    job = models.CharField('Job', max_length=50, choices=JOB_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='employee', blank=True, null=True)
    skill = models.ManyToManyField(Skills)
    cv = RichTextField()

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return str(self.id) + '-' + self.first_name + ' ' + self.last_name