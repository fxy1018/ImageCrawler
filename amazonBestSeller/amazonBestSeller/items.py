# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonbestsellerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    rank = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field() 
    score = scrapy.Field()
    reviews = scrapy.Field()
    editiontype = scrapy.Field()
    price = scrapy.Field()
