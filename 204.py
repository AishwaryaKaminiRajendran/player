n=int(input())
s=0
a=[int(n) for n in input().split()]
for i in range(0,len(a)):
    if a[i]<0:
        s=s+a[i]
print(s)
