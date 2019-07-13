from list_page_parameters import take_out_item
from list_page_parameters import get_guid
from list_page_parameters import get_number_guid
from mysql_module import mysql
from Request_module import request
import re
import execjs



def get_Real_id(date, thread_name):

    """获取解密后的文书id"""


    """提取出 vjk15 和v15x值"""
    # guid = get_guid()
    item = take_out_item()
    vjk15 = item[0]
    vl5x = item[1]

    """构造请求参数"""
    headers = {
        'Cookie': '_gscu_2116842793=42679504lfhl3h15; _gscu_125736681=445830707f1j7a14; Hm_lvt_9e03c161142422698f5b0d82bf699727=1544583072; _gscbrs_2116842793=1; VCode=f2677e4e-fd9f-4789-8538-f26b78fcb04d; ASP.NET_SessionId=2cecaqh3gyp1xi0qmtr2ztfk; Hm_lvt_d2caefee2de09b8a6ea438d74fd98db2=1544585189,1544605416,1545374265,1545617242; Hm_lpvt_d2caefee2de09b8a6ea438d74fd98db2=1545699538; _gscs_2116842793=t45697584x38id111|pv:4; vjkl5=' + vjk15,
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
            }


    # number = get_number(guid)

    page_num = 20
    real_ids = []

    try:
        for page_number in range(1, page_num+1):
            number_guid = get_number_guid()
            guid = number_guid[0]
            number = number_guid[1]

            data = {
                'Param': date,
                'Index': page_number,
                'Page': 10,
                'Order': '法院层级',
                'Direction': 'asc',
                'vl5x': vl5x,
                'number': number,
                'guid': guid
                }

            # print(data, headers)
            while True:
                try:
                    url = 'http://wenshu.court.gov.cn/List/ListContent'
                    rep = request.get(url, headers, data, 15)
                    # print(rep.text)
                    raw = rep.json()

                    # print('runeval及未解密id获取成功')
                    break
                except Exception as e:
                    mysql.Modify_Table2(date)
                    # print('失败，重新获取', e)
                    continue


            pattern6 = re.compile('"Count":"(.*?)"', re.S)
            count = re.findall(pattern6, raw)
            count = count[0]

            if int(count) == 0:
                print(thread_name + ':此次查询无内容' + date)

            else:


                pattern1 = re.compile('"裁判日期":"(.*?)"', re.S)
                date = re.findall(pattern1, raw)
                date = date[0]
                # print(date)

                pattern2 = re.compile('"案号":"(.*?)"', re.S)
                num = re.findall(pattern2, raw)
                num = num[0]

                pattern3 = re.compile('"案件名称":"(.*?)"', re.S)
                title = re.findall(pattern3, raw)
                title = title[0]

                pattern4 = re.compile('"文书ID":"(.*?)"', re.S)
                Undecrypted_ids = re.findall(pattern4, raw)
                print(Undecrypted_ids)


                pattern5 = re.compile('"RunEval":"(.*?)"', re.S)
                RunEval = re.findall(pattern5, raw)
                RunEval = RunEval[0]


                with open('C:/Users/孙佩豪/Desktop/爬虫（工作）/裁判文书网/get_docid.js', 'r', encoding='UTF-8') as fp:
                    js = fp.read()
                    ctx = execjs.compile(js)

                keys = ctx.call("RunEval", RunEval)
                key = re.findall('com.str._KEY="(.*?)";', keys)[0]



                # print(data)
                for Undecrypted_id in Undecrypted_ids:

                    real_id = ctx.call('Navi', Undecrypted_id, key)

                    if real_id in real_ids:
                        print(thread_name + ':查询到重复条数，终止此次查询，开始保存文书id')
                        raise ValueError
                    elif count == '0':
                        print(thread_name + ':查询无内容，终止此次查询，开始保存文书id')
                        raise ValueError
                    else:
                        real_ids.append(real_id)
                        # print(real_ids)



    except Exception as e:
        # print(e)

        if real_ids == [''] or real_ids == []:
            print(thread_name + ':解密失败, 跳过此次检索')
            mysql.Modify_Table2(date)

        else:
            print(real_ids)
            mysql.docid_save(real_ids, thread_name)
            mysql.Modify_Table(date)












