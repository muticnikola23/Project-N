from datetime import timezone

from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, NotificationType, Notification, NotificationSetting
from .serializer import UserSerializer, NotificationTypeSerializer, NotificationSerializer, \
    NotificationSettingSerializer
from .utils.factories import NotificationSenderFactory
import logging
logger = logging.getLogger(__name__)



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NotificationTypeViewSet(viewsets.ModelViewSet):
    queryset = NotificationType.objects.all()
    serializer_class = NotificationTypeSerializer


class NotificationSettingViewSet(viewsets.ModelViewSet):
    queryset = NotificationSetting.objects.all()
    serializer_class = NotificationSettingSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    @action(detail=True, methods=['post'], url_path='send-notifications')
    def send_notification(self, request, pk=None):
        notification = self.get_object()
        if notification.sent:
            return Response({'status': 'Notification already sent.'}, status=status.HTTP_400_BAD_REQUEST)

        notification_type_name = notification.notification_type.name  # Using the name field to determine type
        try:
            sender = NotificationSenderFactory.get_sender(notification_type_name)
            result = sender.send(notification)
            if result:
                notification.sent = True
                notification.date_sent = timezone.now()
                notification.save()
                return Response({'status': 'Notification sent successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Failed to send notification: {str(e)}", exc_info=True)
            return Response({'status': f'Failed to send notification: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'status': 'Unexpected error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

