from huawei_solar import HuaweiSolar
from datetime import datetime
from influxdb import InfluxDBClient

import settings
import time


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
                print("Waiting for \"On-grid\" status...")
                break
            for key in settings.KEYS:
                if key == 'device_status':
                    continue
                result = self.huawei.get(key)
                if type(result.value) == datetime:
                    value = result.value.isoformat()
                else:
                    value = result.value
                point = self.write_point(key, value)

        print("Sleeping 30 seconds...")
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
    huawei_to_influx.get_huawei_solar_data()
