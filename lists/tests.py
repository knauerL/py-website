from django.test import TestCase
from django.urls import resolve
from lists.views import home_page, cat_page, dog_page, right_page, left_page
from django.http import HttpRequest, request, response

# Create your tests here.
class HomePageTest(TestCase):
#TESTS FOR W1 ASSN
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

#TESTS FOR W2 ASSN
    def testCatPage(self):
        found = resolve('/cat.html')
        self.assertEqual(found.func, cat_page, "test.py - CAT PAGE resolves incorrectly")

    def testHomePage(self):
        found = resolve('/dog.html')
        self.assertEqual(found.func, dog_page, "test.py - DOG PAGE resolves incorrectly")
        
#TESTS FOR W3 ASSN
#TO COTTRELL: I know that you said my unit tests look bare, but if I'm being completely honest, I'm completely lost on what these do and how to do them. I understand the functional tests fine and can do them, but these are just like a blind side for me.
    def testLeftPage(self):
        found = resolve('/left.html')
        self.assertEqual(found.func, left_page, 'test.py - LEFT PAGE resolves incorrectly')
    
    def testRightPage(self):
        found = resolve('/right.html')
        self.assertEqual(found.func, right_page, 'test.py - LEFT PAGE resolves incorrectly')