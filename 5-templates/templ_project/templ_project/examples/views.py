import datetime

from django.shortcuts import render, redirect
import random


# Create your views here.

class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age


some_student = Student("John", 20)


def index(request):
    context = {
        "title": "Home",
        "random_int": random.random(),
        "nested": {
            "second": "second value",
        },
        "student_age": some_student.get_age(),
        "students": ["Kalin", "Ivan", "Pesho", "Pesho", "Mariya"],
        "students_second": [],
        "now": datetime.datetime.now(),
        "numbers": [1, 2, 3, 4, 5, 6, 7],
        "name": "Now hardcoded",
        "students_obj": [
            Student('Lili', 23),
            Student('Moni', 20),
            Student('Yavor', 30)
        ],
        "logged_in": True
    }

    # context + template = HtmlResponse('<html>...</html>')
    return render(request, 'examples/partials/index.html', context=context)


def contact_view(request, name):
    return redirect('index', name=name)


def about_view(request):
    return render(request, 'examples/partials/about.html')
