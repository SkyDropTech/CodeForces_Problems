t=int(input())
for _ in range(t):
    a,b,k=map(int,input().split())
    count=1 
    suum=a-b 
    while k==count:
        suum+=a 
        count+=1
        if k!=count:
            suum-=b 
            count+=1 