# from django.contrib import admin
# from sortedm2m_filter_horizontal_widget.forms import SortedFilteredSelectMultiple
#
# from .models import FotoForLowerBanner, LowerBanner1, LowerBanner2, LowerBanner3, TextForLowerBanner, AllLowerBanners, LowerBannerForMainPage
#
#
# class FotoForLowerBannerAdmin(admin.ModelAdmin):
#
#     def has_module_permission(self, request):
#         return False
#
# class TextForLowerBannerAdmin(admin.ModelAdmin):
#
#     fields = ('title', 'text',)
#     def has_module_permission(self, request):
#         return False
#
#
# class LowerBanner1Admin(admin.ModelAdmin):
#
#     filter_horizontal = ('slider', 'link_block_1', 'link_block_2', 'link_block_3',)
#
#
# class LowerBanner2Admin(admin.ModelAdmin):
#
#     filter_horizontal = ('slider_1', 'link_block_1', 'link_block_2', 'slider_2',)
#
#
# class LowerBanner3Admin(admin.ModelAdmin):
#
#     filter_horizontal = ('slider_1', 'link_block_1', 'slider_2', 'link_block_2',)
#
#
# class AllLowerBannersAdmin(admin.ModelAdmin):
#
#     def has_module_permission(self, request):
#         return False
#
#     ordering = ('-low_banner_1', '-low_banner_2', '-low_banner_3',)
#
#
# class LowerBannerForMainPageAdmin(admin.ModelAdmin):
#
#     # filter_horizontal = ('selected_banners',)
#
#
#     def has_add_permission(self, request):
#         num_objects = self.model.objects.count()
#         if num_objects >= 1:
#           return False
#         else:
#           return True
#
#     def formfield_for_manytomany(self, db_field, request=None, **kwargs):
#         if db_field.name == 'selected_banners':
#             kwargs['widget'] = SortedFilteredSelectMultiple()
#         return super(LowerBannerForMainPageAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
#
# admin.site.register(FotoForLowerBanner, FotoForLowerBannerAdmin)
# admin.site.register(TextForLowerBanner, TextForLowerBannerAdmin)
# admin.site.register(LowerBanner1, LowerBanner1Admin)
# admin.site.register(LowerBanner2, LowerBanner2Admin)
# admin.site.register(LowerBanner3, LowerBanner3Admin)
# admin.site.register(AllLowerBanners, AllLowerBannersAdmin)
# admin.site.register(LowerBannerForMainPage, LowerBannerForMainPageAdmin)
#
