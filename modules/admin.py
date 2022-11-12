from django.contrib import admin

from .models import Timer, Calendar, FotoForBanner, Banner, Module


class BannerAdmin(admin.ModelAdmin):

    fields = ('name', 'calendar', 'slider_type', 'slider_fotos',
              'slider_speed', 'timer', 'url', 'text')
    list_display = ('name', 'calendar', 'slider_type', 'url')
    filter_horizontal = ('slider_fotos', )
    ordering = ('name', )

admin.site.register(Timer)
admin.site.register(Calendar)
admin.site.register(FotoForBanner)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Module)


