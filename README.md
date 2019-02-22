# ml-engineer-project
By Corey Gale (coreygale@gmail.com / corey@gumgum.com)

## Create Docker environment

    make docker_up

### Create the API's database for the first time

    make db_create

### Migrate the API's database

    make db_migrate

## Helm chart

You can deploy to Kubernetes using the project's helm chart located in `helm/ml-engineer-project`.

### First release

    make helm_install

### Deploy a new release

    make helm_upgrade

### Delete a release

    make helm_delete

## Example request

    curl --request POST --header "Content-Type: application/json" --data '{"image_url":"https://s3.amazonaws.com/gumgum-interviews/ml-engineer/cat.jpg"}' http://localhost:8000/classify-image

Or simply: `make request`

Response:

    {"processing_time":6.076243,"classification":"tabby","confidence":0.5540751218795776}

#### Image test: apple

    curl --request POST --header "Content-Type: application/json" --data '{"image_url":"https://i.imgur.com/UBNYRsZ.jpg"}' http://localhost:8000/classify-image

Response:

    {"processing_time":5.160117,"classification":"Granny_Smith","confidence":0.9807039499282837}

#### Image test: yorkie

    curl --request POST --header "Content-Type: application/json" --data '{"image_url":"https://i.imgur.com/y8BzuvG.jpg"}' http://localhost:8000/classify-image

Response:

    {"processing_time":5.143928,"classification":"Yorkshire_terrier","confidence":0.9987012147903442}

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
