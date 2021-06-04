from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from profiles.api.views import ProfileList
from profiles.api.views import (ProfileViewSet,
                                ProfileStatusViewSet,
                                AvatarUpdateView)

# """the action item here get: list dic must be provied when calling as_view
#  on a view set"""
# profile_list = ProfileViewSet.as_view({"get": "list"})
# profile_detail = ProfileViewSet.as_view({"get": "retrieve"})

# commented above line as I am using routers to replace those line
router = DefaultRouter()
# here router will generate links of different endpoints by itsalfe
router.register(r"profiles", ProfileViewSet)
router.register(r"status", ProfileStatusViewSet)

urlpatterns = [
    path('profileslv/', ProfileList.as_view(), name='profile-lis'),

    # path('profiles/', profile_list, name='profile-list'),
    # path('profiles/<int:pk>/', profile_detail, name='profile-detail'),
    path('', include(router.urls)),
    path('avatar', AvatarUpdateView.as_view(), name='avater-update'),

]
