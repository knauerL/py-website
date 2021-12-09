from selenium import webdriver
import unittest

#does the selenium
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
    def testH1(self):
        headerText = self.browser.find_element_by_tag_name("h1").text
        self.assertIn('Welcome traveler', headerText, 'Headers do not match')

    def testNameInput(self):
        #txt1 = self.browser.find_elements(By.ID('txt1'))
        #self.assertIn('What is your name?', txt1)
        #self.browser.find_element(By.ID("nameInput")).send_keys("Sydney")

        self.browser.find_element_by_id("btn1").click()
        self.assertIn('Name Input', self.browser.title, 'functional test - doesnt direct to right page')
    
    def testDogBtn(self):
        self.browser.find_element_by_id("btn1").click()
        self.browser.find_element_by_id("btn2").click()
        self.assertIn('Dog Choice', self.browser.title, 'functional test - doesnt direct to right page')

    def testCatBtn(self):
        self.browser.find_element_by_id("btn1").click()
        self.browser.find_element_by_id("btn3").click()
        self.assertIn('Cat Choice', self.browser.title, 'functional test - doesnt direct to right page')


if __name__ == '__main__':
    unittest.main()