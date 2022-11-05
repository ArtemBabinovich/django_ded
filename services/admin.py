from django.contrib import admin

from services.models import ServiceCatalog, Service, ImageForServices

admin.site.register(ServiceCatalog)


class ImageForServicesAdmin(admin.StackedInline):
    model = ImageForServices


@admin.register(Service)
class ImageForServicesAdmin(admin.ModelAdmin):
    inlines = [ImageForServicesAdmin]
    ordering = ('sort_service',)
    list_display = ['title', 'image_title']
    list_display_links = ['title', 'image_title']


# @admin.register(ImageForServices)
# class ImageForServicesAdmin(admin.ModelAdmin):
#     pass
