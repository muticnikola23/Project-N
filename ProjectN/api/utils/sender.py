from .utilities import send_emails, send_sms

class BaseNotificationSender:
    def send(self, notification):
        raise NotImplementedError("Each sender must implement a send method.")

class EmailNotificationSender(BaseNotificationSender):
    def send(self, notification):
        return send_emails(
            subject='Your Notification Subject',
            message=notification.message,
            recipient_list=[notification.recipient.email]
        )

class SMSNotificationSender(BaseNotificationSender):
    def send(self, notification):
        """
        Sends an SMS notification using the provided notification instance.

        Args:
            notification (Notification): The notification instance containing the message and recipient details.

        Returns:
            str: A message indicating the outcome of the send operation.
        """
        # Call the send_sms function with the correct arguments
        return send_sms(
            to=notification.recipient.phone_number,
            body=notification.message  # Aligning parameter name with send_sms function signature.
        )