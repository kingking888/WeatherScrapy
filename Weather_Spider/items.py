# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Weather_timesSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    html = scrapy.Field()


class Weather_daysSpiderItem(scrapy.Item):
    html = scrapy.Field()


class Weather_qualitySpiderItem(scrapy.Item):
    html = scrapy.Field()


class Weather_temperatureSpiderItem(scrapy.Item):
    html = scrapy.Field()
