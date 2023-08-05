from datetime import datetime


class GetTimeEasy:
    """library that makes getting time and date simply"""

    def get_time(self, classifiers=None):
        self.classifiers = classifiers
        if self.classifiers:
            if self.classifiers == 'M' or self.classifiers == 'm' or classifiers == '%m' or classifiers == '%M':
                now = datetime.now()
                self.time = now.strftime('%M')
                return self.time

            if self.classifiers == 'h' or self.classifiers == 'H' or classifiers == '%h' or classifiers == '%H':
                now = datetime.now()
                self.time = now.strftime('%H')
                return self.time

            if self.classifiers == 'S' or self.classifiers == 's' or classifiers == '%s' or classifiers == '%S':
                now = datetime.now()
                self.time = now.strftime('%S')
                return self.time
        else:
            now = datetime.now()
            self.time = now.strftime('%H:%M:%S')
            return self.time

    def get_date(self, classifiers=None):
        if classifiers:
            if classifiers == 'd' or classifiers == 'D' or classifiers == '%d' or classifiers == '%D':
                now = datetime.now()
                self.time = now.day
                return self.time

            if classifiers == 'y' or classifiers == 'Y' or classifiers == '%y' or classifiers == '%Y':
                now = datetime.now()
                self.time = now.year
                return self.time

            if classifiers == 'M' or classifiers == 'm' or classifiers == '%M' or classifiers == '%m':
                now = datetime.now()
                self.time = now.month
                return self.time
        else:
            now = datetime.now()
            self.time = now.date()
            return str(self.time).replace('-', ':')