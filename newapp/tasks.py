from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
import os

@shared_task
def add(x, y):
    return x + y

@shared_task(bind=True)
def celery_send(self, subject, body, recipient):
    try:
        send_mail(
            subject=subject,
            message=body,
            from_email=os.environ.get('EMAIL_HOST_USER'),
            recipient_list=[recipient],
        )
    except Exception as e:
        # логируем ошибку
        self.retry(exc=e, countdown=10, max_retries=3)
        raise e