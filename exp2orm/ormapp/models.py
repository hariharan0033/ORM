from django.db import models
from django.contrib import admin
class Student(models.Model):
    regno=models.IntegerField(primary_key="regno")
    name=models.CharField(max_length=20)
    dept=models.CharField(max_length=40)
    dob=models.DateField()
    cgpa=models.FloatField()

class StudentAdmin(admin.ModelAdmin):
    list_display=("regno", "name", "dept", "dob","cgpa") 