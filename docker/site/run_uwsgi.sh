#!/bin/bash
set -e

# Ensure static directory exists
mkdir -p /app/static

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Compile translations
python manage.py compilemessages
python manage.py compilejsi18n

# Run uwsgi
exec uwsgi --ini uwsgi.ini "$@" 