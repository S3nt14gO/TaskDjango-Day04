from django.db import models

# Create your models here.
class Sections(models.Model):
    id = models.AutoField(primary_key=True)
    section_name = models.CharField(max_length=30)

class Book(models.Model):
    bid = models.AutoField(primary_key=True)
    bname=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    section=models.ForeignKey(to='Sections',on_delete=models.CASCADE)

class AddUser(models.Model):
    uid=models.AutoField(primary_key=True)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    email=models.CharField(max_length=50)

class ApiUser(models.Model):
    aid=models.AutoField(primary_key=True)
    apiname=models.CharField(max_length=30)
    apiaddress=models.CharField(max_length=30)
    apiemail=models.CharField(max_length=50)