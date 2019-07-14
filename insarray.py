n,k=map(int,input().split())
blank=input()
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
Y=[]
for i in range(len(arr2)):
    arr1.append(arr2[i])
    Y.append(max(arr1))
print(*Y,sep=" ")
