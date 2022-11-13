from rest_framework import routers
from django.urls import path, include

from main import viewsAPI
from contacts import APIviews
from modules.APIviews import FotoForBannerViewSet, CalendarViewSet, TimerViewSet, \
    BannerViewSet, ModuleViewSet

from services import views

router = routers.DefaultRouter()
router.register(r'foto_slider_base', viewsAPI.FotoSliderBaseViewSet)
router.register(r'time_slider_base', viewsAPI.TimeSlideBaseViewSet)
router.register(r'mini-slider', viewsAPI.MiniFotoSliderViewSet)
router.register(r'time_mini-slider', viewsAPI.TimeForMiniSliderViewSet)
router.register(r'social_networks', APIviews.SocialNetworksViewSet)
router.register(r'phone', APIviews.PhoneViewSet)
router.register(r'banners/fotos', FotoForBannerViewSet)
router.register(r'banners/calendar', CalendarViewSet)
router.register(r'banners/timer', TimerViewSet)
router.register(r'banners', BannerViewSet)
router.register(r'modules', ModuleViewSet)
# ЮРЛ Сервисов
router.register(r'services', views.ServiceViewSet)
router.register(r'discount', views.PromotionsDiscountsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
