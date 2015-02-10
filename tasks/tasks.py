from __future__ import absolute_import

import time
from proj.celery import app


#@app.task(track_started=True)
@app.task()
def add(x, y):
    time.sleep(5)
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)


@app.task
def dump_context(self, x, y):
    print('Executing task id {0.id}, args: {0.args!r} kwargs: {0.kwargs!r}'.format(
            self.request))