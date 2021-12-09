from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest, request, response

# Create your tests here.
class HomePageTest(TestCase):
    def testHomePage(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page, "test.py - Home resolves incorrectly")

    def testH1(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<html><title>Escape Game</title><body><h1>Welcome traveler</h1><p id="txt1">What is your name?</p><input type="text" id="nameInput"><a href="name.html"><button type="submit"id="btn1">Enter</button></a><br><p id="txt2">There is a dog and a cat. Which one will you follow?</p><a href="dog.html"><button type="submit"id="btn2">Dog</button></a><a href="cat.html"><button type="submit"id="btn3">Cat</button></a></body></html>', html)
        self.assertTrue(html.endswith('</html>'))
        