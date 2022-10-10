from django.contrib import admin
from django.utils.safestring import mark_safe
from main.models import Image, Position, FotoSliderBase, TimeSlideBase, Section, CatalogService
from adminsortable.admin import NonSortableParentAdmin, SortableStackedInline


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
    pass
#     list_display = 'name', 'position', 'is_active'
#     list_editable = 'position', 'is_active'
#     list_filter = 'is_active',
#     search_fields = 'name',

# def has_module_permission(self, request):
#     return False


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
    pass
    # list_display = 'name', 'marker', 'position', 'service', 'is_active',
    # list_editable = 'marker', 'is_active', 'position', 'service', 'is_active',
    # list_filter = 'marker', 'service', 'is_active',
    # search_fields = 'name',
    inlines = [ImageInline]


"""СЕРЕДИНА"""





from django.contrib import admin
from adminsortable.admin import (SortableAdmin, SortableTabularInline)
from .models import (Gallery, GalleryImageRelation)

class GalleryImageRelationInlineAdmin(SortableTabularInline):
    model = GalleryImageRelation
    extra = 1

class GalleryAdmin(NonSortableParentAdmin):
    inlines = (GalleryImageRelationInlineAdmin,)


admin.site.register(Gallery, GalleryAdmin)
