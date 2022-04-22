from huawei_solar import HuaweiSolar
from datetime import datetime
from influxdb import InfluxDBClient
from tenacity import (
    after_log,
    before_log,
    before_sleep_log,
    retry,
    wait_fixed,
)

import settings
import time
import logging.config


logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger(__name__)


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

    def _get_huawei_solar_data(self):
        logger.debug("Starting to get solar data...")
        while True:
            device_status = self.huawei.get('device_status')
            self._write_point('device_status', device_status.value)
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
                point = self._write_point(key, value)

    def _write_point(self, key, value):
        point = [
            {
                "measurement": "huawei",
                "time": datetime.now().isoformat(),
                "fields": {
                    key: value
                }
            }
        ]
        logger.debug(("Writing measurement: {}").format(point))
        self.influx.write_points(point)

    @retry(
        wait=wait_fixed(30),
        before=before_log(logger, logging.DEBUG),
        before_sleep=before_sleep_log(logger, logging.WARNING),
        after=after_log(logger, logging.DEBUG)
    )
    def run(self):
        self._get_huawei_solar_data()



if __name__ == "__main__":
    huawei_to_influx = HuaweiToInflux()
    huawei_to_influx.run()
