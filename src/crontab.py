# coding=utf-8
'''
    Created by: Cristian Steib
    date: 16/12/16
    
'''
import datetime


class Time():
    '''
      clase para establecer el timer de cada job
    '''

    def __init__(self):
        self.lapse = '0'
        self._minute = '*'
        self._hour = '*'
        self._day = '*'
        self._month = '*'
        self._week_day = '*'
        self._crontab = (self._minute, self._hour, self._day, self._month, self._week_day)

    def set_lapse(self, time='0'):
        self.lapse = str(time)
        return self

    def get_lapse(self):
        return self.lapse

    def set_crontab(self, minute='*', hour='*', day='*', month='*', week_day='*'):
        '''
        Like linux crontab

        .--------------- minuto (0-59)
        |  .------------ hora (0-23)
        |  |  .--------- día del mes (1-31)
        |  |  |  .------ mes (1-12) o jan,feb,mar,apr,may,jun,jul... (meses en inglés)
        |  |  |  |  .--- día de la semana (0-6) (domingo=0 ó 7) o sun,mon,tue,wed,thu,fri,sat (días en inglés y español)
        |  |  |  |  |
        *  *  *  *  *

        '''

        self._minute = minute if minute != '*' else self._minute
        self._hour = hour if hour != '*' else self._hour
        self._day = day if day != '*' else self._day
        self._month = month if month != '*' else self._month
        self._week_day = week_day if week_day != '*' else self._week_day

        if week_day != '*':
            week_day = str(week_day)
            days = {
                0: ['mon', 'lun', '1'],
                1: ['tue', 'mar', '2'],
                2: ['wed', 'mie' '3'],
                3: ['thu', 'jue', '4'],
                4: ['fri', 'vie' '5'],
                5: ['sat', 'sab' '6'],
                6: ['sun', 'dom', '0', '7'],
                    }

            wk_day = False
            for key in days:
                for item in days[key]:
                    if week_day == item:
                        self._week_day = key
                        break
                if wk_day != False:
                    break

        self._crontab = (str(self._minute), str(self._hour), str(self._day), str(self._month), str(self._week_day))

    def get_crontab(self):
        return self._crontab

    crontab = property(set_crontab, get_crontab)

    def __isFraction(self, value):
        '''es una fraccion del tiempo'''
        if str(value).count('/'):
            return True
        else:
            return False

    def __isPortion(self, value):
        if str(value).count('.'):
            return True
        else:
            return False

    def time_next(self, start):

        def relative_weekday(wday):
            relative_day = (wday - datetime.datetime.now().weekday())
            relative_day = 7 + relative_day if relative_day < 0 else relative_day
            return relative_day


        absolute = [datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day,
                    datetime.datetime.now().hour, datetime.datetime.now().minute, datetime.datetime.now().second]
        adder = [0, 0, 0, 0, 0, 0, 0]
        # days - seconds - microse - milli - minutes - hours - weeks


        if self.__isFraction(self._minute):
            if self.__isPortion(self._minute):
                adder[1] = int(self._minute[self._minute.index('.') + 1:])
            else:
                adder[4] = int(self._minute[self._minute.index('/') + 1:])
        elif not self._minute == '*':
            absolute[4] = int(self._minute)

        if self.__isFraction(self._hour):
            adder[5] = int(self._hour[self._hour.index('/') + 1:])
        elif not self._hour == '*':
            absolute[3] = int(self._hour)

        if self.__isFraction(self._day):
            adder[0] = int(self._day[self._day.index('/') + 1:])
        elif not self._day == '*':
            absolute[2] = int(self._day)

        if not self._week_day == '*':
            adder[0] = relative_weekday(self._week_day)

        if not self._month == '*':
            absolute[1] = int(self._month)

        future = datetime.datetime(*absolute) + datetime.timedelta(*adder)
        print future
        return future




    @property
    def monday(self):
        self.set_crontab(week_day='mon')
        return self

    @property
    def tuesday(self):
        self.set_crontab(week_day='tue')
        return self

    @property
    def wednesday(self):
        self.set_crontab(week_day='wed')
        return self

    @property
    def monday(self):
        self.set_crontab(week_day='mon')
        return self

    @property
    def thurday(self):
        self.set_crontab(week_day='thu')
        return self

    @property
    def friday(self):
        self.set_crontab(week_day='fri')
        return self

    @property
    def saturday(self):
        self.set_crontab(week_day='sat')
        return self

    @property
    def sunday(self):
        self.set_crontab(week_day='sun')
        return self

    @property
    def seconds(self):
        self.set_crontab(minute='*/0.' + self.lapse)
        return self

    @property
    def minutes(self):
        self.set_crontab(minute='*/' + self.lapse)
        return self

    @property
    def hours(self):
        self.set_crontab(minute='*/' + self.lapse)
        return self

    def day(self):
        pass

    def at(self, time="00:00"):
        time = time.split(':')
        self.set_crontab(hour=time[0], minute=time[1])
