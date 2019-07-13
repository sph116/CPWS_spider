import time
import threading
from realdocid import get_Real_id
from mysql_module import mysql
from queue import Queue
from ip_pool import ip_pool
from list_page_parameters import get_cookie_and_vl5x
from list_page_parameters import take_out_item


class Spider(threading.Thread):

    def __init__(self, name, datequeue, k):

        super().__init__()
        self.name = name
        self.datequeue = datequeue
        self.k = k

    def run(self):

        print(self.name + ':启动')

        while not self.datequeue.empty():
            # date = self.datequeue.get()
            date = '案件类型:行政案件,裁判日期:2013-01-01 TO 2013-01-02'
            get_Real_id(date, self.name)



if __name__ == '__main__':



    start = time.time()
    date_list = mysql.get_date()

    datequeue = Queue()
    threadNum = 1  # 线程数量
    k = 0          # 爬取数初始量

    for i in range(0, len(date_list) - 1):
        datequeue.put(date_list[i])

    threads = []

    """为ip池构造线程"""
    t = threading.Thread(target=ip_pool, args=('Thread_IP',))
    t.setDaemon(True)
    t.start()

    """为获取vjk15构造线程"""
    s = threading.Thread(target=get_cookie_and_vl5x, args=('Thread_vjk15',))
    s.setDaemon(True)
    s.start()


    print('Thread_main:主线程开始休眠！！！！')
    while 1:
        item = take_out_item()
        if item == []:
            time.sleep(2)
            continue
        else:
            print('Thread_main:主线程休眠结束！！！！')
            break



    """构造采集线程"""
    for i in range(1, threadNum + 1):
        thread = Spider("Thread_" + str(i), datequeue, k)
        thread.start()
        threads.append(thread)

    """阻塞"""
    for thread in threads:
        thread.join()

    end = time.time()
    print("-------------------------------")
    print("下载完成. 用时{}秒".format(end - start))







