from django.contrib import admin

from services.models import Services, ServicesCatalog, ServicesCatalogPosition, PositionServices


@admin.register(ServicesCatalog)
class ServicesCatalogAdmin(admin.ModelAdmin):
    """Создание РАЗДЕЛА УСЛУГ"""
    fields = ('title', 'additional_title', 'url', 'additional_title_2', 'color_title',
              'image_for_big_slider', 'is_active', 'timer', 'position')
    list_display = ('title', 'additional_title', 'is_active', 'position')
    list_filter = ['title', 'additional_title', 'position', 'is_active']
    list_display_links = ['title', 'position']
    list_editable = ['is_active']
    prepopulated_fields = {'url': ('title', 'additional_title')}


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    """Создание УСЛУГИ"""
    fields = ('service_title', 'color_service_title', 'marker', 'image_for_mini_slider', 'bottom_description',
              'color_bottom_description', 'service_catalog', 'is_active', 'timer', 'position_service')
    list_display = ('service_title', 'marker', 'service_catalog', 'is_active', 'position_service')
    list_filter = ['position_service', 'service_title', 'marker']
    list_editable = ['marker', 'is_active', 'service_catalog']


@admin.register(ServicesCatalogPosition)
class ChapterPositionAdmin(admin.ModelAdmin):
    """Позиция РАЗДЕЛА """

    def has_module_permission(self, request):
        return False


@admin.register(PositionServices)
class PositionServicesAdmin(admin.ModelAdmin):
    """Позиция УСЛУГИ"""

    def has_module_permission(self, request):
        return False
