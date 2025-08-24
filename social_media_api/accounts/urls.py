from django.urls import path
from .views import RegisterView, LoginView, UserProfileView, FollowUserView, UnfollowUser, FollowingListView, FollowerList
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
        path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
        path('register/', RegisterView.as_view(), name="register"),
        path('login/', LoginView.as_view(), name="login"),
        path('profile/', UserProfileView.as_view(), name="profile"),
        path("follow/<int:user_id>/", FollowUserView.as_view(), name="follow-user"),
        path("unfollow/<int:user_id>/", UnfollowUser.as_view(), name="unfollow-user"),
        path("followers/<str:username>/", FollowerList.as_view(), name="followers-list"),
        path("following/<str:username>/", FollowingListView.as_view(), name="following-list"),
]