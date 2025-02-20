web: gunicorn eapi.wsgi --log-file -
release: python manage.py migrate && python manage.py createsuperuser_auto

