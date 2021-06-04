import json

from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from profiles.api.serializers import ProfileSerializer
from profiles.models import Profile


# create user method


def create_user(**params):
    """take kwargs and create user to the database"""
    return User.objects.create_user(**params)


class UserRegTestCase(APITestCase):
    """Tests user registration systme"""

    def test_registration(self):
        """Test create user with valid payload succesful"""

        payload = {
            'username': 'testuser',
            'email': 'test@email.com',
            'password1': 'superSecurePassword',
            'password2': 'superSecurePassword'
        }
        response = self.client.post('/api/rest-auth/registration/', payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # response should not contain the password
        self.assertNotIn("password", response.data)

    def test_user_duplicate(self):
        """Tests if duplicate user get rejected"""

        payload = {
            'username': 'testuser',
            'email': 'test@email.com',
            'password1': 'superSecurePassword',
            'password2': 'superSecurePassword'
        }
        payload1 = {
            'username': 'testuser',
            'email': 'test@email.com',
            'password': 'superSecurePassword',
        }
        create_user(**payload1)
        response = self.client.post('/api/rest-auth/registration/', payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unauthorized_profile_list_get_request(self):
        """test login required to get profile list"""

        response = self.client.get(reverse('profile-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class ProfileViewSetTestCase(APITestCase):
    """Test Proile api endpoints"""

    # its profile list as we use router for urls and it will add list url this way
    LIST_URL = reverse('profile-list')
    PROFILE_DETAIL_URL = reverse('profile-detail', kwargs={"pk": 1})

    def setUp(self) -> None:
        payload = {
            'username': 'testuser',
            'email': 'test@email.com',
            'password': 'superSecurePassword',
        }
        self.user = create_user(**payload)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token "+self.token.key)

    def test_profile_list_authenticated(self):
        """Test authenticated user can read profile lists"""

        response = self.client.get(self.LIST_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_profile_list_unauthenticated(self):
        """test login required to get profile list"""

        # clearing logged user logged in setUp
        self.client.force_authenticate(user=None)
        response = self.client.get(self.LIST_URL)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_profile_detail_retrieve(self):
        """Test profile dtail api endpoints"""

        # here profile-detali as we used router for urls and it wll add -detail
        # for detail view as queryset was prfile so url is profile-detail
        response = self.client.get(self.PROFILE_DETAIL_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'], 'testuser')

    def test_profile_update_by_owner(self):
        """Test user can update thir profile"""

        payload = {'city': 'tokio', 'bio': 'Genious'}
        res = self.client.put(self.PROFILE_DETAIL_URL,
                              payload)
        self.user.refresh_from_db()  # as we just updated database

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(res.content),
                         {'id': 1, 'user': 'testuser', 'bio': 'Genious',
                         'city': 'tokio', 'avatar': None})

    def test_profile_update_by_random_user(self):
        """test user can update others profile"""

        payload = {
            'username': 'random_user',
            'email': 'test@email.com',
            'password': 'superSecurePassword',
        }
        random_user = create_user(**payload)
        self.client.force_authenticate(user=random_user)

        res = self.client.put(self.PROFILE_DETAIL_URL,
                              {'bio': 'hacked!!'})

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
