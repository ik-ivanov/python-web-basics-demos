from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petstagram.photos.models import Photo
from .models import Like, Comment
from .forms import CommentForm, SearchForm
# Create your views here.


def index(request):
    photos = Photo.objects.all()
    search_form = SearchForm(request.GET)

    if search_form.is_valid():
        search_text = search_form.cleaned_data['search_text']
        photos = photos.filter(tagged_pets__name__icontains=search_text)

    context = {
        "all_photos": photos ,
        "comment_form": CommentForm(),
        "search_form": search_form,
    }

    return render(request, 'common/home-page.html', context=context)


def like_functionality(request, photo_id):
    # naive
    # var:instance  = model (objects -> manager)
    # select * from like where
    # to_photo_id=photo.id == to_photo=photo.id
    photo = Photo.objects.get(pk=photo_id)
    like_object = Like.objects.filter(to_photo=photo).first()

    if like_object:
        # instance
        like_object.delete()
    else:
        new_like_object = Like(to_photo=photo)
        new_like_object.save()

    # http://127.0.0.1:8000/
    return redirect(request.META['HTTP_REFERER'] + f"#{photo_id}")


def share_functionality(request, photo_id):
    #copy(request.META['HTTP_HOST'] + resolve_url('photo details', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f"#{photo_id}")


def comment_functionality(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():

            print('form is valid')

            new_comment_instance = form.save(commit=False)
            new_comment_instance.to_photo = photo
            new_comment_instance.save()

        return redirect(request.META['HTTP_REFERER'] + f"#{photo_id}")
