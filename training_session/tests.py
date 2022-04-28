#Unit Testing
from rest_framework import status
from rest_framework.test import APITestCase


class TrainingSessionTestCase(APITestCase):

    def test_request_session(self):
        correct_data = {
            'title':'Hello Title',
            'description':'Test User ',
           
        }
        response = self.client.post('/api/request_session/',correct_data)
    #    test should return 1
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_ask_question(self):
        correct_data = {
            'title':'Hello Title',
            'description':'Test User ',
        }
        response = self.client.post('/api/ask_question/',correct_data)
    #    test should return 1
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

        