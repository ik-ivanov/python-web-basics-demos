from django.shortcuts import render, redirect
from .models import Profile, Album
from .forms import ProfileModelForm, AlbumModelForm, DeleteAlbumModelForm


# Create your views here.
def home_page(request):
    # profile = Profile.objects.all().firsts() - equal
    profile = Profile.objects.first()
    albums = Album.objects.all()
    form = ProfileModelForm()

    if request.method == "POST":
        form = ProfileModelForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(request.path_info)

    context = {"albums": albums, "add_form": form}

    if profile:
        template = "web/home-with-profile.html"
    else:
        template = "web/home-no-profile.html"

    return render(request, template_name=template, context=context)


def add_album(request):
    profile = Profile.objects.first()

    if not profile:
        redirect('home page')

    form = AlbumModelForm(request.POST or None)

    if form.is_valid():
        album = form.save(commit=False)
        album.profile = profile
        album.save()
        return redirect("home page")

    context = {"profile": profile, "add_form": form}

    return render(request, "web/add-album.html", context)


def album_details(request, id):
    profile = Profile.objects.first()
    context = {"profile": profile, "album": Album.objects.get(id=id)}

    return render(request, "web/album-details.html", context)


def album_edit(request, id):
    profile = Profile.objects.first()
    album = Album.objects.get(id=id)
    form = AlbumModelForm(instance=album)

    context = {"edit_form": form, "profile": profile, "album": album}

    if request.method == "POST":
        form = AlbumModelForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect("home page")

    return render(request, "web/edit-album.html", context)


def album_delete(request, id):
    profile = Profile.objects.first()
    album = Album.objects.get(id=id)
    form = DeleteAlbumModelForm(instance=album)

    if request.method == "POST":
        form = DeleteAlbumModelForm(request.POST, instance=album)
        if form.is_valid():
            album.delete()
            return redirect("home page")

    context = {"delete_form": form, "profile": profile, "album": album}

    return render(request, "web/delete-album.html", context)


def profile_details(request):
    context = {
        "profile": Profile.objects.first()
    }

    return render(request, "web/profile-details.html", context)


def profile_delete(request):
    profiles = Profile.objects.all()
    if request.method == 'POST':
        profiles.delete()
        return redirect('home page')

    return render(request, "web/profile-delete.html")
