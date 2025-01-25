from datetime import timezone

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, NotificationType, Notification, NotificationSetting
from .serializer import UserSerializer, NotificationTypeSerializer, NotificationSerializer, \
    NotificationSettingSerializer
from .utils.utilities import send_email


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NotificationTypeViewSet(viewsets.ModelViewSet):
    queryset = NotificationType.objects.all()
    serializer_class = NotificationTypeSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    @action(detail=True, methods=['post'])
    def send_notification(self, request, pk=None):
        notification = self.get_object()
        if notification.sent:
            return Response({'status': 'Notification already sent.'}, status=status.HTTP_400_BAD_REQUEST)

        # Here, implement your logic to send the notification.
        # For example, use an email library to send an email.
        # Assume the sending operation sets `notification.sent` to True and saves the date_sent.

        notification.sent = True
        notification.date_sent = timezone.now()
        notification.save()

        return Response({'status': 'Notification sent successfully.'}, status=status.HTTP_200_OK)


class NotificationSettingViewSet(viewsets.ModelViewSet):
    queryset = NotificationSetting.objects.all()
    serializer_class = NotificationSettingSerializer

# notifications/views.py
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        send_email(
            'New Notification',
            instance.message,
            [instance.recipient.email]  # Assuming the recipient has an email field
        )
