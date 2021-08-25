import scrapy
from googlenews.items import GooglenewsItem
from scrapy.loader import ItemLoader

class gSpider(scrapy.Spider):
    name= 'gnews6a'
    # start_urls = ['https://www.google.com/search?q=semiconductor&biw=1920&bih=969&tbm=nws&ei=yJUaYbiTEdLarQHR6p-ADw&oq=semiconductor&gs_l=psy-ab.3..0i67k1l2j0i433i131i67k1j0i512i433i395k1j0i433i67i395k1j0i67i395k1l5.4614.5162.0.6646.2.2.0.0.0.0.174.315.0j2.2.0..3..0...1.1.64.psy-ab..0.2.315...0i512i395k1.0.Z2oLMrWsiR0']
    def start_requests(self):
        yield scrapy.Request(f'https://www.google.com/search?q={self.region}+{self.query}&rlz=1C1ONGR_enSG933SG933&tbs=cdr:1,cd_min:{self.start},cd_max:{self.end},sbd:1&tbm=nws&sxsrf=ALeKk01aflpQNP1ZZ_T4be6c1j0AaGca-g:1629088758656&source=lnt&sa=X&ved=2ahUKEwiVoJHG3LTyAhUIA3IKHUJTA3gQpwV6BAgHECw&biw=1920&bih=969&dpr=1')
    
    
    def parse(self, response):
        for articles in response.css('div.dbsr'):
            l = ItemLoader(item = GooglenewsItem(), selector=articles)

            l.add_css('title', 'div.JheGif.nDgy9d')
            # l.add_css('excerpt', 'div.Y3v8qd')
            l.add_css('source','div.XTjFC.WF4CUc')
            l.add_css('date', 'span.WG9SHc span')
            l.add_value('query', self.query)
            # l.add_value('start', self.start)
            # l.add_value('end',self.end)
            l.add_value('region', self.region)
            l.add_css('link','a::attr(href)')

            # yield l.load_item()

            excerpt_page = (articles.css('a::attr(href)').get()).strip(">")
            request = response.follow(
                excerpt_page,
                callback= self.parse_excerpt_page,
                meta={'item': l.load_item()}
            )
            yield request


        # nextPage = response.css('[id="pnnext"]').attrib['href']
        # nextLink = "https://google.com" + nextPage

        # if nextPage is not None:
        #     yield response.follow(nextLink, callback=self.parse)

    def parse_excerpt_page(self, response):
        lnext = ItemLoader(item=response.meta['item'], response=response)
        # lnext.add_xpath('excerpt','.//p/text()')
        lnext.add_xpath('excerpt','.//p[contains(.,"semiconductor")]')
        # lnext.add_xpath('excerpt','.//p[contains(text(),"semiconductor")]')
        return lnext.load_item()