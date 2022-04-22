import os

LOGGING = {
    "version": 1,
    "formatters": {
        "standard": {
            "format": "%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "WARNING",
            "formatter": "standard",
            "stream": "ext://sys.stdout",
        }
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': True
        },
    }
}

HUAWEI_ADDRESS = os.environ.get('HUAWEI_ADDRESS')
HUAWEI_SLAVE = int(os.environ.get('HUAWEI_SLAVE'))
INFLUX_HOST = os.environ.get('INFLUX_HOST')
INFLUX_PORT = os.environ.get('INFLUX_PORT')
INFLUX_USERNAME = os.environ.get('INFLUX_USERNAME')
INFLUX_PASSWORD = os.environ.get('INFLUX_PASSWORD')
INFLUX_DATABASE = os.environ.get('INFLUX_DATABASE')

KEYS = [
    "pv_01_voltage",
    "pv_02_voltage",
    "pv_01_current",
    "pv_02_current",
    "input_power",
    "grid_voltage",
    "line_voltage_A_B",
    "line_voltage_B_C",
    "line_voltage_C_A",
    "phase_A_voltage",
    "phase_B_voltage",
    "phase_C_voltage",
    "grid_current",
    "phase_A_current",
    "phase_B_current",
    "phase_C_current",
    "day_active_power_peak",
    "active_power",
    "reactive_power",
    "power_factor",
    "grid_frequency",
    "efficiency",
    "internal_temperature",
    "insulation_resistance",
    "device_status",
    "startup_time",
    "shutdown_time",
    "fault_code",
    "accumulated_yield_energy",
    "daily_yield_energy",
]
