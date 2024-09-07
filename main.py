from services.notification_service import NotificationService
from services.sms_service import SmsService
from services.email_service import EmailService


def _send_basic_notification():
    print('Enviando notificação para membros básico')
    email_service = NotificationService(EmailService())
    email_service.send_notification()


def _send_premium_notification():
    print('Enviando notificação para membros premium')
    email_service = NotificationService(EmailService())
    email_service.send_notification()

    sms_service = NotificationService(SmsService())
    sms_service.send_notification()

_send_basic_notification()
_send_premium_notification()
