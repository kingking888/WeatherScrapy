# -*- coding: utf-8 -*-
import scrapy
from ..items import Weather_daysSpiderItem


class WeatherDaysSpider(scrapy.Spider):
    name = 'days'
    allowed_domains = ['www.scnewair.cn']
    urls = ["http://www.scnewair.cn:6112/publish/getAllCityDayAQIC"]
    head_google = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0",
        "Cookie": "JSESSIONID=561F426AF99D5755BD5F4F5853C3EB6A"
    }

    def start_requests(self):
        for i in range(len(self.urls)):
            print(self.urls[0])
            yield scrapy.Request(url=self.urls[0], callback=self.parse, headers=self.head_google, encoding='utf-8')

    def parse(self, response):
        items = Weather_daysSpiderItem()
        res = response.text
        items['html'] = res

        yield items
