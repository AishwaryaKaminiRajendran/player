n=int(input())
b=[]
c=0
for i in range(0,n):
    a=input()
    b.append(a)

for x in range(0,len(b)-1):
    y=x+1
    if b[x]==b[y]:
       c=c+1
if c>=1:
    print("yes")
else:
    print("no")
