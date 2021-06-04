from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework import mixins

from profiles.models import Profile, ProfileStatus
from profiles.api.pemissions import IsOwnProfileOrReadOnly, IsOwnStatusOrReadOnly
from profiles.api.serializers import (ProfileSerializer,
                                      ProfileStatusSerializer,
                                      ProfileAvatarSerializer)


# I am using generics updateAPIView as I am oinly going to update avatar
# Using this class
class AvatarUpdateView(generics.UpdateAPIView):
    """Manages users avatar update"""

    # dont need to define queryset as I am going to define get_object method
    serializer_class = ProfileAvatarSerializer
    permission_classes = [IsAuthenticated, ]  # don't need to add user edit
    #                 Permission as get_object will get only logged in user data

    def get_object(self):
        """Here providing profile object as avatar serializer require that"""

        profile_object = self.request.user.profile
        return profile_object


class ProfileViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """Retieve update Profile api"""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnProfileOrReadOnly]

# class ProfileViewSet(ReadOnlyModelViewSet):
#     """manages profile api endpoints views"""

#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticated, ]


# I am useing ModelViewSet here as it will replace above used mixin for update
# retrieve and genericsViewset > check ModelViewSet Code
class ProfileStatusViewSet(ModelViewSet):
    """Handle list, retrieve, update, delete profile status api view"""
    queryset = ProfileStatus.objects.all()
    serializer_class = ProfileStatusSerializer
    permission_classes = [IsAuthenticated, IsOwnStatusOrReadOnly]

    def perform_create(self, serializer):
        """overriding create method as user should be only allowed to create
            for their profiles and so user_prfile field should be selected 
            automatically"""

        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)


# profile list using generics list view
class ProfileList(generics.ListAPIView):
    """Returns profiles list to authenticated user"""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnProfileOrReadOnly]
