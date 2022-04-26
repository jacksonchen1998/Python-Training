"""
Calculate distance between 2 node
"""

from math import sqrt

class Point(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def move_to(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))

def main4():
    p1 = Point(3, 5)
    p2 = Point()

    print(p1)
    print(p2)

    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))

main4()

"""
Clock function
"""

from time import sleep

class Clock(object):
    def __init__(self, hour = 0, minute = 0, second = 0):
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        self._second += 1
        if self._second == 60:
            self._minute += 1
            if self._minute == 60:
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0
                    self._minute = 0
                    self._second = 0

    def show(self):
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)

def main3():
    clock = Clock(23, 59, 58)
    while True:
        print(clock.show())
        sleep(1) # Sleep 1 second
        clock.run()

"""
Define access priority
"""

class Test:
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')

def main2():
    test = Test('hello')
    test._Test__bar() 
    # test.__bar() will cause AttributeError: 'Test' object has no attribute '__bar'
    print(test._Test__foo) 
    # test.__foo will cause AttributeError: 'Test' object has no attribute '__foo'

main2()

"""
class
"""

class Student(object):

    # __init__ is a method to initalize object
    # It create age and name, two attributes for Student object
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def study(self, course_name):
        print('%s is studying %s now' % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print("%s can't watch 18+ movie." % self.name)
        else:
            print("%s is watching movie now." % self.name)

def main():
    student_1 = Student('J', 20)
    student_1.study("Math")
    student_1.watch_movie()

    student_2 = Student('K', 12)
    student_2.study("Chinese")
    student_2.watch_movie()

main()

main3()
