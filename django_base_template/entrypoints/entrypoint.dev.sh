#!/bin/sh
python manage.py makemigrations user_manager --no-input
python manage.py migrate user_manager --no-input
python manage.py collectstatic --no-input
python manage.py shell -c "from django.contrib.auth import get_user_model;User = get_user_model();  User.objects.filter(username='$DJANGO_USR_PWD').exists() or User.objects.create_superuser('$DJANGO_USR_PWD', '$DJANGO_ADMIN_EMAIL', '$DJANGO_USR_PWD')"
exec "$@" 