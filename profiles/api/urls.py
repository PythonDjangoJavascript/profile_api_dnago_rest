from django.urls import path
from profiles.api.views import ProfileList
from profiles.api.views import ProfileViewSet

"""the action item here get: list dic must be provied when calling as_view 
 on a view set"""
profile_list = ProfileViewSet.as_view({"get": "list"})
profile_detail = ProfileViewSet.as_view({"get": "retrieve"})

urlpatterns = [
    path('profileslv/', ProfileList.as_view(), name='profile-lis'),

    path('profiles/', profile_list, name='profile-list'),
    path('profiles/<int:pk>/', profile_detail, name='profile-detail'),
]
