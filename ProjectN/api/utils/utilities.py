from django.core.mail import send_mail
from twilio.rest import Client
from django.conf import settings
import logging
logger = logging.getLogger(__name__)


def send_emails(subject, message, recipient_list):
    try:
        send_mail(
            subject,
            message,
            'from@example.com',
            recipient_list,
            fail_silently=False,
        )
        return True  # Explicitly return True on success
    except Exception as e:
        # Handle exception (maybe log it)
        return False  # Explicitly return False on failure

# Initialize Twilio client globally if this doesn't need to be refreshed often
twilio_client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

def send_sms(to, body, from_=settings.TWILIO_PHONE_NUMBER):
    """
    Sends an SMS message using Twilio API.

    Args:
        to (str): The phone number to send the SMS to.
        body (str): The body of the SMS message.
        from_ (str): The phone number that sends the SMS (Twilio phone number).

    Returns:
        str: A message indicating success with the Twilio message SID, or an error message.
    """
    try:
        message = twilio_client.messages.create(
            body=body,
            from_=from_,
            to=to
        )
        return f"SMS sent successfully: {message.sid}"
    except Exception as e:
        logger.error(f"Failed to send SMS to {to}: {str(e)}")
        return f"Failed to send SMS: {str(e)}"



