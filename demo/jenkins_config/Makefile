# A Self-Documenting Makefile: http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
ARTIFACTORY_URL=sre-gettogether-docker-repo-docker-local.artifactory.swisscom.com
BUILD_DATE=$(shell date +%Y-%m-%dT%T%z)
GIT_COMMIT:=$(shell git rev-parse HEAD)
IMAGE_NAME=sre-gettogther-flask-app
IMAGE_VERSION=1.0.0-1
PROXY=http://server-proxy.corproot.net:8080

.PHONY: docker help
.DEFAULT_GOAL := help

build: ## Build Jenkins' slave image locally
	@echo "==>\033[1m Building ${IMAGE_NAME} with tag ${IMAGE_VERSION}\033[0m"
	docker build --no-cache --force-rm=true \
		-t ${ARTIFACTORY_URL}/${IMAGE_NAME}:${IMAGE_VERSION} \
		-t ${ARTIFACTORY_URL}/${IMAGE_NAME}:latest \
		--build-arg BUILD_DATE=${BUILD_DATE} \
		--build-arg GIT_COMMIT=${GIT_COMMIT} \
		--build-arg http_proxy=${PROXY} \
		--build-arg https_proxy=${PROXY} \
		--build-arg IMAGE_NAME=${IMAGE_NAME} \
		--build-arg IMAGE_VERSION=${IMAGE_VERSION} .
	@echo "\n==>\033[1m Image details\033[0m"
	@docker images ${ARTIFACTORY_URL}/${IMAGE_NAME}:${IMAGE_VERSION}

cleanup: ## Cleanup images
	-docker images -a | grep $(IMAGE_NAME) | awk '{print $$3}' | uniq | xargs docker rmi -f

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

#skipping docker login process

push: ## Push built image to artifactory
	@echo "==> \033[1m Pushing ${IMAGE_NAME} with tag ${IMAGE_VERSION} to ${ARTIFACTORY_URL}\033[0m"
	@docker push ${ARTIFACTORY_URL}/${IMAGE_NAME}:${IMAGE_VERSION}
	@echo "==>\033[1m Pushing ${IMAGE_NAME} with tag 'latest' to ${ARTIFACTORY_URL}\033[0m"
	@docker push ${ARTIFACTORY_URL}/${IMAGE_NAME}:latest