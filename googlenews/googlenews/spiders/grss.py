import scrapy

class rssMode(scrapy.Spider):
    name= 'rssnews'

    def start_requests(self):
        yield scrapy.Request(f'https://news.google.com/rss/search?q={self.query}+after:{self.start}+before:{self.end}&ceid={self.region}:en&hl=en-{self.region}&gl={self.region}')
    

    def parse(self, response):
        articles = response.css('item')
        for article in articles :
            yield {
                'query': self.query,
                'region': self.region,
                'title': article.css('title::text').get(),
                'source':articles.css('source::text').get(),
                'date': articles.css('pubDate::text').get()
            }