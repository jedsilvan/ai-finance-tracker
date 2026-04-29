#!/bin/bash

podman-compose down -v
podman rm -af
podman rmi -af
podman-compose up --build
