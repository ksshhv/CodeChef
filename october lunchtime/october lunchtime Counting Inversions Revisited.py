t=int(input())
while(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l1=[]
    l2=[]
    for i in l:
        s=0
        count=0
        while(s<n):
            if(l[s]<i):
                count+=1
            s+=1
        l1.append(count)
    summ=0
    for i in l1:
        summ+=i
    fsum=0
    fsum+=summ*(k*(k-1))//2
    m=0
    while(m<n):
        count=0
        s=m
        while(s<n):
            if(l[s]<l[m]):
                count+=1
            s+=1
        l2.append(count)
        m+=1
    summm=0
    for i in l2:
        summm+=i
    fsum+=summm*k
    #print(l2)
    print(fsum)
    t-=1
