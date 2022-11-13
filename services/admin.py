from django.contrib import admin
from django import forms

from services.models import ServiceCatalog, Service, ImageForTextDetailService, CountServicesCatalog, \
    ServiceCatalogPosition, ChapterCatalog, ChapterPosition, PositionServices, DetailServer, PositionDetailService, \
    TextDetailService, PromotionsDiscounts, AuthorText

admin.site.register(CountServicesCatalog)
admin.site.register(ServiceCatalog)
admin.site.register(ServiceCatalogPosition)
admin.site.register(ChapterCatalog)
admin.site.register(ChapterPosition)
admin.site.register(Service)
admin.site.register(PositionServices)
admin.site.register(DetailServer)
admin.site.register(PositionDetailService)
admin.site.register(TextDetailService)
admin.site.register(PromotionsDiscounts)
admin.site.register(AuthorText)
admin.site.register(ImageForTextDetailService)


#
# class ImageForTextDetailServiceAdmin(admin.StackedInline):
#     model = ImageForTextDetailService
#
# @admin.register(Service)
# class ServicesAdmin(admin.ModelAdmin):
#     inlines = [ImageForTextDetailServiceAdmin]



