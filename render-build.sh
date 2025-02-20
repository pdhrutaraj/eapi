#!/bin/bash

echo "Running Migrations..."
python manage.py migrate

echo "Creating Superuser (if not exists)..."
python manage.py create_superuser

echo "Collecting Static Files..."
python manage.py collectstatic --noinput

