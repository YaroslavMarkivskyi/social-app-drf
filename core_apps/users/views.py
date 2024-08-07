from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from .serializers import UserSerializer


class CustomUserDetailView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = IsAuthenticated

    def get_objetc(self):
        return self.request.user

    def get_queryset(self):
        return get_user_model().objects.none()
