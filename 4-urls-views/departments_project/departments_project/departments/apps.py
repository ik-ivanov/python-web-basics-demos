from django.apps import AppConfig


class DepartmentsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    # NOTE: the name should be the same as in settings:INSTALLED_APPS
    name = "departments_project.departments"
