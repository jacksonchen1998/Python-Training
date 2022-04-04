list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
list3 = sorted(list1, reverse=True)
list4 = sorted(list1, key=len)

print(list1) # original
print(list2) # create a sorted list
print(list3) # create a reversed sorted list
print(list4) # sort list by list's length
list1.sort()
print(list1) # sort original list

'''
Fib number
'''

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a # save memory, output once a time

def main():
    num = int(input('number in fib : '))
    for val in fib(num):
        print(val)

if __name__ == '__main__':
    main()

'''
tuple vs list

tuple is immutable, and it's faster than list 
'''
import time
start1 = time.time()
t = ['骆昊', 38, True, '四川成都']
print(t, type(t))
print("--- %s seconds ---" % (time.time() - start1))
start2 = time.time()
t_tuple = tuple(t) # tuple can't be change
print(t_tuple, type(t_tuple))
print("--- %s seconds ---" % (time.time() - start2))

'''
Learn set (集合)
'''

set1 = {1, 2, 3}
print(set1)
print("Length : %d" % len(set1))
set2 = set(range(1, 10))
set3 = set((6, 6, 6))
print(set2, set3)
set4 = {num for num in range(1, 100) if num % 5 == 0 and num % 3 == 0}
print(sorted(set4))

print(set2 >= set1) # 比較長度

'''
Dictionary
'''

cost = {'apple' : 100, 'banana' : 66, 'cake' : 101}
print(cost)
item = dict(one = "book", two = "cat", three = "red")
print(item)
cost.update(door = 87)
print(cost.pop('apple', 100))
print(cost)
cost.clear()
print(cost)