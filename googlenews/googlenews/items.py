# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

class GooglenewsItem(scrapy.Item):
    # define the fields for your item here like:
    query = scrapy.Field()
    region = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    source = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    link = scrapy.Field()
    
