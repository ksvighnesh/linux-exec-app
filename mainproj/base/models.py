from operator import mod
from django.db import models

# Create your models here.
class command(models.Model):
    cmd=models.CharField(max_length=20)
    repetition=models.IntegerField()
    sleep_dur=models.IntegerField()

    def __str__(self):
        return self.cmd