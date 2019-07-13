
import pymysql

class Operation_MySQL():

    def __init__(self):

        self.host = 'localhost'
        self.user = 'sph'
        self.password = '123456'
        self.port = 3306
        self.db = 'spider'

    def docid_save(self, real_ids, thread_name):

        db = pymysql.connect(host=self.host, user=self.user, password=self.password, port=self.port, db=self.db)
        cur = db.cursor()


        for real_id in real_ids:
            item = {
                'state': '1',
                'docid': real_id,
            }

            table = 'cpws_xz_2013_2017_docid'
            keys = ', '.join(item.keys())
            values = ', '.join(['%s'] * len(item))
            sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys,
                                                                         values=values)
            try:
                if cur.execute(sql, tuple(item.values())):
                    db.commit()


            except Exception as a:
                print(thread_name + ':插入数据失败, 原因', a)
                db.rollback()

        db.close()
        print(thread_name + '：文书id保存成功')

    def get_date(self):

        db = pymysql.connect(host=self.host, user=self.user, password=self.password, port=self.port, db=self.db)
        cur = db.cursor()

        sql = "select * from cpws_xz_2013_2017"
        try:
            cur.execute(sql)  # 执行sql语句

            results = cur.fetchall()  # 获取查询的所有记录
            date_list = []
            # 遍历结果
            for row in results:
                all_date = list(row)
                if all_date[0] != '2':  # 状态不等于二的url 需要爬取
                    date_list.append(all_date[1])
                else:
                    pass

        except Exception as e:
            print('查询失败 原因： ', e)
            raise e
        db.close()
        print('date_list' + '查询成功')
        return date_list


    def Modify_Table(self, date):

        db = pymysql.connect(host=self.host, user=self.user, password=self.password, port=self.port, db=self.db)
        cur = db.cursor()
        cur.execute("update cpws_xz_2013_2017 set state=3 WHERE date = %s", date)
        db.commit()
        db.close()

    def Modify_Table2(self, date):

        db = pymysql.connect(host=self.host, user=self.user, password=self.password, port=self.port, db=self.db)
        cur = db.cursor()
        cur.execute("update cpws_xz_2013_2017 set state=2 WHERE date = %s", date)
        db.commit()
        db.close()









mysql = Operation_MySQL()