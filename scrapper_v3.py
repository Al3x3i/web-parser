import scrapy
from scrapy.crawler import CrawlerProcess

URL = "https://rozetka.com.ua/elektrotransport/c4625901/"


class BlogSpider(scrapy.Spider):
    name = 'blogspider'

    def start_requests(self):
        urls = [URL]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.log("Parse page: %s" % response.url)
        links = []
        for item in response.css('.catalog-grid__cell.catalog-grid__cell_type_slim'):
            link = item.css('.goods-tile__picture').attrib['href']
            # print("%s" % link)

            links.append(link)

        self.save_to_file(links)

        # Recursive parsing
        # for next_page in response.css('a.next-posts-link'):
        #     yield response.follow(next_page, self.parse)

    def save_to_file(self, data):

        with open("Result.txt", 'w') as filehandle:
            for listitem in data:
                filehandle.write('%s\n' % listitem)


if __name__ == '__main__':
    print("Start parsing")

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        # 'SPIDER_MIDDLEWARES': {
        #     'middlewares.UsSpiderMiddleware': 543,
        'DOWNLOADER_MIDDLEWARES': {
            'middlewares.RotateAgentMiddleware': 543,
        }
    })
    process.crawl(BlogSpider)
    process.start()  # the script will block here until the crawling is finished

    print("End parsing")


# Keep in mind you can structure response data
# https://medium.com/swlh/how-to-use-scrapy-items-05-python-scrapy-tutorial-for-beginners-f25ff2dceaa9
class BooksItem(scrapy.Item):
    title = scrapy.Field()
    final_image = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    stars = scrapy.Field()
    description = scrapy.Field()
    upc = scrapy.Field()
    price_excl_tax = scrapy.Field()
    price_inc_tax = scrapy.Field()
    tax = scrapy.Field()
