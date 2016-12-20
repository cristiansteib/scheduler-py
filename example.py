'''
    Created by: Cristian Steib
    date: 20/12/16
    
'''
from src.scheduler import Schedulling


def job(*args):
    print 'this is = ' + str(args[0])
    print "Starting "
    print "Exiting "
    print''


c = Schedulling()

c.addJob(job, 'Job1', 'j1').every(5).seconds.monday

c.addJob(job, 'Job2', 'j2').every(3).seconds.monday

c.addJob(job, 'Job3', 'j3').every(4).seconds.monday

c.startDaemon()

print 'exit main'
