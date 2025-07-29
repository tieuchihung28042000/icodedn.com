#!/bin/bash
set -e

# Run celery
exec celery -A dmoj worker -l info 