import pymysql
import requests
from lxml import html

def save_date():

    """日期参数"""
    add_date = []
    for i in range(1, 31):
        if i < 10:
            i = '0' + str(i)
            add_date.append(i)
        else:
            add_date.append(i)

    """月份参数"""
    add_month = []
    for i in range(1, 13):
        if i < 10:
            i = '0' + str(i)
            add_month.append(i)
        else:
            add_month.append(i)


    """年份参数"""
    add_year = []
    for i in range(2013, 2018):
        add_year.append(i)

    # """法院层级"""
    # add_aoder = ['高级法院', '中级法院', '初级法院']

    """构造param"""

    params = []

    for year in add_year:
        for month in add_month:
            for date in add_date:
                if int(date) > 10:
                    param = '案件类型:行政案件,' + '裁判日期:' + str(year) + '-' + str(month) + '-' + str(date) + ' TO ' + str(
                        year) + '-' + str(month) + '-' + str(int(date) + 1)
                    params.append(param)
                else:
                    param = '案件类型:行政案件,' + '裁判日期:' + str(year) + '-' + str(month) + '-' + str(date) + ' TO ' + str(
                        year) + '-' + str(month) + '-' + '0' + str(int(date) + 1)
                    params.append(param)


    db = pymysql.connect(host='localhost', user='sph', password='123456', port=3306, db='spider')
    cursor = db.cursor()

    for param in params:
        item = {
            'state': '1',
            'date': param,
        }
        table = 'cpws_xz_2013_2017'
        keys = ', '.join(item.keys())
        values = ', '.join(['%s'] * len(item))
        sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys,
                                                                     values=values)
        try:
            if cursor.execute(sql, tuple(item.values())):
                db.commit()


        except Exception as a:
            print('插入数据失败, 原因', a)
            db.rollback()

    print("数据插入完成")



def lianxi():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    url = "http://wenshu.court.gov.cn/List/List?sorttype=1&conditions=searchWord+3+AJLX++%E6%A1%88%E4%BB%B6%E7%B1%BB%E5%9E%8B:%E8%A1%8C%E6%94%BF%E6%A1%88%E4%BB%B6"
    rep = requests.get(url, headers = headers, timeout = 15)
    if rep.status_code == 200:
        con = rep.content
        sel = html.fromstring(con)
        panduan = sel.xpath('//*[@id="Content"]/div[1]')
        print(panduan)

lianxi()