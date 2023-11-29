from configparser import RawConfigParser
import argparse,json

def get_args():
    parser = argparse.ArgumentParser(description='OceanStore 9000 options!')
    parser.add_argument("-a","--address",type=str,default='0.0.0.0')
    parser.add_argument("-p","--port",type=str,default=9099)
    parser.add_argument("-c", "--config", type=str, default="./conf/config.ini")
    args = parser.parse_args()
    return args
def get_config(config_path):
    config = ConfigParser()
    config.read(config_path,encoding='UTF8')
    hw_host = config.get('default',"host")
    hw_port = config.get('default', "port")
    hw_username = config.get('default', "username")
    hw_password = config.get('default', "password")
    hw_parid_list = config.get('default', "parentID_list")
    parentID_list = json.loads(hw_parid_list)
    return host, port, username, password, parentID_list
