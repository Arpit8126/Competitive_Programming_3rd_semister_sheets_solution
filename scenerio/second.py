employee_id=[]
elements=int(input())
count=0
for i in range(elements):
    id=int(input())
    employee_id.append(id)
for i in employee_id:
    if(i%2==0):
        print(i,end=" ")
        count+=1
if(count==0):
    print("-1")



