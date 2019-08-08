a,b,c=map(str,input().split())
n=int(c)
s=0
for i in range(0,len(a)):
    if a[i]!=b[i]:
        s=s+1
if s==n:
    print("yes")
else:
    print("no")
