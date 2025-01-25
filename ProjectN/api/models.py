from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.name

class NotificationType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_type = models.ForeignKey(NotificationType, on_delete=models.CASCADE)
    message = models.TextField()
    sent = models.BooleanField(default=False)
    date_sent = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.notification_type.name} to {self.recipient.name}"

class NotificationSetting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_type = models.ForeignKey(NotificationType, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.notification_type.name} settings for {self.user.name}"