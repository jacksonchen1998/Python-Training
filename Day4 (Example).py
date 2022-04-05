"""
Find 2 biggest number in the list
"""

def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2

list = [10, -87, 23, 1]
print(max2(list))

"""
get file name
"""

def get_filename(filename, has_dot = False):
    pos = filename.rfind('.')
    #print(pos)
    if 0 < pos < len(filename) - 1: # calculate file name's length
        index = pos if has_dot else pos + 1
        # print(pos)
        # print(index)
        return filename[index:]
    else:
        return ''

print(get_filename("apple.c", ))

"""
Initalize as 4 digits
Function will generate random code
"""

import random

def generate_code(code_len = 4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code

print(generate_code(10))

'''
marquee
'''

# import os
# import time

# def main():
#     content = "Hello World~"
#     while True:
#         os.system('cls')
#         print(content)
#         time.sleep(0.2) # Sleep 200 ms
#         content = content[1:] + content[0]

# main()