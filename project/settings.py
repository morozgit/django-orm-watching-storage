import os
from dotenv import load_dotenv, find_dotenv
from environs import Env

# load_dotenv(find_dotenv())
# language_code = os.environ.get("LANGUAGE_CODE")
# time_zone = os.environ.get("TIME_ZONE")
# secret_key = os.environ.get("SECRET_KEY")
# host = os.environ.get("HOST")
# password = os.environ.get("PASSWORD")
env = Env()
env.read_env()
HOST = env.str("HOST")
PASSWORD = env.str("PASSWORD")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': HOST,
        'PORT': '5434',
        'NAME': 'checkpoint',
        'USER': 'guard',
        'PASSWORD': PASSWORD,
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool('DEBUG')

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = env.str("LANGUAGE_CODE")

TIME_ZONE = env.str("TIME_ZONE")

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

