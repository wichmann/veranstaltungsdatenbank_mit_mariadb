# Dockerfile

# Basisimage basiert auf Ubuntu 24.04
FROM ubuntu:24.04

# Benenne Port, der von der Web-App genutzt wird
EXPOSE 5000

# Arbeitsverzeichnis im Container wechseln
WORKDIR /app

# Alle notwendigen Pakete (Python, MariaDB Connector) installieren
RUN echo 'APT::Install-Suggests "0";' >> /etc/apt/apt.conf.d/00-docker
RUN echo 'APT::Install-Recommends "0";' >> /etc/apt/apt.conf.d/00-docker
RUN DEBIAN_FRONTEND=noninteractive \
  apt-get update \
  && apt-get install -y python3 python3-pip libmariadb3 libmariadb-dev \
  && rm -rf /var/lib/apt/lists/*

# Notwendige Python-Bibliotheken installieren
RUN pip install flask mariadb

# Kopiere lokale Datei in das Container-Image
COPY webapp.py /app

# Konfiguriere den Befehl, der im Container ausgeführt werden soll 
# (Anwendung Python + Skriptname als Parameter)
ENTRYPOINT [ "python" ]
CMD ["webapp.py" ]
