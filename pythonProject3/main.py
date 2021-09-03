import psutil
import configparser
import threading
import json

config = configparser.ConfigParser()
config.read("config.ini")
timestamp = int(config["common"]["interval"])
output_format = config["common"]["output"]
counter = int(config["common"]["counter"])
syslog_json = open("syslog.json", mode='a', encoding='utf_8')
syslog_txt = open("syslog.txt", mode='a', encoding='utf_8')


def make_snapshot():
    global counter
    snapshot = {}
    snapshot['SNAPSHOT' + str(counter)] = get_system_info()
    json.dump(snapshot, syslog_json)
    syslog_txt.write(str(snapshot))
    counter += 1
    config.set("common", "counter", str(counter))
    with open("config.ini", 'w') as configfile:
        config.write(configfile)


def get_system_info():
    TIMESTAMP = {}
    TIMESTAMP['cpu'] = str(psutil.cpu_percent())
    TIMESTAMP['memory'] = str(psutil.swap_memory())
    TIMESTAMP['virtual_memory'] = str(psutil.virtual_memory())
    TIMESTAMP['net_info'] = str(psutil.net_if_addrs().items())
    return TIMESTAMP


threading.Timer(timestamp, make_snapshot).start()
