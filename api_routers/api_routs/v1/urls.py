from rest_framework import routers
from django.urls import path, include


from get_discount.views import GetDiscountAdd
from main import viewsAPI
from contacts import APIviews
from main import viewsAPI
from modules.APIviews import FotoForBannerViewSet, CalendarViewSet, TimerViewSet, \
    BannerViewSet, ModuleViewSet
from about_present.views import AboutPresentAdd, RecipientViewSets, \
    ReasonViewSets, PresentViewSets, RemindForDaysViewSets
from services import views


router = routers.DefaultRouter()
router.register(r'time_slider_base', viewsAPI.TimeSlideBaseViewSet)
# router.register(r'time_mini-slider', viewsAPI.TimeForMiniSliderViewSet)
router.register(r'social_networks', APIviews.SocialNetworksViewSet)
# ЮРЛ БАННЕР
router.register(r'phone', APIviews.PhoneViewSet)
router.register(r'banners/fotos', FotoForBannerViewSet)
router.register(r'banners/calendar', CalendarViewSet)
router.register(r'banners/timer', TimerViewSet)
router.register(r'banners', BannerViewSet)
router.register(r'modules', ModuleViewSet)
# ЮРЛ каллендарь напоминаний
router.register(r'presents/add', AboutPresentAdd, basename='present_add')
router.register(r'recipient', RecipientViewSets)
router.register(r'reason', ReasonViewSets)
router.register(r'present', PresentViewSets)
router.register(r'remind_for_days', RemindForDaysViewSets)
# ЮРЛ получения скидки
router.register(r'discont/add', GetDiscountAdd, basename='discont_add')
# ЮРЛ Сервисов
router.register(r'block_services', views.ServicesCatalogViewSet, basename='block_services')
router.register(r'big_slider', views.BigSliderViewSet, basename='big_slider')
router.register(r'small_slider', views.SmallSliderViewSet, basename='small_slider')

urlpatterns = [
    path('api/', include(router.urls)),
]
