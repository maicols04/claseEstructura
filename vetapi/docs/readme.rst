.. _readme:
.. include:: ../README.rst


podman run -dt --rm  --pod new:db --name mariadb -e MYSQL_ROOT_PASSWORD=superS3cret! -e MYSQL_USER=vetdb -e MYSQL_DATABASE=vetpass -e MYSQL_PASSWORD=password -p 3306:3306 -p 8082:8080 mariadb:10.4.4

podman run -dt --rm --pod db --name adminer adminer:standalone
podman run -dt --rm --pod db --name adminer adminer:4.8.1-standalone

podman run --link some_database:db -p 8080:8080 adminer
podman run --link some_database:db -p 8080:8080 -e ADMINER_PLUGINS='tables-filter tinymce' adminer

uvicorn main:app --reload

Software
Base de datos:
https://dev.mysql.com/downloads/windows/installer/8.0.html

En caso de usar docker compose:
´
version: '3.1'

services:
  adminer:
    image: adminer
    restart: always
    ports:
      - 8080:8080
  db:
    image: mysql:5.6
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD:superS3cret!
      MYSQL_USER=vetdb
      MYSQL_DATABASE=vetuser
      MYSQL_PASSWORD=vetpass
´
