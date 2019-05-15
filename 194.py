p,r=map(str,input().split())
if p=="S" and r=="R":
    print("R")
elif p=="S" and r=="P":
    print("S")
elif p=="R" and r=="S":
    print("R")
elif p=="R" and r=="P":
    print("P")
elif p=="P" and r=="S":
    print("S")
elif p=="P" and r=="R":
    print("P")
elif p=="S" and r=="S":
    print("D")
elif p=="P" and r=="P":
    print("D")
elif p=="R" and p=="R":
    print("D")
