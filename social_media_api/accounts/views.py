from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer
from django.shortcuts import get_object_or_404

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class =  RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes =  [AllowAny]

    def post(self, requests, *args, **kwargs):
        serializer = self.get_serializer(data=requests.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    
class UserProfileView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class FollowUserView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request, username):
        target_user = get_object_or_404(CustomUser, username=username)

        if request.user == target_user:
              return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        
        #Follow user if not already following
        request.user.following.add(target_user)
        return Response({"detail": f"You are now following {target_user.username}"}, status=status.HTTP_200_OK)

class UnfollowUser(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, username):
        target_user = get_object_or_404(CustomUser, username=username)

        if request.user == target_user:
            return Response({"detail": "You can not unfollow yourself"}, status=status.HTTP_400_BAD_REQUEST)
        
        #Unfollow a user if following
        request.user.following.remove(target_user)
        return Response({"detail": f"You unfollowed {target_user.username}"}, status=status.HTTP_200_OK)
    
class FollowerList(APIView):
    """List all followers(public)"""
    permission_classes=[AllowAny]

    def get(self, request, username):
        user = get_object_or_404(CustomUser, username=username)
        followers=user.followers.all().values("id", "username")
        return Response({"followers": list(followers)}, status=status.HTTP_200_OK)
    
class FollowingListView(APIView):
    """List a certain user is following"""
    permission_classes=[AllowAny]

    def get(self, request, username):
        user=get_object_or_404(CustomUser, username=username)
        following=user.following.all().values("id", "username")
        return Response({"following": list(following)}, status=status.HTTP_200_OK)
    
