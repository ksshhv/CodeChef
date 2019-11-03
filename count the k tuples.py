import math
x=int(input())
while(x):
    a,b=input().split()
    a=int(a)
    b=int(b)
    if(a<b):
        print(b)
    if(a==b):
        print(b+math.factorial(a))
    if(a>b):
        print(b+math.factorial(a)//math.factorial(a-b+1))
    x-=1
