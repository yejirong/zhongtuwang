# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhongtuwangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    names = scrapy.Field()  # '书名': names
    author = scrapy.Field()  # '作者': author
    publisher = scrapy.Field()  # '出版社': publisher
    out_data = scrapy.Field()  # '出版时间': out_data
    price = scrapy.Field()  # '定价（折后）': price
    price1 = scrapy.Field()  # '原价': price1
    beat = scrapy.Field()  # '打折数': beat
    commnet = scrapy.Field()  # '评论数': commnet
    collection = scrapy.Field()  # '读者评分': collection
    paper = scrapy.Field()  # '页数': paper
    pack = scrapy.Field()  # '包装': pack
    isbn = scrapy.Field()  # 'Isbn': isbn

