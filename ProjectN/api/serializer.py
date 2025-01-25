from rest_framework import serializers
from .models import User, NotificationType, Notification, NotificationSetting

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone_number']

class NotificationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationType
        fields = ['id', 'name', 'description']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'notification_type', 'message', 'sent', 'date_sent']

class NotificationSettingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.name')
    notification_type = serializers.ReadOnlyField(source='notification_type.name')

    class Meta:
        model = NotificationSetting
        fields = ['id', 'user', 'notification_type', 'is_active']
