list=[]
n=int(input("Enter the number of elements : "))
for i in range(n):
    element=int(input("Enter element : "))
    list.append(element)
for i in range(n):
    for j in range(i+1,n):
        if(list[j]>list[i]):
            list[i],list[j]=list[j],list[i]
print("The maximum value in the array is : ",list[0])
