from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from .models import Notifications
from .serializers import NotificationsSerializer

class NotificationListView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def get(self, request):
        notifications=Notifications.objects.filter(recipient=request.user).order_by("-timestamp")

        # Separate read and unread notifications
        unread=notifications.filter(read=False)
        read=notifications.filter(read=True)

        serializer_unread = NotificationsSerializer(unread, many=True)
        serializer_read = NotificationsSerializer(read, many=True)

        return Response({
            "unread": serializer_unread.data,
            "read": serializer_read.data
        })
    
class MarkNotificationsAsReadView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def post(self, request, notification_id):
        try:
            notification = Notifications.objects.get(id=notification_id, recipient=request.user)
            notification.read=True
            notification.save()
            return Response({"detail": "Notification marked as read"}, status=status.HTTP_200_OK)
        except Notifications.DoesNotExist:
            return Response({"detail": "Notification not found"}, status=status.HTTP_404_NOT_FOUND)