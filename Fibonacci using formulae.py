# cook your dish here
import math
x=int(input())
l=[0,1]
y = 2
while(y<120):
    l.append((l[y-1]+l[y-2])%10)
    y+=1
#print(l)
while(x>0):
    t=int(input())
    s=round(math.log(t,2))
    k=int(math.pow(2,s))
    print(l[(k-1)%60])
    x-=1
