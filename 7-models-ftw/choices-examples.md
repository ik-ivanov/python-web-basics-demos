# Option 1


```python
LEVEL_CHOICES = (
    (1, 'Junior'),
    (2, 'Middle'),
    (3, 'Senior'),
)
class Employee(models.Model):
    level = models.IntegerField(choices=LEVEL_CHOICES, default=1)
```



# Option 2



```python
class LevelChoices(Enum):
    JUNIOR = 1
    MIDDLE = 2
    SENIOR = 3
class Employee(models.Model):
    level = models.IntegerField(choices=LevelChoices.choices(), default=LevelChoices.JUNIOR)
```



# Option 3



```python
class EmployeeLevelChoices(models.IntegerChoices):  # can also be TextChoices, etc.
    JUNIOR = 1, 'Junior'
    MIDDLE = 2, 'Middle'
    SENIOR = 3, 'Senior'
class Employee(models.Model):
    level = models.IntegerField(choices=EmployeeLevelChoices.choices(), default=EmployeeLevelChoices.JUNIOR)
```



# Option 4




```python
class Employee(models.Model):
    LEVEL_JUNIOR = 1
    LEVEL_MIDDLE = 2
    LEVEL_SENIOR = 3
    LEVEL_CHOICES = (
        (LEVEL_JUNIOR, 'Junior'),
        (LEVEL_MIDDLE, 'Middle'),
        (LEVEL_SENIOR, 'Senior'),
    )
    level = models.IntegerField(choices=LEVEL_CHOICES, default=LEVEL_JUNIOR)

# Bonus when we define choices like this. We can say:
# Employee.LEVEL_JUNIOR
```




# Option 5 - combine IntegerChoices and in model declaration




```python
class Employee(models.Model):
    class EmployeeLevelChoices(models.IntegerChoices):
        JUNIOR = 1, 'Junior'
        MIDDLE = 2, 'Middle'
        SENIOR = 3, 'Senior'
    level = models.IntegerField(choices=EmployeeLevelChoices.choices(), default=EmployeeLevelChoices.JUNIOR)

# Bonus when we define choices like this. We can say:
# Employee.EmployeeLevelChoices.JUNIOR
``` 