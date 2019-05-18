n,k=map(int,input().split())
a=[int(n) for n in input().split()]
for i in range(0,len(a)):
    if a[i]==k:
        print("yes")
        break
else:
    print("no")
