n=int(input())
l=[]
max=0
for i in range(n):
    a=int(input())
    l.append(a)
for a in l:
    if(a>max):
        max=a
print(max)
