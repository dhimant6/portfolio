from django.db import models

# Create your models here.
class resume(models.Model):
    Brief_description = models.CharField(max_length=200)
    Education = models.TextField(blank=True)
    Experience = models.DecimalField(decimal_places=2, max_digits=1000)
    Projects = models.CharField(max_length=200)
    IsActive = models.BooleanField()
