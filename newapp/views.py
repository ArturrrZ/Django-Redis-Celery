import os
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from .tasks import celery_send
import re

# Create your views here.
def home(request):
    return HttpResponse("Home View")

def anon_email_old(request):
    if request.method == 'POST':
        subject = request.POST.get("subject")
        body = request.POST.get("body")
        recipient = request.POST.get("recipient")
        # sendind via django function saving the email cuz of configurations in settings.py
        #
        # send_mail(
        #     subject,
        #     body,
        #     # "no-reply@gmail.com", #if mail.backends.filebased
        #     os.environ.get("EMAIL_HOST_USER"),
        #     [recipient],
        # )
        #
        celery_send.delay(subject, body, recipient)
        return HttpResponse("Sending...")
    return render(request, "newapp/anon_email.html")

def anon_email(request):
    if request.method == 'POST':
        subject = request.POST.get("subject", "").strip()
        body = request.POST.get("body", "").strip()
        recipient = request.POST.get("recipient", "").strip()

        if not subject or not body or not recipient:
            return render(request, "newapp/anon_email.html", {
                "error": "Fill out all the fields!"
            })
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", recipient):
            return render(request, "newapp/anon_email.html", {
                "error": "Invalid email address."
            })
        celery_send.delay(subject, body, recipient)
        return render(request, "newapp/anon_email.html", {
            "success": "Email has been sent"
        })

    return render(request, "newapp/anon_email.html")