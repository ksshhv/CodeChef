t=int(input())
while(t):
    x,y,q=map(int,input().split())
    rows=[0]*x
    column=[0]*y
    while(q):
        a,b=map(int,input().split())
        rows[a-1]+=1
        column[b-1]+=1
        q-=1
    odd1=0
    odd2=0
    print(rows,column)
    for i in rows:
        if(i%2==1):
            odd1+=1
    for j in column:
        if(j%2==1):
            odd2+=1
    print(odd1*(y-odd2)+odd2*(x-odd1))
    t-=1
