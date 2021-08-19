import scrapy
import datetime

class gSpider(scrapy.Spider):
    name= 'gnews2'

    def start_requests(self):
        yield scrapy.Request(f'https://www.google.com/search?q={self.query}&rlz=1C1ONGR_en{self.region}933SG933&tbs=cdr:1,cd_min:{self.start},cd_max:{self.end},sbd:1&tbm=nws&sxsrf=ALeKk01aflpQNP1ZZ_T4be6c1j0AaGca-g:1629088758656&source=lnt&sa=X&ved=2ahUKEwiVoJHG3LTyAhUIA3IKHUJTA3gQpwV6BAgHECw&biw=1920&bih=969&dpr=1')
    
    
    def parse(self, response):
        for articles in response.css('div.yr3B8d.KWQBje'):
            
            txt = articles.css('span.WG9SHc span::text').get()
            if 'hour' in txt or 'hours' in txt:
                D = datetime.date.today()
                yield {
                    'title': articles.css('div.JheGif.nDgy9d::text').get(),
                    'excerpt': articles.css('div.Y3v8qd::text').get(),
                    'source': articles.css('div.XTjFC.WF4CUc::text').get(),
                    'date': D.strftime('%d %b %Y'),
                    'query': self.query,
                    'start_period': self.start,
                    'end_period': self.end,
                    'region': self.region,
                }
            elif 'day' in txt or 'days' in txt:
                N = int(articles.css('span.WG9SHc span::text').get().split(" ")[0])
                D = datetime.date.today() - datetime.timedelta(days=N) 
                yield {
                    'title': articles.css('div.JheGif.nDgy9d::text').get(),
                    'excerpt': articles.css('div.Y3v8qd::text').get(),
                    'source': articles.css('div.XTjFC.WF4CUc::text').get(),
                    'date': D.strftime('%d %b %Y'),
                    'query': self.query,
                    'start_period': self.start,
                    'end_period': self.end,
                    'region': self.region,
                    
                }
            elif 'week' in txt or 'weeks' in txt:
                N = int(articles.css('span.WG9SHc span::text').get().split(" ")[0])
                D = datetime.date.today() - datetime.timedelta(days=N*7) 
                yield {
                    'title': articles.css('div.JheGif.nDgy9d::text').get(),
                    'excerpt': articles.css('div.Y3v8qd::text').get(),
                    'source': articles.css('div.XTjFC.WF4CUc::text').get(),
                    'date': D.strftime('%d %b %Y'),
                    'query': self.query,
                    'start_period': self.start,
                    'end_period': self.end,
                    'region': self.region,
                }
            elif 'month' in txt or 'months' in txt:
                N = int(articles.css('span.WG9SHc span::text').get().split(" ")[0])
                D = datetime.date.today() - datetime.timedelta(days=N*30) 
                yield {
                    'title': articles.css('div.JheGif.nDgy9d::text').get(),
                    'excerpt': articles.css('div.Y3v8qd::text').get(),
                    'source': articles.css('div.XTjFC.WF4CUc::text').get(),
                    'date': D.strftime('%d %b %Y'),
                    'query': self.query,
                    'start_period': self.start,
                    'end_period': self.end,
                    'region': self.region,
                }
            else:
                yield {
                    'title': articles.css('div.JheGif.nDgy9d::text').get(),
                    'excerpt': articles.css('div.Y3v8qd::text').get(),
                    'source': articles.css('div.XTjFC.WF4CUc::text').get(),
                    'date': articles.css('span.WG9SHc span::text').get(),
                    'query': self.query,
                    'start_period': self.start,
                    'end_period': self.end,
                    'region': self.region,
                }
        nextPage = response.css('[id="pnnext"]').attrib['href']
        nextLink = "https://google.com" + nextPage

        if nextPage is not None:
            yield response.follow(nextLink, callback=self.parse)