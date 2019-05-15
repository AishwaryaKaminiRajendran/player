a,b=map(int,input().split())
c=a|b
d=bin(c)
e=0
for i in range(0,len(d)):
    if d[i]=="1":
        e=e+1
print(e)
