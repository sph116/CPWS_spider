import execjs
import time
from Request_module import request1
from Request_module import request2

def get_guid():
    f = open("C:/Users/孙佩豪/Desktop/爬虫（工作）/裁判文书网/get_guid.js", 'r', encoding='UTF-8')
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    ctx = execjs.compile(htmlstr)
    guid = ctx.call("get_guid")
    # print('guid获取成功')
    return guid


def get_number_guid():
    guid = get_guid()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    data = {"guid": guid}
    url = 'http://wenshu.court.gov.cn/ValiCode/GetCode'
    while 1:
        try:
            rep = request2.get(url, headers, data, 15)


            number = rep.text

            # print('nummber参数获取成功')

            number_guid = []
            number_guid.append(guid)
            number_guid.append(number)

            return number_guid


        except Exception as e:
            # print('获取失败,重新请求', e)
            continue


item = []
def get_cookie_and_vl5x(thread_name):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    url = "http://wenshu.court.gov.cn/List/List?sorttype=1&conditions=searchWord+3+AJLX++%E6%A1%88%E4%BB%B6%E7%B1%BB%E5%9E%8B:%E8%A1%8C%E6%94%BF%E6%A1%88%E4%BB%B6"

    """请求失败重新获取，直到请求成功"""
    global item
    print(thread_name + ':启动')
    while 1:

        while 1:
            try:
                rep = request1.get(url, headers, 15)
                if rep.status_code == 200:
                    cookies = rep.cookies.get_dict()
                    last_vjkl5 = cookies['vjkl5']
                    f = open("C:/Users/孙佩豪/Desktop/爬虫（工作）/裁判文书网/spider/JSForVl5x.js", 'r', encoding='UTF-8')
                    line = f.readline()
                    htmlstr = ''
                    while line:
                        htmlstr = htmlstr + line
                        line = f.readline()
                    ctx = execjs.compile(htmlstr)
                    vl5x = ctx.call("getKey2", last_vjkl5)
                    item.append(last_vjkl5)
                    item.append(vl5x)
                    print(thread_name + ':cookie到期，已重新获取vjk15参数------------')
                    time.sleep(270)


            except Exception as e:
                # print('获取失败,重新请求', e)
                continue

def take_out_item():
    global item
    return item



