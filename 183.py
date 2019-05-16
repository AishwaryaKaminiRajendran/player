n=int(input())
a=[int(n) for n in input().split()]
b=[]
c=[]
for i in range(0,len(a)):
    if a[i]==0:
        b.append(a[i])
    else:
        c.append(a[i])
d=c+b
for j in range(0,len(d)):
    print(d[j],end=" ")
