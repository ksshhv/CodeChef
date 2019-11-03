import math
t=int(input())
while(t):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    x=0
    y=0
    for i in range(len(l)):
        if i<a and l[i]==l[b-1]:
            y+=1
        if i<b and l[i]==l[b-1]:
            x+=1
    ans=math.factorial(y)//(math.factorial(x)*math.factorial(y-x))
    #print(x)
    #print(y)
    print(int(ans))
    t-=1
