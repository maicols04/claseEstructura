.. _readme:
.. include:: ../README.rst


podman run -dt --rm  --pod new:db --name mariadb -e MYSQL_ROOT_PASSWORD=superS3cret! -e MYSQL_USER=demo -e MYSQL_DATABASE=demodb -e MYSQL_PASSWORD=password -p 3306:3306 -p 8082:8080 mariadb:10.4.4
podman run -dt --rm  --pod new:db --name mariadb -e MYSQL_ROOT_PASSWORD=superS3cret! -e MYSQL_USER=vetdb -e MYSQL_DATABASE=vetpass -e MYSQL_PASSWORD=password -p 3306:3306 -p 8082:8080 mariadb:10.4.4

podman run -dt --rm --pod db --name adminer adminer:standalone
podman run -dt --rm --pod db --name adminer adminer:4.8.1-standalone

podman run --link some_database:db -p 8080:8080 adminer
podman run --link some_database:db -p 8080:8080 -e ADMINER_PLUGINS='tables-filter tinymce' adminer

uvicorn main:app --reload


