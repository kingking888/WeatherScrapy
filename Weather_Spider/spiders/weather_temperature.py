# -*- coding: utf-8 -*-
import scrapy
from ..items import Weather_temperatureSpiderItem
import json, pymysql


class WeatherTemperatureSpider(scrapy.Spider):
    name = 'temperature'
    allowed_domains = ['t.weather.sojson.com/api/weather/city']
    urls = ['http://t.weather.sojson.com/api/weather/city/']
    head_google = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0",
        "Cookie": "JSESSIONID=561F426AF99D5755BD5F4F5853C3EB6A"
    }

    def start_requests(self):
        '''
            每日更新，因为json文件中字典无序,所以取出的城市代码不一定和前一次取出的相同，所以生成的id会有所不同，
            但是设置id为主键要出错，所以当每次插入数据之前先删除以前的数据
        '''
        self.deleteData()

        # 记录第几个城市天气信息，方便记录id
        self.n = 0
        with open("./city_code.json", "r", encoding='utf-8') as f:
            code = json.loads(f.read())
        for code in code.values():
            url = self.urls[0] + code
            yield scrapy.Request(url=url, callback=self.parse, headers=self.head_google, encoding='utf-8')

    def parse(self, response):

        items = Weather_temperatureSpiderItem()
        res = json.loads(response.text)
        res["id"] = str(self.n)
        items['html'] = json.dumps(res)
        self.n += 1
        yield items

    # 删除数据
    def deleteData(self, condition=""):
        db = pymysql.connect(host="localhost",
                             port=3306,
                             user="root",
                             password="root",
                             db="weather_quality")
        cursor = db.cursor()  # 获取游标对象
        if condition == "":
            delete = "DELETE FROM temperaturedata"
        else:
            delete = "DELETE * FROM temperaturedata WHERE '%s'" % (condition)
        print(delete)
        try:
            cursor.execute(delete)
            db.commit()
            # print('删除数据成功')
        except:
            db.rollback()
            print("删除数据失败")
        finally:
            db.close()
