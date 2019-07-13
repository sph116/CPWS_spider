import random
import requests
import time
from ip_pool import get_ip
from lxml import html




class download():
    def __init__(self):
        self.a = 'a'
        # self.UA_list = [
        #     'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        #     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        #     'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
        #     'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
        #     'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
        #     'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
        #     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        #     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        #     'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
        #     'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
        #     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
        #     'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
        #     'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
        #     'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        #     'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
        #     'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
        #     'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
        #     'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        # ]

    def get(self, url, headers, data, timeout, proxy=None, num_retries=1, ip_times=5):


        if proxy == None:  ##当代理为空时，不使用代理获取response（别忘了response啥哦！之前说过了！！）
            try:
                rep = requests.post(url=url, headers=headers, data=data, timeout=timeout)
                # print('rep.json', rep.text)
                if rep.json == [] or rep.json == '<bound method Response.json of <Response [200]>>' or rep.text == '"remind"' \
                        or rep.status_code != 200 or '504' in rep.text or 405 in rep.text or 'Maximum number' in rep.text:
                    # print("请求失败，重试")
                    raise ValueError
                else:
                    return(rep)


            except Exception as e:              ##如过上面的代码执行报错则执行下面的代码
                # print(e)


                if num_retries > 0:  ##num_retries是我们限定的重试次数

                    # time.sleep(b)  ##延迟十秒
                    # print('获取网页出错，' + str(b) + 'S后将获取倒数第：', num_retries, u'次')
                    return self.get(url, headers, data, timeout, num_retries=num_retries-1)


                else:
                    # time.sleep(0.1)
                    """获取代理"""
                    a = get_ip()
                    ip1 = "http://" + a
                    proxy = {'http': ip1}
                    return self.get(url, headers, data, timeout, proxy)
        else:
            try:

                # print('get raw正在启用代理： ', proxy)
                rep = requests.post(url=url, headers=headers, data=data, timeout=timeout, proxies=proxy)
                # print(rep.text)
                if rep.json == [] or rep.json == '<bound method Response.json of <Response [200]>>' or rep.text == '"remind"' \
                        or rep.status_code != 200 or '504' in rep.text or '405' in rep.text or 'Maximum number' in rep.text:
                    # print("抓取失败，重试")
                    raise ValueError
                else:
                    return (rep)

            except Exception as e:
                # print(e)

                if ip_times > 0:
                    # print('代理爬取失败，重试第', ip_times, '次')

                    a = get_ip()
                    ip2 = "http://" + a
                    proxy = {'http': ip2}

                    return self.get(url, headers, data, timeout, proxy, ip_times=ip_times - 1)


                else:
                    print('代理也不好使了！取消代理:', data)
                    return requests.post(url=url, headers=headers, data=data, timeout=timeout)




class download1():
    def __init__(self):
        self.a = 'a'
        # self.UA_list = [
        #     'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        #     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        #     'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
        #     'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
        #     'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
        #     'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
        #     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        #     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        #     'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
        #     'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
        #     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
        #     'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
        #     'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
        #     'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        #     'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
        #     'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
        #     'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
        #     'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        # ]

    def get(self, url, headers, timeout, proxy=None, num_retries=2, ip_times=10):


        if proxy == None:  ##当代理为空时，不使用代理获取response（别忘了response啥哦！之前说过了！！）
            try:
                rep = requests.get(url=url, headers=headers, timeout=timeout)
                con = rep.content
                sel = html.fromstring(con)
                panduan = sel.xpath('//*[@id="Content"]/div[1]/text()')
                panduan = str(panduan).replace('[', '').replace(']', '').replace(',', '')


                if '您的访问频次' in panduan:

                    # print("请求失败，重试")
                    raise ValueError
                else:
                    return(rep)


            except Exception as e:              ##如过上面的代码执行报错则执行下面的代码
                # print(e)


                if num_retries > 0:  ##num_retries是我们限定的重试次数
                    # a = random.uniform(0.3, 0.5)
                    # b = round(a, 3)
                    # time.sleep(b)  ##延迟十秒
                    # print('获取网页出错，' + str(b) + 'S后将获取倒数第：', num_retries, u'次')
                    return self.get(url, headers, timeout, num_retries=num_retries-1)


                else:
                    # time.sleep(0.1)
                    """获取代理"""
                    a = get_ip()
                    ip1 = "http://" + a
                    proxy = {'http': ip1}
                    return self.get(url, headers, timeout, proxy)
        else:
            try:

                # print('正在启用代理： ', proxy)
                rep = requests.get(url=url, headers=headers, timeout=timeout, proxies=proxy)
                con = rep.content
                sel = html.fromstring(con)
                panduan = sel.xpath('//*[@id="Content"]/div[1]/text()')
                panduan = str(panduan).replace('[', '').replace(']', '').replace(',', '')

                if '您的访问频次' in panduan:
                    # print("抓取失败，重试")
                    raise ValueError
                else:
                    return (rep)


            except Exception as e:
                # print(e)

                if ip_times > 0:
                    # print('代理爬取失败，重试第', ip_times, '次')
                    # time.sleep(0.5)
                    a = get_ip()
                    ip2 = "http://" + a
                    proxy = {'http': ip2}

                    return self.get(url, headers, timeout, proxy, ip_times=ip_times - 1)


                else:
                    print('代理也不好使了！取消代理:', data)
                    return requests.post(url=url, headers=headers, timeout=timeout)


