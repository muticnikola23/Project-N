from rest_framework.routers import DefaultRouter
from .views import UserViewSet, NotificationTypeViewSet, NotificationViewSet, NotificationSettingViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'notification_types', NotificationTypeViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'notification_settings', NotificationSettingViewSet)

urlpatterns = router.urls
