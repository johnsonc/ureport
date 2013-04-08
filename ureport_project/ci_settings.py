from settings import *
IBM_TABLES_MANAGED = True
USE_NEW_START_POLL = True
INTERNAL_IPS = ('127.0.0.1')

GEOSERVER_URL = ""
DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME': 'local_test',
        'HOST': 'localhost',
        'USER': 'argha',
        'ROUTER_URL' : "http://95.138.170.64:13013/cgi-bin/sendsms?from=8500&username=kannel&password=kannel&text=%(text)s&to=%(recipient)s&smsc=SMPPSim"
    },
    'geoserver': {
    'ENGINE' : 'django.db.backends.postgresql_psycopg2',
    'NAME': 'geoserver',
    'HOST': 'localhost',
    'USER': 'argha',
    'ROUTER_URL':'http://95.138.170.64:13013/cgi-bin/sendsms?from=8500&username=kannel&password=kannel&text=%(text)s&to=%(recipient)s&smsc=SMPPSim'
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        }
}

INSTALLED_BACKENDS = {
    "message_tester": {
        "ENGINE": "rapidsms.backends.bucket",
    },
}

STATIC_URL="/static/media/"

# to help you get started quickly, many django/rapidsms apps are enabled
# by default. you may wish to remove some and/or add your own.
INSTALLED_APPS = [
    "ureport",
    "djtables",
    "mptt",
    "uni_form",
    "django_extensions",
    "rapidsms.contrib.handlers",

    "django.contrib.sites",
    "django.contrib.auth",
    "django.contrib.admin",
    "django.contrib.sessions",
    "django.contrib.contenttypes",
    "django.contrib.humanize",
    "django.contrib.staticfiles",

    # the rapidsms contrib apps.
    "rapidsms.contrib.default",
    "rapidsms.contrib.locations",
    "rapidsms.contrib.locations.nested",
    "geoserver",
    "rapidsms.contrib.messaging",
    "rapidsms.contrib.registration",
    "eav",
    "auth",
    "rapidsms_httprouter",
    "poll",
    "generic",
    "contact",
    "script",
    "unregister",
    "tracking",
    "uganda_common",
    "rapidsms",
    "rapidsms_xforms",
    "ussd",
    "monitor",
    "message_classifier",
    "celery",
    "djcelery",
    #"permission",
   # nothing after south
    "south",
    "debug_toolbar",
]

SMS_APPS = [
    "monitor",
    "ureport",
    "script",
    "poll",
    "unregister",
    #"rapidsms_xforms",
]
#TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
#NOSE_ARGS = [
#    '--with-coverage',
#    '--cover-package=ureport',
#    ]
#TEST_RUNNER = 'django_test_coverage.runner.run_tests'
COMPUTE_COVERAGE="ureport"

LOGGING = {
    'version' : 1,

    'handlers': {
        'command': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': './command_log'
        }
    },
    'loggers': {
        'command': {
            'level': 'DEBUG',
            'handlers': ['command']
        }
    }
}
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
        'django_log_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/Users/argha/develop/ureport/ureport_log.log',
            'formatter': 'simple',
            'backupCount': 50,
            'maxBytes': 2 ** 20,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['django_log_file'],
            'level': 'DEBUG',
            'propagate': True,
            },
     }
}