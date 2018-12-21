from django.test import TestCase

# Create your tests here.
from django.core.urlresolvers import reverse
from django.urls import resolve
from .views import home
class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        reponse = self.client.get(url)
        self.assertEquuals(response.status_code,200)
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)
