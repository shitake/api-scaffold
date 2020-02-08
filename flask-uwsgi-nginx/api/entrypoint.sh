#!/bin/bash
/usr/sbin/nginx -g 'daemon off;' &
uwsgi --ini /home/api/api.ini
