# ml-engineer-project
By Corey Gale (mechtrondev@gmail.com)

## Docker environment usage

    make docker

### Create the API's database for the first time

    docker exec -it <db_container_id> /bin/sh
    mysql -ppassword -e 'CREATE DATABASE IF NOT EXISTS api;'

### Migrate the API's database

    docker exec -it <api_container_id> /bin/sh
    python3 manage.py migrate
