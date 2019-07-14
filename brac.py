u=(input())
counto=0
countc=0
for i in u:
    if(i=='('):
        counto=counto+1
    else:
        countc=countc+1
if(counto==countc):
    print("yes")
else:
    print("no")
