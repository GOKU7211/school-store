from django.db import models

# Create your models here.
class formdb(models.Model):
    Gender=(
        ('Male','Male'),
        ('Female','Female')
    )
    name=models.CharField(max_length=255)
    dob=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=6,choices=Gender)
    phone=models.IntegerField()
    address=models.CharField(max_length=500)
    email=models.CharField(max_length=100)
    department=models.CharField(max_length=50)
    course=models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Department(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Course(models.Model):
    name=models.CharField(max_length=100)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name