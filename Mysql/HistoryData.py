from security import db,db2

class monitorTime():
    def __init__(self,starttime,endtime):
        # 开始时间
        self.starttime = starttime
        #结束时间
        self.endttime = endtime

    #时间转换
    def transport(self):
        pass


# 计算函数：
class sqlcli():
    def __init__(self, sql,starttime,endtime,itemid):
        # sql语句
        self.sql=sql
        # 开始时间
        self.starttime = starttime
        #结束时间
        self.endttime = endtime

        self.cursor = db.cursor()

    def data(self):
        # sql数据的条数
        self.number = self.cursor.execute(self.sql)
        # 综合结果
        self.result = self.cursor.fetchall()

    def avg(self):
        for i in (self.number-1):
            num = self.result[2]+num
        avg = num/self.number
        print(avg)

    def max(self):
        pass

    def min(self):
        pass

    def close(self):
        self.cursor.close()



