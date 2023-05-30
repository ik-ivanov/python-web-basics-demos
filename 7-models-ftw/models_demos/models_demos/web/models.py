from django.db import models


# DJANGO ORM -
# one model == one table in db
# defines structure
# stores data (db to python and python to db)
# do operations on db via python code

# class EmployeeProject(models.Model):
#     employee_id = models.ForeignKey('Employee', on_delete=models.CASCADE)
#     project_id = models.ForeignKey('Project', on_delete=models.CASCADE)
#     created_on = models.DateTimeField(auto_now_add=True)


class Department(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.pk} {self.name}"

class Project(models.Model):
    name = models.CharField(max_length=100)
    size = models.PositiveIntegerField()


class Employee(models.Model):
    LEVEL_JUNIOR = 'jur'
    LEVEL_MIDDLE = 'mid'
    LEVEL_SENIOR = 'sen'
    LEVEL_CHOICES = (
        (LEVEL_JUNIOR, 'Junior'),
        (LEVEL_MIDDLE, 'Middle'),
        (LEVEL_SENIOR, 'Senior'),
    )

    # CASCADE (Department + all connected Employees)
    # RESTRICT/PROTECT (if Department has employees, stop deletion and prevent Employee deletion)
    # SET_NULL - set to null if it is optional

    department = models.ForeignKey(to='Department', on_delete=models.RESTRICT,
                                   null=True)

    project = models.ManyToManyField(Project)  # through=EmployeeProject

    # Varying char (30), VARCHAR (30), TEXT2
    first_name = models.CharField(max_length=30, verbose_name="First name")
    middle_name = models.CharField(max_length=50, default="Doe", blank=True)
    last_name = models.CharField(max_length=40)

    description = models.TextField(default="Should be filled in.")

    age = models.IntegerField()  # - +
    experience = models.PositiveIntegerField()
    birth_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)  # only first time
    updated_on = models.DateTimeField(auto_now=True)  # each time update

    is_manager = models.BooleanField(default=None)

    email = models.EmailField(unique=True)

    # junior, mid, senior, (unicorn)
    level = models.CharField(max_length=len(LEVEL_SENIOR), choices=LEVEL_CHOICES, default=LEVEL_JUNIOR)

    # define structure into DB
    # gets data from DB via models (instances)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"ID: {self.pk}; Names: {self.full_name}"


class Profile(models.Model):
    DESK_ONE = 'first'
    DESK_TWO = 'last'
    DESK_CHOICES = (
        (DESK_ONE, 'desk 1'),
        (DESK_TWO, 'desk 2'),
    )
    desk = models.CharField(choices=DESK_CHOICES)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)


class NullBlankDemo(models.Model):
    # can be blank, but can't be null
    blank = models.IntegerField(blank=True, null=False)
    # can't be blank, can be null
    null = models.IntegerField(blank=False, null=True)
    # can be blank, can be null
    blank_null = models.IntegerField(blank=True, null=True)
    # can't be blank, can't be null
    default = models.IntegerField(blank=False, null=False)
