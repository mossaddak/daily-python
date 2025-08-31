'''
Requirements: firebase_admin
'''

from firebase_admin import db

from django.db.models.signals import post_save
from django.dispatch import receiver

from notifications.models import Notification


@receiver(post_save, sender=Notification)
def send_notification_to_firebase_database(sender, instance, created, *args, **kwargs):
    if created:
        target = instance.target
        url = f"/notifications/admin"
        if target:
            url = f"/notifications/{str(target.uid)}"
        ref = db.reference(url)
        # Push notification data
        ref.push(
            {
                "uid": str(instance.uid),
                "title": instance.title,
                "user_kind": instance.user_kind,
                "kind": instance.kind,
                "model_kind": instance.model_kind,
                "is_read": instance.is_read,
                "description": instance.description,
                "timestamp": {".sv": "timestamp"},
            }
        )
