from rest_framework import routers
from django.urls import path, include

from main import viewsAPI
from contacts import APIviews
from services import views
from modules.APIviews import FotoForBannerViewSet, CalendarViewSet, TimerViewSet, \
    BannerViewSet, ModuleViewSet

router = routers.DefaultRouter()
router.register(r'foto_slider_base', viewsAPI.FotoSliderBaseViewSet)
router.register(r'time_slider_base', viewsAPI.TimeSlideBaseViewSet)
router.register(r'mini-slider', viewsAPI.MiniFotoSliderViewSet)
router.register(r'time_mini-slider', viewsAPI.TimeForMiniSliderViewSet)
router.register(r'social_networks', APIviews.SocialNetworksViewSet)
# ЮРЛ Сервисов
router.register(r'services', views.ServicesCatalogViewSet)
# ЮРЛ БАННЕР
router.register(r'phone', APIviews.PhoneViewSet)
router.register(r'banners/fotos', FotoForBannerViewSet)
router.register(r'banners/calendar', CalendarViewSet)
router.register(r'banners/timer', TimerViewSet)
router.register(r'banners', BannerViewSet)
router.register(r'modules', ModuleViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]
