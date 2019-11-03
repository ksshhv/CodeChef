t=int(input())
while(t):
    n=int(input())
    ls=[]
    sm=0
    while(n):
        lst=list(map(int,input().split()))
        sm+=lst[0]
        lst1=lst[1:]
        ls.append(lst)
        while(sm):
            
            sm-=1
        n-=1
    t-=1
