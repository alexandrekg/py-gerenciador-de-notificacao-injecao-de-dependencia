from services.notification_service import NotificationManager
from services.sms_service import SmsService
from services.email_service import EmailService


def _send_basic_notification():
    print('Enviando notificação para membros básico')
    notification_service = NotificationManager(EmailService())
    notification_service.send_notification()


def _send_premium_notification():
    print('Enviando notificação para membros premium')
    notification_service = NotificationManager(EmailService())
    notification_service.send_notification()

    notification_service = NotificationManager(SmsService())
    notification_service.send_notification()


news1 = _send_basic_notification()
news2 = _send_basic_notification()

premium_news = _send_premium_notification()
