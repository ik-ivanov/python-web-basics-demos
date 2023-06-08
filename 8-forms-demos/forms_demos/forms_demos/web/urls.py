from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('model-form/<int:pk>/', views.model_form_view, name='model-form'),
]
