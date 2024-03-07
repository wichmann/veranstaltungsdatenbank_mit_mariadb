# Veranstaltungsdatenbank

## Deployment mit Docker

    docker build https://github.com/wichmann/veranstaltungsdatenbank.git -t verandb
    docker run -p 5000:5000 -d verandb
