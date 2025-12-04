import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        #Explore response
        print('Response:', response)
        print('Response Status:', response.status)
        print('Response Headers:', response.headers)

        # View page content
        print('Page Content:', response.text[:500])

        #Page Title
        page_title = response.css('title::text').get()
        print('Page Title:', page_title)

        #Extract all quotes, authors, and tags
        quotes = response.css('div.quote')
        for quote in quotes:
            quote_text = quote.css('span.text::text').get()
            author = quote.css('small.author::text').get()
            tags = quote.css('div.tags a.tag::text').getall()

            yield {
                'Quote': quote_text,
                'Author': author,
                'Tags': tags
            }

            # Navigate to Next page
            next_page = response.css('li.next a::attr(href)').get()
            if next_page:
                yield response.follow(next_page, callback=self.parse)