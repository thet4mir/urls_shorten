from .base import * # noqa


SECRET_KEY = 'django-insecure-_-o9$&(-tfizn!&=i8j20kc#_l3o&%v4t0)igcktnbz&!pz$wm'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']
SITE_ID = 1

DATABASES = {
    'default': {
        'ENGINE'   : 'django.db.backends.mysql',
        'NAME'     : 'urls',
        'USER'     : 'root',
        'PASSWORD' : 'toor',
        'HOST'     : 'localhost',
        'PORT'     : 3306,
        'OPTIONS' : {
            # 'init_command' : "SET sql_mode='STRICT_TRANS_TABLES'",
        },
        'TEST': {
            'NAME': ':memory',
            'ENGINE': 'django.db.backends.sqlite3',
            'CHARSET': 'UTF8',
        },
        'ATOMIC_REQUESTS': True,
    }
}
