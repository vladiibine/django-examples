from django.contrib import admin

# Register your models here.
from django.contrib.admin import filters

from .models import Item


class ComplexListFilter(filters.SimpleListFilter):
    title = 'complex filter'
    parameter_name = 'complex'
    template = 'admin_complex_filter/filter_template.html'

    def lookups(self, request, model_admin):
        return(
            (1, 11),
            (2, 22)
        )

    def queryset(self, request, queryset):
        return queryset


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_filter = (ComplexListFilter, 'available')
