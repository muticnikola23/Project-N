from .sender import EmailNotificationSender, SMSNotificationSender

class NotificationSenderFactory:
    @staticmethod
    def get_sender(notification_type_name):
        # Maps notification type names to sender classes
        sender_map = {
            'video/x-mpeg': EmailNotificationSender,
            'video/mpeg': EmailNotificationSender,
            'text/plain': SMSNotificationSender
        }
        sender_class = sender_map.get(notification_type_name.lower())
        if sender_class:
            return sender_class()
        else:
            raise ValueError(f"Unsupported notification type: {notification_type_name}")

