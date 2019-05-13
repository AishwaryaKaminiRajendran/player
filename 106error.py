a=int(input())
b=[int(a) for a in input().split()]
#c=sorted(b)
#print(c)
c=[]
for i in range (0,len(b)-1):
    for j in range(1,len(b)-1):
        if b[i]==b[j]:
            c.append(b[i])
            del(b[i])
        else:
            c.append(b[i])
for k in c:
    print(k,end=" ")
            
