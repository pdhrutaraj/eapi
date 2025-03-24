import os
from django.contrib.auth import get_user_model

User = get_user_model()

username = os.environ.get('DJANGO_SUPERUSER_USERNAME','admin')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL','pdhrutaraj@gmail.com')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD','admin')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print('Superuser created successfully!')
else:
    print('Superuser already exists.')
