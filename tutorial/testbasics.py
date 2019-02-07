import random
import time
import math
import os

#inp = raw_input()

print time.localtime(time.time())
def s():
    return time.asctime(time.localtime(time.time()))
print s()

x = random.randint(0,100)
print x
print math.sqrt(x)

dict1 = dict()

dict1['red'] = '1'
dict1['blue']= '2'

textfile = open('test.txt')
text = textfile.readlines()

print text[5]

for i in range(1,5):
    print i

for x in 'shana'[::-1]:
    print x

textfile.close()

textfile2 = open('test.txt', 'a')
textfile2.write('test')
textfile2.writelines('test2\n')
textfile2.close()

textfile3 = open('test2.txt', 'w')
textfile3.writelines('check this out')
textfile3.close()

a = 9999999999999999999999999999999999
b = 2

while a > b:
    a = math.sqrt(a)
    print a

def
