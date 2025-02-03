from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, NotificationViewSet, NotificationTypeViewSet, NotificationSettingViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'notification_types', NotificationTypeViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'notification_settings', NotificationSettingViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API documentation for all endpoints",
        terms_of_service="https://www.yourcompany.com/terms/",
        contact=openapi.Contact(email="contact@yourcompany.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
