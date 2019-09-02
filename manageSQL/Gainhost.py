#
# from security import db,db2
# # cursor = db.cursor()
# # cursor.execute("select * from hosts;")
# # result = cursor.fetchall()
# # for row in result:
# #     print(type(row))
# # db.commit()
# # cursor.close()
#
# """
# 获得zabbix的ip地址和hostid
# select hostid,ip from interface
# 匹配2个数据库
# """
# # def test():
# #     cursor = db.cursor()
# #     cursor.execute("select hostid,ip from interface;")
# #     result = cursor.fetchall()
# #     for row in result:
# #         hostid=row[0]
# #         ip=row[1]
# #         sqlcomm = "insert into host (ip,hostid) values ('{0}',{1});".format(str(ip),hostid)
# #         print(sqlcomm)
# #         cursor2 = db2.cursor()
# #         cursor2.execute(sqlcomm)
# #         db2.commit()
# #         cursor2.close()
# #     db.commit()
# #     cursor.close()
# # newtest = test()
#
# # class item():
# #     def __init__(self):
# #         cursor = db.cursor()
# #         data=cursor.execute("select hostid,ip from hosts;")
# #         result = cursor.fetchall()
# #         for row in result:
# #             print(type(data))
# #         db.commit()
# #         cursor.close()
#
#
# """
# 通过hostid 或者zabbix的服务器name
# select name from hosts where hostid=
# """
# # def test():
# #     cursor2 = db2.cursor()
# #     cursor2.execute("select hostid from host;")
# #     result = cursor2.fetchall()
# #     for row in result:
# #         hostid=row[0]
# #         cursor = db.cursor()
# #         sqlcomm2 = "select name from hosts where hostid={0}".format(hostid)
# #         cursor.execute(sqlcomm2)
# #         namebase = cursor.fetchall()
# #         for name in namebase:
# #             sqlcomm3 = "update host set name='{0}' where hostid={1}".format(name[0],hostid)
# #             print(sqlcomm3)
# #             cursor2.execute(sqlcomm3)
# #     db2.commit()
# #     cursor2.close()
# #
# # newtest=test()
#
#
# """
# 通过hostid 或者zabbix的服务器itemid, 从name获得项目分配
# select itemid,name, from items where hostid=
# """
# """
# 匹配问题
# index指str2在str1中的开始下标，为-1则证明str1中不包含str2
# def stringCompare2(str1, str2):
#     if str1.index(str2) > -1:
#         print("yes2")
#
# """
#
# """
# 服务器内存
# """
#
# # def test():
# #     cursor2 = db2.cursor()
# #     cursor2.execute("select hostid from host;")
# #     result = cursor2.fetchall()
# #     for row in result:
# #         hostid=row[0]
# #         # print(hostid)
# #         cursor1 = db.cursor()
# #         sqlcomm1 = "select groupid from hosts_groups where hostid={0};".format(hostid)
# #         cursor1.execute(sqlcomm1)
# #         result2 = cursor1.fetchall()
# #         for row1 in result2:
# #
# #             if row1[0] == 15:
# #                 print("这是network设备:",hostid)
# #             elif row1[0] ==16:
# #                 """
# #                 服务器的内存
# #                 """
# #                 cursor = db.cursor()
# #                 sqlcomm2 = "select itemid,name from items where hostid={0}".format(hostid)
# #                 cursor.execute(sqlcomm2)
# #                 data = cursor.fetchall()
# #                 for mydata in data:
# #                     # sqlcomm3 = "update host set name='{0}' where hostid={1}".format(name[0],hostid)
# #                     itemid = mydata[0]
# #                     name=mydata[1]
# #
# #                     if name.find("Memory utilization") >= 0:
# #                         if name.find("SNMPINDEX") >= 0:
# #                             pass
# #                         else:
# #                             sqlcomm3 = "update host set memoryitemid={0} where hostid={1}".format(itemid,hostid)
# #                             cursor2.execute(sqlcomm3)
# #                     else:
# #                         pass
# #
# #                     # print(itemid,name)
# #                     # cursor2.execute(sqlcomm3)
# #             else:
# #                 pass
# #     db2.commit()
# #     cursor2.close()
# #
# # newtest=test()
#
#
#
#
#
#
#
# """
# 得到 自己数据库的hostid
# """
#
# def myhost():
#     hostid = []
#     myhost_cursor = db2.cursor()
#     myhost_cursor.execute("select hostid from host;")
#     result = myhost_cursor.fetchall()
#     for row in result:
#         hostid.append(row[0])
#     db2.commit()
#     myhost_cursor.close()
#     return hostid
#
#
#
#
# """
# 输入hostid 得到 groupid
# """
# class zabbix_info():
#     def __init__(self,hostid):
#         self.hostid = hostid
#         self.cursor = db.cursor()
#         # cursor.execute("select * from hosts;")
#         # result = cursor.fetchall()
#         # for row in result:
#         #     print(type(row))
#         # db.commit()
#         # cursor.close()
#
#     def groupid(self):
#         groupid_sql = "select groupid from hosts_groups where hostid={0};".format(self.hostid)
#         self.cursor.execute(groupid_sql)
#         result = self.cursor.fetchall()
#         self.cursor.close()
#         # print(result[0][0])
#         db.commit()
#         self.cursor.close()
#         return result[0][0]
#
# """
# 得到服务器cpu itemid
# """
# class cpuitemid():
#     def __init__(self):
#         self.cursor = db.cursor()
#         self.cursor2 = db2.cursor()
#         self.hostid_list = myhost()
#
#     def items(self):
#         for hostid in self.hostid_list:
#             groupid_sql = "select groupid from hosts_groups where hostid={0};".format(hostid)
#             self.cursor.execute(groupid_sql)
#             group_result = self.cursor.fetchall()
#
#             if group_result[0][0] == 15:
#                 # network
#                 cpu_list2 = []
#                 sql_commit2 = "select itemid,name from items where hostid={0}".format(hostid)
#                 self.cursor.execute(sql_commit2)
#                 result2 = self.cursor.fetchall()
#                 for row in result2:
#                     cpu_itemid = row[0]
#                     cpu_name=row[1]
#                     if cpu_name.find("CPU utilization") >=0:
#                         if cpu_name.find("#SNMPINDEX}")>=0:
#                             pass
#                         else:
#                             cpu_list2.append(str(cpu_itemid))
#                 cpu_list4 = " ".join(cpu_list2)
#                 sql_commit3 = "update host set cpuitemid='{0}' where hostid={1};".format(cpu_list4, hostid)
#                 self.cursor2.execute(sql_commit3)
#                 db2.commit()
#
#
#             elif group_result[0][0] == 16:
#                 # server
#                 cpu_list1 = []
#                 sql_commit1 = "select itemid,name from items where hostid={0}".format(hostid)
#                 self.cursor.execute(sql_commit1)
#                 result1 = self.cursor.fetchall()
#                 for row in result1:
#                     cpu_itemid = row[0]
#                     cpu_name=row[1]
#                     if cpu_name.find("CPU utilization") >=0:
#                         if cpu_name.find("#SNMPINDEX}")>=0:
#                             pass
#                         else:
#                             cpu_list1.append(str(cpu_itemid))
#                 cpu_list3 = " ".join(cpu_list1)
#                 sql_commit2 = "update host set cpuitemid='{0}' where hostid={1};".format(cpu_list3,hostid)
#                 self.cursor2.execute(sql_commit2)
#                 db2.commit()
#
#             else:
#                 pass
#
#         db.commit()
#         self.cursor.close()
#
# """
# 获取硬盘
#
# C:\\ Label:  Serial Number 8a4381c: Storage utilization
#
#
# """
# class diskitemid():
#     def __init__(self):
#         self.cursor = db.cursor()
#         self.cursor2 = db2.cursor()
#         self.hostid_list = myhost()
#
#     def serverdisk(self):
#         """
#         服务器硬盘空间
#
#         """
#         for hostid in self.hostid_list:
#             """
#             每个hostid检查itemid
#             """
#             groupid_sql = "select groupid from hosts_groups where hostid={0};".format(hostid)
#             self.cursor.execute(groupid_sql)
#             group_result = self.cursor.fetchall()
#
#             """
#             检查groupid 15network  16server
#             分类
#             """
#             if group_result[0][0] == 16:
#                 sql_commit2 = "select itemid,name from items where hostid={0};".format(hostid)
#                 self.cursor.execute(sql_commit2)
#                 server_item = self.cursor.fetchall()
#                 for server_row in server_item:
#                     if server_row[1].find("Storage utilization") >= 0:
#                         if server_row[1].find("C:") >= 0:
#                             sql_commit_diskC = "update host set diskc='{0}' where hostid={1};".format(server_row[0],hostid)
#                             # print(sql_commit_diskC)
#                             self.cursor2.execute(sql_commit_diskC)
#                         elif server_row[1].find("D:") >= 0:
#                             sql_commit_diskD = "update host set diskd='{0}' where hostid={1};".format(server_row[0],hostid)
#                             # print(sql_commit_diskD)
#                             self.cursor2.execute(sql_commit_diskD)
#                         elif server_row[1].find("E:") >= 0:
#                             sql_commit_diskE = "update host set diske='{0}' where hostid={1};".format(server_row[0],hostid)
#                             # print(sql_commit_diskE)
#                             self.cursor2.execute(sql_commit_diskE)
#                         elif server_row[1].find("F:") >= 0:
#                             sql_commit_diskF = "update host set diskf='{0}' where hostid={1};".format(server_row[0],hostid)
#                             # print(sql_commit_diskF)
#                             self.cursor2.execute(sql_commit_diskF)
#                         else:
#                             pass
#
#                 db2.commit()
#
#             elif group_result[0][0] == 15:
#                 pass
#             else:
#                 pass
#         db.commit()
#
#
#
#
#
#
#
#
