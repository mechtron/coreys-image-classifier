# ml-engineer-project
By Corey Gale (mechtrondev@gmail.com)

## Create Docker environment

    make docker

### Create the API's database for the first time

    docker exec -it <db_container_id> /bin/sh
    mysql -ppassword -e 'CREATE DATABASE IF NOT EXISTS api;'

### Migrate the API's database

    docker exec -it <api_container_id> /bin/sh
    python3 manage.py migrate

## Example request

    make request

### User management

##### Create a new user

    curl --request POST --header "Content-Type: application/json" --data '{"username":"corey", "password": "abc123"}' http://localhost:8000/auth/users/

Response:

    {"email":"","username":"corey","id":1}

##### Login

    curl --request POST --header "Content-Type: application/json" --data '{"username":"corey", "password": "abc123"}' http://localhost:8000/auth/token/login/

Response:

    {"auth_token":"1f0c0622859710318b2abfeca7f13bca1ab21621"}

##### Logout

    curl --request POST --header 'Authorization: Token efe3b535b5a62588a8279360660a7201bf59acad' http://localhost:8000/auth/token/logout/

Response: `204`

##### Make authenticated request

    curl --request GET --header 'Authorization: Token efe3b535b5a62588a8279360660a7201bf59acad' http://localhost:8000/auth/users/me/

Response:

    {"email":"","id":1,"username":"corey"}

##### Change password

    curl --request POST --header 'Authorization: Token efe3b535b5a62588a8279360660a7201bf59acad' --header "Content-Type: application/json" --data '{"current_password": "abc123", "new_password": "xyz123"}' http://localhost:8000/auth/password/

Response: `204`
