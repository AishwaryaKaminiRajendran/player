n=int(input())
a=[int(n) for n in input().split()]
b=[int(n) for n in input().split()]
#print(a,b)
c=b[::-1]
s=0
for i in range(0,len(a)):
    for j in range(0,len(c)):
        if a[i]==c[j]:
            s=s+1
if s==n:
    print("yes")
else:
    print("no")
