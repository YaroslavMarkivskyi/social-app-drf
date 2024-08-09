from django.urls import path

from .views import (
    ProfielListAPIView,
    ProfileDetailAPIView,
    UpdateProfileAPIView,
    FollowerListView,
    FollowAPIView,
    UnfollowApiView
)


urlpatterns = [
    path("all/", ProfielListAPIView.as_view(), name="all-profiles"),
    path("me/", ProfileDetailAPIView.as_view(), name="my-profile"),
    path("me/update/", UpdateProfileAPIView.as_view(), name="update-profile"),
    path("me/followers/", FollowerListView.as_view(), name="followers"),
    path("<uuid:user_id>/follow/", FollowAPIView.as_view(), name="follow"),
    path("<uuid:user_id>/unfollow/", UnfollowApiView.as_view(), name="unfollow"),
]
