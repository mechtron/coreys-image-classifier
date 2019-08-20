eval $(minikube docker-env) && \
cd api && docker build -t classifier_api . && \
cd ../web && docker build -t classifier_web .