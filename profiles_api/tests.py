#Unit Testing

import json
from urllib import response
from .models import UserProfile

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from profiles_api.serializers import UserProfileSerializer

class RegistrationTestCase(APITestCase):

    def test_registration1(self):
        correct_data = {
            'email':'test@planetball.com',
            'name':'Test User ',
            'password':'some_strong_password123',
        }
        response = self.client.post('/api/profile/',correct_data)
    #    test should return 1
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_registration2(self):
        incorrect_data = {
            'email':'test',
            'name':'Test User ',
            'password':'some_strong_password123',
        }
        response = self.client.post('/api/profile/',incorrect_data)
    #    test should return 1
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

        