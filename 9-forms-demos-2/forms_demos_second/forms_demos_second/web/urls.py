from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_image/", views.create_image_view, name="create image"),
    path("create_document/", views.create_document_view, name="create document"),
    path("create_pet/", views.create_pet_view, name="create pet"),
    path("create_pet_photo/", views.create_pet_photo_view, name="create pet photo"),
]



