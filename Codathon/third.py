n=int(input())
l=[]
found=0
for i in range(n):
    a=int(input())
    l.append(a)
m=int(input())
for i in range(n):
    if(l[i]==m):
        found=i
        break
if(found>=0):
    print(found)
else:
    print(-1)

