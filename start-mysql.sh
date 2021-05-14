# start.sh


source /home/andrew/flask-sailnavsim/myenv/bin/activate
# rm /home/andrew/flask-sailnavsim/sailnavsim_web/meow.db

psql -d postgres <<EOF
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE datname = 'sailnavsim-dev';
DROP DATABASE "sailnavsim-dev";
EOF

psql -d postgres <<EOF
CREATE DATABASE "sailnavsim-dev"
WITH OWNER = sailnavsim
ENCODING = 'UTF8'
LC_COLLATE = 'C.UTF-8'
LC_CTYPE = 'C.UTF-8'
TABLESPACE = pg_default
CONNECTION LIMIT = -1;
EOF

export SECRET_KEY=meow
# export SQLALCHEMY_DATABASE_URI="sqlite:///meow.db"
export SQLALCHEMY_DATABASE_URI="postgresql://sailnavsim:sailnavsim@localhost/sailnavsim-dev"
export FLASK_APP=wsgi.py
export FLASK_DEBUG=1
export APP_CONFIG_FILE=config.py
flask run --host=0.0.0.0

