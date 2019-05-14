s=input()
c=0

for i in range(0,len(s)):
    if s[i]=="a" or s[i]=="b":
        c=c+1
if c==len(s):
    print("yes")
else:
    a=0
    for i in range(0,len(s)):
        if s[i]!="a" and s[i]!="b":
            a=a+1

if a==1:
    print("yes")
else:
    print("no")
