
CELERY_IMPORTS = ("tasks", )

CELERY_RESULT_BACKEND = "redis"
CELERY_REDIS_HOST = "10.35.14.80"
CELERY_REDIS_PORT = 6379
CELERY_REDIS_DB = 9

BROKER_URL = "redis://%s:%s/%s" % (CELERY_REDIS_HOST, CELERY_REDIS_PORT,
                                   CELERY_REDIS_DB)