# stack ka ander first in last oput use hota h 
s=[]
s.append(1)
s.append(2)
s.append(3)
s.append(4)

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())


from collections import deque
stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)




print(stack)           #deque([1, 2, 3, 4])
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack)           #deque([])
