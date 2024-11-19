from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length = 400)
    task_created_date = models.DateField()
    users = models.ManyToManyField(User,related_name="task")
    status = models.CharField(max_length = 200,choices=[('Pending','pending'),('processing','processing'),('completed','completed')],default="pending")

    def __str__(self) -> str:
        return self.task_name


