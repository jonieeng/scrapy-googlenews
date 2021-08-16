# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

def split_date(value):
    newdate = value.split()
    return newdate[1] + ' ' + newdate[2] + ' ' + newdate[3]

def strip_item(value):
    excerpt = value.strip(",")
    return excerpt


class GooglenewsItem(scrapy.Item):
    # define the fields for your item here like:
    query = scrapy.Field()
    region = scrapy.Field()
    title = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    date = scrapy.Field(input_processor = MapCompose(remove_tags, split_date), output_processor = TakeFirst())
    source = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    link = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    excerpt = scrapy.Field(input_processor = MapCompose(strip_item), output_processor = TakeFirst())
    
