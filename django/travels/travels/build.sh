#!/bin/sh
set -o errexit

pwd
ls -l

cd ..

pwd
ls -l

python -m pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
