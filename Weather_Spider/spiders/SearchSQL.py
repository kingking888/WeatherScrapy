'''
    -*- coding: utf-8 -*- 
    @Time : 2020/2/2 16:05 
    @Author : Bulin Liang 
    @File : SearchSQL.py 
    @Software: PyCharm
'''

'''
该文件完成功能：
    查询城市空气质量，提供给ui界面生成信息使用
    1、小时报
    2、日报
    3、预报
'''
import pymysql, datetime, re
from xpinyin import Pinyin


class SearchSQL(object):
    db = pymysql.connect(host="localhost",
                         port=3306,
                         user="root",
                         password="root",
                         db="weather_quality")

    def __init__(self):
        cursor = self.db.cursor()  # 获取游标对象
        # 查询语句，使用模糊查找
        select = "SELECT cityname FROM timesdata GROUP BY cityname"
        pinyin = Pinyin()
        try:
            cursor.execute(select)  # 执行语句
            self.db.commit()
            result = cursor.fetchall()  # 输出字段
            global city_name, city_num
            # city_name[0]存放城市名，city_name[1]存放城市名拼音
            self.city_name = [[], []]
            for name in result:
                self.city_name[0].append(name[0])
                name_temp = pinyin.get_pinyin(f"{name[0]}")
                self.city_name[1].append(re.sub('-', '', name_temp))
        except:
            self.db.rollback()  # 发生错误时回滚

    def prediction(self, city_name):
        cursor = self.db.cursor()  # 获取游标对象
        # 查询语句，使用模糊查找
        select = "SELECT * FROM qualitydata WHERE cityname = '%s'" % (city_name)
        try:
            cursor.execute(select)  # 执行语句
            self.db.commit()
            result = cursor.fetchall()  # 输出字段
            return result[0]
        except:
            self.db.rollback()  # 发生错误时回滚

    def temperature(self, city_name):
        cursor = self.db.cursor()  # 获取游标对象
        # 查询语句，使用模糊查找
        select = "SELECT * FROM temperaturedata WHERE cityname = '%s'ORDER BY shidu desc,times" % (city_name)
        try:
            cursor.execute(select)  # 执行语句
            self.db.commit()
            result = cursor.fetchall()  # 输出字段
            return result[0]
        except:
            self.db.rollback()  # 发生错误时回滚

    def airDatas(self, column, table, cityname):
        cursor = self.db.cursor()  # 获取游标对象
        table = table + "data"
        select = "SELECT %s,timepoint FROM %s WHERE cityname = '%s'" % (column, table, cityname)
        try:
            cursor.execute(select)  # 执行语句
            self.db.commit()
            result = cursor.fetchall()  # 输出字段
            return result
        except:
            self.db.rollback()  # 发生错误时回滚


    # 将时间戳格式化为系统格式
    def timeChange(self):
        month = datetime.datetime.now().month
        hour = datetime.datetime.now().hour
        timeStamp = str(month) + '_' + str(hour)
        return timeStamp


if __name__ == '__main__':
    select = SearchSQL()
    select.db.close()