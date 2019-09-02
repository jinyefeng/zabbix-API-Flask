import json,requests
from Function.resource import gain

"""
zabbix security data
"""


# class gain():
#
#     def __init__(self,data):
#         self.data = json.dumps(data)
#
#     def responer(self):
#         __zabbix_api ="http://10.47.0.115/zabbix/api_jsonrpc.php"
#
#         result = requests.post(url=__zabbix_api,data=self.data,headers={'Content-Type': 'application/json'})
#
#         return result.json()["result"]
#
#

class Auto():

    def __init__(self):
        pass

    def login(self):
        __zabbix_username = "Admin"
        __zabbix_password = "zabbix"
        data = {
            "jsonrpc":"2.0",
            "method":"user.login",
            "params":{"user":__zabbix_username ,"password":__zabbix_password},
            "id":1
        }
        result = gain(data)
        return result.responer()

    def logout(self):
        data = {
            "jsonrpc": "2.0",
            "method": "user.logout",
            "params": [],
            "id": 1,
            "auth": "45037833f83ae7eb8c18e8a201958855"        #变量
        }
        result = gain(data).responer()
        return result



test = Auto()
print(test.login())