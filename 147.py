s=input().split()
if len(s)==1 or len(s)==2:
     for i in range(0,len(s)):
        print(s[i],end=" ")
else:
    print(s[0],end=" ")
    for i in range(1,len(s)-1):
        print(s[i][::-1],end=" ")
    print(s[-1])
