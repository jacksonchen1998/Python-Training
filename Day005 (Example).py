"""
Calculate which day is the date
"""
def is_leap_year(year): # 算閏年
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def which_day(year, month, date):
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date

def main():
    print(which_day(1980, 1, 1))
    print(which_day(2020, 12, 31))

main()

"""
巴斯卡三角形
"""
def triangle():
    num = int(input("Please input a number : "))
    tri = [[None]] * num # Create num * num 2D array
    for row in range(len(tri)):
        tri[row] = [None] * (row + 1) # Left side set as 1
        for col in range(len(tri[row])):
            if col == 0 or col == row:
                tri[row][col] = 1
            else:
                tri[row][col] = tri[row - 1][col] + tri[row - 1][col - 1]
            print(tri[row][col], end = '\t')
        print()

triangle()

"""
Using random module's sample to choose the number of different element
Left side sorted number of ball
Right side append random integer
"""
from random import randint, randrange, sample

def display(balls):
    for index, ball in enumerate(balls): # for loop for two variable
        if index == len(balls) - 1:
            print('|', end='')
        print('%02d' % ball, end='') # 2 位數
    print()

def random_select():
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    selected_balls = sample(red_balls, 6)
    selected_balls.sort() # sort original list
    selected_balls.append(randint(1, 16))
    return selected_balls

def main2():
    num = int(input('Choose the size of different number : '))
    for _ in range(num):
        display(random_select())

main2()
