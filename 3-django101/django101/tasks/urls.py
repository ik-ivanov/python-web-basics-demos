# urls for tasks app
from django.urls import path
from tasks.views import index, list_tasks, list_tasks_template

urlpatterns = [
    path('', index),
    path('list/', list_tasks),
    path('with-template/', list_tasks_template)
]
