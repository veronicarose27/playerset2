p,q=map(int,input().split())
p1=list(map(int,input().split()))
q1=list(map(int,input().split()))
k1=[]
y1=[]
for i in range(0,q):
    k1.append(q1[i])
    y1.append(max(k1))
print(*y1)
