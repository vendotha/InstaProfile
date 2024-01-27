import datetime
from time import time

from django.db import models



branch = [('CSE','CSE'),('ECE','ECE'),('EEE','EEE'),('MECH','MECH'),('CIVIL','CIVIL')]
types = [('1st Year','1st Year'),('2nd Year','2nd Year'),('3rd Year','3rd Year')]
class Profile(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    date = models.DateField()
    pin = models.CharField(max_length=12)
    phone = models.BigIntegerField()
    email = models.EmailField()

    profession = models.CharField(choices=branch,max_length=20,null=True,blank=False,default='CSE')     #Branch
    status = models.CharField(choices=types,max_length=20,null=True,blank=False,default='employee')     #Year
    present = models.BooleanField(default=False)
    image = models.ImageField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name +' '+self.last_name


class LastFace(models.Model):
    last_face = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.last_face

