# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import time
import pymysql
import re


class WeatherSpiderPipeline(object):
    def createTable(self, sql, db):
        cursor = db.cursor()  # 获取游标对象
        # 创建数据库，如果数据库已经存在，注意主键不要重复，否则出错

        try:
            print(sql)
            cursor.execute(sql)
        except Exception as info:
            print(info)

    def insertSQL(self, spiderName, db, datas):
        cursor = db.cursor()  # 获取游标对象
        if spiderName == "times":
            for i in range(len(datas)):
                data = datas[i]["columns"]
                # 日_小时_顺序
                id = str(time.localtime().tm_mday) + "_" + str(time.localtime().tm_hour) + "_" + str(i)
                cityname = data["CITYNAME"] + "市"
                timepoint = self.timeChange(data["TIMEPOINT"])  # 将时间戳格式化为系统格式
                AQI = data["AQI"]
                SO2 = data["SO2"]
                NO2 = data["NO2"]
                CO = data["CO"]
                O3 = data["O3"]
                PM2_5 = data["PM2_5"]
                PM10 = data["PM10"]
                # 插入数据语句
                insert = "insert into timesdata (id,cityname,timepoint, AQI,SO2 , NO2 ,CO , O3 ,PM2_5 ,PM10)" \
                         " values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s' , '%s')" % \
                         (id, cityname, timepoint, AQI, SO2, NO2, CO, O3, PM2_5, PM10)
                try:
                    cursor.execute(insert)
                    db.commit()
                    print('插入小时报数据成功')
                except:
                    db.rollback()
                    print("插入小时报数据失败")

        elif spiderName == "days":
            for i in range(len(datas)):
                data = datas[i]["columns"]
                id = str(time.localtime().tm_mday) + "_0_" + str(i)
                cityname = data["CITYNAME"] + "市"
                timepoint = self.timeChange(data["TIMEPOINT"])  # 将时间戳格式化为系统格式
                AQI = data["AQI"]
                SO2 = data["SO2"]
                NO2 = data["NO2"]
                CO = data["CO"]
                O3 = data["O3"]
                PM2_5 = data["PM2_5"]
                PM10 = data["PM10"]
                insert = "insert into daysdata (id,cityname,timepoint, AQI,SO2 , NO2 ,CO , O3 ,PM2_5 ,PM10)" \
                         " values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s' , '%s')" % \
                         (id, cityname, timepoint, AQI, SO2, NO2, CO, O3, PM2_5, PM10)
                try:
                    cursor.execute(insert)
                    db.commit()
                    print('插入日报数据成功')
                except:
                    db.rollback()
                    print("插入日报数据失败")

        elif spiderName == "quality":
            time_temp = self.timeChange(datas["timePoint"])  # 将时间戳格式化为系统格式
            timepoint = re.split(" ", time_temp)[0]
            flag = int(datas['flag'])
            datas = datas["forecast"]
            i = 0
            for k, v in datas.items():
                data = datas[k]
                id = str(time.localtime().tm_mday) + "_" + str(time.localtime().tm_hour) + "_" + str(i)
                cityname = data["CITYNAME"]
                temp_pull = data["PRIMARYPOLLUTANT"].split('|')
                temp_aqi = data["AQI"].split('|')
                temp_quality = data["QUALITY"].split('|')
                if flag == 1:
                    temp_pull.pop(0)
                    temp_aqi.pop(0)
                    temp_quality.pop(0)
                pullutant = re.sub("'|\[|]| ", "", str(temp_pull))
                aqi = re.sub("'|\[|]| ", "", str(temp_aqi))
                quality = re.sub("'|\[|]| ", "", str(temp_quality))
                # print(id, cityname, timepoint, pullutant, type(AQI))
                insert = "insert into qualitydata (id,cityname,timepoint, pullutant,aqi,quality)" \
                         "values('%s', '%s', '%s', '%s', '%s', '%s')" % \
                         (id, cityname, timepoint, pullutant, aqi, quality)
                i += 1
                try:
                    cursor.execute(insert)
                    db.commit()
                    print('插入空气质量预报数据成功')
                except:
                    db.rollback()
                    print("插入空气质量预报数据失败")
        elif spiderName == "temperature":
            cityname = datas["cityInfo"]["city"]
            forecast = datas["data"]["forecast"]
            shidu = datas["data"]["shidu"]
            temperature = datas["data"]["wendu"]
            times = datas["time"]
            for i in range(len(forecast)):
                if i > 0:
                    shidu = 0
                    temperature = 0
                    times = forecast[i]["ymd"]
                id = datas["id"] + '_' + str(i)
                week = forecast[i]["week"]
                # # 将高低温文字和温度使用“ ”分割，取出温度
                high_low = re.sub("℃", "", forecast[i]["low"].split(" ")[1]) + "/" + forecast[i]["high"].split(" ")[1]
                fx = forecast[i]["fx"]
                fl = forecast[i]["fl"]
                types = forecast[i]["type"]
                notice = forecast[i]["notice"]
                insert = "insert into temperaturedata(id,cityname,times, week,high_low , temperature ,shidu , fx ,fl ,types,notice)" \
                         " values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s' , '%s', '%s')" % \
                         (id, cityname, times, week, high_low, temperature, shidu, fx, fl, types, notice)
                try:
                    cursor.execute(insert)
                    db.commit()
                    print('插入天气预报数据成功')
                except:
                    db.rollback()
                    print("插入天气预报数据失败")

    # 将时间戳格式化为系统格式
    def timeChange(self, timeStamp):
        timeStamp = timeStamp / 1000
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)  # 将时间格式转换为字符串
        # print(otherStyleTime)
        return otherStyleTime

    def process_item(self, item, spider):
        # 转换html成dict类型并取出数据
        datas_temp = json.loads(item["html"])
        datas = datas_temp["data"]
        db = pymysql.connect(host="localhost",
                             port=3306,
                             user="root",
                             password="root",
                             db="weather_quality")

        if spider.name == "times":
            print("times")
            print("保存小时报信息至数据库...")
            # 必须加\，否则报错
            createTimes = "CREATE TABLE timesdata(" \
                          "id char(20) primary key ," \
                          "cityname char(20)," \
                          "timepoint char(20)," \
                          "AQI char(20)," \
                          "SO2 char(20)," \
                          "NO2 char(20)," \
                          "CO char(20)," \
                          "O3 char(20)," \
                          "PM2_5 char(20)," \
                          "PM10 char(20))"
            # 创建数据表timesdata
            self.createTable(createTimes, db)
            # 数据提取及插入
            self.insertSQL(spider.name, db, datas)

        elif spider.name == "days":
            print("days")
            print("保存日报信息至数据库...")
            createDays = "CREATE TABLE daysdata(" \
                         "id char(20)," \
                         "cityname char(20), " \
                         "timepoint date," \
                         "AQI char(20)," \
                         "SO2 char(20)," \
                         "NO2 char(20)," \
                         "CO char(20)," \
                         "O3 char(20)," \
                         "PM2_5 char(20)," \
                         "PM10 char(20))"
            # 创建数据表timesdata
            self.createTable(createDays, db)
            # 数据提取及插入
            self.insertSQL(spider.name, db, datas)

        elif spider.name == "quality":
            print("quality")
            print("保存预报信息至数据库...")
            createQuality = "CREATE TABLE qualitydata(" \
                            "id char(20)," \
                            "cityname char(10), " \
                            "timepoint char(15)," \
                            "pullutant char(80)," \
                            "aqi char(80)," \
                            "quality char(50))"
            # 创建数据表timesdata
            self.createTable(createQuality, db)
            # 数据提取及插入
            self.insertSQL(spider.name, db, datas)
        elif spider.name == "temperature":
            print("temperature")
            print("保存天气温度至数据库...")
            createTemperature = "CREATE TABLE temperaturedata(" \
                                "id  char(5)," \
                                "cityname char(10), " \
                                "times char(20) ," \
                                "week char(10)," \
                                "high_low char(10)," \
                                "temperature char(3)," \
                                "shidu char(5)," \
                                "fx char(10)," \
                                "fl char(10)," \
                                "types char(20)," \
                                "notice char(20))"
            # 创建数据表timesdata
            self.createTable(createTemperature, db)
            # 数据提取及插入
            self.insertSQL(spider.name, db, datas_temp)

        db.close()

        return item
