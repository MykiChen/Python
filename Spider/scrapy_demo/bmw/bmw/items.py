# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class BmwItem(scrapy.Item):
    category = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()