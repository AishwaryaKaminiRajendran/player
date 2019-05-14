a=int(input())
s=bin(a)
c=0
for i in range(0,len(s)):
    if s[i]=="1":
        c=c+1
print(c)
