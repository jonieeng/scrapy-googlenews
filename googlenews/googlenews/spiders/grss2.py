import scrapy
from scrapy.spiders import XMLFeedSpider
from googlenews.items import GooglenewsItem
from scrapy.loader import ItemLoader


class rssMode(XMLFeedSpider):
    name= 'rssnews2'
    itertag= 'item'

    def start_requests(self):
        yield scrapy.Request(f'https://news.google.com/rss/search?q={self.query}+after:{self.start}+before:{self.end}&ceid={self.region}:en&hl=en-{self.region}&gl={self.region}')
    

    def parse_node(self, response, node):

        item = GooglenewsItem()
        item['region'] = self.region
        item['query'] = self.query
        item['link'] = node.xpath('link/text()').get()
        item['title'] = node.xpath('title/text()').get()
        item['source'] = node.xpath('source/text()').get()
        item['date'] = node.xpath('pubDate/text()').get()
        
        return item