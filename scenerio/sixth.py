n=int(input())
l=[]
highest=0
count=0
for i in range(n):
    a=int(input())
    l.append(a)
for i in range(n):
    if(l[i]==0):
        count+=1
        if(l[i+1]==1):
            if(count>highest):
                highest=count
                count=0

print(highest)        
            
    
