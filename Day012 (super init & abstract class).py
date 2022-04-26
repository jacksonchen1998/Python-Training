class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('%s is playing' % self._name)

    def watch(self):
        if self._age >= 18:
            print('%s is watching movie' % self._name)
        else:
            print('%s is watching TV' % self._name)

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s is in %s grade, and is studying %s now' % (self._name, self._grade, course))

class Teacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s %sis teaching us %s' % (self._name, self._title, course))

def main():
    student = Student('Jackson', 13, 'senior')
    student.study('Math')
    student.watch()
    teacher = Teacher('James', 60, 'Professor')
    teacher.watch()

main()

# Abstract class, it can't be build.
# Only can be inherited by other class
from abc import ABCMeta, abstractmethod

class Pet(object, metaclass=ABCMeta):
    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """Make sound"""
        pass

class Dog(Pet):
    def make_voice(self):
        print('%s: Woff woff...' % self._nickname)

class Cat(Pet):
    def make_voice(self):
        print('%s: Meow meow...' % self._nickname)

def main2():
    pets = [Dog('Wealth'), Cat('Kitty'), Dog('Yellow')]
    for pet in pets:
        pet.make_voice()

main2()
