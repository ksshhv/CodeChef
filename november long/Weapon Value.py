# cook your dish here
def xorng(a,b):
    s=""
    j=0
    while(j<10):
        s+=str(int(a[j])^int(b[j]))
        j+=1
    return s
t=int(input())
while(t):
    lst=[]
    n=int(input())
    m=n
    while(m):
        lst.append(input())
        m-=1
    k="0000000000"
    l=0
    #print(x)
    while(l<n):
        k=xorng(k,(lst[l]))
        #print(k)
        l+=1
    print(k.count("1"))
    t-=1
