n,k=map(int,input().split())
a=[int(n) for n in input().split() ]
b=[int(k) for k in input().split() ]  
for i in range(0,len(b)):
    a.append(b[i])
    print(max(a),end=" ")
