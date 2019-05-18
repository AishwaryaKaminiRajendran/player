s=input()
c=0
d=0
for i in range(0,len(s)):
    if s[i]!=" ":
        c=c+1
for j in range(2,c):
    if c%j==0:
        d=d+1
if d==0:
    print("yes")
else:
    print("no")
