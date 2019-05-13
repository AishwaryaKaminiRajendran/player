str1=input().split()
print(str1)
for i in range(0,len(str1)):
    #print(len(str1[i]))
    for j in range (0,len(str1)):
        if len(str1[i])==len(str1[j]):
            print(str1[i],end=" ")
        elif len(str1[i])>len(str1[j]):
            print(str1[i],end=" ")
            
        else:
            print(str1[j],end=" ")
        # TODO: write code... range(1,len(str1)):
        
        
