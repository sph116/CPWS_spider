
import requests
import time


using_ips = []

def ip_pool(thread_name):

    global using_ips


    print(thread_name + ':启动')

    time_ips_group = {}
    while 1:
        if len(using_ips) < 20:
            try:
                url = 'http://www.xiongmaodaili.com/xiongmao-web/api/gbip?secret=0d7ef4694748d22adfb7ce398957b846&orderNo=GB20181017090741MlZEkUb2&count=5&isTxt=1'
                html = requests.get(url)
                ips = html.text.strip().split('。')
                # print(ips)

                now = int(time.time())
                now_ips = {now: ips}
                time_ips_group.update(now_ips)
                for ip in ips:
                    using_ips.insert(0, ip)
                print(thread_name + ':当前ip池的ip数量为：' + str(len(using_ips)))
                # print(using_ips)
                # print(time_ips_group)
            except Exception as e:
                print(e)
                continue
            time.sleep(8)
        else:
            now = int(time.time())
            del_list = []
            for key in time_ips_group.keys():
                if now - key > 300:
                    for ip in time_ips_group.get(key):
                        try:
                            using_ips.remove(ip)
                        except:
                            pass
                    del_list.append(key)
            if del_list != []:
                for key in del_list:
                    del time_ips_group[key]
                print(thread_name + ":清除过期IP")



def get_ip():
    global using_ips
    while len(using_ips) == 0:
        pass
    a = using_ips.pop(0)
    return a

