t=int(input())
for i in range(t):
    n = int(input())
    if (n==1):
        print(0)
        continue
    if (n==2):
        print(1)
        continue
    if (n%2==0):
        print(2)
        continue
    else:
        if (n==3):
            print(2)
        else:
            print(3)
    
