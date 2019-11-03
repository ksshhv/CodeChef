import math
x=int(input())
l=[0,1]
y = 2
while(y<10000000):
    l.append((l[y-1]+l[y-2])%10)
    y+=1
#print(l)
while(x):
    c=0
    t=int(input())
    z=t
    while(t>=2):
        t/=2
        c+=1
    k=int(math.pow(2,c))
    print(l[k-1])
    x-=1
