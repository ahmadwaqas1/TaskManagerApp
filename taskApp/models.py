from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Task(models.Model):
    title           = models.CharField(max_length=100)
    discreption     = models.TextField(blank=True)
    task_st_date    = models.DateTimeField(default=datetime.now, blank=True)
    task_end_date   = models.DateTimeField(default=datetime.now, blank=True)
    is_important    = models.BooleanField(default=False)
    is_published    = models.BooleanField(default=True)
    is_Finished     = models.BooleanField(default=False)
    is_completed    = models.BooleanField(default=False)
    is_failed       = models.BooleanField(default=False)
    user_id         = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='user')


    def __str__(self):
        return self.title 