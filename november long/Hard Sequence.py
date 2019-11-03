lst=[0,0,1,0,2,0,2,2,1,6,0,5,0,2,6,5]
r=16
while(r<128):
    x=lst[r-1]
    if (x in lst[:(r-1)]):
        y= max(idx for idx, val in enumerate(lst[:r-1])  
                                    if val == lst[r-1])
        lst.append(r-1-y)
    else:
        lst.append(0)
    r+=1
#print(lst)
t=int(input())
while(t):
    n=int(input())
    print(lst[:n].count(lst[n-1]))
    t-=1
