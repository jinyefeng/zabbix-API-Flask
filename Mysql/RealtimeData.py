"""
实时数据 history表
items:监控项目
代码模块：CPU,Memory,Disk
"""
from security import db,db2

"""
得到IP 输入服务器的性能
"""
class monitor_item():
    def __init__(self,result):
        self.result = result

    def hostname(self):
        return {"hostname":self.result[0][2]}


    def itemid(self):
        for row in self.result:
            host_name = row[2]
            cpu_itemid = row[3]
            memory_itemid=row[4]
            diskC_itemid=row[5]
            diskD_itemid=row[6]
            diskE_itemid=row[7]
            diskF_itemid=row[8]
            return {"cpu":cpu_itemid,"memory":memory_itemid,"diskc":diskC_itemid,"diskd":diskD_itemid,"diske":diskE_itemid,"diskf":diskF_itemid}

"""
输入sql语句 
得到设备的性能数据（非CPU）
"""
def getdata(data):
    cursor = db.cursor()
    sql_comm = " select value from history where itemid={0} ORDER BY clock DESC LIMIT 1;".format(data)
    cursor.execute(sql_comm)
    result = cursor.fetchall()
    for row in result:
        return row[0]

    db.commit()
    cursor.close()


"""
输入sql语句 
得到需要的数据
得到设备的CPU性能数据
"""
def getcpudata(data):
    cursor = db.cursor()
    number = len(data)
    sum = 0

    for row in data:
        # row string类型
        sql_comm = " select value from history where itemid='{0}' ORDER BY clock DESC LIMIT 1;".format(row)
        cursor.execute(sql_comm)
        result = cursor.fetchall()
        for row in result:
            sum = sum + row[0]
    cpu_result =sum/number
    # print("该CPU的总量",sum)
    # print("该CPU的个数",number)
    return cpu_result

"""
输入IP地址
输出设备性能数据
"""
class monitor_data():
    def __init__(self,ip):
        #获得监控项数据
        self.cursor=db.cursor()
        #获得 主机信息
        self.cursor2=db2.cursor()

        self.ip = ip
        self.cpu_result = 0
        self.memory_result = 0
        self.disk_c = 0
        self.disk_d = 0
        self.disk_e = 0
        self.disk_f = 0

    def host(self):
        sql_cli = "select * from host where ip='{0}';".format(self.ip)
        self.cursor2.execute(sql_cli)
        item_list = self.cursor2.fetchall()
        item = monitor_item(item_list)
        item.itemid()
        # 获得
        for key in item.itemid():
            itemid = item.itemid()[key]

            if key == "cpu":
                # cpu tiemid 列表

                itemid2 = itemid.split(" ")
                cpu_result = getcpudata(itemid2)
                self.cpu_result = cpu_result

            elif key == "cpuitemid" or key =="memory" or key =="diskc" or key =="diskd" or key =="diske" or key =="diskf":
                if item.itemid()[key] == None:
                    pass
                else:
                    non_cpu_result = getdata(item.itemid()[key])
                    if key == "memory":
                        self.memory_result =non_cpu_result
                        # print("内存",non_cpu_result)
                    elif key == "diskc":
                        self.disk_c = non_cpu_result
                        # print("C",non_cpu_result)
                    elif key == "diskd":
                        self.disk_d = non_cpu_result
                        # print("D",non_cpu_result)
                    elif key == "diske":
                        self.disk_e = non_cpu_result
                        # print("E",non_cpu_result)
                    elif key == "diskf":
                        self.disk_f = non_cpu_result
                        # print("F",non_cpu_result)
                    else:
                        pass

            else:
                pass
        db.commit()
        db2.commit()
        self.cursor.close()
        self.cursor2.close()
        return {"cpu":self.cpu_result,"memory":self.memory_result,"C":self.disk_c,"D":self.disk_d,"E":self.disk_e,"F":self.disk_f}






