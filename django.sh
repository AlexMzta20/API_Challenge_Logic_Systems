#!/bin/sh

# Espera a que la base de datos esté lista antes de iniciar el servidor Django
until nc -z -v -w30 $DB_HOST $DB_PORT; do
 echo 'Waiting for PostgreSQL...'
 sleep 1
done
echo "PostgreSQL is up and running!"

# Realiza las migraciones de la base de datos
python manage.py makemigrations api
python manage.py migrate

# Inicia el servidor Django
exec "$@"