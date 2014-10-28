from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Someone opens up the homepage
        self.browser.get('http://localhost:8000')

        # Does the page title mention to-do
        self.assertIn('To-Do', self.browser.title)
        print("Browser title was " + browser.title)
        self.fail('Finish the test!')

        # Does a enter a to-do item appear

        # Enter "Buy peacock feathers" into text box

        # Hit enter, page updates with item in to-do list 
        # "1: Buy peacock feathers"

        # Still a text box, enter "Use peacock feathers to make a fly"

        # Page updates and shows both items

        # Explanatory text about remembering users with a unique URL
         
        # Click on URL, to-do list still there
         
        # Leave session

if __name__ == '__main__':
    unittest.main(warnings='ignore')
