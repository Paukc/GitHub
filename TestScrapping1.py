from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
#  from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor


class Pelicula(Item):
    titulo = Field()
    year = Field()
    sinopsis = Field()
    link = Field()


class StarzCrawler(CrawlSpider):
    name = 'Starz'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/95.0.4638.69 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 2
    }

    download_delay = 1
    allowed_domains = ['starz.com/ar/es/']
    start_urls = ['https://www.starz.com/ar/es/view-all/blocks/1402530']  # 'https://www.starz.com/ar/es/movies/']
    itertag = 'item'

    rules = (
        Rule(
            LinkExtractor(
                allow=r'/view-all/blocks/1402530/'), follow=True, callback='parse_items'
        ),
    )

    def parse_items(self, response):
        item = ItemLoader(Pelicula(), response)
        item.add_xpath('titulo', '//head//div[@class="grid-row"]//h3[@class="title text-center on-hover"/text()]',
                       MapCompose(lambda i: i.replace('\n', ' ').replace('\r', ' ').strip()))
        """item.add_xpath('year', '//li/text()', MapCompose(lambda i: i.replace('\n', ' ').replace('\r', ' ').strip()))
        item.add_xpath('sinopsis', '//div[2class="logline truncate-container"/p[@class="is-truncated"/text()]',
                                            MapCompose(lambda i: i.replace('\n', ' ').replace('\r', ' ').strip()))
        item.add_xpath('link', '//link[@rel="canonical"/herf', MapCompose(lambda i: i.replace('\n', ' ').replace('\r', 
        ' ').strip()))
"""

        yield item.load_item()
