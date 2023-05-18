from django.contrib import admin
from tasks.models import Task


# alternatively you can use a decorator
# @admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'priority')


admin.site.register(Task, TaskAdmin)
