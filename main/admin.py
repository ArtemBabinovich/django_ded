from django.contrib import admin
from django.utils.safestring import mark_safe

from main.models import FotoSliderBase, TimeSlideBase, Service, CatalogService, Image, Position

admin.site.register(FotoSliderBase)
admin.site.register(TimeSlideBase)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    """Позиция в списке"""

    def has_module_permission(self, request):
        return False


class ImageInline(admin.TabularInline):
    """Фотографии"""
    model = Image
    extra = 2
    readonly_fields = 'preview',

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="80" height="80">')

    preview.short_description = 'Превью Фотографии'


@admin.register(Service)
class ServicAdmin(admin.ModelAdmin):
    """Раздел"""
    list_display = 'name', 'position', 'is_active'
    list_editable = 'position', 'is_active'
    list_filter = 'is_active',
    search_fields = 'name',


@admin.register(CatalogService)
class CatalogServiceAdmin(admin.ModelAdmin):
    """Услуги"""
    list_display = 'name', 'marker', 'position', 'service', 'is_active',
    list_editable = 'marker', 'is_active', 'position', 'service', 'is_active',
    list_filter = 'marker', 'service', 'is_active',
    search_fields = 'name',
    inlines = ImageInline,


