#!/bin/bash

echo "Running Migrations..."
python3 manage.py migrate

echo "Creating Superuser (if not exists)..."
python3 manage.py createsuperuser



