n=int(input())
a=list(map(int,input().split()))
p=list(map(int,input().split()))
l=1
while(l<=n):
    if l in p:
        x=0
        b=[]
        while(x<n-1):
            if(p[x]==l):
                b.append(x+2)
            x+=1
        b.sort()
        y=0
        while(y<len(b)):
            print(b[y], end=" ")
            y+=1
        print()
    else:
        print("0")
    l+=1
