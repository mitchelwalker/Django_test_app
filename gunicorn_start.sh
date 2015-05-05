#!/bin/bash

NAME="kcoa"                              #Name of the application (*)
DJANGODIR=/home/dev/public_html/devjango/kcoa             # Django project directory (*)
SOCKFILE=/var/www/gunicorn.sock        # we will communicate using this unix socket (*)
USER=dev                                        # the user to run as (*)
GROUP=nobody                                     # the group to run as (*)
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn (*)
DJANGO_SETTINGS_MODULE=kcoa.settings             # which settings file should Django use (*)
DJANGO_WSGI_MODULE=kcoa.wsgi                     # WSGI module name (*)

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /var/www/test/venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /home/dev/public_html/devjango/kcoa/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user $USER \
  --bind=unix:$SOCKFILE
