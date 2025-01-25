from django.core.mail import send_mail

def send_email(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        'from@example.com',  # Email defined in EMAIL_HOST_USER
        recipient_list,
        fail_silently=False,
    )
