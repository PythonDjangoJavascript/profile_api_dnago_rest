from rest_framework import serializers
from profiles.models import Profile, ProfileStatus


class ProfileSerializer(serializers.ModelSerializer):
    """Serializes Profile Model"""

    user = serializers.StringRelatedField(read_only=True)
    """Setting avatar read only here because I want use use separate
    serializer for avatar"""
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


class ProfileAvatarSerializer(serializers.ModelSerializer):
    """Serializes Avatar (user image) only"""

    class Meta:
        model = Profile
        fields = ("avatar", )


class ProfileStatusSerializer(serializers.ModelSerializer):
    """Serializes Profile status model"""

    class Meta:
        model = ProfileStatus
        fields = "__all__"
