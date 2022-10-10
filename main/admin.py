from django.contrib import admin
from django.utils.safestring import mark_safe
from main.models import Image, Position, FotoSliderBase, TimeSlideBase, Section, CatalogService
from adminsortable.admin import NonSortableParentAdmin, SortableStackedInline
from adminsortable.admin import (SortableTabularInline)
from .models import (Gallery, GalleryImageRelation)

admin.site.register(FotoSliderBase)
admin.site.register(TimeSlideBase)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    """Позиция в списке"""

    def has_module_permission(self, request):
        return False


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    """Раздел"""

    def has_module_permission(self, request):
        return False


class ImageInline(SortableStackedInline):
    """Фотографии"""
    model = Image
    extra = 1
    max_num = 30  # мак. колличество фото
    readonly_fields = 'preview',

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="80" height="80">')

    preview.short_description = 'Превью Фотографии'


@admin.register(CatalogService)
class CatalogServiceAdmin(NonSortableParentAdmin):
    """Услуги"""
    inlines = [ImageInline]

    def has_module_permission(self, request):
        return False


class GalleryImageRelationInlineAdmin(SortableTabularInline):
    """Соединение и сортировка"""
    model = GalleryImageRelation
    extra = 1


@admin.register(Gallery)
class GalleryAdmin(NonSortableParentAdmin):
    """Левая панель"""
    inlines = (GalleryImageRelationInlineAdmin,)
