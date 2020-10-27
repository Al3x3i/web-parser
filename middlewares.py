import os
import time

from scrapy.http import HtmlResponse
from selenium import webdriver


class RotateAgentMiddleware(object):

    def set_geckodriver_firefox_path(self):
        dirname = os.path.dirname(__file__)
        os.environ["PATH"] += ":" + os.path.join(dirname, "geckodriver-v0.26.0-linux64")

    def process_request(self, request, spider):
        self.set_geckodriver_firefox_path()
        # webdriver setting
        options = webdriver.FirefoxOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1200x600')

        # webdriver request
        driver = webdriver.Firefox(firefox_options=options)
        driver.get(request.url)
        time.sleep(1)

        body = driver.page_source
        current_url = driver.current_url

        driver.quit()
        return HtmlResponse(current_url, body=body, encoding='utf-8', request=request)
