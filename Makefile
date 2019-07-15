docker_up:
	docker-compose up -d --build

docker_down:
	docker-compose down

docker_image:
	./scripts/docker_build.sh

request:
	curl --request POST --header "Content-Type: application/json" --data '{"image_url":"https://s3.amazonaws.com/gumgum-interviews/ml-engineer/cat.jpg"}' http://localhost:8000/classify-image

db_create:
	docker exec classifier_db mysql -ppassword -e 'CREATE DATABASE IF NOT EXISTS api;'

db_migrate:
	docker exec classifier_api python3 manage.py migrate

minikube_docker_build:
	sh minikube_docker.sh

minikube_enable_ingress:
	minikube addons enable ingress

helm_install:
	helm install --name classifier-dev --namespace=classifier helm/ml-engineer-project

helm_upgrade:
	helm upgrade classifier-dev --namespace=classifier helm/ml-engineer-project

helm_delete:
	helm delete --purge classifier-dev

helm_deps:
	helm repo add google https://kubernetes-charts.storage.googleapis.com
	helm dependency update helm/ml-engineer-project
