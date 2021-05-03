# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ReItem(scrapy.Item):
    # define the fields for your item here like:
    crawled_url = scrapy.Field()
    content = scrapy.Field()
    images_urls = scrapy.Field()
    images = scrapy.Field()
    files_urls = scrapy.Field()
    files = scrapy.Field()
    pass
