from flask import Flask
from flask import render_template,request,redirect,session,flash,url_for
from flask import Blueprint,request,jsonify,json
import json
from flask_cors import *

app = Flask(__name__)

"""
默认的主页
"""
@app.route("/")
def index():
    return ("Monitor API")

from Mysql.RealtimeData import monitor_data,monitor_item
from Mysql.ipGroup import all_ip
@app.route("/one", methods=["GTE","POST"])
def one():
    if request.method == "POST":
        data = request.get_data()
        json_data = json.loads(data.decode("utf-8"))
        ip = json_data.get("ip")
        host = monitor_data(ip)
        result = host.host()
        return jsonify(result)
    else:
        return "You are Fail"

#导入蓝图
from api_1.CurrentMonitor import currentMonitor
app.register_blueprint(currentMonitor)


"""
调用数据库连接参数
可移动至Mysql/Connection.py
"""
# from security import mysql_url
# app.config["SQLALCHEMY_DATABASE_URI"] = mysql_url
# app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

"""
程序实例app调用sql连接
"""
# from Mysql.Connection import init_db
# init_db(app)

# r'/*' 是通配符，让本服务器所有的URL 都允许跨域请求
CORS(app, resources=r'/*')


"""
程序入口
"""
if __name__ == "__main__":
    app.run(host='127.0.0.5',debug=app.config['DEBUG'],port=80,threaded=True)