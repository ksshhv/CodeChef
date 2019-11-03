x=int(input())
def pretty(x):
    r=0
    r=(x//10)
    x-=r*10
    r*=3
    if(x>1):
        r+=1
    if(x>2):
        r+=1
    if(x>8):
        r+=1
    return r
while(x):
    a,b=map(int,input().split())
    print(pretty(b)-pretty(a-1))
    x-=1
