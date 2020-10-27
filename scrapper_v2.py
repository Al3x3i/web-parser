import scrapy
from scrapy.crawler import CrawlerProcess

URL = "https://www.test.com/"


class BlogSpider(scrapy.Spider):
    name = 'blogspider'

    def start_requests(self):
        urls = [URL]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.log("Parse page: %s" % response.url)
        print(response.text)


if __name__ == '__main__':
    print("Start parsing")

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    process.crawl(BlogSpider)
    process.start()  # the script will block here until the crawling is finished

    print("End parsing")
