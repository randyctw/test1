import logging
import os
import time
import requests
from glob import glob
from prometheus_client import start_http_server, Gauge

# Logging 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class CustomExporter:
    def __init__(self) -> None:
        self.ports = Gauge('gameserver','shows the users connected to the port', labelnames=['svrname', 'app'])
    
    def call(self):
        params = {
        'key': '722f27e83d4a05ba44df933ff8ccdf84',
        }

        response = requests.get('https://goblinslayer-clb.pro.g123-cpp.com/login/zonelist2', params=params)
        return response.json()['data']['serverlist']

    def main(self):
        exporter_port = int(os.environ.get("EXPORTER_PORT", "9877"))
        start_http_server(exporter_port)
        while True:
            servers = self.call()
            for server in servers:
                number = server['srvname']
                online = server['cur_online']
                self.ports.labels(svrname=number, app='goblinslayer').set(float(online))
                logging.info(f'{number}: {online}')
            time.sleep(30)

            

if __name__ == "__main__":
    print('test')
    c = CustomExporter()
    c.main()
    