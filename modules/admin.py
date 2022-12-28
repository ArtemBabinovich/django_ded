from django.contrib import admin

from .models import  FotoForBanner, Banner1, Title1ForBanner2, Title2ForBanner2, Banner2, Banner3,\
    TextForBanner4, Banner4, Banner5


class Banner1Admin(admin.ModelAdmin):

    # fields = '__all__'
    filter_horizontal = ('slider', )
    ordering = ('banner_position', )


class Banner2Admin(admin.ModelAdmin):

    # fields = '__all__'
    filter_horizontal = ('slider_1', 'text_1', 'slider_2', 'text_2',)
    ordering = ('banner_position', )


class Banner3Admin(admin.ModelAdmin):

    # fields = '__all__'
    filter_horizontal = ('slider', )
    ordering = ('banner_position', )


class Banner4Admin(admin.ModelAdmin):

    # fields = '__all__'
    filter_horizontal = ('slider', 'text',)
    ordering = ('banner_position', )


class Banner5Admin(admin.ModelAdmin):

    # fields = '__all__'
    filter_horizontal = ('slider',)
    ordering = ('banner_position', )

admin.site.register(Banner1, Banner1Admin)
admin.site.register(Title1ForBanner2)
admin.site.register(Title2ForBanner2)
admin.site.register(Banner2, Banner2Admin)
admin.site.register(Banner3, Banner3Admin)
admin.site.register(TextForBanner4)
admin.site.register(Banner4, Banner4Admin)
admin.site.register(Banner5, Banner5Admin)
admin.site.register(FotoForBanner)

