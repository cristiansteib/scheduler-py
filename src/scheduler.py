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


class JobFunction():
    def __init__(self, function, *args, **kwargs):
        self.a = args
        self.k = kwargs
        self.function = function

    def start(self):
        self.function(*self.a, **self.k)


class Job():
    def __init__(self, name='Job'):
        self.name = name
        self.time = Time()
        self.lastrun = None
        self.nextrun = datetime.datetime.now()

    def last_run(self, time):
        self.lastrun = time

    def get_last_run(self):
        return self.lastrun

    def next_run(self, time):
        self.nextrun = time

    def job(self, function, *args, **kwargs):
        self.job = JobFunction(function, *args, **kwargs)

    def start(self):
        self.lastrun = datetime.datetime.now()
        self.nextrun = self.time.time_next(self.lastrun)
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

    def __init__(self, instance_schedulling):
        self.schedulling = instance_schedulling
        job_scheduler = JobThread(self.schedulerDaemon)
        job_scheduler.start()

    def schedulerDaemon(self):
        ''' funcion que se encarga de ejecutar cada job en su momento '''
        while True:
            for job in self.schedulling.jobs:
                if datetime.datetime.now() > job.nextrun:
                    job.start()
            time.sleep(0.5)




class Schedulling():
    ''' Class for programming the scheduler

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


def daemon(*args):
    print args[0]
    print "Starting "
    print "Exiting "


c = Schedulling()

c.addJob(daemon, 'primero', 'j1').every(5).seconds.monday

c.addJob(daemon, '2', 'j2').every(3).seconds.monday

c.addJob(daemon, '3', 'j3').every(4).seconds.monday

c.startDaemon()

print ' exit main'
