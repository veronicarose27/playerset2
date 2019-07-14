import math
count=0
n,k,=map(int,input().split())
for j in range(0,k):    
    for i in range(n,k+1):
        if(math.sqrt(i)==j):
            count=count+1
print(count)
