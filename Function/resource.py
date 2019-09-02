import json,requests

"""
zabbix post data class method
"""


class gain():

    def __init__(self,data):
        self.data = json.dumps(data)

    def responer(self):
        __zabbix_api ="http://10.47.0.115/zabbix/api_jsonrpc.php"

        result = requests.post(url=__zabbix_api,data=self.data,headers={'Content-Type': 'application/json'})

        return result.json()["result"]


