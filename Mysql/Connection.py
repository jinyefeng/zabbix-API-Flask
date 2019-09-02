"""
笔记文件

"""
from security import db,db2


"""
简单引用
实例化 db 如果在程序入口，造成循环引用（环形引用）
实例化db 数据库
方法懒加载，需要使用才初始化
"""

# 测试
# db = pymysql.connect("10.47.0.115","python","CCsys333!","zabbix")
#
# cursor = db.cursor()
# cursor.execute("select * from hosts;")
# result = cursor.fetchall()
#
# print("_______________________________________")
# for row in result:
#     print(type(row))
# db.commit()
# cursor.close()

"""
Description :
pymysql.Connect()参数说明
host(str):      MySQL服务器地址
port(int):      MySQL服务器端口号
user(str):      用户名
passwd(str):    密码
db(str):        数据库名称
charset(str):   连接编码

connection对象支持的方法
cursor()        使用该连接创建并返回游标
commit()        提交当前事务
rollback()      回滚当前事务
close()         关闭连接

cursor对象支持的方法
execute(sql, args)     执行一个数据库的查询命令
fetchone()      取得结果集的下一行
fetchmany(size) 获取结果集的下几行
fetchall()      获取结果集中的所有行
close()         关闭游标对象

"""



"""
cursor()是 pymysql的游标，输入mysql命令
cursor = db.cursor()
cursor.execute("sql")
cursor.close()
"""


