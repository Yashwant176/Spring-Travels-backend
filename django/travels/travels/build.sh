#!/bin/sh
set -o errexit

pwd
ls -l

pip install -r django/travels/requirements.txt

python django/travels/manage.py collectstatic --no-input
python django/travels/manage.py migrate
