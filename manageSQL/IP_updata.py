from security import db,db2

class IP():
    def __init__(self):
        self.cursor = db.cursor()
        self.cursor2 = db2.cursor()
        self.monitor_IP = []
        self.zabbix_IP = {}

        """
        获得monitor ip地址列表
        """

    def get_monitor_ip(self):
        sql_comment = "select ip,hostid from host;"
        self.cursor2.execute(sql_comment)
        result = self.cursor2.fetchall()

        for row in result:
            self.monitor_IP.append(row[0])

        return self.monitor_IP

        """
        获得zabbix ip地址字典{hostid:ip-address}
        """

    def get_zabbix_ip(self):
            sql_comment = "select hostid,ip from interface;"
            self.cursor.execute(sql_comment)
            result = self.cursor.fetchall()

            for row in result:
                self.zabbix_IP[row[0]]=row[1]
            return self.zabbix_IP

    def close_sql(self):
        db.commit()
        self.cursor.close()
        db2.commit()
        self.cursor2.close()

class updata_ip():
    def __init__(self):
        self.cursor2 = db2.cursor()
        current_ip =IP()
        #列表
        self.monitor_ip = current_ip.get_monitor_ip()
        #字典
        self.zabbix_ip = current_ip.get_zabbix_ip()

    def updata(self):
        for key in self.zabbix_ip:
            if self.zabbix_ip[key] in self.monitor_ip:
                pass

            else:
                print(self.zabbix_ip[key])
                sql_comment = "insert into host (ip,hostid) values ('{0}',{1});".format(self.zabbix_ip[key],key)
                self.cursor2.execute(sql_comment)
        db2.commit()
        self.cursor2.close()

