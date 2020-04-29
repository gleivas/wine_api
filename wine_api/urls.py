from django.urls import path, include
from rest_framework import routers

from wine_reviews import views

router = routers.DefaultRouter()
router.register(r'api/wines', views.WineViewSet, basename='wine')

urlpatterns = [
    path('', include(router.urls)),
]
