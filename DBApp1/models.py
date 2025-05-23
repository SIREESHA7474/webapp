from django.db import models

# Create your models here.
class Student(models.Model):
    empno = models.IntegerField()
    empname = models.CharField(max_length=20)
    salary = models.IntegerField()
