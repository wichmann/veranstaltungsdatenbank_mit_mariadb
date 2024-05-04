[![Docker](https://github.com/wichmann/veranstaltungsdatenbank/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/wichmann/veranstaltungsdatenbank/actions/workflows/docker-publish.yml)
[![Docker Image CI](https://github.com/wichmann/veranstaltungsdatenbank/actions/workflows/docker-image.yml/badge.svg)](https://github.com/wichmann/veranstaltungsdatenbank/actions/workflows/docker-image.yml)
[![MIT License](https://img.shields.io/badge/license-MIT-red.svg?style=flat)](http://choosealicense.com/licenses/mit/)

# Veranstaltungsdatenbank

## Deployment mit Docker

    docker build https://github.com/wichmann/veranstaltungsdatenbank.git -t verandb
    docker run -p 5000:5000 -d verandb

## Deployment mit Docker Compose

    git clone https://github.com/wichmann/veranstaltungsdatenbank.git
    docker compose up -d
