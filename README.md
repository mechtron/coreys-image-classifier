# coreys-image-classifier

By Corey Gale (`mechtrondev[at]gmail.com`)

## Production environment

[Try it out!](https://cic.k8s.sandbox.ggops.com)

## Features

- Classification of 1000 different objects
- API with user management
- SPA-style web client
- Top 10 classifications page
- Classification caching

## Tech stack

### Frontend

- [Bootstrap](https://getbootstrap.com)
- [VueJS](https://vuejs.org)

### Backend

- [Python](https://www.python.org)
- [Django REST Framework](https://www.django-rest-framework.org)
- [Djoser](https://github.com/sunscrapers/djoser)
- [TensorFlow](https://www.tensorflow.org)
- [Keras](https://keras.io)
- [ImageNet](http://www.image-net.org)
- [MySQL](https://www.mysql.com)
- [Redis](https://redis.io)

### DevOps

- [Docker](https://www.docker.com)
- [Kubernetes](https://kubernetes.io)
- [EKS](https://aws.amazon.com/eks/)
- [Helm](https://helm.sh)
- [Ambassador](https://www.getambassador.io)
- [Envoy](https://www.envoyproxy.io)

[Stack visualized](https://cic.k8s.sandbox.ggops.com/#/about)

## 📕 Docs

Head over to the [projects docs page](https://corey.tech/coreys-image-classifier/) to learn how to:

- Start the dev environment
- Trigger database migrations
- Build the app's Docker images
- Deploy the app's Helm chart
- Make common API requests (like requesting a classification)

[Project docs](https://corey.tech/coreys-image-classifier/)

## To do

1. Add Prometheus metrics endpoints to API and Web apps
1. Visualize metrics with Grafana dashboards
