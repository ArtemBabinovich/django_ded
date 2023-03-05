from django.urls import path, include
from rest_framework import routers

from about_present.views import AboutPresentAdd, FullApiInfoViewSets
from contacts import APIviews
from get_discount.views import GetDiscountAdd
# from lower_banner.views import LowerBannerForMainPageViewSet
from main import viewsAPI
from modules.APIviews import ModuleForMainPageViewSet
from read_tips.views import ContentTips1ApiViewSets
from services import views
from social_networks.views import SubscribeSocialNetworksApiView
from video_app.views import VideoApiViewSets

router = routers.DefaultRouter()
router.register(r'time_slider_base', viewsAPI.TimeSlideBaseViewSet)
# router.register(r'time_mini-slider', viewsAPI.TimeForMiniSliderViewSet)
router.register(r'social_networks', APIviews.SocialNetworksViewSet)
# ЮРЛ БАННЕР
router.register(r'phone', APIviews.PhoneViewSet)
router.register(r'banners/main_page', ModuleForMainPageViewSet, basename='main_page')
# ЮРЛ каллендарь напоминаний
router.register(r'presents/add', AboutPresentAdd, basename='present_add')
router.register(r'presents/get', FullApiInfoViewSets, basename='present_get')
# ЮРЛ получения скидки
router.register(r'discont/add', GetDiscountAdd, basename='discont_add')
# ЮРЛ Сервисов
router.register(r'block_services', views.ServicesCatalogViewSet, basename='block_services')
router.register(r'big_slider', views.BigSliderViewSet, basename='big_slider')
router.register(r'small_slider', views.SmallSliderViewSet, basename='small_slider')
router.register(r'small_slider_with_pagination', views.NewSmallSliderViewSet, basename='small_slider_with_pagination')
# URL ссылок для видео
router.register(r'video_links', VideoApiViewSets, basename='video_links')
# URL для Читать советы(read_tips)
router.register(r'content_tips', ContentTips1ApiViewSets, basename='content_tips')
# URL для Ссылок на социальные сети
router.register(r'url_for_social_networks', SubscribeSocialNetworksApiView, basename='url_for_social_networks')
# router.register(r'lower_banners/main_page', LowerBannerForMainPageViewSet, basename='lower_banner_main_page')

urlpatterns = [
    path('api/', include(router.urls)),
]
