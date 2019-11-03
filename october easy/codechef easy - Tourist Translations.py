x,l1=input().split()
x=int(x)
l0="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
l1=l1+l1.upper()
while(x):
    a=input()
    z=0
    while(z<len(a)):
        if(a[z]=="_"):
            print(" ",end="")
        elif(l0.find(a[z])>-1):
            print(l1[l0.find(a[z])],end="")
        else:
            print(a[z],end="")
        z+=1
    print()
    x-=1
