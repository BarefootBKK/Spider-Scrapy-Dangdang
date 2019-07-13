# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookspiderItem(scrapy.Item):
    name = scrapy.Field()
    author = scrapy.Field()
    press = scrapy.Field()
    now_price = scrapy.Field()
    pre_price = scrapy.Field()
    discount = scrapy.Field()
    pub_date = scrapy.Field()
    outline = scrapy.Field()
    img_url = scrapy.Field()
    link = scrapy.Field()
    size = scrapy.Field()
    paper = scrapy.Field()
    package = scrapy.Field()
    suit = scrapy.Field()
    isbn = scrapy.Field()
    category = scrapy.Field()
    detail = scrapy.Field()
    catalogue = scrapy.Field()
    content = scrapy.Field()
    author_detail = scrapy.Field()
