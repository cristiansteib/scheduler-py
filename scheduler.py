# coding=utf-8
'''
    Created by: Cristian Steib
    date: 16/12/16
    
'''

import threading
import time
from crontab import Time
import datetime

class JobThread(threading.Thread):
    def __init__(self, function, *args, **kwargs):
        self.a = args
        self.k = kwargs
        threading.Thread.__init__(self)
        self.function = function

    def run(self):
        self.function(*self.a, **self.k)


class Job():
    def __init__(self, name='Job'):
        self.name = name
        self.time = Time()
        self.lastrun = None
        self.nextrun = None

    def last_run(self, time):
        self.lastrun = time

    def get_last_run(self):
        return self.lastrun

    def next_run(self, time):
        self.nextrun = time

    def job(self, function, *args, **kwargs):
        self.job = JobThread(function, *args, **kwargs)

    def start(self):
        self.lastrun = datetime.datetime.time(datetime.datetime.now())
        self.nextrun = self.time.time_next(self.lastrun)

        print self.nextrun
        self.job.start()

    def isAlive(self):
        return self.job.isAlive()

    def every(self, time=1):
        return self.time.set_lapse(time)

    def cron(self):
        return self.time




    def __str__(self):
        return self.name


class Scheduler():
    ''' esta clase corre las funciones del schedullign'''

    def __init__(self, instance_schedulling):
        self.schedulling = instance_schedulling
        job_scheduler = JobThread(self.scheduler)
        job_scheduler.start()

    def scheduler(self):
        ''' funcion que se encarga de ejecutar cada job en su momento '''
        start_at = datetime.datetime.time(datetime.datetime.now())

        print self.schedulling.jobs[0].start()

        # while True:
        #    time.sleep(1)


class Schedulling():
    ''' Clase para programar el scheduler, es una abstraccion para el usuario

    '''

    def __init__(self):
        self.jobs = []

    def addJob(self, function, name='Job', *args, **kwargs):
        job = Job(name=name)
        job.job(function, *args, **kwargs)
        self.jobs.append(job)
        return job

    def startDaemon(self):
        scheduler = Scheduler(self)

    def get_jobs(self):
        return self.jobs

    def __str__(self):
        names = []
        for j in self.jobs:
            names.append(str(j))
        return str(names)


def daemon():
    print 'daemo'
    print "Starting "
    print "Exiting "


c = Schedulling()

c.addJob(daemon, 'primero').every(20).seconds.monday
print c.get_jobs()[0]
c.startDaemon()
print ' exit main'
