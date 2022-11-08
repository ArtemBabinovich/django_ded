from django.contrib import admin
from .models import Timer, Calendar, FotoForBanner, Banner, Module


class BannerAdmin(admin.ModelAdmin):
    pass
#     list_display = ('calendar', 'slider_fotos', 'timer')
#     list_editable = ('calendar', 'slider_fotos', 'timer')


admin.site.register(Timer)
admin.site.register(Calendar)
admin.site.register(FotoForBanner)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Module)


# Register your models here.
