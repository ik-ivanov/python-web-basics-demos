from django.db import models
from .validators import ValueInRangeValidator


# Create your models here.


class TodoModel(models.Model):
    text = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    priority = models.IntegerField(
        validators=[
            ValueInRangeValidator(2, 100),
        ]
    )
    url_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.text} - {self.priority}"


def dynamic_upload_to_user_folder(instance, filename):
    authenticated_user = instance.user
    files_path_for_user = f"images/{authenticated_user.username}/"

    return files_path_for_user + filename

class ImageModel(models.Model):
    # upload_to == MEDIA_ROOT/images/ ...... name.jpeg
    image = models.ImageField(blank=True, null=True, upload_to=dynamic_upload_to_user_folder)
    description = models.CharField(max_length=100, blank=True, null=True)


class DocumentModel(models.Model):
    # upload_to == MEDIA_ROOT/documents/ ...... name.txt
    document = models.FileField(blank=True, null=True, upload_to="documents/")
    description = models.CharField(max_length=100, blank=True, null=True)


# create pet model and photo model, add many-to-many relations
class PetModel(models.Model):
    name = models.CharField(max_length=100)
    linked_photos = models.ManyToManyField("PhotoModel", blank=True, related_name="pets")

    def __str__(self):
        return f"{self.name}"


class PhotoModel(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to="pets_photos/")
    alt_text = models.CharField(max_length=100, blank=True, null=True)
    pet = models.ManyToManyField(PetModel, related_name="photos")


    def __str__(self):
        return f"{self.pet.name} - {self.alt_text}"
