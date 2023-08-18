from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    title = models.CharField(max_length=200 , blank=True,null=True)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False, null=True)
    
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):  # new
        return reverse("task_detail", args=[str(self.id)])
    