from .base import FunctionalTest
from unittest import skip

class ItemValidationTest(FunctionalTest):
        
    def test_cannot_add_empty_list_items(self):
        # User opens home page and accidentally submits empty item
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_new_item').send_keys('\n')
        
        # Error message appears, item cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")
        
        # User enters correct item
        self.brower.find_element_by_id('id_new_item').send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')
        
        # User submits second blank item
        self.browser.find_element_by_id('id_new_item').send_keys('\n')
        
        # Similar warning appears
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")
        
        # User fills some text in
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')
