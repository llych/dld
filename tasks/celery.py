from __future__ import absolute_import
from celery import Celery


app = Celery('tasks', 
            broker='redis://localhost:6379/0',
            backend='redis://localhost:6379/1',
            include=['proj.tasks',]
            )

app.conf.update( 
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/1' ,
    CELERY_TASK_RESULT_EXPIRES=3600,
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],  # Ignore other content
    CELERY_RESULT_SERIALIZER='json',
    CELERY_TIMEZONE='Europe/Oslo',
    CELERY_ENABLE_UTC=True,
    CELERY_TRACK_STARTED=True,
) 



if __name__ == '__main__':
    app.worker_main()