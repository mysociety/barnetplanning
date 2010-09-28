#!/usr/bin/python 

import os, sys

file_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)))
for path in (os.path.normpath(file_dir + "/../.."), os.path.normpath(file_dir + "/..")):
    if path not in sys.path:
        sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'barnetplanning.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

