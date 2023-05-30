from django.contrib import admin
from .models import Employee, NullBlankDemo, Department, Project, Profile


# Register your models here.




@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'first_name', 'last_name', 'age', 'level']
    list_filter = ['level']
    search_fields = ('first_name', 'last_name', 'email')
    # fields = [('first_name', 'last_name'), 'email', 'age', 'level']
    fieldsets = (
        ('Personal Info!', {'fields': ('first_name', 'middle_name', 'last_name')}),
        ('HR STUFF', {'fields': ('is_manager', 'email', 'level')})
    )

@admin.register(NullBlankDemo)
class NullBlankDemoAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass