from rest_framework import serializers
from .models import Notifications

class NotificationsSerializer(serializers.ModelSerializer):
    actor=serializers.StringRelatedField()
    recipient = serializers.StringRelatedField()

    class Meta:
        model = Notifications
    fields = ["id", "recipient", "actor", "verb", "target_object_id", "timestamp", "read"]