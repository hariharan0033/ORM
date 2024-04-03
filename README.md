# Ex02 Django ORM Web Application
## Date: 03/04/2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

```
models.py
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

admin.py
from django.contrib import admin
from .models import Student,StudentAdmin
admin.site.register(Student,StudentAdmin)

```

## OUTPUT

![alt text](<Screenshot (175).png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
