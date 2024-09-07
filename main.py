from services.notification_service import NotificationManager
from services.sms_service import SmsService
from services.email_service import EmailService


def _send_basic_notification():
    print('Enviando notificação para membros básico')
    email_service = NotificationManager(EmailService())
    email_service.send_notification()


def _send_premium_notification():
    print('Enviando notificação para membros premium')
    email_service = NotificationManager(EmailService())
    email_service.send_notification()

    sms_service = NotificationManager(SmsService())
    sms_service.send_notification()

_send_basic_notification()
_send_premium_notification()
