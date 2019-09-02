
from security import db,db2

"""
获得所有的IP列表
"""

class all_ip():
    def __init__(self):
        #获得 主机信息
        self.cursor2=db2.cursor()

    def ip_list(self):
        ip_list = []
        self.cursor2.execute("select ip from host;")
        result = self.cursor2.fetchall()
        for row in result:
            ip_list.append(row[0])
        self.cursor2.close()
        return ip_list


"""
输出 server的IP列表和network的IP列表
"""

class Group_IP():
    def __init__(self):
        #获得 主机信息
        self.cursor = db.cursor()
        self.cursor2=db2.cursor()


    def ip_group_list(self):

        server_ip_list = []
        network_ip_list = []

        #获得所有数据库的IP
        self.cursor2.execute("select ip from host;")
        result = self.cursor2.fetchall()

        for row in result:

            #检查hostid  通过IP查询  row[0] IP地址
            ip_address = row[0]

            hostid_sql = "select hostid from host where ip='{0}';".format(ip_address)
            self.cursor2.execute(hostid_sql)
            hostid  = self.cursor2.fetchall()


            #检查是否是server还是Network
            #groupid 15network  16server
            groupid_sql = "select groupid from hosts_groups where hostid={0};".format(hostid[0][0])
            self.cursor.execute(groupid_sql)
            groupid  = self.cursor.fetchall()
            for raw in groupid:
                o = raw[0]
                if raw[0] == 15:
                    network_ip_list.append(ip_address)
                elif raw[0] == 16:
                    server_ip_list.append(ip_address)
                else:
                    pass
        return {"server_ip_list":server_ip_list,"network_ip_list":network_ip_list}
