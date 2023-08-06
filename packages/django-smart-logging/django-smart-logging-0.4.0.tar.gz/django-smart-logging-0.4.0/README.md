django-smart-logging
====================

[![master](https://gitlab.com/os4d/django-logging-dbconfig/badges/master/pipeline.svg)](https://gitlab.com/os4d/django-logging-dbconfig/-/commits/master)
[![develop](https://gitlab.com/os4d/django-logging-dbconfig/badges/master/pipeline.svg)](https://gitlab.com/os4d/django-logging-dbconfig/-/commits/develop)
[![coverage](https://gitlab.com/os4d/django-logging-dbconfig/badges/develop/coverage.svg)](https://gitlab.com/os4d/django-logging-dbconfig/-/graphs/develop/charts)

Plugin for django-smart-admin that allows changing python logging configuration (level/handlers/propagate) without the need to restart the app

Configuration
-------------

SMART_LOG_INSPECT = False
SMART_LOG_HANDLERS = 2  # 1 show handlers / 2 change handlers 
SMART_LOG_MAXSIZE = 100
SMART_LOG_FORMAT = "%(levelname)s %(asctime)s %(module)s: %(message)s"
SMART_LOG_PREFIX = "smart-log"
SMART_LOG_REDIS = ""
SMART_LOG_DEBUG = False
