docker_up:
	docker-compose up -d --build

docker_down:
	docker-compose down

docker_image:
	sh ./scripts/docker_build.sh

request:
	curl --request POST --header "Content-Type: application/json" --data '{"image_url":"https://coreys-image-classifier-example-images.s3.amazonaws.com/ninja.png"}' http://localhost:8000/classify-image

db_create:
	docker exec classifier_db mysql -ppassword -e 'CREATE DATABASE IF NOT EXISTS api;'

db_migrate:
	docker exec classifier_api python3 manage.py migrate

minikube_docker_build:
	sh minikube_docker.sh

minikube_enable_ingress:
	minikube addons enable ingress

helm_upgrade_install:
	helm upgrade --install classifier --namespace=classifier helm/coreys-image-classifier

helm_upgrade_install_secure:
ifeq ($(API_SECRET),)
	@echo API_SECRET must be set
endif
ifeq ($(MYSQL_PASSWORD),)
	@echo MYSQL_PASSWORD must be set
endif
	helm upgrade --install classifier --namespace=classifier helm/coreys-image-classifier --set api.apiSecret=$(API_SECRET) --set mysql.mysqlPassword=$(MYSQL_PASSWORD)

helm_delete:
	helm delete --purge classifier

helm_deps:
	helm repo add google https://kubernetes-charts.storage.googleapis.com
	helm dependency update helm/coreys-image-classifier
