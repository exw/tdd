from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

import django.http

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.PhantomJS()
        # self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Visit webpage
        self.browser.get('http://localhost:8000')

        # To-Do in title
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text

        # Enter todo item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )

        # Test todo item "Buy peacock feathers"
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)

        # After refresh page should update with item
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # Test todo list can retain multiple items
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers')
        inputbox.send_keys(Keys.ENTER)

        # After refresh page should update with multiple items
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers')

        self.fail('Finish the test')
        

if __name__ == '__main__':
    unittest.main(warnings='ignore')
