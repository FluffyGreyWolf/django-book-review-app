from django.test import TestCase, Client
from reviews.views import welcome_view

class TestWelcomeView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_welcome_view(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)