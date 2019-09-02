from flask import Blueprint,request,jsonify,json
from flask import render_template
from flask import Blueprint,request,jsonify,json

#跨域 flask-cors

"""
blueprint
"""

currentMonitor = Blueprint("currentMonitor",__name__)

"""
Web Route
"""
from Mysql.RealtimeData import monitor_data,monitor_item
from Mysql.ipGroup import *

"""
Method: GET
所有server组的 性能状态
"""
@currentMonitor.route("/currentMonitor/server")
def server():
   ip_pool =  Group_IP()
   data_pool = {}

   ip_list = ip_pool.ip_group_list()
   for row in ip_list["server_ip_list"]:
      data_device = monitor_data(row)
      data_pool[row]=data_device.host()

   return jsonify(data_pool)


"""
Method: GET
所有network组的 性能状态
"""
@currentMonitor.route("/currentMonitor/network")
def network():
   ip_pool =  Group_IP()
   data_pool = {}

   ip_list = ip_pool.ip_group_list()
   for row in ip_list["network_ip_list"]:
      data_device = monitor_data(row)
      data_pool[row]=data_device.host()

   return jsonify(data_pool)

