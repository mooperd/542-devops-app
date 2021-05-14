QUERY="CREATE DATABASE $MYSQL_SCHEMA;"

env

# Create Database
mysql --host=$MYSQL_HOST --user=$MYSQL_USER --password=$MYSQL_PWD -e "$QUERY"

# Run application
gunicorn -b 0.0.0.0:8080 --access-logfile - wsgi:app

