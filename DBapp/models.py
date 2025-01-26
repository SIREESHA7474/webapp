from django.db import models

# Create your models here.
#create table employee(empno int,empname varchar(20))
class Department(models.Model):
    deptno = models.IntegerField(primary_key=True)
    deptname = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

class Employee(models.Model):
    empno = models.IntegerField(primary_key=True)
    empname = models.CharField(max_length=20)
    salary = models.IntegerField()
    department = models.ForeignKey(Department,null=True,on_delete=models.SET_NULL)#models.cascade=if department is is dlt employees also dlt and models.sel_null=if the department is dlt not dlt the emplyee 