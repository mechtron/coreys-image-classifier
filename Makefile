docker:
	docker-compose up -d --build

docker_down:
	docker-compose down

request:
	curl --request POST --header "Content-Type: application/json" --data '{"image_url":"https://s3.amazonaws.com/gumgum-interviews/ml-engineer/cat.jpg"}' http://localhost:8000/classify-image

db_create:
	docker exec classifier_db mysql -ppassword -e 'CREATE DATABASE IF NOT EXISTS api;'

db_migrate:
	docker exec classifier_api python3 manage.py migrate

helm_install:
	helm install --name ml-engineer-project helm/ml-engineer-project

helm_upgrade:
	helm upgrade ml-engineer-project helm/ml-engineer-project

helm_delete:
	helm delete --purge ml-engineer-project
