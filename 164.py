n,k=map(int,input().split())
a=[int(n) for n in input().split()]
b=[]
for i in range(0,len(a)):
    if a[i]==k:
        print(k)
        break
else:
    for j in range(0,len(a)):
        if a[j]<k:
            b.append(a[j])
    print(max(b))
