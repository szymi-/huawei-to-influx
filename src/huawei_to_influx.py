from huawei_solar import ConnectionException, HuaweiSolar
from datetime import datetime
from influxdb import InfluxDBClient

import settings
import time


class OffGrid(Exception):
    pass


class HuaweiToInflux:
    def __init__(self):
        self.huawei = HuaweiSolar(settings.HUAWEI_ADDRESS, slave=settings.HUAWEI_SLAVE)
        self.influx = InfluxDBClient(
            host=settings.INFLUX_HOST, port=settings.INFLUX_PORT, 
            username=settings.INFLUX_USERNAME, password=settings.INFLUX_PASSWORD, ssl=False
        )
        self.influx.switch_database(settings.INFLUX_DATABASE)


    def get_huawei_solar_data(self):
        print("Starting to get solar data...")
        while True:
            device_status = self.huawei.get('device_status')
            self.write_point('device_status', device_status.value)
            if device_status.value != 'On-grid':
                raise OffGrid
            for key in settings.KEYS:
                if key == 'device_status':
                    continue
                result = self.huawei.get(key)
                if type(result.value) == datetime:
                    value = result.value.isoformat()
                else:
                    value = result.value
                point = self.write_point(key, value)



    def run(self):
        try:
            self.get_huawei_solar_data()
        except (OffGrid, ConnectionException) as e:
            print("Waiting... ({})".format(e))
            time.sleep(30)
            self.get_huawei_solar_data()


    def write_point(self, key, value):
        point = [
            {
                "measurement": "huawei",
                "time": datetime.now().isoformat(),
                "fields": {
                    key: value
                }
            }
        ]
        print("Writing measurement:")
        print(point)
        self.influx.write_points(point)


if __name__ == "__main__":
    huawei_to_influx = HuaweiToInflux()
    huawei_to_influx.run()
