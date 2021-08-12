import scrapy

class gSpider(scrapy.Spider):
    name= 'hello'
    start_urls = ['https://www.google.com/search?q=semiconductor&rlz=1C1ONGR_enSG933SG933&biw=1920&bih=969&tbm=nws&sxsrf=ALeKk03i0RNUCTt_bpisLK7yZ7HkhGHYDQ%3A1628702919250&ei=xwgUYf_TDpPgrQH_1qqoBg&oq=semiconductor&gs_l=psy-ab.3..0i433i131i67k1l2j0i67k1j0i433i131i67k1j0i512i433k1j0i512k1l5.3096.4756.0.4943.13.6.0.7.7.0.101.426.5j1.6.0....0...1c.1.64.psy-ab..0.13.446...0i433i131k1j0i512i433i131k1j0i433k1j0i433i67k1.0.gz4CnzvXmPU']

    def parse(self, response):
        for articles in response.css('div.yr3B8d.KWQBje'):
            yield {
                'title': articles.css('div.JheGif.nDgy9d::text').get(),
                'excerpt':articles.css('div.Y3v8qd::text').get(),
                'source':articles.css('div.XTjFC.WF4CUc::text').get(),
                'date': articles.css('span.WG9SHc span::text').get()
            }

        nextPage = response.css('[id="pnnext"]').attrib['href']
        nextLink = "https://google.com" + nextPage
        if nextPage is not None:
            yield response.follow(nextLink, callback=self.parse)