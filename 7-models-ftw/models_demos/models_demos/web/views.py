from django.shortcuts import render,  redirect, get_object_or_404, get_list_or_404
from .models import Employee, Department, Salary
import random

from django.contrib.auth.models import User


# Create your views here.
def index(request):
    # lazy (until used, it is not executed)
    #first_department = Department.objects.filter(name='IT').first()

    employees = Employee.objects.all()
    employees2 = Employee.objects.filter(first_name__startswith="K")
    department = Department.objects.filter(name="ETT")
    salary = Salary.objects.filter(amount__gt=1000).first()

    context = {
        "employees": employees,
        "employees2": employees2,
        "fun_department": department,
        "salary": salary,
    }



    return render(request, "web/index.html", context)


def details_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    context = {
        "employee": employee,
    }
    return render(request, "web/details.html", context)

def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete() # not lazy
    return redirect("index")


def details_department(request, pk, slug):
    department = get_object_or_404(Department, pk=pk, slug=slug)
    # department = Department.objects.get(pk=pk, slug=slug)
    context = {
        "department": department,
    }
    return render(request, "web/details_department.html", context)