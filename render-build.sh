#!/bin/bash

echo "Running Migrations..."
python manage.py migrate

echo "Creating Superuser (if not exists)..."
python manage.py createsuperuser

echo "Collecting Static Files..."
python manage.py collectstatic --noinput

