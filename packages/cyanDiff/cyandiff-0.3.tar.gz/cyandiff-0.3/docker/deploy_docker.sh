#!/usr/bin/env bash
set -e

TAG=0.0.2

export BUILDAH_FORMAT=docker

docker build \
    -t "czhu1729/team40:${TAG}" \
    -t "czhu1729/team40:latest" .

docker login docker.io
docker push "czhu1729/team40:${TAG}"
docker push "czhu1729/team40:latest"

docker rmi -f czhu1729/team40:${TAG}