n=input()
c=0
for i in range(0,len(n)):
    if n[i]=="1" or n[i]=="2" or n[i]=="3" or n[i]=="4" or n[i]=="5" or n[i]=="6" or n[i]=="7" or n[i]=="8" or n[i]=="9" or n[i]=="A" or n[i]=="B" or n[i]=="C" or n[i]=="D" or n[i]=="E" or n[i]=="F":
        c=c+1
if c==len(n):
    print("yes")
else:
    print("no")
