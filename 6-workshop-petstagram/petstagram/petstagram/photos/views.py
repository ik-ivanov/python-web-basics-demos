from django.shortcuts import render
from .models import Photo

# Create your views here.

def photo_add(request):
    return render(request, 'photos/photo-add-page.html')


def photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)

    context = {
        "photo": photo,
        "likes": photo.like_set.count(),
        "comments": photo.comment_set.all(),
    }

    return render(
        request,
        'photos/photo-details-page.html',
        context=context
    )


def photo_edit(request, pk):
    return render(request, 'photos/photo-edit-page.html')
