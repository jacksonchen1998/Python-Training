class Person_slot(object):

    __slots__ = ('_name', '_age', '_gender')
    # Define Person_slot only has _name, _age, _gender

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
        if self._age <= 16:
            print('%s is playing basketball now.' % self._name)
        else:
            print('%s is swimming now.' % self._name)

def main2():
    person = Person_slot('Joe', 26)
    person.play()
    person._gender = 'Men'
    
    person._is_gay = True 
    # It will cause error, because __slots__ = ('_name', '_age', '_gender')
    # AttributeError: 'Person_slot' object has no attribute '_is_gay'

main2()

"""
Attribute's and function's access priority

Python is Dynamic programming language
, which at runtime execute many common programming behaviours that 
static programming languages perform during compilation.
"""

class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property # getter : get attribute
    def name(self):
        return self._name

    @property # getter : get attribute
    def age(self):
        return self._age

    # If don't have this part : Peter is boxing now.
    @age.setter # setter : set
    def age(self, age):
        self._age = age

    # def age(self):
    #     return self._age
    # Peter is boxing now.

    def play(self):
        if self._age <= 16:
            print('%s is playing baseball now.' % self._name)
        else:
            print('%s is boxing now.' % self._name)

def main():
    person = Person('Peter', 26)
    person.play()

    person.age = 11
    person.play()

main()