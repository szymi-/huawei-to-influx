build-docker:
	docker build -t huawei-to-influx .

provision-influx:
	echo create database grafana | docker compose exec influx influx

run-docker:
	docker compose up -d

down-docker:
	docker compose down

first-run: build-docker run-docker provision-influx
