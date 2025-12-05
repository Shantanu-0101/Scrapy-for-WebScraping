import scrapy


class QuotesScraperSpider(scrapy.Spider):
    name = "quotes_scraper"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        yield {'response': response}
 