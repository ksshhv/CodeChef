t=int(input())
while(t):
    x=int(input())
    ft=0
    ot=0
    key=0
    while(x):
        p,q,r=map(int,input().split())
        if(p==1):
            key=0
            ft=q
            ot=r
            print("YES")
        elif(p==2):
            if(q<ft and key==0):
                ft=r
                ot=q
                print("YES")
            elif(q<ot and key==0):
                ft=q
                ot=r
                print("YES")
            elif(r<ft and key==0):
                ft=q
                ot=r
                print("YES")
            elif(r<ot and key==0):
                ft=r
                ot=q
                print("YES")
            elif(q==r):
                ft=ot=r
                print("YES")
            else:
                key=1
                ot=r
                ft=q
                print("NO")
        #print(ft,ot)
        x-=1
    t-=1
