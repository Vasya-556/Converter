from backend.converter.api.urls import *
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from backend.converter.api.views import load_files

class TestUrls(SimpleTestCase):
    def test_load_files(self):
        url = reverse('load')
        resolved = resolve(url)
        self.assertEqual(resolved.func.__name__, load_files.__name__)