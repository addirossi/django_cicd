from django.test import TestCase
from rest_framework.test import APIClient


class TestLogistic(TestCase):
    def test_sample_view(self):
        client = APIClient()
        response = client.get('/test/')
        self.assertEqual(response.status_code, 200)
