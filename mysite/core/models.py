from django.db import models

# Create your models here.

class Class1(models.Model):
    field1 = models.CharField(max_length=240)
    field2 = models.DateField(auto_now=True)

