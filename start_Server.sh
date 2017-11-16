#!/bin/bash
. dj2.7/bin/activate
#python ./manage.py runserver localhost:8000 >> django.log &
uwsgi --ini django.ini

