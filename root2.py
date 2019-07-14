u=int(input())
for i in range(1,u):
    if(2**i==u):
        print("yes")
        break
else:
    print("no")
