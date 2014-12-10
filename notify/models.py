

# Create your models here.
__author__ = 'tj'
from django.db import models
from django.contrib.auth.models import User

class UserRecords(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.ForeignKey(User)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    lemo = models.CharField(max_length=500)

class Node(models.Model) :
    id = models.AutoField(primary_key=True)
    nodeip = models.CharField(max_length=20)
    nodename = models.CharField(max_length=20)
    nodeinfo = models.CharField(max_length=1000)
