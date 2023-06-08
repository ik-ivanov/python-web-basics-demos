from django.contrib import admin
from .models import Person


# Register your models here.

# class PersonInline(admin.TabularInline):
#     model = Person
#     extra = 0

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "age"]
    list_filter = ["age"]
    search_fields = ["name"]
    ordering = ["name"]
    # fields = ["name", "age"]
    # readonly_fields = ["name"]
    # exclude = ["password"]
    # filter_horizontal = ["age"]
    # filter_vertical = ["age"]
    # raw_id_fields = ["hobbies"]
    # autocomplete_fields = ["hobbies"]
    # radio_fields = {"hobbies": admin.HORIZONTAL}
    # prepopulated_fields = {"name": ["age"]}
    # list_editable = ["age"]
    # list_display_links = ["name"]
    # list_per_page = 10
    # list_max_show_all = 100
    # save_as = True
    # save_as_continue = True
    # save_on_top = True
    # preserve_filters = True
    # inlines = [PersonInline]
    # actions = [my_action]
    # actions_on_top = True
    # actions_on_bottom = True
    # actions_selection_counter = True
    # date_hierarchy = "age"
    # empty_value_display = "Empty"
    # show_full_result_count = True
    # show_admin_actions = True
    # list_select_related = True
