from unittest import TestCase

from rest_framework.test import APIClient


class MyTest(TestCase):
    def test_ok(self):
        assert True

    def test_sample_view(self):
        url = "/api/v1/test/"
        client = APIClient()
        response = client.get(url)
        assert response.status_code == 200
