from .base import FunctionalTest
import time
from selenium.webdriver.support.ui import WebDriverWait

TEST_EMAIL = 'edith@mockmyid.com'

class LoginTest(FunctionalTest):

    def test_login_with_persona(self):
        # User tries to sign in
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_login').click()
        
        # Login box appears
        self.switch_to_new_window('Mozilla Persona')
        
        # User logs in
        self.browser.find_element_by_id(
            'authentication_email'
        ).send_keys(TEST_EMAIL)
        self.browser.find_element_by_tag_name('button').click()
        
        self.switch_to_new_window('To-Do')
        
        # User is logged in
        self.wait_to_be_logged_in(email=TEST_EMAIL)
        
        # Refresh the page
        self.browser.refresh()
        self.wait_to_be_logged_in(email=TEST_EMAIL)
        
        # User clicks logout
        self.browser.find_element_by_id('id_logout').click()
        self.wait_to_be_logged_out(email=TEST_EMAIL)
        
        # Refresh
        self.browser.refresh()
        self.wait_to_be_logged_out(email=TEST_EMAIL)
        
    def switch_to_new_window(self, text_in_title):
        retries = 60
        while retries > 0:
            for handle in self.browser.window_handles:
                self.browser.switch_to_window(handle)
                if text_in_title in self.browser.title:
                    return
            retries -= 1
            time.sleep(0.5)
        self.fail('could not find window')
