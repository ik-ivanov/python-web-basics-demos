from django.urls import path
from preparation_project.web import views

"""
3. Routes
• http://localhost:8000/ - home page
• http://localhost:8000/album/add/ - add album page
• http://localhost:8000/album/details/<id>/ - album details page
• http://localhost:8000/album/edit/<id>/ - edit album page
• http://localhost:8000/album/delete/<id>/ - delete album page
• http://localhost:8000/profile/details/ - profile details page
• http://localhost:8000/profile/delete/ - delete profile page
"""


urlpatterns = [
    path("", views.home_page, name="home page"),
    path("album/add/", views.add_album, name="add album page"),
    path("album/details/<int:id>/", views.album_details, name="album details page"),
    path("album/edit/<int:id>/", views.album_edit, name="edit album page"),
    path("album/delete/<int:id>/", views.album_delete, name="delete album page"),

    path("profile/details/", views.profile_details, name="profile details page"),
    path("profile/delete/", views.profile_delete, name="delete profile page"),

]
