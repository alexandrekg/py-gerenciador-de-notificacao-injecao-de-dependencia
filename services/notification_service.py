class NotificationService:
    def __init__(self, notification_service):
        self.notification_service = notification_service

    def send_notification(self):
        self.notification_service.send_notification()
