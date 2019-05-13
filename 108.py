n=int(input())
a=[int(n) for n in input().split()]
f=0
for i in range(0,len(a)):
    f=f+a[i]
    print(f,end=" ")
    
