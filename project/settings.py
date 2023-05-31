import os
from environs import Env


env = Env()
env.read_env()
DB_HOST = env.str("HOST")
DB_PASSWORD = env.str("PASSWORD")
DB_PORT = env.str("PORT")
DB_NAME = env.str("NAME")
DB_USER = env.str("DB_USER")
DB_DEBUG = env.bool('DEBUG')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': DB_HOST,
        'PORT': DB_PORT,
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'DEBUG': DB_DEBUG,
        'ALLOWED_HOSTS': ALLOWED_HOSTS
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env.str("SECRET_KEY")

ROOT_URLCONF = 'project.urls'

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

