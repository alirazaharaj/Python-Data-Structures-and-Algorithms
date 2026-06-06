que=[]

# First in first out 
que.insert(0,1)
que.insert(0,2)
que.insert(0,3)
que.insert(0,4)
que.insert(0,5)

print(que.pop())   #1
print(que.pop())   #2
print(que.pop())   #3
print(que.pop())   #4
print(que.pop())   #5
# print(que.pop())   #IndexError: pop from empty list



# Two sided que jis ma ham dono sides sa value enter kar sakta  ha 
from collections import deque
que =deque()

que.appendleft(5)
que.appendleft(6)
que.appendleft(7)

print(que.pop())


import time
import os
from collections import deque
que =deque() 

name=input('Enter name: ')
order=input('Enter order: ')
print('========================= Your order place sucessfully =========================')
order1=[name,order]
que.appendleft(order1)
time.sleep(2)

serve=que.pop()

print(f'Mr.{serve[0]} you order {serve[1]}.\n========================= Thanks =========================')


que1=deque()

for i in range(0,11):
    que1.appendleft(bin(i)[2:])

for i in range(0,11):
    print(que1.pop())
