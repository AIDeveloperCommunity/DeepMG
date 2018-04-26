from django.db import models


# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)


class Log(models.Model):
    """
	Log Management Table
	"""
    ClientIp = models.CharField(max_length=15)
    sessionID = models.AutoField(primary_key=True, serialize=False)
    StartTime = models.DateTimeField(default=datetime.datetime.now())
    EndTime = models.DateTimeField()
