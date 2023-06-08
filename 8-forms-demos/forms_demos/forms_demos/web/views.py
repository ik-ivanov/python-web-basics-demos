from django.shortcuts import render
from .models import Person
from .forms import PersonForm, PersonModelForm
# Create your views here.


def index(request):
    name = None

    people = Person.objects.all()

    update_person = Person.objects.get(id=2)
    # form = PersonForm(instance=update_person)
    form = PersonForm(initial=update_person.__dict__)

    if request.method == 'POST':
        form = PersonForm(request.POST)
        # 1. Validate the form
        # 2. If valid, fills cleaned_data dictionary
        if form.is_valid():
            name = form.cleaned_data["name"]
            Person.objects.create(**form.cleaned_data)

    context = {
        "form": form,
        "name": name,
        "people": people,
    }

    return render(request, "web/index.html", context)


def model_form_view(request, pk):
    person = Person.objects.get(pk=pk)
    form = PersonModelForm(instance=person)

    if request.method == "POST":
        form = PersonModelForm(request.POST, instance=person)
        # apply password hashing

        if form.is_valid():
            password = form.cleaned_data["password"]
            password_strong = f"{password}123!!!"
            form.cleaned_data["password"] = password_strong

            form.save()

    context = {
        "model_form": form,
        "person": person,
    }

    return render(request, "web/model_form.html", context)
