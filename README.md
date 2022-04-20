# huawei-to-influx

Tool to collect data from Huawei inverter and save it in Influxdb to display in Grafana. I used to have a Fronius inverter and kept Fronius related scripts in [this repo](https://github.com/szymi-/fronius-to-influx). Since I changed my inverter to Huawei after adding some new solar panels, I had to create a new script for collecting Huawei data. I rely on [this library](https://gitlab.com/Emilv2/huawei-solar/).

# How to start

Install make, docker and docker-compose. To run for the first time:

    export HUAWEI_ADDRESS=<inverter_ip_address>
    make first run
    
This will build docker image, fetch Influx and Grafana imaages and run everything. 

# Configure Grafana

Log in to Grafana (it should be available at http://localhost:3000) and configure Influx datasource. You will only need to configure URL: http://influx:8086 and database name: grafana. You can make your configuration a little more sofisticated, but you will have to tweak docker-compose.yml and other configuration yourself.

# Add dashboard and panels

You can use the dashboard from `sample_dashboards/` dir as a starting point.

# Adding more metrics

I don't have a battery attached to my inverter at this time. So I did not include any battery related configuration in my settings. But these settings can be easily added - just add the keys you are interested in to the list in `src/settings.py`. Available keys can be found here: https://gitlab.com/Emilv2/huawei-solar/-/blob/master/src/huawei_solar/huawei_solar.py#L499

# How to prepare inverter to serve data via modbus

It turned out to be quite tricky to get modbust to work. I am writing down what I know here - maybe somebody will find this information useful.

Install mobile app for inverter configuration and management: https://intl.fusionsolar.huawei.com/pvmswebsite/nologin/assets/build/index.html#/jumppage

Follow this guide to prepare inverter to serve data via modbus: https://forum.huawei.com/enterprise/en/modbus-tcp-guide/thread/789585-100027 To enable modbus, installer access is required. Default installer password should be (or was in my case) `00000a`. 

Upgrade firmware of your inverter components. In my case, the following firmware versions work (inverter and modbus):

![image](https://user-images.githubusercontent.com/7512741/164323457-181d2865-9586-4f49-8750-ac8f53899e0a.png)

In addition, dongle firmware should be at vesion V100R001C00SPC127. I got the firmware from Huawei support after contacting them via email (eu_inverter_support@huawei.com). Dongle can be accessed via it's built in access point just like the inverter. The wifi is active for some time after dongle restart (take the dongle out and insert it back in to restart). Installer password is again `00000a`. Newer versions of firmware may not work (I think Huawei decided to disallow users to access this data directly. Who knows, maybe they will change their mind in newer firmware versions.)

# Example graphs 

![image](https://user-images.githubusercontent.com/7512741/164311783-00a0e48b-e850-47a5-8562-6e5e99b20e39.png)

![image](https://user-images.githubusercontent.com/7512741/164311919-abe71f8e-4053-43a8-884f-2ce8e5d0b091.png)

![image](https://user-images.githubusercontent.com/7512741/164312048-5d113c1b-0a3a-4533-a224-2b14da55ecc2.png)

![image](https://user-images.githubusercontent.com/7512741/164312428-2e1f3324-f70b-4e19-892c-3fe6cbe6c651.png)
