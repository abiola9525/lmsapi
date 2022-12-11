from django.urls import path
from rest_framework.routers import DefaultRouter
from ass.views import AssignmentViewSet




router = DefaultRouter()
router.register(r'', AssignmentViewSet, basename='assignments')
urlpatterns = router.urls


