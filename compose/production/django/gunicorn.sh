#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

python /app/manage.py migrate

/usr/local/bin/gunicorn guia.wsgi -w 4 -b 0.0.0.0:5000 --chdir=/app \
    --error-logfile=- \
    --access-logfile=- \
    --log-level info
