# Dockerfile

# Basisimage basiert auf Ubuntu 24.04
FROM python:3.11-alpine

# Benenne Port, der von der Web-App genutzt wird
EXPOSE 5000

# Arbeitsverzeichnis im Container wechseln
WORKDIR /app

# Alle notwendigen Pakete (Python, MariaDB Connector) installieren
RUN apk add mariadb-connector-c mariadb-connector-c-dev gcc libc-dev

# Notwendige Python-Bibliotheken installieren
RUN pip install --break-system-packages flask mariadb

# Kopiere lokale Datei in das Container-Image
COPY webapp.py /app

# Konfiguriere den Befehl, der im Container ausgeführt werden soll 
# (Anwendung Python + Skriptname als Parameter)
ENTRYPOINT [ "python3" ]
CMD ["webapp.py" ]
