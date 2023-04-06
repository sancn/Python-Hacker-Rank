from collections import deque
choice=int(input("How many operations you want to  perform:"))
d=deque()
for i in range(choice):
    d.append(1)
    d.append(2)
    d.append(3)
    d.appendleft(4)
    d.pop()
    d.popleft()
print(d)
    
