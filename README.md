[![Docker](https://github.com/wichmann/veranstaltungsdatenbank/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/wichmann/veranstaltungsdatenbank/actions/workflows/docker-publish.yml)
[![Docker Image CI](https://github.com/wichmann/veranstaltungsdatenbank/actions/workflows/docker-image.yml/badge.svg)](https://github.com/wichmann/veranstaltungsdatenbank/actions/workflows/docker-image.yml)
[![MIT License](https://img.shields.io/badge/license-MIT-red.svg?style=flat)](http://choosealicense.com/licenses/mit/)

# Veranstaltungsdatenbank

## Deployment mit vorgebauten Image von Github Package Repository

    git clone https://github.com/wichmann/veranstaltungsdatenbank_mit_mariadb.git
    docker compose up -d

## Deployment mit selbstgebautem Image

    git clone https://github.com/wichmann/veranstaltungsdatenbank_mit_mariadb.git
    docker compose -f docker-compose.build.yml up --build -d

## Ausgabe der Log-Nachrichten

    docker compose logs -f
