n,k=map(int,input().split())
a=[int(n) for n in input().split()]
b=[]
for j in range(0,len(a)):
    if a[j]>k:
        b.append(a[j])
print(min(b))
