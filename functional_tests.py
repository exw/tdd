from selenium import webdriver
from selenium.webdriver.common.keys import keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.PhantomJS()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Visit webpage
        self.browser.get = ('http://localhost:8000')

        # To-Do in title
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text

        # Enter todo item
        inputbox = self.browser.find_element_by_tag_name('id_new_item').text
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )

        # Test todo item "Buy peacock feathers"
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)

        # After refresh page should update with item
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
                any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        self.fail('Finish the test')
        

if __name__ == '__main__':
    unittest.main(warnings='ignore')
