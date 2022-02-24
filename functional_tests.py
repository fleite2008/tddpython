from selenium import webdriver
from pygeckodriver import geckodriver_path




browser = webdriver.Firefox(executable_path=geckodriver_path)
browser.get('http://localhost:8000')

assert 'Congratulations' in browser.title