```py
cron = Schedulling()  
cron.addJob( function, JobName , *args, **kwargs ).every(5).seconds.monday
cron.addJob( function, JobName , *args, **kwargs ).every(8).minutes
cron.addJob( function, JobName , *args, **kwargs ).every().monday.at('10:30')


cron.startDaemon()
```