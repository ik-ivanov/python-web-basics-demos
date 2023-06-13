from django.shortcuts import render
from .forms import TodoForm, TodoModelForm, ImageModelForm, DocumentModelForm, PetModelForm, PhotoModelForm
from .models import ImageModel, TodoModel, DocumentModel, PetModel, PhotoModel

# Create your views here.

# API == Applicable Programming Interface


def index(request):
    form_type = TodoModelForm
    todos = TodoModel.objects.all()

    print(todos)

    form = form_type()

    if request.method == "POST":
        form = form_type(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()

    context = {
        "form": form,
        "todos": todos,
    }

    return render(request, "web/index.html", context)


def create_image_view(request):
    form_type = ImageModelForm

    form = form_type()

    if request.method == "POST":
        form = form_type(request.POST, request.FILES)
        if form.is_valid():

            authenticated_user = request.user
            files_path_for_user = f"images/{authenticated_user.username}/"

            print(form.cleaned_data)
            image = form.save()
            image.save()

    context = {
        "form": form,
        "images": ImageModel.objects.all(),
    }

    return render(request, "web/create_image.html", context)


def create_document_view(request):
    form_type = DocumentModelForm

    form = form_type()

    if request.method == "POST":
        form = form_type(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    context = {
        "form": form,
    }

    return render(request, "web/create_document.html", context)


# create new view for pets
def create_pet_view(request):
    form_type = PetModelForm
    photos_with_lora = PhotoModel.objects.filter(pet__name="Lora")
    # pet_photos = PetModel.objects.get(name="Lora").photos.all()

    form = form_type()

    if request.method == "POST":
        form = form_type(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    context = {
        "form": form,
        "photos_with_lora": photos_with_lora

    }

    return render(request, "web/create_pet.html", context)


def create_pet_photo_view(request):
    form_type = PhotoModelForm

    form = form_type()

    if request.method == "POST":
        form = form_type(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            image.save()


    context = {
        "form": form,
    }

    return render(request, "web/create_photo.html", context)