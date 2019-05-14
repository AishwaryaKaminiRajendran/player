n,k=map(int,input().split())
b=[]

for i in range(0,n):
    a=input()
    b.append(a)
print(b)
for x in range(0,len(b)-k):
    for y in range(x+1,k):
        if b[x]==b[y]:
            c=c+1
if c==k-1:
    print("yes")
else:
    print("no")
