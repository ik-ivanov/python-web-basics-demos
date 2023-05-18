from django.db import models


class Task(models.Model):
    # varchar
    title = models.CharField(max_length=30, null=False)
    # text
    description = models.TextField()
    # int
    priority = models.IntegerField(default=1)
