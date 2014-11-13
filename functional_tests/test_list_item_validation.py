from .base import FunctionalTest
from unittest import skip

class ItemValidationTest(FunctionalTest):
        
    def test_cannot_add_empty_list_items(self):
        # User opens home page and accidentally submits empty item
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        
        # Error message appears, item cannot be blank
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")
        
        # User enters correct item
        self.get_item_input_box().send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')
        
        # User submits second blank item
        self.get_item_input_box().send_keys('\n')
        
        # Similar warning appears
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")
        
        # User fills some text in
        self.get_item_input_box().send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')
        
    def test_cannot_add_duplicate_items(self):
        # User starts a new list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy wellies\n')
        self.check_for_row_in_list_table('1: Buy wellies')
        
        # User enters duplicate item
        self.get_item_input_box().send_keys('Buy wellies\n')
        
        # Error message appears
        self.check_for_row_in_list_table('1: Buy wellies')
        error = self.get_error_element()
        self.assertEqual(error.text, "You've already got this in your list")
        
    def test_error_messages_are_cleared_on_input(self):
        # User start a new list that causes validation error
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        error = self.get_error_element()
        self.assertTrue(error.is_displayed())
        
        # User starts typing into input box to clear the error
        self.get_item_input_box().send_keys('a')
        
        # Error message disappears
        error = self.get_error_element()
        self.assertFalse(error.is_displayed())
        
    def get_error_element(self):    
        return self.browser.find_element_by_css_selector('.has-error')
