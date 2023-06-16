from django.shortcuts import render, redirect
from petstagram.common.forms import CommentForm
from .forms import PhotoAddForm, PhotoEditForm
from .models import Photo


# Create your views here.

def photo_add(request):
    form = PhotoAddForm()

    if request.method == "POST":
        form = PhotoAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        "form": form,
    }

    return render(request, 'photos/photo-add-page.html', context=context)


def photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    comment_form = CommentForm()

    context = {
        "photo": photo,
        "likes": photo.like_set.count(),
        "comments": photo.comment_set.all(),
        "comment_form": comment_form,
    }

    return render(
        request,
        'photos/photo-details-page.html',
        context=context
    )


def photo_edit(request, pk):
    photo = Photo.objects.get(pk=pk)
    form = PhotoEditForm(instance=photo)

    if request.method == "POST":
        form = PhotoEditForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('photo details', pk=pk)

    context = {
        "photo": photo,
        "form": form,
    }

    return render(request, 'photos/photo-edit-page.html', context)


def photo_delete(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('index')

