from django.urls import path, include
from rest_framework import routers

from about_present.views import AboutPresentAdd, FullApiInfoViewSets
from contacts import APIviews
from get_discount.views import GetDiscountAdd
from main import viewsAPI
from modules.APIviews import ModuleForMainPageViewSet
from services import views

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

urlpatterns = [
    path('api/', include(router.urls)),
]
