import scrapy

class gSpider(scrapy.Spider):
    name= 'gnews'
    start_urls = ['https://www.google.com/search?q=semiconductor+trends&sxsrf=ALeKk03-JfkEO9ENt0lstr0YA3CP8OADmQ%3A1628840838478&source=hp&ei=hiMWYejUGtXJ-gTGgLXgAg&iflsig=AINFCbYAAAAAYRYxljLcJ-u4xVutRWo7lWaNAA_vj-zI&oq=semiconductor+trends&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCABDIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToOCC4QsQMQgwEQxwEQowI6CAgAEIAEELEDOggILhCxAxCDAToLCC4QgAQQsQMQgwE6DgguEIAEELEDEMcBEKMCOhEILhCABBCxAxCDARDHARCvAToOCC4QgAQQsQMQxwEQ0QM6CwguEIAEEMcBEK8BOg4ILhCABBCxAxDHARCvAToRCC4QgAQQsQMQgwEQxwEQ0QM6CAguEIAEELEDOggIABCABBDJAzoFCAAQkgM6DgguEIAEEMcBEK8BEJMCOgsILhCABBDHARDRAzoFCC4QgARQvAdYyihgsiloAHAAeACAAUyIAeQIkgECMjCYAQCgAQE&sclient=gws-wiz&ved=0ahUKEwjor8j8wK3yAhXVpJ4KHUZADSwQ4dUDCAc&uact=5']
    def parse(self, response):
        for articles in response.css('div.tF2Cxc'):
            yield {
                'title': articles.css('h3.LC20lb.DKV0Md::text').get(),

            }

        nextPage = response.css('[id="pnnext"]').attrib['href']
        nextLink = "https://google.com" + nextPage
        if nextPage is not None:
            yield response.follow(nextLink, callback=self.parse)