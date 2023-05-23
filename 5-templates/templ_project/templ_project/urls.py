"""
URL configuration for templ_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("templ_project.examples.urls")),
    path('second/', include("templ_project.second"))
]


"""
1. create app with startapp
2. add app to settings.py
3. add urls in app
4. include urls in project urls
5. set the app name if moving the app into the project folder
    1. move app to project
    2. change apps.py app_name to project.app_name
    3. change in settings (installed apps) app_name to project.app_name
    4. change in urls.py - include app_name.urls to project.app_name.urls
"""