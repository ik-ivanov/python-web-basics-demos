from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=12)
    password = models.CharField(
        max_length=50,
        editable=True,
    ) # DO NOT DO THIS LIKE THAT

    def __str__(self):
        return self.name
