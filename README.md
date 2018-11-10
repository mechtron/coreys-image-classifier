# ml-engineer-project
By Corey Gale (mechtrondev@gmail.com)

## Create Docker environment

    make docker

### Create the API's database for the first time

    make db_create

### Migrate the API's database

    make db_migrate

## Example request

    make request

### Reporting endpoint

Note: only authorized usernames (`admin` and `corey`) can access this endpoint.

    curl --request GET --header 'Authorization: Token 2cc009873ddf3c49ff0000fb6b77a87782a73b8f' http://localhost:8000/report

Response (truncated response for a dataset of `n=20000` random classifications):

    [
        {
            "image_url":"https://s3.amazonaws.com/gumgum-interviews/ml-engineer/162.jpg",
            "classification_count":35,
            "processing_time_avg":6.79950286,
            "processing_time_max":9.7266,
            "processing_time_min":3.0883
        },
        ...
    ]

### Secret endpoint

Note: only authenticated users can access this endpoint.

    curl --request GET --header 'Authorization: Token 2cc009873ddf3c49ff0000fb6b77a87782a73b8f' http://localhost:8000/secret

Response: `Hi corey`

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
