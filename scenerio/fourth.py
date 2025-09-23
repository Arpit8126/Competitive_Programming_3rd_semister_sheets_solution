n=int(input())
count=0
for i in range(n):
    l=list(map(int,input().split()))
    if(l[0]>=75 and l[1]>=80):
        count+=1
print(count)
