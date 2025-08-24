from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = settings.AUTH_USER_MODEL

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications_sent")
    verb=models.CharField(max_length=255) #commented, liked, followed
    #Generic relation to the object the action is related to or is about
    target_content_type=models.ForeignKey(ContentType, on_delete=models.CASCADE)
    target_object_id=models.PositiveIntegerField()
    target = GenericForeignKey("target_content_type", "target_object_id")

    timestamp = models.DateTimeField(auto_now_add=True)
    read=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.actor} {self.verb} {self.target} → {self.recipient}"
        