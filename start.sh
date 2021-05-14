QUERY="CREATE DATABASE $MYSQL_SCHEMA;"

# Create Database
mysql --host $MYSQL_HOST --user $MYSQL_USER -p $MYSQL_PWD -e "$QUERY"

# Run application
gunicorn -b 0.0.0.0:8080 --access-logfile - wsgi:app

