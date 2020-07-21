#!/bin/bash
docker start web-app
docker exec -it web-app /bin/bash -c ' chown -R www-data  /var/www/html/flag/'