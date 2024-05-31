from rest_framework.test import APITestCase
from django.http import HttpResponse
from health.models import HealthTest

# Create your tests here.


class HealthListViewTests(APITestCase):
    def setUp(self):
        HealthTest.objects.create(message='Test message')

    def test_index_returns_http_response(self):
        request = self.client.get('/health/')
        self.assertIsInstance(request, HttpResponse)

    def test_index_returns_200(self):
        request = self.client.get('/health/')
        self.assertEqual(request.status_code, 200)

    def test_index_html_content_equal_stored_message(self):
        request = self.client.get('/health/')
        self.assertEqual(request.content, b'Test message')

    def test_index_returns_none_when_no_health_tests(self):
        HealthTest.objects.all().delete()
        request = self.client.get('/health/')
        self.assertEqual(request.content, b'None')