class download2():
    def __init__(self):
        self.a = 'a'
        # self.UA_list = [
        #     'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        #     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        #     'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
        #     'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
        #     'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
        #     'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
        #     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        #     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        #     'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
        #     'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
        #     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
        #     'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
        #     'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
        #     'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        #     'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
        #     'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
        #     'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
        #     'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        # ]

    def get(self, url, headers, data, timeout, proxy=None, num_retries=2, ip_times=10):


        if proxy == None:  ##当代理为空时，不使用代理获取response（别忘了response啥哦！之前说过了！！）
            try:
                rep = requests.post(url=url, headers=headers, data=data, timeout=timeout, proxies=proxy)
                con = rep.content
                sel = html.fromstring(con)
                panduan = sel.xpath('//head/title/text()')
                panduan2 = sel.xpath('//body/h2/text()')
                panduan = str(panduan).replace('[', '').replace(']', '').replace(',', '')
                panduan2 = str(panduan2).replace('[', '').replace(']', '').replace(',', '')
                if '502' in panduan or '504' in panduan or '404' in panduan2 or len(rep.text) > 15:
                    # print("请求失败，重试")
                    raise ValueError
                else:
                    return(rep)


            except Exception as e:              ##如过上面的代码执行报错则执行下面的代码
                # print(e)


                if num_retries > 0:  ##num_retries是我们限定的重试次数
                    # a = random.uniform(0.3, 0.5)
                    # b = round(a, 3)
                    # time.sleep(b)  ##延迟十秒
                    # print('获取网页出错，' + str(b) + 'S后将获取倒数第：', num_retries, u'次')
                    return self.get(url, headers, data, timeout, num_retries=num_retries-1)


                else:
                    # time.sleep(0.1)
                    """获取代理"""
                    a = get_ip()
                    ip1 = "http://" + a
                    proxy = {'http': ip1}
                    return self.get(url, headers, data, timeout, proxy)
        else:
            try:

                # print('getnumber正在启用代理： ', proxy)
                rep = requests.post(url=url, headers=headers, data=data, timeout=timeout, proxies=proxy)
                con = rep.content
                sel = html.fromstring(con)
                panduan = sel.xpath('//head/title/text()')
                panduan2 = sel.xpath('//body/h2/text()')
                panduan = str(panduan).replace('[', '').replace(']', '').replace(',', '')
                panduan2 = str(panduan2).replace('[', '').replace(']', '').replace(',', '')
                if '502' in panduan or '504' in panduan or '404' in panduan2 or len(rep.text) > 15:
                    # print("抓取失败，重试")
                    raise ValueError
                else:
                    return (rep)

            except:

                if ip_times > 0:
                    # print('代理爬取失败，重试第', ip_times, '次')
                    # time.sleep(0.5)
                    a = get_ip()
                    ip2 = "http://" + a
                    proxy = {'http': ip2}

                    return self.get(url, headers, data, timeout, proxy, ip_times=ip_times - 1)


                else:
                    print('取消代理:', data)
                    return requests.post(url=url, headers=headers, data=data, timeout=timeout)







request = download()
request1 = download1()
request2 = download2()





