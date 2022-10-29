from rest_framework import routers
from main import viewsAPI
from django.urls import path, include
from contacts import APIviews


router = routers.DefaultRouter()
router.register(r'foto_slider_base', viewsAPI.FotoSliderBaseViewSet)
router.register(r'time_slider_base', viewsAPI.TimeSlideBaseViewSet)
router.register(r'mini-slider', viewsAPI.MiniFotoSliderViewSet)
router.register(r'time_mini-slider', viewsAPI.TimeForMiniSliderViewSet)
router.register(r'social_networks', APIviews.SocialNetworksViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
