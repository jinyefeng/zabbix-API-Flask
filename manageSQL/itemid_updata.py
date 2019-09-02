from security import db,db2

class updata_itemid():
    def __init__(self):
        self.cursor = db.cursor()
        self.cursor2 = db2.cursor()
        self.hostid = []

    """
    monitor的hostid列表
    """
    def hostid_list(self):
        self.cursor2.execute("select hostid from host;")
        result = self.cursor2.fetchall()
        for row in result:
            self.hostid.append(row[0])

    # 优先调用hostid_list

    def name(self):
        for id in self.hostid:
            sqlcomm = "select name from hosts where hostid={0}".format(id)
            self.cursor.execute(sqlcomm)
            namebase = self.cursor.fetchall()
            for name in namebase:
                sqlcomm2 = "update host set name='{0}' where hostid={1}".format(name[0],id)
                print(sqlcomm2)
                self.cursor2.execute(sqlcomm2)


    def cpu(self):
        pass



    def memory(self):
        for id in self.hostid:
            sqlcomm1 = "select groupid from hosts_groups where hostid={0};".format(id)
            self.cursor1.execute(sqlcomm1)
            result = self.cursor1.fetchall()
            for row in result:
                if row[0] == 15:
                    print("这是network设备:",id)
                elif row[0] ==16:
                    sqlcomm2 = "select itemid,name from items where hostid={0}".format(id)
                    self.cursor.execute(sqlcomm2)
                    data = self.cursor.fetchall()
                    for mydata in data:
                        # sqlcomm3 = "update host set name='{0}' where hostid={1}".format(name[0],hostid)
                        itemid = mydata[0]
                        name=mydata[1]

                        if name.find("Memory utilization") >= 0:
                            if name.find("SNMPINDEX") >= 0:
                                pass
                            else:
                                sqlcomm3 = "update host set memoryitemid={0} where hostid={1}".format(itemid,id)
                                self.cursor2.execute(sqlcomm3)
                        else:
                            pass
                else:
                    pass

    def disk(self):
        for hostid in self.hostid:
            """
            每个hostid检查itemid
            """
            groupid_sql = "select groupid from hosts_groups where hostid={0};".format(hostid)
            self.cursor.execute(groupid_sql)
            group_result = self.cursor.fetchall()

            """
            检查groupid 15network  16server
            分类
            """
            if group_result[0][0] == 16:
                sql_commit2 = "select itemid,name from items where hostid={0};".format(hostid)
                self.cursor.execute(sql_commit2)
                server_item = self.cursor.fetchall()
                for server_row in server_item:
                    if server_row[1].find("Storage utilization") >= 0:
                        if server_row[1].find("C:") >= 0:
                            sql_commit_diskC = "update host set diskc='{0}' where hostid={1};".format(server_row[0],hostid)
                            # print(sql_commit_diskC)
                            self.cursor2.execute(sql_commit_diskC)
                        elif server_row[1].find("D:") >= 0:
                            sql_commit_diskD = "update host set diskd='{0}' where hostid={1};".format(server_row[0],hostid)
                            # print(sql_commit_diskD)
                            self.cursor2.execute(sql_commit_diskD)
                        elif server_row[1].find("E:") >= 0:
                            sql_commit_diskE = "update host set diske='{0}' where hostid={1};".format(server_row[0],hostid)
                            # print(sql_commit_diskE)
                            self.cursor2.execute(sql_commit_diskE)
                        elif server_row[1].find("F:") >= 0:
                            sql_commit_diskF = "update host set diskf='{0}' where hostid={1};".format(server_row[0],hostid)
                            # print(sql_commit_diskF)
                            self.cursor2.execute(sql_commit_diskF)
                        else:
                            pass
            elif group_result[0][0] == 15:
                pass
            else:
                pass

