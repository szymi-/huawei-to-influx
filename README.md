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

# How to prepare inverter to serve data via modbus

TODO

# Example graphs 

![image](https://user-images.githubusercontent.com/7512741/164311783-00a0e48b-e850-47a5-8562-6e5e99b20e39.png)

![image](https://user-images.githubusercontent.com/7512741/164311919-abe71f8e-4053-43a8-884f-2ce8e5d0b091.png)

![image](https://user-images.githubusercontent.com/7512741/164312048-5d113c1b-0a3a-4533-a224-2b14da55ecc2.png)

![image](https://user-images.githubusercontent.com/7512741/164312428-2e1f3324-f70b-4e19-892c-3fe6cbe6c651.png)
