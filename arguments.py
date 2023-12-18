from configparser import RawConfigParser
import argparse,json

def get_args():
    parser = argparse.ArgumentParser(description='OceanStore 9000 options!')
    parser.add_argument("-a","--address",type=str,default='0.0.0.0')
    parser.add_argument("-p","--port",type=str,default=9099)
    parser.add_argument("-c", "--config", type=str, default="./conf/config.ini")
    parser.add_argument("-ca", "--auth_config", type=str, default="./conf/auth.ini")
    args = parser.parse_args()
    return args
def get_config(config_path):
    config = RawConfigParser()
    config.read(config_path,encoding='UTF8')
    hw_host = config.get('default',"host")
    hw_port = config.get('default', "port")
    hw_username = config.get('default', "username")
    hw_password = config.get('default', "password")
    hw_parid_list = config.get('default', "parentID_list")
    parentID_list = json.loads(hw_parid_list)
    return host, port, username, password, parentID_list
def get_auth(auth_path):
    config = RawConfigParser()
    config.read(auth_path,encoding='UTF8')
    auth_user = config.get('auth',"username")
    auth_passwd = config.get('auth',"password")
    return auth_user,auth_passwd
