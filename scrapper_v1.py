import os

from selenium import webdriver

# Update system PATH in linux for using Selenium in Firefox
dirname = os.path.dirname(__file__)
os.environ["PATH"] += ":" + os.path.join(dirname, "geckodriver-v0.26.0-linux64")

options = webdriver.FirefoxOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600')

driver = webdriver.Firefox(firefox_options=options)
driver.get('https://www.linkedin.com')
