from django.urls import path
from .views import old_view, new_view, department_by_slug_view

# basic
urlpatterns = [
    path("old/", old_view, name='old page'),
    path("new-page/", new_view, name='new page'),
    # /departments/<slug>
    path("<slug:department_name>/", department_by_slug_view, name="department by slug")
]
