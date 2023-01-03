from django.contrib import admin

from .models import  FotoForBanner, Banner1, Title1ForBanner2, Title2ForBanner2, Banner2, Banner3,\
    TextForBanner4, Banner4, Banner5, ModuleForMainPage


from django.contrib import admin

class ModuleForMainPageAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    if num_objects >= 1:
      return False
    else:
      return True




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

class FotoForBannerAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False

class Title1ForBanner2Admin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False

class Title2ForBanner2Admin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False

class TextForBanner4Admin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False

admin.site.register(Banner1, Banner1Admin)
admin.site.register(Banner2, Banner2Admin)
admin.site.register(Banner3, Banner3Admin)
admin.site.register(Banner4, Banner4Admin)
admin.site.register(Banner5, Banner5Admin)
admin.site.register(ModuleForMainPage, ModuleForMainPageAdmin)
admin.site.register(FotoForBanner, FotoForBannerAdmin)
admin.site.register(Title1ForBanner2, Title1ForBanner2Admin)
admin.site.register(Title2ForBanner2, Title2ForBanner2Admin)
admin.site.register(TextForBanner4, TextForBanner4Admin)




