import pymysql


class CxtMysql:
    def __init__(self):
        self.connection = pymysql.connect(
            host='192.168.1.242',
            port=3306,
            user='cxt',
            password='j5jELwkcJnePxS6o03N7XoTvkda4Qmq3JkZZQHAd',
            database='chanxintong_prod',
            charset='utf8mb4'
        )
        self.cursor = self.connection.cursor()

    def delete_data(self, uuid_list):
        try:
            sql = 'delete from t_article_detail where uuid in {}'.format(uuid_list)
            print(sql)
            self.cursor.execute(sql)
            self.connection.commit()
            self.cursor.close()
        except Exception as e:
            pass
