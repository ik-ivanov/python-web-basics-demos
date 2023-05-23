from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/<name>', views.contact_view, name="contact page"),
    path('about/', views.about_view, name="about page")
]