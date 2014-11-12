from .base import FunctionalTest
from unittest import skip

class ItemValidationTest(FunctionalTest):
        
    def test_cannot_add_empty_list_items(self):
        # User opens home page and accidentally submits empty item
        
        # Error message appears, item cannot be blank
        
        # User enters correct item
        
        # User submits second blank item
        
        # Similar warning appears
        
        # User fills some text in
        self.fail('write me!')

