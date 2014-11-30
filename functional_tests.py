from selenium import webdriver

browser = webdriver.PhantomJS()
<<<<<<< HEAD
browser.get = ('http://localhost:8000')
=======
browser.get('http://localhost:8000')
>>>>>>> 1a72bafcf4768af1487c8efd7b56d16ccf86610b

assert 'Django' in browser.title
