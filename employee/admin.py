from django.contrib import admin
from . models import Employee, Skills
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'department',
        'job',
        'full_name',
    )

    def full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name

    search_fields = ('first_name',)
    list_filter = ('job',)
    filter_horizontal = ('skill',)


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Skills)