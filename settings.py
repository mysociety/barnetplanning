import os
import sys

package_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)))
paths = (
    os.path.normpath(package_dir + "/pylib"),
    os.path.normpath(package_dir + "/commonlib/pylib"),
    os.path.normpath(package_dir + "/commonlib/pylib/djangoapps"),
)
for path in paths:
    if path not in sys.path:
        sys.path.append(path)

import mysociety.config
mysociety.config.set_file(os.path.abspath(package_dir + "/conf/general"))

# Django settings for planning project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SERVER_EMAIL = mysociety.config.get('BUGS_EMAIL')
ADMINS = (
    ('mySociety bugs', mysociety.config.get('BUGS_EMAIL')),
)
DEFAULT_FROM_EMAIL = 'Barnet Planning Alerts <%s>' % mysociety.config.get('FROM_EMAIL')

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': mysociety.config.get('BARNETPLANNING_DB_NAME'),            # Or path to database file if using sqlite3.
        'USER': mysociety.config.get('BARNETPLANNING_DB_USER'),           # Not used with sqlite3.
        'PASSWORD': mysociety.config.get('BARNETPLANNING_DB_PASS'),         # Not used with sqlite3.
        'HOST': mysociety.config.get('BARNETPLANNING_DB_HOST'),             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': mysociety.config.get('BARNETPLANNING_DB_PORT')              # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = mysociety.config.get('DJANGO_SECRET_KEY')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'barnetplanning.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    package_dir + '/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.gis',
    'emailconfirmation',
    'applications',
    'alerts',
    'static_texts',
    'south',
)
