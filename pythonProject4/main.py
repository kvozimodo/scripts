import psutil
import configparser
import threading
import json

syslog_json = open("syslog.json", mode='a', encoding='utf_8')
syslog_txt = open("syslog.txt", mode='a', encoding='utf_8')


class SnapshotMaker():
    config = configparser.ConfigParser()
    config.read("config.ini")
    timestamp = int(config["common"]["interval"])
    output_format = config["common"]["output"]
    counter = int(config["common"]["counter"])
    def __init__(self, syslog_json, syslog_txt):
        self.syslog_json = syslog_json
        self.syslog_txt = syslog_txt


    def make_snapshot(self):
        global counter
        snapshot = {}
        snapshot['SNAPSHOT' + str(self.counter)] = self.get_system_info()
        json.dump(snapshot, syslog_json)
        syslog_txt.write(str(snapshot))
        self.counter += 1
        self.config.set("common", "counter", str(self.counter))
        with open("config.ini", 'w') as configfile:
            self.config.write(configfile)

    def get_system_info(self):
        TIMESTAMP = {}
        TIMESTAMP['cpu'] = str(psutil.cpu_percent())
        TIMESTAMP['memory'] = str(psutil.swap_memory())
        TIMESTAMP['virtual_memory'] = str(psutil.virtual_memory())
        TIMESTAMP['net_info'] = str(psutil.net_if_addrs().items())
        return TIMESTAMP



snapshoter = SnapshotMaker(syslog_json, syslog_txt)
threading.Timer(snapshoter.timestamp, snapshoter.make_snapshot).start()
