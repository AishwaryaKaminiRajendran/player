a,b=map(int,input().split())
c=0
for i in range(a,b+1):
    for j in range(1,b+1):
        if j**2==i:
            c=c+1
print(c)
