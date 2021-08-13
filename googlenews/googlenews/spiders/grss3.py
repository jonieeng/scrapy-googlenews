import scrapy
from scrapy.spiders import XMLFeedSpider
from googlenews.items import GooglenewsItem
from scrapy.loader import ItemLoader

class rssMode(scrapy.Spider):
    name= 'rssnews3'
    allowed_domains = ['https://news.google.com/rss']

    def start_requests(self):
        yield scrapy.Request(f'https://news.google.com/rss/search?q={self.query}+after:{self.start}+before:{self.end}&ceid={self.region}:en&hl=en-{self.region}&gl={self.region}')
    

    def parse(self, response):

        for article in response.xpath('//channel/item'):
            l = ItemLoader(item = GooglenewsItem(), selector=article)
            l.add_xpath('link','link')
            l.add_xpath('date','pubDate')
            l.add_value('region', self.region)
            l.add_value('query', self.query)
            l.add_xpath('title','title')
            l.add_xpath('source', 'source')

            yield l.load_item()
            