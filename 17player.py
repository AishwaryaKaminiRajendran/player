a,b=map(int,input().split())
co=0
c=[int(a) for a in input().split()]
for i in range(0,len(c)-1):
    for j in  range(1,len(c)):
        if c[i]+c[j]==b:
            co=co+1
            break
        break
if co>=1:
    print("yes")
else:
    print("no")
