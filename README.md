# huawei-to-influx

Tool to collect data from Huawei inverter and save it in Influxdb to display in Grafana.

# How to start

Install make, docker and docker-compose. To run for the first time:

    export HUAWEI_ADDRESS=<inverter_ip_address>
    make first run
    
This will build docker image, fetch Influx and Grafana containers and run everything. 

# Configure Grafana

Log in to Grafana (it should be available at http://localhost:3000) and configure Influx datasource. You will only need to configure URL: http://influx:8086 and database name: grafana. You can make your configuration a little more sofisticated, but you will have to tweak docker-compose.yml and other configuration yourself.

# Add dashboard and panels

TODO

# How to prepare your inverter to serve data via modbus

TODO

# Example graphs 

TODO
