from selenium import webdriver
import unittest

class FunctionalTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://localhost:8000')
    def tearDown(self) :
        self.browser.quit()

    #from lecture notes
    # def test_Title(self):
    #     self.assertIn('Django', self.browser.title, 'Wrong title')
    
    #tests for w1 assn
    def testWelcomeScreen(self):
        self.assertIn()


if __name__ == '__main__':
    unittest.main()