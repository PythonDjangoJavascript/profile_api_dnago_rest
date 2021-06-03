from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from profiles.models import Profile
from profiles.api.serializers import ProfileSerializer


class ProfileViewSet(ReadOnlyModelViewSet):
    """manages profile api endpoints views"""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, ]

# profile list using generics list view


class ProfileList(generics.ListAPIView):
    """Returns profiles list to authenticated user"""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, ]
