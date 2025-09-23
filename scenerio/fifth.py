n=int(input())
l=[]
count=0
for i in range(n):
    a=int(input())
    l.append(a)
target=int(input())
for i in range(n):
    for j in range(i+1,n):
        if(l[i]+l[j]==target):
            count+=1
print(count)
    
