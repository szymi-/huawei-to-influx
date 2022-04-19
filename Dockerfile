FROM python:3.6

ADD ./ /root/huawei-to-influx
RUN pip install -r /root/huawei-to-influx/requirements.txt
ENTRYPOINT ["python", "-u", "/root/huawei-to-influx/src/huawei_to_influx.py"]
