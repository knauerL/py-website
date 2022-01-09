import unittest
from unittest.case import skip
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
    @skip
    def testH1(self):
        headerText = self.browser.find_element_by_tag_name("h1").text
        self.assertIn('Welcome traveler', headerText, 'Headers do not match')
    @skip
    def testDogBtn(self):
        self.browser.find_element_by_id("submit").click()
        self.browser.find_element_by_id("btn2").click()
        self.assertIn('Dog Choice', self.browser.title, 'functional test - doesnt direct to right page')
    @skip
    def testCatBtn(self):
        self.browser.find_element_by_id("submit").click()
        self.browser.find_element_by_id("btn3").click()
        self.assertIn('Cat Choice', self.browser.title, 'functional test - doesnt direct to right page')

#TESTS FOR W2 ASSN 
    @skip
    def testNameInput(self):
        txt1 = self.browser.find_element_by_id('txt1').text
        self.assertIn('What is your name?', txt1)
        self.browser.find_element_by_id("plName").send_keys("Sydney")

        self.browser.find_element_by_id("submit").click()
        self.assertIn('Sydney', self.browser.title, 'functional test - doesnt direct to right page')
    @skip
    def testNameRedir(self):
        self.browser.find_element_by_id("submit").click()
        pTxt = self.browser.find_element_by_tag_name("p").text
        self.assertIn('There is a dog and a cat. Which one will you follow?', pTxt, 'functional test - doesnt direct to right page')

#TESTS FOR W3 ASSN
    @skip
    def testTreeImages(self):
        self.browser.find_element_by_id("submit").click()
        self.browser.find_element_by_id("btn3").click()
        self.browser.find_element_by_id("btn5").click()
        #imgId = self.browser.find_element_by_id('trees')
        self.assertIn('trees', self.browser.find_element_by_id('trees'), 'functional test - trees ID not found')
    @skip
    def testRightPage(self):
        self.browser.find_element_by_id("submit").click()
        self.browser.find_element_by_id("btn3").click()
        self.browser.find_element_by_id("btn5").click()
        self.assertIn('http://localhost:8000/right.html', self.browser.current_url, 'functional test - doesnt direct to right page')
    @skip
    def testLeftPage(self):
        self.browser.find_element_by_id("submit").click()
        self.browser.find_element_by_id("btn3").click()
        self.browser.find_element_by_id("btn4").click()
        self.assertIn('http://localhost:8000/left.html', self.browser.current_url, 'functional test - doesnt direct to right page')

#TESTS FOR W4 ASSN
    def testWinBtn(self):
        self.browser.find_element("submit").click()
        self.browser.find_element_by_id("btn3").click()
        self.browser.find_element_by_id("btn4").click()
        self.browser.find_element_by_id("btn6").click()
        self.assertIn('http://localhost:8000/win.html', self.browser.current_url, 'functional test - doesnt direct to the winning page page')

    def testLoseBtn(self):
        self.browser.find_element("submit").click()
        self.browser.find_element_by_id("btn3").click()
        self.browser.find_element_by_id("btn4").click()
        self.browser.find_element_by_id("btn7").click()
        self.assertIn('http://localhost:8000/lose.html', self.browser.current_url, 'functional test - doesnt direct to the losing page page')

    def testWinPage(self):
        self.browser.find_element("submit").click()
        self.browser.find_element_by_id("btn3").click()
        self.browser.find_element_by_id("btn4").click()
        self.browser.find_element_by_id("btn6").click()
        h1Txt = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("You've successfully defeated your enemy, congratulations.", h1Txt, 'functional test - doesnt direct to the winners page page')
    
    def testLosePage(self):
        self.browser.find_element("submit").click()
        self.browser.find_element_by_id("btn3").click()
        self.browser.find_element_by_id("btn4").click()
        self.browser.find_element_by_id("btn7").click()
        h1Txt = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("You chose wrong, and you've been killed, rest in peace.", h1Txt, 'functional test - doesnt direct to the losers page page')


if __name__ == '__main__':
    unittest.main()