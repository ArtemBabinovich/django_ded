from django.contrib import admin
from django.utils.safestring import mark_safe
from main.models import Image, Position, FotoSliderBase, TimeSlideBase, CatalogService, Contact, Politics
from adminsortable.admin import NonSortableParentAdmin, SortableStackedInline
from adminsortable.admin import SortableTabularInline
from .models import Gallery, GalleryImageRelation

admin.site.register(FotoSliderBase)
admin.site.register(TimeSlideBase)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Контакты"""
    list_display = '__str__', 'phone1', 'phone2', 'phone3'
    fields = 'maps', 'attention_info', 'photo_map', 'preview1', 'info_photo_map', 'photo_st', 'preview2', 'info_photo_st', 'address', 'website', 'email', 'skype', 'phone1', 'phone2', 'phone3'
    list_editable = 'phone1', 'phone2', 'phone3'
    readonly_fields = 'preview1', 'preview2',

    def preview1(self, obj):
        return mark_safe(f'<img src="{obj.photo_map.url}" width="200" height="200">')

    preview1.short_description = 'Превью Фотографии (КАК ДОБРАТЬСЯ)'

    def preview2(self, obj):
        return mark_safe(f'<img src="{obj.photo_st.url}" width="200" height="200">')

    preview2.short_description = 'Превью Фотографии (ВХОД В СТУДИЮ)'


@admin.register(Politics)
class PoliticsAdmin(admin.ModelAdmin):
    list_display = 'title', 'body_description', 'is_active'
    list_editable = 'is_active',
    list_filter = 'is_active',




@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    """Позиция в списке"""

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
    list_display = 'name', 'marker', 'price', 'is_active'
    list_editable = 'marker', 'price', 'is_active'
    list_filter = 'marker', 'is_active'
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
    list_display = 'name', 'position', 'is_active',
    list_editable = 'position', 'is_active'
    list_filter = 'is_active',
    inlines = (GalleryImageRelationInlineAdmin,)
