from configparser import ConfigParser
import argparse

def get_args():
    parser = argparse.ArgumentParser(description='OceanStore 9000 options!')
    parser.add_argument("-a","--address",type=str,default='localhost')
    parser.add_argument("-p","--port",type=str,default=9099)
    parser.add_argument("-c", "--config", type=str, default="./conf/config.ini")
    args = parser.parse_args()
    return args
def get_config(config_path):
    config = ConfigParser()
    config.read(config_path,encoding='UTF8')
    host = config.get('default',"host")
    port = config.get('default', "port")
    username = config.get('default', "username")
    password = config.get('default', "password")
    return host, port, username, password
