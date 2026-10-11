from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):
    def __init__(self, email):
        self.email = email

    def send(self, message):
        print(f"Sending email to {self.email}: {message}")


class SMSNotification(Notification):
    def __init__(self, phone):
        self.phone = phone

    def send(self, message):
        print(f"Sending SMS to {self.phone}: {message}")


class PushNotification(Notification):
    def __init__(self, device_id):
        self.device_id = device_id

    def send(self, message):
        print(f"Sending push notification to {self.device_id}: {message}")


class NotificationFactory:
    @staticmethod
    def create_notification(notification_type, recipient):
        if notification_type == "email":
            return EmailNotification(recipient)
        elif notification_type == "sms":
            return SMSNotification(recipient)
        elif notification_type == "push":
            return PushNotification(recipient)
        else:
            raise ValueError("Unsupported notification type")


class NotificationService:
    def __init__(self, factory):
        self.factory = factory

    def notify(self, notification_type, recipient, message):
        notification = self.factory.create_notification(
            notification_type, recipient
        )
        notification.send(message)


factory = NotificationFactory()
service = NotificationService(factory)

service.notify("email", "user@example.com", "Your order has been shipped.")
service.notify("sms", "+37499123456", "Your verification code is 1234.")
service.notify("push", "device_101", "You have a new message.")
