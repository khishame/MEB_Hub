from django.db import models
from django.utils import timezone

# Create your models here.
class Campus(models.Model):
    campus_id = models.BigAutoField(primary_key=True)
    campus_name = models.CharField(max_length=164)
    location = models.CharField(max_length=164)

    def __str__(self):
        return f"{self.campus_id} {self.campus_name} {self.location}"

class Student(models.Model):
    studentNumber = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100, default="")
    surname = models.CharField(max_length=100, default="")
    studentEmail = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    campus_id = models.ForeignKey(Campus, on_delete=models.CASCADE)
    login_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.studentNumber} {self.name} {self.surname}"

class RegisteredStudent(models.Model):
    studentNumber = models.CharField(max_length=20, primary_key=True)
    campus_id = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.studentNumber} {self.campus_id}"

class Admin(models.Model):
    admin_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    campus_id = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.admin_id} {self.name} {self.surname}"
