from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest, response

# Create your tests here.
class HomePageTest(TestCase):
    def testHomePage(self):
        found = resolve('/')
        self.assertEqual(response, 'home.html')