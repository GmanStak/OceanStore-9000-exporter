import requests, sys
from requests.exceptions import HTTPError
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class OceanStor(object):
    def __init__(self, host, port, username, password, timeout) -> None:
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.timeout = timeout
        self.url = f'https://{self.host}:{self.port}/deviceManager/v1/rest'
        self.session = requests.Session()
        self.session.verify = False

    def login(self):
        try:
            response = self.session.post(self.url + '/xxxxx/sessions',json={'scope': 0,'username': self.username,'password': self.password})
        except HTTPError as HttpErr:
            print(HttpErr)
        except Exception as err:
            print(err)
        resp = response.json()
        if resp['error']['code'] != 0:
            sys.exit(3)
        elif not 'deviceid' in resp['data']:
            sys.exit(3)
        else:
            self.deviceID = resp['data']['deviceid']
            self.session.headers.update({'iBaseToken': resp['data']['iBaseToken'], 'Content-Type': 'application/json', 'Accept': 'application/json'})
        return True
    def logout(self):
        try:
            resp = self.session.delete(self.url + '/' + self.deviceID + '/sessions')
        except HTTPError as HttpErr:
            print(HttpErr)
        except Exception as err:
            print(err)
        return True

    def get_cpu(self):
        try:
            response = self.session.get(self.url + '/' + self.deviceID + '/cpu')
        except HTTPError as err:
            print(err)
        data = response.json()
        return data

    def get_memory(self):
        try:
            response = self.session.get(self.url + '/' + self.deviceID + '/memory')
        except HTTPError as err:
            print(err)
        data = response.json()
        return data

    def get_disk(self):
        try:
            response = self.session.get(self.url + '/' + self.deviceID + '/disk')
        except HTTPError as err:
            print(err)
        data = response.json()
        return data

    def get_cluster_info(self):
        try:
            response = self.session.get(self.url + '/' + self.deviceID + '/cluster_nas_service')
        except HTTPError as err:
            print(err)
        data = response.json()
        return data

    def get_eth_id(self,eth_id=''):
        try:
            response = self.session.get(self.url + '/' + self.deviceID + '/eth_port' + eth_id)
        except HTTPError as err:
            print(err)
        data = response.json()
        return data

    def get_allfsquota(self,parentID):
        try:
            url = f"https://{self.host}:{self.port}/deviceManager/rest/{self.deviceID}/S3_StoragePolicy?parentID="+f"{parentID}"
            response = self.session.get(url)
        except HTTPError as err:
            print(err)
        data = response.json()
        return data

    def get_fsquota(self,fsquota_id = ''):
        try:
            response = self.session.get(self.url + '/' + self.deviceID + '/fsquota' + fsquota_id)
        except HTTPError as err:
            print(err)
        data = response.json()
        return data

    def get_sys_node(self):
        try:
            response = self.session.get(self.url + '/' + self.deviceID + '/sys_node')
        except HTTPError as err:
            print(err)
        data = response.json()
        return data

    def get_node_fs_service(self):
        try:
            response = self.session.get(self.url + '/' + self.deviceID + '/node_fs_service')
        except HTTPError as err:
            print(err)
        data = response.json()
        return data

    def get_nodePool(self,nodePool_id=''):
        try:
            response = self.session.get(self.url + '/' + self.deviceID + '/nodePool' + nodePool_id)
        except HTTPError as err:
            print(err)
        data = response.json()
        return data

    def get_cluster_nas_service(self):
        try:
            response = self.session.get(self.url + '/' + self.deviceID + '/cluster_nas_service')
        except HTTPError as err:
            print(err)
        data = response.json()
        return data

    def get_global_api(self,type_id,device_id,metric_id):
        try:
            response = self.session.get(self.url + '/' + self.deviceID + f'/performance_statistic/cur_statistic_data?CMO_STATISTIC_UUID={type_id}:{device_id}&CMO_STATISTIC_DATA_ID={metric_id}&CMO_STATISTIC_TIME_SPAN=0')
        except HTTPError as err:
            print(err)
        data = response.json()
        return data
