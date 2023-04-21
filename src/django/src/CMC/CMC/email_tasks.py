from __future__ import absolute_import, unicode_literals
from celery import shared_task

@shared_task
def sendEmail(receiver):
    if receiver is None:
        print("No receiver specified")
        return None
    print(f"Sending email to {receiver}")
    return receiver