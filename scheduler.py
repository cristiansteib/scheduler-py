# coding=utf-8
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
        self.crontab = ('*', '*', '*', '*', '*')

    def set_lapse(self, time):
        self.lapse = time

    def get_lapse(self):
        return self.time

    lapse = property(get_lapse, set_lapse)

    def set_crontab(self, minute='*', hour='*', day='*', month='*', week_day='*'):
        '''
        Like linux crontab

        .--------------- minuto (0-59)
        |  .------------ hora (0-23)
        |  |  .--------- día del mes (1-31)
        |  |  |  .------ mes (1-12) o jan,feb,mar,apr,may,jun,jul... (meses en inglés)
        |  |  |  |  .--- día de la semana (0-6) (domingo=0 ó 7) o sun,mon,tue,wed,thu,fri,sat (días en inglés)
        |  |  |  |  |
        *  *  *  *  *

        '''
        week_day = str(week_day)

        days = {0: ['sun', 'dom', '0', '7'],
                1: ['mon', 'lun', '1'],
                2: ['tue', 'mar', '2'],
                3: ['wed', 'mie' '3'],
                4: ['thu', 'jue', '4'],
                5: ['fri', 'vie' '5'],
                6: ['sat', 'sab' '6'],
                }
        wk_day = False
        for key in days:
            for item in days[key]:
                if week_day == item:
                    wk_day = key
                    break
            print wk_day
            if wk_day == False:
                break

        self.set_crontab(str(minute), str(hour), str(day), str(month), str(wk_day))

    def get_crontab(self):
        return self.crontab

    crontab = property(set_crontab, get_crontab)


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

        return job

    def get_jobs(self):
        return self.jobs


def daemon():
    print "Starting "
    print "Exiting "


c = Schedule()
print c.addJob(daemon).every().lapse

print ' exit main'
