
import pymysql
mysql_url = "mysql+pymysql://python:CCsys333!@10.47.0.115:3306/zabbix"

db = pymysql.connect("10.47.0.115","python","CCsys333!","zabbix")
db2 = pymysql.connect("10.47.0.115","python","CCsys333!","monitor")
