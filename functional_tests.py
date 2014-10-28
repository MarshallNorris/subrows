from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Does a enter a to-do item appear
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a to-do item')
        
        # Enter "Buy peacock feathers" into text box
        inputbox.send_keys('Buy peacock feathers')
        
        # Hit enter, page updates with item in to-do list 
        # "1: Buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)
        
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )

        # Still a text box, enter "Use peacock feathers to make a fly"
        self.fail('Finish the test!')

        # Page updates and shows both items

        # Explanatory text about remembering users with a unique URL
         
        # Click on URL, to-do list still there
         
        # Leave session

if __name__ == '__main__':
    unittest.main(warnings='ignore')
