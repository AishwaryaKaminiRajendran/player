n,k=map(int,input().split())
a=[]
a.append(n)
a.append(k)
b=max(a)
c=[]
for i in range(1,b+1):
    if n%i==0:
        if k%i==0:
            c.append(i)
print(max(c))
