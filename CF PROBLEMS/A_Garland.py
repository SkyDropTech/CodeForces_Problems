t=int(input())
res=""
for _ in range(t):
    s=input() 
    lst=list(s)
    lst1=[]
    for j in range(4):
        x=lst.count(lst[j])
        lst1.append(x)
    if len(set(lst))==1:
        res+="-1\n"
    elif max(lst1)<=2:
        res+="4\n"
    else:
        res+="6\n"
print(res)
