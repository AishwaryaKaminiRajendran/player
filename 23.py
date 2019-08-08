n,k=map(int,input().split())
x=[int(n) for n in input().split() ]
b=[int(k) for k in input().split() ]  
for i in range(0,len(b)):
    x.append(b[i])
    print(max(x),end=" ")
