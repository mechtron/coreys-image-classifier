# coreys-image-classifier

By Corey Gale (`mechtrondev[at]gmail.com`)

## Production environment

    https://classifier.k8s.prod.sandbox.ggops.com

## Create Docker environment

    make docker_up

### Create the API's database for the first time

    make db_create

### Migrate the API's database

    make db_migrate

## Helm chart

You can deploy to Kubernetes using the project's helm chart located in `helm/coreys-image-classifier`.

### First release

    make helm_deps && make helm_upgrade_install

### Deploy a new release

    make helm_upgrade_install

### Delete a release

    make helm_delete

## Example request

    curl --request POST --header "Content-Type: application/json" --data '{"image_url":"https://coreys-image-classifier-example-images.s3.amazonaws.com/ninja.png"}' http://localhost:8000/classify-image

Or simply: `make request`

Response:

    {"processing_time":6.076243,"classification":"Yorkshire_terrier","confidence":0.9685871601104736}

#### Image test: apple

    curl --request POST --header "Content-Type: application/json" --data '{"image_url":"https://coreys-image-classifier-example-images.s3.amazonaws.com/apple.jpg"}' http://localhost:8000/classify-image

Response:

    {"processing_time":5.160117,"classification":"Granny_Smith","confidence":0.9807039499282837}

#### Image test: cat

    curl --request POST --header "Content-Type: application/json" --data '{"image_url":"https://coreys-image-classifier-example-images.s3.amazonaws.com/cat.jpg"}' http://localhost:8000/classify-image

Response:

    {"processing_time":5.143928,"classification":"tabby","confidence":0.5540751218795776}

### Reporting endpoint

Note: only authorized usernames (`admin` and `corey`) can access this endpoint.

    curl --request GET --header 'Authorization: Token <AUTH_TOKEN_HERE>' http://localhost:8000/report

Response (truncated response for a dataset of `n=20000` random classifications):

    [
        {
            "image_url":"https://example.com/162.jpg",
            "classification_count":35,
            "processing_time_avg":6.79950286,
            "processing_time_max":9.7266,
            "processing_time_min":3.0883
        },
        ...
    ]

### Secret endpoint

Note: only authenticated users can access this endpoint.

    curl --request GET --header 'Authorization: Token <AUTH_TOKEN_HERE>' http://localhost:8000/secret

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

    curl --request POST --header 'Authorization: Token <AUTH_TOKEN_HERE>' http://localhost:8000/auth/token/logout/

Response: `204`

##### Make authenticated request

    curl --request GET --header 'Authorization: Token <AUTH_TOKEN_HERE>' http://localhost:8000/auth/users/me/

Response:

    {"email":"","id":1,"username":"corey"}

##### Change password

    curl --request POST --header 'Authorization: Token <AUTH_TOKEN_HERE>' --header "Content-Type: application/json" --data '{"current_password": "abc123", "new_password": "xyz123"}' http://localhost:8000/auth/password/

Response: `204`

### Build and tag Docker images

##### API

    APP_DIR=api IMAGE_NAME=mechtron/coreys-image-classifier-api COMMIT_TAG=API_v1.1 make docker_image

##### Web

    APP_DIR=web IMAGE_NAME=mechtron/coreys-image-classifier-web COMMIT_TAG=Web_v1.3 make docker_image

### To do

- Add GitHub Actions deployment pipeline
- Add Prometheus metrics & Grafana dashboard
