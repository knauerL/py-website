import unittest
from selenium import webdriver

class FunctionalTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://localhost:8000')
    def tearDown(self) :
        self.browser.quit()

    #from lecture notes
    # def test_Title(self):
    #     self.assertIn('Django', self.browser.title, 'Wrong title')
    
#TESTS FOR W1 ASSN
    def testH1(self):
        headerText = self.browser.find_element_by_tag_name("h1").text
        self.assertIn('Welcome traveler', headerText, 'Headers do not match')
    
    def testDogBtn(self):
        self.browser.find_element_by_id("submit").click()
        self.browser.find_element_by_id("btn2").click()
        self.assertIn('Dog Choice', self.browser.title, 'functional test - doesnt direct to right page')

    def testCatBtn(self):
        self.browser.find_element_by_id("submit").click()
        self.browser.find_element_by_id("btn3").click()
        self.assertIn('Cat Choice', self.browser.title, 'functional test - doesnt direct to right page')

#TESTS FOR W2 ASSN 
    def testNameInput(self):
        txt1 = self.browser.find_element_by_id('txt1').text
        self.assertIn('What is your name?', txt1)
        self.browser.find_element_by_id("plName").send_keys("Sydney")

        self.browser.find_element_by_id("submit").click()
        self.assertIn('Sydney', self.browser.title, 'functional test - doesnt direct to right page')

    def testNameRedir(self):
        self.browser.find_element_by_id("submit").click()
        pTxt = self.browser.find_element_by_tag_name("p").text
        self.assertIn('There is a dog and a cat. Which one will you follow?', pTxt, 'functional test - doesnt direct to right page')


if __name__ == '__main__':
    unittest.main()