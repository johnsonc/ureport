from .base import *

try:
    # attempt to load local settings, if they exist
    from .local import *
except:
    pass

DEBUG = TEMPLATE_DEBUG = True

GEOSERVER_URL = ''
