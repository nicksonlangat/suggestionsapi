from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FeedbackViewSet
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'feedback', FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]