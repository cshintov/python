"""

Code example from Think Python, by Allen B. Downey.
Available from http://thinkpython.com

Copyright 2012 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

"""

class Time(object):
    """Represents the time of day.
       
    attributes: seconds(seconds since midnight) 
    """
    def __init__(self, hour=0, minute=0, second=0):
        if is_valid(hour,minute,second):
            minutes = hour * 60 + minute
            seconds = minutes * 60 + second
            self.seconds = seconds
        else :
            raise ValueError('Given time is Invalid')

    def __str__(self):
        return '%.2d:%.2d:%.2d' % self.time_to_tuple ()

    def print_time(self):
        print str(self)
    
    def time_to_tuple(self):
        """converts a time object to a tuple of hours,minutes,seconds."""
        minutes, second = divmod(self.seconds, 60)
        hour, minute = divmod(minutes, 60)
        return hour,minute,second
    
    def is_after(self, other):
        """Returns True if t1 is after t2; false otherwise."""
        return self.seconds > other.seconds

    def __add__(self, other):
        """Adds two Time objects or a Time object and a number.

        other: Time object or number of seconds
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)

    def add_time(self, other):
        """Adds two time objects."""
        seconds = self.seconds + other.seconds
        return int_to_time(seconds)

    def increment(self, seconds):
        """Returns a new Time that is the sum of this time and seconds."""
        seconds += self.seconds
        return int_to_time(seconds)

def int_to_time(seconds):
    '''converts the seconds since midnight to a time object'''
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    time = Time(hour,minute,second)
    return time

def is_valid(hour,minute,second):
    """Checks whether a Time object satisfies the invariants.
        checked at the time of creation  of the time object"""
    if hour < 0 or minute < 0 or second < 0:
        return False
    if minute >= 60 or second >= 60:
        return False
    return True

def main():
    start = Time(9, 45, 00)
    start.print_time()
    
    end = start.increment(1337)
    end.print_time()
    
    print 'Is end after start?',
    print end.is_after(start)

    print 'Using __str__'
    print start, end
    
    start = Time(9, 45)
    duration = Time(1, 35)
    print start + duration
    print start + 1337
    print 1337 + start
    
    print 'Example of polymorphism'
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print total
    

if __name__ == '__main__':
    main()
