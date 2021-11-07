import scrapy


class Movies(scrapy.Spider):
    name = 'Movies'
    allowed_domains = ['https://www.starz.com/ar/es/']
    start_urls = ['https://www.starz.com/ar/es/view-all/blocks/1402530']

    def parse(self, response):
        rows = response.xpath('//div').get()
        for row in rows:
            title = row.xpath('./h3/text()').get()

        yield {
            'titles': title
        }

