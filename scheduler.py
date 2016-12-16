'''
    Created by: Cristian Steib
    date: 16/12/16
    
'''

import threading
import time


class Time():
    '''
      clase para establecer el timer de cada job
    '''

    def __init__(self):
        self.lapse = 0

    def set_lapse(self, time):
        self.lapse = time

    def get_lapse(self):
        return self.time

    lapse = property(get_lapse, set_lapse)


class JobThread(threading.Thread):
    def __init__(self, function, *args, **kwargs):
        threading.Thread.__init__(self)

        self.function = function

    def run(self):
        self.function()


class Job():
    def __init__(self, name='Job'):
        self.name = name
        self.time = Time()

    def job(self, function, *args, **kwargs):
        self.job = JobThread(function, args, **kwargs)

    def start(self):
        self.job.start()

    def isAlive(self):
        return self.job.isAlive()

    def every(self, time=1):
        return self.time

    def __str__(self):
        return str(self.name)


class Scheduler():
    def __init__(self):
        pass


class Schedule():
    ''' Clase para programar el scheduler, es una abstraccion para el usuario

    '''

    def __init__(self):
        self.jobs = []

    def addJob(self, function, name='Job1', *args, **kwargs):
        job = Job(name=name)
        job.job(function, args, kwargs)
        self.jobs.append(job)

    def get_jobs(self):
        return self.jobs


def daemon():
    print "Starting "
    print "Exiting "


c = Schedule()
c.addJob(daemon)

print ' exit main'
