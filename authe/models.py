from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class registermodel(User):
    phone=models.BigIntegerField(unique=True)
    age=models.IntegerField()
    choices=[['Male','MALE'],['Female','FEMALE']]
    gender=models.CharField(max_length=10,choices=choices)
    dob=models.DateField()









   